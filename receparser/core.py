from collections import namedtuple,defaultdict
from operator import itemgetter
from .codes import dpc_codes,ika_codes 

class MonthlyRece:
    def __init__(self,file,codes=None):
        if codes == "dpc":
            self.codes = dpc_codes
        elif codes == "ika":
            self.codes = ika_codes
             
        with open(file,'r',encoding='shift_jis') as f:
            self.raw_text = f.read()
            self.IR_text = self.raw_text.split('\n')[0]
            self.IR = Rece([self.IR_text],self.codes)[0] # IRは絶対一行目に来るだろ、という暫定実装
            # TODO ReceオブジェクトのAPIをいじったので、RE指定をするように。

        d = "RE"
        self.RE_data = [d + e for e in self.raw_text.split(d) if e][1:]
        # RE区切りのリストデータ。それぞれのリストは１レセプトのテキスト塊
        self.monthly_dict = defaultdict(list)
        for text in self.RE_data:
            lst = text.split('\n')
            rece = Rece(lst,self.codes)
            # ここが問題。同月に２つのIDが登場することがある！　入外混在してたり、DPCで出来高・DPCだったり。
            # ひとまず回避として、IDをキーにreceのリストを返すよう仕様変更
            self.monthly_dict[rece.id].append(rece)
    
    def __getitem__(self,pos):
        return self.monthly_dict[pos]
    
    def keys(self):
        return self.monthly_dict.keys()
    
    def values(self):
        return self.monthly_dict.values()
    
    def items(self):
        return self.monthly_dict.items()
    
    
    def __len__(self):
        return len(self.monthly_dict)
    
    def __str__(self):
        return str(self.monthly_dict)
    
    def __eq__(self,other):
        return self.monthly_dict == other.monthly_dict
    
    def __repr__(self):
        return 'Rece:{}'.format(self.IR)
    
class Rece:
    def __init__(self,lst,codes):
        self.codes = codes
        self.rece_list = self.make_rece(lst,codes)
        # TODO いくつかの属性情報は、この段階で持っていてもいいかも。
        # 例：診療区分01と99の全体コメント、REなど。
    
    def make_rece(self,lst,codes):
        rece_list = []
        counter = 1 # レセ電一連番号
        data_class = "" # 診療識別
        for row in lst:
            #TODO このrow[0:2] in codes.keys()判定はもう少しスマートにしたい
            if row and row[0:2] in codes.keys():
                code = row[0:2]
                tmp = self.make_record(row,code)
                # ここで摘要レコードには追加を行う
                # 破壊的変更。rece_dictは単純なリストにすること。rece_listになる
                # COレコードをどうにかしたい。追加ロジックを組めないか？
                if code in ['SI','IY','TO','CO']:
                    if len(tmp['診療識別']) > 0: # 診療識別がレコードに存在する場合、つまり連番スタート
                        if tmp['診療識別'] == data_class: #既に出ている診療識別だった場合
                            counter = counter + 1
                        else:
                            counter = 1
                        tmp['レセ電一連番号'] = counter
             
                        data_class = tmp['診療識別']
                    elif len(tmp['診療識別']) == 0:
                        tmp['レセ電一連番号'] = counter #修正。カウンター変数をそのまま突っ込む。連番はグループに使うもの。
                
                    else:
                        tmp['レセ電一連番号'] = 'error'
                  
                # 追加ここまで｡
                rece_list.append(tmp)
        return rece_list
    
    def make_record(self,text,code):
        dic = {}
        for k,v in zip(self.codes[code],text.split(',')):
            if k:
                dic[k] = v
        return dic
    
    #def keys(self):
    #    return self.rece_dict.keys()
    
    #def values(self):
    #    return self.rece_dict.values()
    
    #def items(self):
    #    return self.rece_dict.items()
    
    def __getitem__(self,pos):
        if isinstance(pos,int):
            return self.rece_list[pos]
        elif isinstance(pos,str):
            return [record for record in self.rece_list if record['レコード識別情報'] == pos]

        # 数字が来たら単純なリスト位置を、COなどのコードが来たらレコードの塊を返す。
        #if len(self.rece_dict[pos]) == 1:
         #   return self.rece_dict[pos][0]
        #else:
         #   return self.rece_dict[pos]
    
    def __len__(self):
        return len(self.rece_list)
    
    def __str__(self):
        return str(self.rece_list)
    
    def __eq__(self,other):
        return self.rece_list == other.rece_list
    
    def __repr__(self):
        return 'Rece:{}'.format(self.rece_list)
    
    @property
    def id(self):
        return self.rece_list[0]['カルテ番号等'] #一行目に必ずREが来ると信じた実装
    # TODO これを['RE']['カルテ番号等']で呼び出せるようにしたい。
    # [0]をデフフォルトにする、とかそういう挙動。itemngetter(range(0,len(lst)))みたいなのを動的に作成するか
    # この下位クラスを用意すべきかも。defaultdictをパックしたクラス？
    
    
    


        
   