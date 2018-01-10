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
        d = "RE"
        self.RE_data = [d + e for e in self.raw_text.split(d) if e][1:]
        # RE区切りのリストデータ。それぞれのリストは１レセプトのテキスト塊
        self.monthly_dict = {}
        for text in self.RE_data:
            lst = text.split('\n')
            rece = Rece(lst,self.codes)
            self.monthly_dict[rece.id] = rece
    
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
        return 'Rece:{}'.format(self.monthly_dict)
    
class Rece:
    def __init__(self,lst,codes):
        self.codes = codes
        self.rece_dict = self.make_rece(lst,codes)
    
    def make_rece(self,lst,codes):
        rece_dict = defaultdict(list)
        for row in lst:
            #TODO このrow[0:2] in codes.keys()判定はもう少しスマートにしたい
            if row and row[0:2] in codes.keys():
                code = row[0:2]
                tmp = self.make_record(row,code)
                rece_dict[code].append(tmp)
        return rece_dict
    
    def make_record(self,text,code):
        dic = {}
        for k,v in zip(self.codes[code],text.split(',')):
            if k:
                dic[k] = v
        return dic
    
    def keys(self):
        return self.rece_dict.keys()
    
    def values(self):
        return self.rece_dict.values()
    
    def items(self):
        return self.rece_dict.items()
    
    def __getitem__(self,pos):
        if len(self.rece_dict[pos]) == 1:
            return self.rece_dict[pos][0]
        else:
            return self.rece_dict[pos]
    
    def __len__(self):
        return len(self.rece_dict)
    
    def __str__(self):
        return str(self.rece_dict)
    
    def __eq__(self,other):
        return self.race_dict == other.rece_dict
    
    def __repr__(self):
        return 'Rece:{}'.format(self.rece_dict)
    
    @property
    def id(self):
        return self.rece_dict['RE'][0]['カルテ番号等']
    # TODO これを['RE']['カルテ番号等']で呼び出せるようにしたい。
    # [0]をデフフォルトにする、とかそういう挙動。itemngetter(range(0,len(lst)))みたいなのを動的に作成するか
    # この下位クラスを用意すべきかも。defaultdictをパックしたクラス？
    
    
    


        
   