<<<<<<< HEAD

=======
IR = ['レコード識別番号','審査支払機関','都道府県','点数表','医療機関コード',None,'医療機関名称',
'請求年月','マルチボリューム識別情報','電話番号']
>>>>>>> 61ee16d428491ffc49e51fceaa606fc9de52b704

RE = ['レコード識別番号','レセプト番号','レセプト種別','診療年月','氏名','男女区分','生年月日','給付割合',
      '入院年月日','病棟区分','一部負担金区分','レセプト特記事項','病床数','カルテ番号等','割引点数単価',
      None,None,None,'検索番号','記録条件仕様年月情報','請求情報',
      '診療科名1','診療科_人体の部位1','診療科_性別等1','診療科_医学的処置1','診療科_特定疾病1',
      '診療科名2','診療科_人体の部位2','診療科_性別等2','診療科_医学的処置2','診療科_特定疾病2',
      '診療科名3','診療科_人体の部位3','診療科_性別等3','診療科_医学的処置3','診療科_特定疾病3',
      'カタカナ氏名','患者の状態']

HO = ['レコード識別番号','保険者番号','被保険者証の記号','被保険者証の番号','診療実日数','合計点数',
      None,'食事_回数','食事_合計金額','職務上の理由','証明者番号','負担金額_医療保険',
      '負担金額_減免区分','負担金額_減額割合','負担金額_減額金額']
      
SN = ['レコード識別番号','負担者種別','確認区分','保険者番号等','被保険者証等の記号','被保険者証等の番号',
'枝番','受給者番号',None]



KO = ['レコード識別情報','公費負担医療_負担者番号','公費負担医療_受給者番号','公費負担医療_任意給付区分',
      '診療実日数','合計点数','負担金額_公費','負担金額_公費給付対象外来一部負担金','負担金額_公費給付対象入院一部負担金',None,
      '食事療養・生活療養_回数','食事療養・生活療養_合計金額']

GR = ['レコード識別情報','医科点数表算定理由','DPCコード']

SJ = ['レコード識別情報','症状詳記区分','症状詳記データ']

# BU = ['レコード識別番号','診断群分類番号','今回入院年月日','今回退院年月日','DPC転帰区分','死因']

# SB = ['レコード識別番号','傷病名コード','修飾語コード','傷病名称','ICD10コード','傷病名区分','死因',
  #   '補足コメント']

SY = ['レコード識別番号','傷病名コード','診療開始日','転帰区分','修飾語コード','傷病名称',
      '主傷病','補足コメント']

# KK = ['レコード識別番号',None,'DPC算定対象となる病棟以外の病棟移動の有無','予定・緊急入院区分',
  #    '前回退院年月日','前回同一傷病での入院の有無','入院時年齢','出生時体重','JCS',None,
   #   'Burn Index','重症度等',None,None]


# SK = ['レコード識別情報','診療行為コード','区分番号','実施（予定）年月日',None,'診療区分コード',
  #    '診療名称']

# GA = ['レコード識別情報','診療年月','請求調整区分','外泊等','診断群分類番号',
#     '医療機関別係数','翌月再入院（ 転棟） 予定の有無']

#HH = ['レコード識別情報','診療年月','請求調整区分','自他保険区分', 
#      '負担区分', '入院期間区分','入院期間区分別点数','入院期間区分別入院日数',
#      '包括小計点数']

#GT = ['レコード識別情報','診療年月','請求調整区分','自他保険区分',
#      '負担区分','包括小計点数合算','包括評価点数','調整点数','今月包括合計点数',
#      '診療識別','保険変更_変更年月日','保険変更_文字データ']

SI = ['レコード識別情報','診療識別','負担区分','診療行為コード','数量データ','点数','回数',
      'コメントデータ1','文字データ1','コメントデータ2','文字データ2','コメントデータ3','文字データ3',
      1, 2, 3, 4, 5, 6, 7, 8,
 9, 10, 11,12, 13,14, 15, 16,
 17, 18, 19, 20, 21, 22, 23, 24,
 25, 26, 27, 28, 29, 30, 31]

IY = ['レコード識別情報','診療識別','負担区分','医薬品コード','使用量','点数','回数',
      'コメントデータ1','文字データ1','コメントデータ2','文字データ2','コメントデータ3','文字データ3',
      1, 2, 3, 4, 5, 6, 7, 8,
 9, 10, 11,12, 13,14, 15, 16,
 17, 18, 19, 20, 21, 22, 23, 24,
 25, 26, 27, 28, 29, 30, 31]

TO = ['レコード識別情報','診療識別','負担区分','特定器材コード','使用量','点数','回数',
      '単位コード','単価',None,'商品名及び規格又はサイズ',
      'コメントデータ1','文字データ1','コメントデータ2','文字データ2','コメントデータ3','文字データ3',
      1, 2, 3, 4, 5, 6, 7, 8,
 9, 10, 11,12, 13,14, 15, 16,
 17, 18, 19, 20, 21, 22, 23, 24,
 25, 26, 27, 28, 29, 30, 31]

#CD = ['レコード識別情報','実施年月日','診療識別','順序番号',
# '行為明細番号','レセプト電算処理システム用コード','使用量',
# '数量データ','単位コード','回数','特定器材名称']

CO = ['レコード識別情報','診療識別','負担区分','コメントコード','文字データ']

ika_codes = {'IR':IR,'RE':RE,'HO':HO,'GR':GR,'SJ':SJ,'KO':KO,'SY':SY,
         'SI':SI,'IY':IY,'TO':TO,'CO':CO,'SN':SN}