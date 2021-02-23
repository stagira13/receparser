from datetime import date
from japanera import (Japanera, EraDate, EraDateTime)
janera = Japanera()

G_dic = {'1':'明治','2':'大正','3':'昭和','4':'平成','5':'令和'}


def gengo_helper(string):
    if len(string) == 5:
        G = string[0]
        YY = string[1:3]
        MM = string[3:5]
        gengo = G_dic[G]
        gengo_month = f'{gengo}{YY}年{MM}月'
        
        d = janera.strptime(gengo_month,"%-E%-o年%m月")
        western_month = f'{d[0].year}{d[0].month:02d}'
        return western_month
    
    elif len(string) == 7:
        G = string[0]
        YY = string[1:3]
        MM = string[3:5]
        DD = string[5:7]
        gengo = G_dic[G]
        gengo_date = f'{gengo}{YY}年{MM}月{DD}日'
        
        d = janera.strptime(gengo_date,"%-E%-o年%m月%d日")
        western_date = f'{d[0].year}{d[0].month:02d}{d[0].day:02d}'
        return western_date
    else:
        return string


def nyugai_helper(string):
    try:
        num = int(string)
    except:
        raise ValueError(f'{string}: 整数に変換できない引数です')
    if num % 2 == 1:
        return '入院'
    else:
        return '外来'
    

def exact_any_data(R,record_key):
    '''
    test
    属性情報を何も付加しないバージョン
    付加するなら、dic={} dic.update(r['RE'][0])みたいなコードが必須。
    ネストしたループになりそう
    '''
    data = []
    for key in R.keys():
        for r in R[key]:
            data.extend(r[record_key])
    return data

def exact_HO_data_ika(R):
    '''
    DPCと医科でわけている
    '''
    data = []
    for key in R.keys():
        for r in R[key]:
            # １患者あたり複数レセがあることを想定し、forループ。R[key]はレセオブジェクトのリストを返す
            # rは必ずレセオブジェクト
            dic = {}
            string = r['RE'][0]['レセプト種別'] #string: 入外等のフラグデータ。数値
            nyugai = nyugai_helper(string)
        
            if len(r['HO']) > 0:
                hoken = 'HO'
                syoku = '食事_合計金額'
            else:
                hoken = 'KO'
                syoku = '食事療養・生活療養_合計金額'
     
            dic['入外'] = nyugai
            dic['ID'] = key
            dic['合計点数'] = r[hoken][0]['合計点数']
            dic['診療実日数'] = r[hoken][0]['診療実日数']
            dic['食事合計金額'] = r[hoken][0][syoku]      
            dic['DPC出来高分類'] = '出来高'
            dic['生年月日'] = gengo_helper(r['RE'][0]['生年月日'])
            dic['診療科名1'] = r['RE'][0]['診療科名1']
            dic['診療年月'] = gengo_helper(r['RE'][0]['診療年月'])
            
            dic['医療機関名称'] = R.IR['医療機関名称']
            # dic['請求年月'] = R.IR['請求年月']

            data.append(dic)

    return data

def exact_HO_data_dpc(R):
    '''
    DPC版。基本、レセ総括区分をフィルターしてないので、
    後処理でフィルターしないと点数が重複する。注意。（総括レセのみ数えること）
    '''
    data = []
    for key in R.keys():
        for r in R[key]:
            # １患者あたり複数レセがあることを想定し、forループ。R[key]はレセオブジェクトのリストを返す
            # rは必ずレセオブジェクト
            dic = {}
            string = r['RE'][0]['レセプト種別'] #string: 入外等のフラグデータ。数値
            nyugai = nyugai_helper(string)
        
            if len(r['HO']) > 0:
                hoken = 'HO'
                syoku = '食事_合計金額'
            else:
                hoken = 'KO'
                syoku = '食事療養・生活療養_合計金額'
     
            dic['入外'] = nyugai
            dic['ID'] = key
            dic['合計点数'] = r[hoken][0]['合計点数']
            dic['診療実日数'] = r[hoken][0]['診療実日数']
            dic['食事合計金額'] = r[hoken][0][syoku]      
            dic['DPC出来高分類'] = r['RE'][0]['レセプト総括区分']
            dic['生年月日'] = gengo_helper(r['RE'][0]['生年月日'])
            dic['診療科名'] = r['RE'][0]['診療科名']
            dic['診療年月'] = gengo_helper(r['RE'][0]['診療年月'])
            
            dic['医療機関名称'] = R.IR['医療機関名称']
            # dic['請求年月'] = R.IR['請求年月']

            data.append(dic)

    return data