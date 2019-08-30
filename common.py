import logging
import datetime
import pymongo

def getMinDate(datetimeObjList):
    curMinDatetimeObj = datetime.datetime.now()
    for datetimeObj in datetimeObjList:
        if curMinDatetimeObj > datetimeObj:
            curMinDatetimeObj = datetimeObj
        
    return curMinDatetimeObj

def setupLogging(fileName):
    # setup log file and log depth 

    fileHandler = logging.FileHandler(fileName)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter( logging.Formatter('%(asctime)s:%(levelname)s:[%(filename)s.%(funcName)s]%(message)s', '%m-%d %H:%M:%S'))

    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter( logging.Formatter('%(asctime)s:%(levelname)s:[%(filename)s.%(funcName)s]%(message)s', '%m-%d %H:%M:%S'))

    logger = logging.getLogger('')

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


def tryCatchWrapped(func):
    # this is for decorator

    def wrapperFunc(*args, **kwargs):
        try:
            result =  func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(str(e), exc_info=True)
            return None

    return wrapperFunc

@tryCatchWrapped
def getDBConnection(databaseName="whalebroker", ip="127.0.0.1", port=27017):
    conn = pymongo.MongoClient(str(ip), int(port))
    db = conn.get_database(databaseName)
    return db

@tryCatchWrapped
def sortJsonList(jsonList,keyName="time", reverse=False):
    sortedJsonList = sorted(jsonList, key=lambda k: k.get(keyName, 0), reverse=reverse)
    return sortedJsonList

PROXY_LIST = [
'203.246.112.133:3128',
'121.165.92.44:8080',
'195.122.185.95:3128',
'159.69.203.169:3128',
'139.59.143.247:3129',
'199.247.21.76:3128',
'46.4.199.156:3128',
'185.22.174.69:10010',
'94.242.59.135:1448',
'198.211.102.155:8080',
'144.202.25.22:8080',
'159.65.69.157:8118',
'23.254.226.105:8888',
'198.143.178.87:3128',
'208.108.120.58:8080',
'176.235.143.71:8080',
'167.249.181.191:3128',
'163.172.148.169:3128',
'51.158.98.121:8811',
'51.158.99.51:8811',
'51.158.119.4:8811',
'51.158.111.242:8811',
'162.144.250.249:8888',
'81.163.55.241:41258',
'51.15.53.4:3128',
'51.38.81.24:8080',
'111.93.246.34:3128',
'95.141.36.112:8686',
'62.173.145.48:3128',
'200.41.148.2:8080',
'181.52.237.106:31707',
'168.228.51.197:52748',
'95.179.198.239:8080',
'95.179.238.28:8080',
'148.217.94.54:3128',
'37.26.136.181:60193',
'212.56.218.90:61555',
'91.134.196.197:3128',
'94.23.93.151:3128',
]

# 2019/07/24
CODE_TABLE = [
    {
        "fullCode": "KR7060310000",
        "shortCode": "A060310",
        "codeName": "3S",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095570008",
        "shortCode": "A095570",
        "codeName": "AJ네트웍스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7068400001",
        "shortCode": "A068400",
        "codeName": "AJ렌터카",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006840003",
        "shortCode": "A006840",
        "codeName": "AK홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7054620000",
        "shortCode": "A054620",
        "codeName": "APS홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7265520007",
        "shortCode": "A265520",
        "codeName": "AP시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7211270004",
        "shortCode": "A211270",
        "codeName": "AP위성",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7027410000",
        "shortCode": "A027410",
        "codeName": "BGF",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7282330000",
        "shortCode": "A282330",
        "codeName": "BGF리테일",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7138930003",
        "shortCode": "A138930",
        "codeName": "BNK금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001460005",
        "shortCode": "A001460",
        "codeName": "BYC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001461003",
        "shortCode": "A001465",
        "codeName": "BYC우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001040005",
        "shortCode": "A001040",
        "codeName": "CJ",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079160008",
        "shortCode": "A079160",
        "codeName": "CJ CGV",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7035760008",
        "shortCode": "A035760",
        "codeName": "CJ ENM",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000120006",
        "shortCode": "A000120",
        "codeName": "CJ대한통운",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011150000",
        "shortCode": "A011150",
        "codeName": "CJ씨푸드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011151008",
        "shortCode": "A011155",
        "codeName": "CJ씨푸드1우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001041003",
        "shortCode": "A001045",
        "codeName": "CJ우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7097950000",
        "shortCode": "A097950",
        "codeName": "CJ제일제당",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7097951008",
        "shortCode": "A097955",
        "codeName": "CJ제일제당 우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7051500007",
        "shortCode": "A051500",
        "codeName": "CJ프레시웨이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037560000",
        "shortCode": "A037560",
        "codeName": "CJ헬로",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7058820002",
        "shortCode": "A058820",
        "codeName": "CMG제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023460009",
        "shortCode": "A023460",
        "codeName": "CNH",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065770000",
        "shortCode": "A065770",
        "codeName": "CS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083660001",
        "shortCode": "A083660",
        "codeName": "CSA 코스믹",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000590000",
        "shortCode": "A000590",
        "codeName": "CS홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012030003",
        "shortCode": "A012030",
        "codeName": "DB",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7306620006",
        "shortCode": "A306620",
        "codeName": "DB금융스팩6호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7322780008",
        "shortCode": "A322780",
        "codeName": "DB금융스팩7호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016610008",
        "shortCode": "A016610",
        "codeName": "DB금융투자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005830005",
        "shortCode": "A005830",
        "codeName": "DB손해보험",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000990002",
        "shortCode": "A000990",
        "codeName": "DB하이텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000991000",
        "shortCode": "A000995",
        "codeName": "DB하이텍1우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7139130009",
        "shortCode": "A139130",
        "codeName": "DGB금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001530005",
        "shortCode": "A001530",
        "codeName": "DI동일",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7068790005",
        "shortCode": "A068790",
        "codeName": "DMS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004840005",
        "shortCode": "A004840",
        "codeName": "DRB동일",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7241520006",
        "shortCode": "A241520",
        "codeName": "DSC인베스트먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7155660004",
        "shortCode": "A155660",
        "codeName": "DSR",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7069730000",
        "shortCode": "A069730",
        "codeName": "DSR제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017940008",
        "shortCode": "A017940",
        "codeName": "E1",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7245620000",
        "shortCode": "A245620",
        "codeName": "EDGC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037370004",
        "shortCode": "A037370",
        "codeName": "EG",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079190005",
        "shortCode": "A079190",
        "codeName": "EMW",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007700008",
        "shortCode": "A007700",
        "codeName": "F&F",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7130500002",
        "shortCode": "A130500",
        "codeName": "GH신소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114090004",
        "shortCode": "A114090",
        "codeName": "GKL",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032860009",
        "shortCode": "A032860",
        "codeName": "GMR 머티리얼즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "HK0000307485",
        "shortCode": "A900290",
        "codeName": "GRT",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078930005",
        "shortCode": "A078930",
        "codeName": "GS",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7083450007",
        "shortCode": "A083450",
        "codeName": "GST",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006360002",
        "shortCode": "A006360",
        "codeName": "GS건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001250000",
        "shortCode": "A001250",
        "codeName": "GS글로벌",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007070006",
        "shortCode": "A007070",
        "codeName": "GS리테일",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7078931003",
        "shortCode": "A078935",
        "codeName": "GS우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7028150001",
        "shortCode": "A028150",
        "codeName": "GS홈쇼핑",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045890001",
        "shortCode": "A045890",
        "codeName": "GV",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078150000",
        "shortCode": "A078150",
        "codeName": "HB테크놀러지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012630000",
        "shortCode": "A012630",
        "codeName": "HDC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039570007",
        "shortCode": "A039570",
        "codeName": "HDC아이콘트롤스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7089470009",
        "shortCode": "A089470",
        "codeName": "HDC현대EP",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7294870001",
        "shortCode": "A294870",
        "codeName": "HDC현대산업개발",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036640001",
        "shortCode": "A036640",
        "codeName": "HRS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7082740002",
        "shortCode": "A082740",
        "codeName": "HSD엔진",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7299170001",
        "shortCode": "A299170",
        "codeName": "IBKS제10호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7254120009",
        "shortCode": "A254120",
        "codeName": "IBKS제5호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7264850009",
        "shortCode": "A264850",
        "codeName": "IBKS제6호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7276920006",
        "shortCode": "A276920",
        "codeName": "IBKS제7호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7297570004",
        "shortCode": "A297570",
        "codeName": "IBKS제9호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003560000",
        "shortCode": "A003560",
        "codeName": "IHQ",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7095340006",
        "shortCode": "A095340",
        "codeName": "ISC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7099520009",
        "shortCode": "A099520",
        "codeName": "ITX엠투엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7175330000",
        "shortCode": "A175330",
        "codeName": "JB금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR8392080006",
        "shortCode": "A950170",
        "codeName": "JTC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7234080000",
        "shortCode": "A234080",
        "codeName": "JW생명과학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7067290007",
        "shortCode": "A067290",
        "codeName": "JW신약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001060003",
        "shortCode": "A001060",
        "codeName": "JW중외제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001062009",
        "shortCode": "A001067",
        "codeName": "JW중외제약2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001061001",
        "shortCode": "A001065",
        "codeName": "JW중외제약우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7096760004",
        "shortCode": "A096760",
        "codeName": "JW홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7035900000",
        "shortCode": "A035900",
        "codeName": "JYP Ent.",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024840001",
        "shortCode": "A024840",
        "codeName": "KBI메탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7105560007",
        "shortCode": "A105560",
        "codeName": "KB금융",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024120008",
        "shortCode": "A024120",
        "codeName": "KB오토시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002380004",
        "shortCode": "A002380",
        "codeName": "KCC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7021320007",
        "shortCode": "A021320",
        "codeName": "KCC건설",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036670008",
        "shortCode": "A036670",
        "codeName": "KCI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009070004",
        "shortCode": "A009070",
        "codeName": "KCTC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009440009",
        "shortCode": "A009440",
        "codeName": "KC그린홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7112190004",
        "shortCode": "A112190",
        "codeName": "KC산업",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7119650000",
        "shortCode": "A119650",
        "codeName": "KC코트렐",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7044180008",
        "shortCode": "A044180",
        "codeName": "KD",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092220003",
        "shortCode": "A092220",
        "codeName": "KEC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7151860004",
        "shortCode": "A151860",
        "codeName": "KG ETS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7046440004",
        "shortCode": "A046440",
        "codeName": "KG모빌리언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035600006",
        "shortCode": "A035600",
        "codeName": "KG이니시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001390004",
        "shortCode": "A001390",
        "codeName": "KG케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7060720000",
        "shortCode": "A060720",
        "codeName": "KH바텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001940006",
        "shortCode": "A001940",
        "codeName": "KISCO홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7083470005",
        "shortCode": "A083470",
        "codeName": "KJ프리텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122450000",
        "shortCode": "A122450",
        "codeName": "KMH",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052900008",
        "shortCode": "A052900",
        "codeName": "KMH하이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058400003",
        "shortCode": "A058400",
        "codeName": "KNN",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114450000",
        "shortCode": "A114450",
        "codeName": "KPX생명과학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025000001",
        "shortCode": "A025000",
        "codeName": "KPX케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7092230002",
        "shortCode": "A092230",
        "codeName": "KPX홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000040006",
        "shortCode": "A000040",
        "codeName": "KR모터스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7044450005",
        "shortCode": "A044450",
        "codeName": "KSS해운",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7030200000",
        "shortCode": "A030200",
        "codeName": "KT",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033780008",
        "shortCode": "A033780",
        "codeName": "KT&G",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7030210009",
        "shortCode": "A030210",
        "codeName": "KTB투자증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036030005",
        "shortCode": "A036030",
        "codeName": "KTH",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058850009",
        "shortCode": "A058850",
        "codeName": "KTcs",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7058860008",
        "shortCode": "A058860",
        "codeName": "KTis",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7060370004",
        "shortCode": "A060370",
        "codeName": "KT서브마린",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093050003",
        "shortCode": "A093050",
        "codeName": "LF",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003550001",
        "shortCode": "A003550",
        "codeName": "LG",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034220004",
        "shortCode": "A034220",
        "codeName": "LG디스플레이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001120005",
        "shortCode": "A001120",
        "codeName": "LG상사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7051900009",
        "shortCode": "A051900",
        "codeName": "LG생활건강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7051901007",
        "shortCode": "A051905",
        "codeName": "LG생활건강우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003551009",
        "shortCode": "A003555",
        "codeName": "LG우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032640005",
        "shortCode": "A032640",
        "codeName": "LG유플러스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011070000",
        "shortCode": "A011070",
        "codeName": "LG이노텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7066570003",
        "shortCode": "A066570",
        "codeName": "LG전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7066571001",
        "shortCode": "A066575",
        "codeName": "LG전자우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7108670001",
        "shortCode": "A108670",
        "codeName": "LG하우시스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7108671009",
        "shortCode": "A108675",
        "codeName": "LG하우시스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7051910008",
        "shortCode": "A051910",
        "codeName": "LG화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7051911006",
        "shortCode": "A051915",
        "codeName": "LG화학우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079550000",
        "shortCode": "A079550",
        "codeName": "LIG넥스원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7183350008",
        "shortCode": "A183350",
        "codeName": "LPK로보틱스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7006260004",
        "shortCode": "A006260",
        "codeName": "LS",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000680009",
        "shortCode": "A000680",
        "codeName": "LS네트웍스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010120004",
        "shortCode": "A010120",
        "codeName": "LS산전",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7229640008",
        "shortCode": "A229640",
        "codeName": "LS전선아시아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023150006",
        "shortCode": "A023150",
        "codeName": "MH에탄올",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7065150005",
        "shortCode": "A065150",
        "codeName": "MP그룹",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7219550001",
        "shortCode": "A219550",
        "codeName": "MP한강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035420009",
        "shortCode": "A035420",
        "codeName": "NAVER",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7160550000",
        "shortCode": "A160550",
        "codeName": "NEW",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053290003",
        "shortCode": "A053290",
        "codeName": "NE능률",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7181710005",
        "shortCode": "A181710",
        "codeName": "NHN",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7104200001",
        "shortCode": "A104200",
        "codeName": "NHN벅스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060250008",
        "shortCode": "A060250",
        "codeName": "NHN한국사이버결제",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005940002",
        "shortCode": "A005940",
        "codeName": "NH투자증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005941000",
        "shortCode": "A005945",
        "codeName": "NH투자증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034310003",
        "shortCode": "A034310",
        "codeName": "NICE",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7030190003",
        "shortCode": "A030190",
        "codeName": "NICE평가정보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008260002",
        "shortCode": "A008260",
        "codeName": "NI스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004250007",
        "shortCode": "A004250",
        "codeName": "NPC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004251005",
        "shortCode": "A004255",
        "codeName": "NPC우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010060002",
        "shortCode": "A010060",
        "codeName": "OCI",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024940009",
        "shortCode": "A024940",
        "codeName": "PN풍년",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005490008",
        "shortCode": "A005490",
        "codeName": "POSCO",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7218410009",
        "shortCode": "A218410",
        "codeName": "RFHIC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091340000",
        "shortCode": "A091340",
        "codeName": "S&K폴리텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7100840008",
        "shortCode": "A100840",
        "codeName": "S&TC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7064960008",
        "shortCode": "A064960",
        "codeName": "S&T모티브",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003570009",
        "shortCode": "A003570",
        "codeName": "S&T중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036530004",
        "shortCode": "A036530",
        "codeName": "S&T홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010950004",
        "shortCode": "A010950",
        "codeName": "S-Oil",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010951002",
        "shortCode": "A010955",
        "codeName": "S-Oil우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7019550003",
        "shortCode": "A019550",
        "codeName": "SBI인베스트먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR8392070007",
        "shortCode": "A950110",
        "codeName": "SBI핀테크솔루션즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7034120006",
        "shortCode": "A034120",
        "codeName": "SBS",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7101060002",
        "shortCode": "A101060",
        "codeName": "SBS미디어홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7046140000",
        "shortCode": "A046140",
        "codeName": "SBS콘텐츠허브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036120004",
        "shortCode": "A036120",
        "codeName": "SCI평가정보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7099220006",
        "shortCode": "A099220",
        "codeName": "SDN",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036540003",
        "shortCode": "A036540",
        "codeName": "SFA반도체",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7255220006",
        "shortCode": "A255220",
        "codeName": "SG",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7040610008",
        "shortCode": "A040610",
        "codeName": "SG&G",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049470008",
        "shortCode": "A049470",
        "codeName": "SGA",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7184230001",
        "shortCode": "A184230",
        "codeName": "SGA솔루션즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7224880005",
        "shortCode": "A224880",
        "codeName": "SGA임베디드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7004060000",
        "shortCode": "A004060",
        "codeName": "SG세계물산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001380005",
        "shortCode": "A001380",
        "codeName": "SG충방",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002360006",
        "shortCode": "A002360",
        "codeName": "SH에너지화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009160003",
        "shortCode": "A009160",
        "codeName": "SIMPAC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7123700007",
        "shortCode": "A123700",
        "codeName": "SJM",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025530007",
        "shortCode": "A025530",
        "codeName": "SJM홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034730002",
        "shortCode": "A034730",
        "codeName": "SK",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7232330001",
        "shortCode": "A232330",
        "codeName": "SK3호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307070003",
        "shortCode": "A307070",
        "codeName": "SK4호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011790003",
        "shortCode": "A011790",
        "codeName": "SKC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7057500001",
        "shortCode": "A057500",
        "codeName": "SKC 솔믹스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7178920005",
        "shortCode": "A178920",
        "codeName": "SKC코오롱PI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018670000",
        "shortCode": "A018670",
        "codeName": "SK가스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001740000",
        "shortCode": "A001740",
        "codeName": "SK네트웍스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001741008",
        "shortCode": "A001745",
        "codeName": "SK네트웍스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006120000",
        "shortCode": "A006120",
        "codeName": "SK디스커버리",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006121008",
        "shortCode": "A006125",
        "codeName": "SK디스커버리우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7210980009",
        "shortCode": "A210980",
        "codeName": "SK디앤디",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036490001",
        "shortCode": "A036490",
        "codeName": "SK머티리얼즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052260007",
        "shortCode": "A052260",
        "codeName": "SK바이오랜드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR703473K016",
        "shortCode": "A03473K",
        "codeName": "SK우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7096770003",
        "shortCode": "A096770",
        "codeName": "SK이노베이션",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7096771001",
        "shortCode": "A096775",
        "codeName": "SK이노베이션우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001510007",
        "shortCode": "A001510",
        "codeName": "SK증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001511005",
        "shortCode": "A001515",
        "codeName": "SK증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7285130001",
        "shortCode": "A285130",
        "codeName": "SK케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR728513K010",
        "shortCode": "A28513K",
        "codeName": "SK케미칼우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017670001",
        "shortCode": "A017670",
        "codeName": "SK텔레콤",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000660001",
        "shortCode": "A000660",
        "codeName": "SK하이닉스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7048550008",
        "shortCode": "A048550",
        "codeName": "SM C&C",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7063440002",
        "shortCode": "A063440",
        "codeName": "SM Life Design",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR8392100002",
        "shortCode": "A950180",
        "codeName": "SNK",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005610001",
        "shortCode": "A005610",
        "codeName": "SPC삼립",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011810009",
        "shortCode": "A011810",
        "codeName": "STX",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7077970002",
        "shortCode": "A077970",
        "codeName": "STX엔진",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7071970008",
        "shortCode": "A071970",
        "codeName": "STX중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7289080004",
        "shortCode": "A289080",
        "codeName": "SV인베스트먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084870005",
        "shortCode": "A084870",
        "codeName": "TBH글로벌",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002710002",
        "shortCode": "A002710",
        "codeName": "TCC스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7089230007",
        "shortCode": "A089230",
        "codeName": "THE E&M",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7161570007",
        "shortCode": "A161570",
        "codeName": "THE MIDONG",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032540007",
        "shortCode": "A032540",
        "codeName": "TJ미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7048770002",
        "shortCode": "A048770",
        "codeName": "TPC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7246690002",
        "shortCode": "A246690",
        "codeName": "TS인베스트먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7284610003",
        "shortCode": "A284610",
        "codeName": "TS트릴리온",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7038340006",
        "shortCode": "A038340",
        "codeName": "UCI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7073570004",
        "shortCode": "A073570",
        "codeName": "WI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024070005",
        "shortCode": "A024070",
        "codeName": "WISCOM",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7052300001",
        "shortCode": "A052300",
        "codeName": "W홀딩컴퍼니",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037270006",
        "shortCode": "A037270",
        "codeName": "YG PLUS",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7040300006",
        "shortCode": "A040300",
        "codeName": "YTN",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051390003",
        "shortCode": "A051390",
        "codeName": "YW",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052220001",
        "shortCode": "A052220",
        "codeName": "iMBC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079940003",
        "shortCode": "A079940",
        "codeName": "가비아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078890001",
        "shortCode": "A078890",
        "codeName": "가온미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000500009",
        "shortCode": "A000500",
        "codeName": "가온전선",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7192410009",
        "shortCode": "A192410",
        "codeName": "감마누",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000860007",
        "shortCode": "A000860",
        "codeName": "강남제비스코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7217730001",
        "shortCode": "A217730",
        "codeName": "강스템바이오텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035250000",
        "shortCode": "A035250",
        "codeName": "강원랜드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011420007",
        "shortCode": "A011420",
        "codeName": "갤럭시아에스엠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7094480001",
        "shortCode": "A094480",
        "codeName": "갤럭시아컴즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7063080006",
        "shortCode": "A063080",
        "codeName": "게임빌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039240007",
        "shortCode": "A039240",
        "codeName": "경남스틸",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053950002",
        "shortCode": "A053950",
        "codeName": "경남제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002100006",
        "shortCode": "A002100",
        "codeName": "경농",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009450008",
        "shortCode": "A009450",
        "codeName": "경동나비엔",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7267290005",
        "shortCode": "A267290",
        "codeName": "경동도시가스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012320008",
        "shortCode": "A012320",
        "codeName": "경동인베스트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011040003",
        "shortCode": "A011040",
        "codeName": "경동제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000050005",
        "shortCode": "A000050",
        "codeName": "경방",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7214390007",
        "shortCode": "A214390",
        "codeName": "경보제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012610002",
        "shortCode": "A012610",
        "codeName": "경인양행",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009140005",
        "shortCode": "A009140",
        "codeName": "경인전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024910002",
        "shortCode": "A024910",
        "codeName": "경창산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013580006",
        "shortCode": "A013580",
        "codeName": "계룡건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012200002",
        "shortCode": "A012200",
        "codeName": "계양전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012201000",
        "shortCode": "A012205",
        "codeName": "계양전기우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004200002",
        "shortCode": "A004200",
        "codeName": "고려개발",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002140002",
        "shortCode": "A002140",
        "codeName": "고려산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7198440000",
        "shortCode": "A198440",
        "codeName": "고려시멘트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049720006",
        "shortCode": "A049720",
        "codeName": "고려신용정보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010130003",
        "shortCode": "A010130",
        "codeName": "고려아연",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002240000",
        "shortCode": "A002240",
        "codeName": "고려제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014570006",
        "shortCode": "A014570",
        "codeName": "고려제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7098460009",
        "shortCode": "A098460",
        "codeName": "고영",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038530002",
        "shortCode": "A038530",
        "codeName": "골드퍼시픽",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KYG1990V1041",
        "shortCode": "A900280",
        "codeName": "골든센츄리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215000001",
        "shortCode": "A215000",
        "codeName": "골프존",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7121440002",
        "shortCode": "A121440",
        "codeName": "골프존뉴딘홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7183410000",
        "shortCode": "A183410",
        "codeName": "골프존데카",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7076340009",
        "shortCode": "A076340",
        "codeName": "관악산업",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7009290008",
        "shortCode": "A009290",
        "codeName": "광동제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014200000",
        "shortCode": "A014200",
        "codeName": "광림",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017040007",
        "shortCode": "A017040",
        "codeName": "광명전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017900002",
        "shortCode": "A017900",
        "codeName": "광전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7037710001",
        "shortCode": "A037710",
        "codeName": "광주신세계",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7026910000",
        "shortCode": "A026910",
        "codeName": "광진실업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090150004",
        "shortCode": "A090150",
        "codeName": "광진윈텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7267320000",
        "shortCode": "A267320",
        "codeName": "교보7호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307280008",
        "shortCode": "A307280",
        "codeName": "교보8호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7030610000",
        "shortCode": "A030610",
        "codeName": "교보증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7329050009",
        "shortCode": "A329050",
        "codeName": "구스앤홈",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7053270005",
        "shortCode": "A053270",
        "codeName": "구영테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007690001",
        "shortCode": "A007690",
        "codeName": "국도화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005320007",
        "shortCode": "A005320",
        "codeName": "국동",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001140003",
        "shortCode": "A001140",
        "codeName": "국보",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7066620006",
        "shortCode": "A066620",
        "codeName": "국보디자인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043650001",
        "shortCode": "A043650",
        "codeName": "국순당",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006050009",
        "shortCode": "A006050",
        "codeName": "국영지앤엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060480001",
        "shortCode": "A060480",
        "codeName": "국일신동",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078130002",
        "shortCode": "A078130",
        "codeName": "국일제지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002720001",
        "shortCode": "A002720",
        "codeName": "국제약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7243870003",
        "shortCode": "A243870",
        "codeName": "굿센",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7083420000",
        "shortCode": "A083420",
        "codeName": "그린케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7186230009",
        "shortCode": "A186230",
        "codeName": "그린플러스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7014530000",
        "shortCode": "A014530",
        "codeName": "극동유화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KYG3931T1076",
        "shortCode": "A900070",
        "codeName": "글로벌에스엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7204620009",
        "shortCode": "A204620",
        "codeName": "글로벌텍스프리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019660000",
        "shortCode": "A019660",
        "codeName": "글로본",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014280002",
        "shortCode": "A014280",
        "codeName": "금강공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014281000",
        "shortCode": "A014285",
        "codeName": "금강공업우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7053260006",
        "shortCode": "A053260",
        "codeName": "금강철강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008870008",
        "shortCode": "A008870",
        "codeName": "금비",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001570001",
        "shortCode": "A001570",
        "codeName": "금양",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002990000",
        "shortCode": "A002990",
        "codeName": "금호산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002991008",
        "shortCode": "A002995",
        "codeName": "금호산업우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011780004",
        "shortCode": "A011780",
        "codeName": "금호석유",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011781002",
        "shortCode": "A011785",
        "codeName": "금호석유우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7214330003",
        "shortCode": "A214330",
        "codeName": "금호에이치티",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001210004",
        "shortCode": "A001210",
        "codeName": "금호전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7073240004",
        "shortCode": "A073240",
        "codeName": "금호타이어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036190007",
        "shortCode": "A036190",
        "codeName": "금화피에스시",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049080005",
        "shortCode": "A049080",
        "codeName": "기가레인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035460005",
        "shortCode": "A035460",
        "codeName": "기산텔레콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092440007",
        "shortCode": "A092440",
        "codeName": "기신정기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000270009",
        "shortCode": "A000270",
        "codeName": "기아차",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024110009",
        "shortCode": "A024110",
        "codeName": "기업은행",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7013700000",
        "shortCode": "A013700",
        "codeName": "까뮤이앤씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7308100007",
        "shortCode": "A308100",
        "codeName": "까스텔바쟉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004540001",
        "shortCode": "A004540",
        "codeName": "깨끗한나라",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004541009",
        "shortCode": "A004545",
        "codeName": "깨끗한나라우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7187790001",
        "shortCode": "A187790",
        "codeName": "나노",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7074610007",
        "shortCode": "A074610",
        "codeName": "나노메딕스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7151910007",
        "shortCode": "A151910",
        "codeName": "나노스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7121600001",
        "shortCode": "A121600",
        "codeName": "나노신소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039860002",
        "shortCode": "A039860",
        "codeName": "나노엔텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091970004",
        "shortCode": "A091970",
        "codeName": "나노캠텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7244880001",
        "shortCode": "A244880",
        "codeName": "나눔테크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7288490006",
        "shortCode": "A288490",
        "codeName": "나라소프트",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7051490001",
        "shortCode": "A051490",
        "codeName": "나라엠앤디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7190510008",
        "shortCode": "A190510",
        "codeName": "나무가",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7242040004",
        "shortCode": "A242040",
        "codeName": "나무기술",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089600001",
        "shortCode": "A089600",
        "codeName": "나스미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7293580007",
        "shortCode": "A293580",
        "codeName": "나우아이비캐피탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138610001",
        "shortCode": "A138610",
        "codeName": "나이벡",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7130580004",
        "shortCode": "A130580",
        "codeName": "나이스디앤비",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036800001",
        "shortCode": "A036800",
        "codeName": "나이스정보통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7082660002",
        "shortCode": "A082660",
        "codeName": "나인컴플렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001260009",
        "shortCode": "A001260",
        "codeName": "남광토건",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008350001",
        "shortCode": "A008350",
        "codeName": "남선알미늄",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008351009",
        "shortCode": "A008355",
        "codeName": "남선알미우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004270005",
        "shortCode": "A004270",
        "codeName": "남성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003920006",
        "shortCode": "A003920",
        "codeName": "남양유업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003921004",
        "shortCode": "A003925",
        "codeName": "남양유업우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002070001",
        "shortCode": "A002070",
        "codeName": "남영비비안",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025860008",
        "shortCode": "A025860",
        "codeName": "남해화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7111710000",
        "shortCode": "A111710",
        "codeName": "남화산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091590000",
        "shortCode": "A091590",
        "codeName": "남화토건",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7168330009",
        "shortCode": "A168330",
        "codeName": "내츄럴엔도텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7072770001",
        "shortCode": "A072770",
        "codeName": "네오디안테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7253590004",
        "shortCode": "A253590",
        "codeName": "네오셈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7212560007",
        "shortCode": "A212560",
        "codeName": "네오오토",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095660007",
        "shortCode": "A095660",
        "codeName": "네오위즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042420000",
        "shortCode": "A042420",
        "codeName": "네오위즈홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7085910008",
        "shortCode": "A085910",
        "codeName": "네오티스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092730001",
        "shortCode": "A092730",
        "codeName": "네오팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7290660000",
        "shortCode": "A290660",
        "codeName": "네오펙트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7153460001",
        "shortCode": "A153460",
        "codeName": "네이블",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007390008",
        "shortCode": "A007390",
        "codeName": "네이처셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086220001",
        "shortCode": "A086220",
        "codeName": "네추럴FNP",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7033640004",
        "shortCode": "A033640",
        "codeName": "네패스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7087730008",
        "shortCode": "A087730",
        "codeName": "네패스신소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005720008",
        "shortCode": "A005720",
        "codeName": "넥센",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005721006",
        "shortCode": "A005725",
        "codeName": "넥센우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002350007",
        "shortCode": "A002350",
        "codeName": "넥센타이어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002351005",
        "shortCode": "A002355",
        "codeName": "넥센타이어1우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7089140008",
        "shortCode": "A089140",
        "codeName": "넥스턴",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065170003",
        "shortCode": "A065170",
        "codeName": "넥스트BT",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003580008",
        "shortCode": "A003580",
        "codeName": "넥스트사이언스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7137940003",
        "shortCode": "A137940",
        "codeName": "넥스트아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041140005",
        "shortCode": "A041140",
        "codeName": "넥슨지티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217270008",
        "shortCode": "A217270",
        "codeName": "넵튠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225570001",
        "shortCode": "A225570",
        "codeName": "넷게임즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7251270005",
        "shortCode": "A251270",
        "codeName": "넷마블",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7104620000",
        "shortCode": "A104620",
        "codeName": "노랑풍선",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090350000",
        "shortCode": "A090350",
        "codeName": "노루페인트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7090351008",
        "shortCode": "A090355",
        "codeName": "노루페인트우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000320002",
        "shortCode": "A000320",
        "codeName": "노루홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000321000",
        "shortCode": "A000325",
        "codeName": "노루홀딩스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7194700001",
        "shortCode": "A194700",
        "codeName": "노바렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7285490009",
        "shortCode": "A285490",
        "codeName": "노바텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7229500004",
        "shortCode": "A229500",
        "codeName": "노브메타파마",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7006280002",
        "shortCode": "A006280",
        "codeName": "녹십자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7144510005",
        "shortCode": "A144510",
        "codeName": "녹십자랩셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7031390008",
        "shortCode": "A031390",
        "codeName": "녹십자셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7142280007",
        "shortCode": "A142280",
        "codeName": "녹십자엠에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005250006",
        "shortCode": "A005250",
        "codeName": "녹십자홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005252002",
        "shortCode": "A005257",
        "codeName": "녹십자홀딩스2우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7065560005",
        "shortCode": "A065560",
        "codeName": "녹원씨엔아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004370003",
        "shortCode": "A004370",
        "codeName": "농심",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7072710007",
        "shortCode": "A072710",
        "codeName": "농심홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7054050000",
        "shortCode": "A054050",
        "codeName": "농우바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7040160004",
        "shortCode": "A040160",
        "codeName": "누리텔레콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069140002",
        "shortCode": "A069140",
        "codeName": "누리플랜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7126870005",
        "shortCode": "A126870",
        "codeName": "뉴로스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060260007",
        "shortCode": "A060260",
        "codeName": "뉴보텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012340006",
        "shortCode": "A012340",
        "codeName": "뉴인텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214870008",
        "shortCode": "A214870",
        "codeName": "뉴지랩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7270870009",
        "shortCode": "A270870",
        "codeName": "뉴트리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7144960002",
        "shortCode": "A144960",
        "codeName": "뉴파워프라즈마",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "USU652221081",
        "shortCode": "A900100",
        "codeName": "뉴프라이드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7085670008",
        "shortCode": "A085670",
        "codeName": "뉴프렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7119860005",
        "shortCode": "A119860",
        "codeName": "다나와",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064260003",
        "shortCode": "A064260",
        "codeName": "다날",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093640001",
        "shortCode": "A093640",
        "codeName": "다믈멀티미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039560008",
        "shortCode": "A039560",
        "codeName": "다산네트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058730003",
        "shortCode": "A058730",
        "codeName": "다스코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023590003",
        "shortCode": "A023590",
        "codeName": "다우기술",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032190001",
        "shortCode": "A032190",
        "codeName": "다우데이타",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7323350009",
        "shortCode": "A323350",
        "codeName": "다원넥스뷰",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7068240001",
        "shortCode": "A068240",
        "codeName": "다원시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086080009",
        "shortCode": "A086080",
        "codeName": "다이노나",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7271850000",
        "shortCode": "A271850",
        "codeName": "다이오진",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7019680008",
        "shortCode": "A019680",
        "codeName": "대교",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7019681006",
        "shortCode": "A019685",
        "codeName": "대교우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006370001",
        "shortCode": "A006370",
        "codeName": "대구백화점",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008060006",
        "shortCode": "A008060",
        "codeName": "대덕전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR700806K010",
        "shortCode": "A00806K",
        "codeName": "대덕전자1우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7178600003",
        "shortCode": "A178600",
        "codeName": "대동고려삼",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7000490003",
        "shortCode": "A000490",
        "codeName": "대동공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7020400008",
        "shortCode": "A020400",
        "codeName": "대동금속",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008830002",
        "shortCode": "A008830",
        "codeName": "대동기어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7048470009",
        "shortCode": "A048470",
        "codeName": "대동스틸",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008110009",
        "shortCode": "A008110",
        "codeName": "대동전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004780003",
        "shortCode": "A004780",
        "codeName": "대륙제관",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005750005",
        "shortCode": "A005750",
        "codeName": "대림B&Co",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000210005",
        "shortCode": "A000210",
        "codeName": "대림산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000211003",
        "shortCode": "A000215",
        "codeName": "대림산업우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004440004",
        "shortCode": "A004440",
        "codeName": "대림씨엔에스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017650003",
        "shortCode": "A017650",
        "codeName": "대림제지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006570006",
        "shortCode": "A006570",
        "codeName": "대림통상",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007720006",
        "shortCode": "A007720",
        "codeName": "대명코퍼레이션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7317850006",
        "shortCode": "A317850",
        "codeName": "대모",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7290670009",
        "shortCode": "A290670",
        "codeName": "대보마그네틱",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078140001",
        "shortCode": "A078140",
        "codeName": "대봉엘에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001680008",
        "shortCode": "A001680",
        "codeName": "대상",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001681006",
        "shortCode": "A001685",
        "codeName": "대상우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7084690007",
        "shortCode": "A084690",
        "codeName": "대상홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7084691005",
        "shortCode": "A084695",
        "codeName": "대상홀딩스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036480002",
        "shortCode": "A036480",
        "codeName": "대성미생물",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7128820008",
        "shortCode": "A128820",
        "codeName": "대성산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7117580001",
        "shortCode": "A117580",
        "codeName": "대성에너지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025440009",
        "shortCode": "A025440",
        "codeName": "대성엘텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7027830009",
        "shortCode": "A027830",
        "codeName": "대성창투",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7104040001",
        "shortCode": "A104040",
        "codeName": "대성파인텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016710006",
        "shortCode": "A016710",
        "codeName": "대성홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7262830003",
        "shortCode": "A262830",
        "codeName": "대신밸런스제4호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7303030001",
        "shortCode": "A303030",
        "codeName": "대신밸런스제5호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307750000",
        "shortCode": "A307750",
        "codeName": "대신밸런스제6호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7020180006",
        "shortCode": "A020180",
        "codeName": "대신정보통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003540002",
        "shortCode": "A003540",
        "codeName": "대신증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003542008",
        "shortCode": "A003547",
        "codeName": "대신증권2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003541000",
        "shortCode": "A003545",
        "codeName": "대신증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7045390002",
        "shortCode": "A045390",
        "codeName": "대아티아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009190000",
        "shortCode": "A009190",
        "codeName": "대양금속",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7108380007",
        "shortCode": "A108380",
        "codeName": "대양전기공업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006580005",
        "shortCode": "A006580",
        "codeName": "대양제지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014160006",
        "shortCode": "A014160",
        "codeName": "대영포장",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7047040001",
        "shortCode": "A047040",
        "codeName": "대우건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009320003",
        "shortCode": "A009320",
        "codeName": "대우부품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7042660001",
        "shortCode": "A042660",
        "codeName": "대우조선해양",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003090008",
        "shortCode": "A003090",
        "codeName": "대웅",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7069620003",
        "shortCode": "A069620",
        "codeName": "대웅제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007680002",
        "shortCode": "A007680",
        "codeName": "대원",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000430009",
        "shortCode": "A000430",
        "codeName": "대원강업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7311840003",
        "shortCode": "A311840",
        "codeName": "대원모방",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7048910004",
        "shortCode": "A048910",
        "codeName": "대원미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005710009",
        "shortCode": "A005710",
        "codeName": "대원산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006340004",
        "shortCode": "A006340",
        "codeName": "대원전선",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006341002",
        "shortCode": "A006345",
        "codeName": "대원전선우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003220001",
        "shortCode": "A003220",
        "codeName": "대원제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024890006",
        "shortCode": "A024890",
        "codeName": "대원화성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7290380005",
        "shortCode": "A290380",
        "codeName": "대유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002880003",
        "shortCode": "A002880",
        "codeName": "대유에이텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7290120005",
        "shortCode": "A290120",
        "codeName": "대유에이피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000300004",
        "shortCode": "A000300",
        "codeName": "대유플러스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7120240007",
        "shortCode": "A120240",
        "codeName": "대정화금",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003310000",
        "shortCode": "A003310",
        "codeName": "대주산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114920002",
        "shortCode": "A114920",
        "codeName": "대주이엔티",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7078600004",
        "shortCode": "A078600",
        "codeName": "대주전자재료",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012800009",
        "shortCode": "A012800",
        "codeName": "대창",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7015230006",
        "shortCode": "A015230",
        "codeName": "대창단조",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7096350004",
        "shortCode": "A096350",
        "codeName": "대창솔루션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140520008",
        "shortCode": "A140520",
        "codeName": "대창스틸",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131220006",
        "shortCode": "A131220",
        "codeName": "대한과학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010170009",
        "shortCode": "A010170",
        "codeName": "대한광통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054670005",
        "shortCode": "A054670",
        "codeName": "대한뉴팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001070002",
        "shortCode": "A001070",
        "codeName": "대한방직",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023910003",
        "shortCode": "A023910",
        "codeName": "대한약품",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006650006",
        "shortCode": "A006650",
        "codeName": "대한유화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001440007",
        "shortCode": "A001440",
        "codeName": "대한전선",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7084010008",
        "shortCode": "A084010",
        "codeName": "대한제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001790005",
        "shortCode": "A001790",
        "codeName": "대한제당",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001793009",
        "shortCode": "A001799",
        "codeName": "대한제당3우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001791003",
        "shortCode": "A001795",
        "codeName": "대한제당우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001130004",
        "shortCode": "A001130",
        "codeName": "대한제분",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003490000",
        "shortCode": "A003490",
        "codeName": "대한항공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003491008",
        "shortCode": "A003495",
        "codeName": "대한항공우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005880000",
        "shortCode": "A005880",
        "codeName": "대한해운",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003830007",
        "shortCode": "A003830",
        "codeName": "대한화섬",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016090003",
        "shortCode": "A016090",
        "codeName": "대현",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7069460004",
        "shortCode": "A069460",
        "codeName": "대호에이엘",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7021040001",
        "shortCode": "A021040",
        "codeName": "대호피앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7021041009",
        "shortCode": "A021045",
        "codeName": "대호피앤씨우",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067080002",
        "shortCode": "A067080",
        "codeName": "대화제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7192080000",
        "shortCode": "A192080",
        "codeName": "더블유게임즈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7035290006",
        "shortCode": "A035290",
        "codeName": "더블유에프엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012510004",
        "shortCode": "A012510",
        "codeName": "더존비즈온",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7302920004",
        "shortCode": "A302920",
        "codeName": "더콘텐츠온",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7213420003",
        "shortCode": "A213420",
        "codeName": "덕산네오룩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7077360006",
        "shortCode": "A077360",
        "codeName": "덕산하이메탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004830006",
        "shortCode": "A004830",
        "codeName": "덕성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004831004",
        "shortCode": "A004835",
        "codeName": "덕성우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7090410002",
        "shortCode": "A090410",
        "codeName": "덕신하우징",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024900003",
        "shortCode": "A024900",
        "codeName": "덕양산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7263600009",
        "shortCode": "A263600",
        "codeName": "덕우전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7194480000",
        "shortCode": "A194480",
        "codeName": "데브시스터즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263800005",
        "shortCode": "A263800",
        "codeName": "데이타솔루션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7199150004",
        "shortCode": "A199150",
        "codeName": "데이터스트림즈",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7139050009",
        "shortCode": "A139050",
        "codeName": "데일리블록체인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017680000",
        "shortCode": "A017680",
        "codeName": "데코앤이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7206560005",
        "shortCode": "A206560",
        "codeName": "덱스터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7145720009",
        "shortCode": "A145720",
        "codeName": "덴티움",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7067990002",
        "shortCode": "A067990",
        "codeName": "도이치모터스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002150001",
        "shortCode": "A002150",
        "codeName": "도화엔지니어링",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006620009",
        "shortCode": "A006620",
        "codeName": "동구바이오제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7100130004",
        "shortCode": "A100130",
        "codeName": "동국S&C",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005160007",
        "shortCode": "A005160",
        "codeName": "동국산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7075970004",
        "shortCode": "A075970",
        "codeName": "동국알앤에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001230002",
        "shortCode": "A001230",
        "codeName": "동국제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7086450004",
        "shortCode": "A086450",
        "codeName": "동국제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023450000",
        "shortCode": "A023450",
        "codeName": "동남합성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004140000",
        "shortCode": "A004140",
        "codeName": "동방",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7099410003",
        "shortCode": "A099410",
        "codeName": "동방선기",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007590003",
        "shortCode": "A007590",
        "codeName": "동방아그로",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005960000",
        "shortCode": "A005960",
        "codeName": "동부건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005961008",
        "shortCode": "A005965",
        "codeName": "동부건설우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7281740001",
        "shortCode": "A281740",
        "codeName": "동부스팩5호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016380008",
        "shortCode": "A016380",
        "codeName": "동부제철",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016381006",
        "shortCode": "A016385",
        "codeName": "동부제철우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7083370007",
        "shortCode": "A083370",
        "codeName": "동북아12호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7083380006",
        "shortCode": "A083380",
        "codeName": "동북아13호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7026960005",
        "shortCode": "A026960",
        "codeName": "동서",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002210003",
        "shortCode": "A002210",
        "codeName": "동성제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7102260007",
        "shortCode": "A102260",
        "codeName": "동성코퍼레이션",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033500000",
        "shortCode": "A033500",
        "codeName": "동성화인텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005190004",
        "shortCode": "A005190",
        "codeName": "동성화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025950007",
        "shortCode": "A025950",
        "codeName": "동신건설",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000640003",
        "shortCode": "A000640",
        "codeName": "동아쏘시오홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7170900005",
        "shortCode": "A170900",
        "codeName": "동아에스티",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7088130000",
        "shortCode": "A088130",
        "codeName": "동아엘텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7028100006",
        "shortCode": "A028100",
        "codeName": "동아지질",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7282690007",
        "shortCode": "A282690",
        "codeName": "동아타이어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7041930009",
        "shortCode": "A041930",
        "codeName": "동아화성",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001520006",
        "shortCode": "A001520",
        "codeName": "동양",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001522002",
        "shortCode": "A001527",
        "codeName": "동양2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001523000",
        "shortCode": "A001529",
        "codeName": "동양3우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7084670009",
        "shortCode": "A084670",
        "codeName": "동양고속",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7030790000",
        "shortCode": "A030790",
        "codeName": "동양네트웍스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002900009",
        "shortCode": "A002900",
        "codeName": "동양물산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7082640004",
        "shortCode": "A082640",
        "codeName": "동양생명",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7060380003",
        "shortCode": "A060380",
        "codeName": "동양에스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001521004",
        "shortCode": "A001525",
        "codeName": "동양우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079960001",
        "shortCode": "A079960",
        "codeName": "동양이엔피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008970006",
        "shortCode": "A008970",
        "codeName": "동양철관",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7228340006",
        "shortCode": "A228340",
        "codeName": "동양파일",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092780006",
        "shortCode": "A092780",
        "codeName": "동양피스톤",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7104460001",
        "shortCode": "A104460",
        "codeName": "동양피엔에프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088910005",
        "shortCode": "A088910",
        "codeName": "동우팜투테이블",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094170008",
        "shortCode": "A094170",
        "codeName": "동운아나텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049770001",
        "shortCode": "A049770",
        "codeName": "동원F&B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7013120001",
        "shortCode": "A013120",
        "codeName": "동원개발",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018500009",
        "shortCode": "A018500",
        "codeName": "동원금속",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006040000",
        "shortCode": "A006040",
        "codeName": "동원산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7030720007",
        "shortCode": "A030720",
        "codeName": "동원수산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014820005",
        "shortCode": "A014820",
        "codeName": "동원시스템즈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014821003",
        "shortCode": "A014825",
        "codeName": "동원시스템즈우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7163560006",
        "shortCode": "A163560",
        "codeName": "동일고무벨트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7109860007",
        "shortCode": "A109860",
        "codeName": "동일금속",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032960007",
        "shortCode": "A032960",
        "codeName": "동일기연",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004890000",
        "shortCode": "A004890",
        "codeName": "동일산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002690006",
        "shortCode": "A002690",
        "codeName": "동일제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023790009",
        "shortCode": "A023790",
        "codeName": "동일철강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005290002",
        "shortCode": "A005290",
        "codeName": "동진쎄미켐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025900002",
        "shortCode": "A025900",
        "codeName": "동화기업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000020008",
        "shortCode": "A000020",
        "codeName": "동화약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000150003",
        "shortCode": "A000150",
        "codeName": "두산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000152009",
        "shortCode": "A000157",
        "codeName": "두산2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011160009",
        "shortCode": "A011160",
        "codeName": "두산건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7241560002",
        "shortCode": "A241560",
        "codeName": "두산밥캣",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000151001",
        "shortCode": "A000155",
        "codeName": "두산우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7042670000",
        "shortCode": "A042670",
        "codeName": "두산인프라코어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034020008",
        "shortCode": "A034020",
        "codeName": "두산중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016740003",
        "shortCode": "A016740",
        "codeName": "두올",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7078590007",
        "shortCode": "A078590",
        "codeName": "두올산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7270020001",
        "shortCode": "A270020",
        "codeName": "두원석재",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7073190001",
        "shortCode": "A073190",
        "codeName": "듀오백",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7176750008",
        "shortCode": "A176750",
        "codeName": "듀켐바이오",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7030350003",
        "shortCode": "A030350",
        "codeName": "드래곤플라이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7203650007",
        "shortCode": "A203650",
        "codeName": "드림시큐리티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060570009",
        "shortCode": "A060570",
        "codeName": "드림어스컴퍼니",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7192650000",
        "shortCode": "A192650",
        "codeName": "드림텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7220110001",
        "shortCode": "A220110",
        "codeName": "드림티엔터테인먼트",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7217620004",
        "shortCode": "A217620",
        "codeName": "디딤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7187870001",
        "shortCode": "A187870",
        "codeName": "디바이스이엔지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066670001",
        "shortCode": "A066670",
        "codeName": "디스플레이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024090003",
        "shortCode": "A024090",
        "codeName": "디씨엠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003160009",
        "shortCode": "A003160",
        "codeName": "디아이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7092200005",
        "shortCode": "A092200",
        "codeName": "디아이씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7110990009",
        "shortCode": "A110990",
        "codeName": "디아이티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263690000",
        "shortCode": "A263690",
        "codeName": "디알젬",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214680001",
        "shortCode": "A214680",
        "codeName": "디알텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263720005",
        "shortCode": "A263720",
        "codeName": "디앤씨미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7109740001",
        "shortCode": "A109740",
        "codeName": "디에스케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033430000",
        "shortCode": "A033430",
        "codeName": "디에스티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131030009",
        "shortCode": "A131030",
        "codeName": "디에이치피코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7196490007",
        "shortCode": "A196490",
        "codeName": "디에이테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066900002",
        "shortCode": "A066900",
        "codeName": "디에이피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7127120004",
        "shortCode": "A127120",
        "codeName": "디엔에이링크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092070002",
        "shortCode": "A092070",
        "codeName": "디엔에프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7134580000",
        "shortCode": "A134580",
        "codeName": "디엠티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039840004",
        "shortCode": "A039840",
        "codeName": "디오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7196450001",
        "shortCode": "A196450",
        "codeName": "디오스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013570007",
        "shortCode": "A013570",
        "codeName": "디와이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7210540001",
        "shortCode": "A210540",
        "codeName": "디와이파워",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079810008",
        "shortCode": "A079810",
        "codeName": "디이엔티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7227100005",
        "shortCode": "A227100",
        "codeName": "디자인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7113810006",
        "shortCode": "A113810",
        "codeName": "디젠스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043360007",
        "shortCode": "A043360",
        "codeName": "디지아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7197140007",
        "shortCode": "A197140",
        "codeName": "디지캡",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7106520000",
        "shortCode": "A106520",
        "codeName": "디지탈옵틱",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7068930007",
        "shortCode": "A068930",
        "codeName": "디지털대성",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033130006",
        "shortCode": "A033130",
        "codeName": "디지틀조선",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033310004",
        "shortCode": "A033310",
        "codeName": "디케이디앤아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7105740005",
        "shortCode": "A105740",
        "codeName": "디케이락",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263020000",
        "shortCode": "A263020",
        "codeName": "디케이앤디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7290550003",
        "shortCode": "A290550",
        "codeName": "디케이티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007340003",
        "shortCode": "A007340",
        "codeName": "디티알오토모티브",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7187220009",
        "shortCode": "A187220",
        "codeName": "디티앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7026890004",
        "shortCode": "A026890",
        "codeName": "디피씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7163430002",
        "shortCode": "A163430",
        "codeName": "디피코",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7131180002",
        "shortCode": "A131180",
        "codeName": "딜리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042510008",
        "shortCode": "A042510",
        "codeName": "라온시큐어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7232680009",
        "shortCode": "A232680",
        "codeName": "라온테크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7050120005",
        "shortCode": "A050120",
        "codeName": "라이브플렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7171120009",
        "shortCode": "A171120",
        "codeName": "라이온켐텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069540003",
        "shortCode": "A069540",
        "codeName": "라이트론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7285770004",
        "shortCode": "A285770",
        "codeName": "라이프사이언스테크놀로지",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7115390007",
        "shortCode": "A115390",
        "codeName": "락앤락",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7200350007",
        "shortCode": "A200350",
        "codeName": "래몽래인",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7171010002",
        "shortCode": "A171010",
        "codeName": "램테크놀러지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084650001",
        "shortCode": "A084650",
        "codeName": "랩지노믹스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217500008",
        "shortCode": "A217500",
        "codeName": "러셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092590009",
        "shortCode": "A092590",
        "codeName": "럭스피아",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7033600008",
        "shortCode": "A033600",
        "codeName": "럭슬",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7141080002",
        "shortCode": "A141080",
        "codeName": "레고켐바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060300001",
        "shortCode": "A060300",
        "codeName": "레드로버",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038390001",
        "shortCode": "A038390",
        "codeName": "레드캡투어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7228850004",
        "shortCode": "A228850",
        "codeName": "레이언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7238120000",
        "shortCode": "A238120",
        "codeName": "로고스바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215100009",
        "shortCode": "A215100",
        "codeName": "로보로보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090360009",
        "shortCode": "A090360",
        "codeName": "로보스타",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7238500003",
        "shortCode": "A238500",
        "codeName": "로보쓰리",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7108490004",
        "shortCode": "A108490",
        "codeName": "로보티즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "HK0000295359",
        "shortCode": "A900260",
        "codeName": "로스웰",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067730002",
        "shortCode": "A067730",
        "codeName": "로지시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7071280002",
        "shortCode": "A071280",
        "codeName": "로체시스템즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032350001",
        "shortCode": "A032350",
        "codeName": "롯데관광개발",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000400002",
        "shortCode": "A000400",
        "codeName": "롯데손해보험",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023530009",
        "shortCode": "A023530",
        "codeName": "롯데쇼핑",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004000006",
        "shortCode": "A004000",
        "codeName": "롯데정밀화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7286940002",
        "shortCode": "A286940",
        "codeName": "롯데정보통신",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7280360009",
        "shortCode": "A280360",
        "codeName": "롯데제과",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004990008",
        "shortCode": "A004990",
        "codeName": "롯데지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR700499K014",
        "shortCode": "A00499K",
        "codeName": "롯데지주우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005300009",
        "shortCode": "A005300",
        "codeName": "롯데칠성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005301007",
        "shortCode": "A005305",
        "codeName": "롯데칠성우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011170008",
        "shortCode": "A011170",
        "codeName": "롯데케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002270007",
        "shortCode": "A002270",
        "codeName": "롯데푸드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7071840003",
        "shortCode": "A071840",
        "codeName": "롯데하이마트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7038060000",
        "shortCode": "A038060",
        "codeName": "루멘스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7082800004",
        "shortCode": "A082800",
        "codeName": "루미마이크로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7162120000",
        "shortCode": "A162120",
        "codeName": "루켄테크놀러지스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7085370005",
        "shortCode": "A085370",
        "codeName": "루트로닉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR708537K039",
        "shortCode": "A08537M",
        "codeName": "루트로닉3우C",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060240009",
        "shortCode": "A060240",
        "codeName": "룽투코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058470006",
        "shortCode": "A058470",
        "codeName": "리노공업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039980008",
        "shortCode": "A039980",
        "codeName": "리노스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019570001",
        "shortCode": "A019570",
        "codeName": "리더스 기술투자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016100000",
        "shortCode": "A016100",
        "codeName": "리더스코스메틱",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7197210008",
        "shortCode": "A197210",
        "codeName": "리드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012700001",
        "shortCode": "A012700",
        "codeName": "리드코프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7302550009",
        "shortCode": "A302550",
        "codeName": "리메드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7131100000",
        "shortCode": "A131100",
        "codeName": "리켐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215090002",
        "shortCode": "A215090",
        "codeName": "리퓨어유니맥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7277070009",
        "shortCode": "A277070",
        "codeName": "린드먼아시아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042500009",
        "shortCode": "A042500",
        "codeName": "링네트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7219420007",
        "shortCode": "A219420",
        "codeName": "링크제니시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7027740000",
        "shortCode": "A027740",
        "codeName": "마니커",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7305090003",
        "shortCode": "A305090",
        "codeName": "마이크로디지탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7098120009",
        "shortCode": "A098120",
        "codeName": "마이크로컨텍솔",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7227950003",
        "shortCode": "A227950",
        "codeName": "마이크로텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7147760003",
        "shortCode": "A147760",
        "codeName": "마이크로프랜드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038290003",
        "shortCode": "A038290",
        "codeName": "마크로젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7204320006",
        "shortCode": "A204320",
        "codeName": "만도",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001080001",
        "shortCode": "A001080",
        "codeName": "만호제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7267980001",
        "shortCode": "A267980",
        "codeName": "매일유업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005990007",
        "shortCode": "A005990",
        "codeName": "매일홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7127160000",
        "shortCode": "A127160",
        "codeName": "매직마이크로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093520005",
        "shortCode": "A093520",
        "codeName": "매커스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7141070003",
        "shortCode": "A141070",
        "codeName": "맥스로텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088980008",
        "shortCode": "A088980",
        "codeName": "맥쿼리인프라",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7094800000",
        "shortCode": "A094800",
        "codeName": "맵스리얼티1",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7100590009",
        "shortCode": "A100590",
        "codeName": "머큐리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067280008",
        "shortCode": "A067280",
        "codeName": "멀티캠퍼스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7072870009",
        "shortCode": "A072870",
        "codeName": "메가스터디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215200007",
        "shortCode": "A215200",
        "codeName": "메가스터디교육",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7133750000",
        "shortCode": "A133750",
        "codeName": "메가엠디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7200580009",
        "shortCode": "A200580",
        "codeName": "메디쎄이",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7041920000",
        "shortCode": "A041920",
        "codeName": "메디아나",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7233250000",
        "shortCode": "A233250",
        "codeName": "메디안디노스틱",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7236340006",
        "shortCode": "A236340",
        "codeName": "메디젠휴먼케어",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7086900008",
        "shortCode": "A086900",
        "codeName": "메디톡스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015540008",
        "shortCode": "A015540",
        "codeName": "메디파트너생명공학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7078160009",
        "shortCode": "A078160",
        "codeName": "메디포스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065650004",
        "shortCode": "A065650",
        "codeName": "메디프론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138040001",
        "shortCode": "A138040",
        "codeName": "메리츠금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008560005",
        "shortCode": "A008560",
        "codeName": "메리츠종금증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000060004",
        "shortCode": "A000060",
        "codeName": "메리츠화재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7021880000",
        "shortCode": "A021880",
        "codeName": "메이슨캐피탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140410002",
        "shortCode": "A140410",
        "codeName": "메지온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241770007",
        "shortCode": "A241770",
        "codeName": "메카로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090370008",
        "shortCode": "A090370",
        "codeName": "메타랩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7059210005",
        "shortCode": "A059210",
        "codeName": "메타바이오메드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058110008",
        "shortCode": "A058110",
        "codeName": "멕아이씨에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7096640008",
        "shortCode": "A096640",
        "codeName": "멜파스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017180001",
        "shortCode": "A017180",
        "codeName": "명문제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7257370007",
        "shortCode": "A257370",
        "codeName": "명성티엔에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7267060002",
        "shortCode": "A267060",
        "codeName": "명진홀딩스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7012690004",
        "shortCode": "A012690",
        "codeName": "모나리자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005360003",
        "shortCode": "A005360",
        "codeName": "모나미",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7149940009",
        "shortCode": "A149940",
        "codeName": "모다",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080420003",
        "shortCode": "A080420",
        "codeName": "모다이노칩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080160005",
        "shortCode": "A080160",
        "codeName": "모두투어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7204210009",
        "shortCode": "A204210",
        "codeName": "모두투어리츠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7100030006",
        "shortCode": "A100030",
        "codeName": "모바일리더",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7087260006",
        "shortCode": "A087260",
        "codeName": "모바일어플라이언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101330009",
        "shortCode": "A101330",
        "codeName": "모베이스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7250060001",
        "shortCode": "A250060",
        "codeName": "모비스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033200007",
        "shortCode": "A033200",
        "codeName": "모아텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009680000",
        "shortCode": "A009680",
        "codeName": "모토닉",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7118990001",
        "shortCode": "A118990",
        "codeName": "모트렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006920003",
        "shortCode": "A006920",
        "codeName": "모헨즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009580002",
        "shortCode": "A009580",
        "codeName": "무림P&P",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001810001",
        "shortCode": "A001810",
        "codeName": "무림SP",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009200007",
        "shortCode": "A009200",
        "codeName": "무림페이퍼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033920000",
        "shortCode": "A033920",
        "codeName": "무학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008420002",
        "shortCode": "A008420",
        "codeName": "문배철강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7279600001",
        "shortCode": "A279600",
        "codeName": "미디어젠",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7028040004",
        "shortCode": "A028040",
        "codeName": "미래SCI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095500005",
        "shortCode": "A095500",
        "codeName": "미래나노텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025560004",
        "shortCode": "A025560",
        "codeName": "미래산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7218150001",
        "shortCode": "A218150",
        "codeName": "미래생명자원",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007120009",
        "shortCode": "A007120",
        "codeName": "미래아이앤지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006800007",
        "shortCode": "A006800",
        "codeName": "미래에셋대우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR700680K019",
        "shortCode": "A00680K",
        "codeName": "미래에셋대우2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7265480004",
        "shortCode": "A265480",
        "codeName": "미래에셋대우스팩1호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7310200001",
        "shortCode": "A310200",
        "codeName": "미래에셋대우스팩2호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006801005",
        "shortCode": "A006805",
        "codeName": "미래에셋대우우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7100790005",
        "shortCode": "A100790",
        "codeName": "미래에셋벤처투자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7085620003",
        "shortCode": "A085620",
        "codeName": "미래에셋생명",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7049950009",
        "shortCode": "A049950",
        "codeName": "미래컴퍼니",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7213090004",
        "shortCode": "A213090",
        "codeName": "미래테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7207760000",
        "shortCode": "A207760",
        "codeName": "미스터블루",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225850007",
        "shortCode": "A225850",
        "codeName": "미애부",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7002840007",
        "shortCode": "A002840",
        "codeName": "미원상사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7268280005",
        "shortCode": "A268280",
        "codeName": "미원에스씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7107590002",
        "shortCode": "A107590",
        "codeName": "미원홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7134380005",
        "shortCode": "A134380",
        "codeName": "미원화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003650009",
        "shortCode": "A003650",
        "codeName": "미창석유",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7059090001",
        "shortCode": "A059090",
        "codeName": "미코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214610008",
        "shortCode": "A214610",
        "codeName": "미코바이오메드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7201490000",
        "shortCode": "A201490",
        "codeName": "미투온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214180002",
        "shortCode": "A214180",
        "codeName": "민앤지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7155900004",
        "shortCode": "A155900",
        "codeName": "바다로19호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7206640005",
        "shortCode": "A206640",
        "codeName": "바디텍메드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018700005",
        "shortCode": "A018700",
        "codeName": "바른손",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035620004",
        "shortCode": "A035620",
        "codeName": "바른손이앤에이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064520000",
        "shortCode": "A064520",
        "codeName": "바른전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7029480001",
        "shortCode": "A029480",
        "codeName": "바른테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053030003",
        "shortCode": "A053030",
        "codeName": "바이넥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064550007",
        "shortCode": "A064550",
        "codeName": "바이오니아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208710004",
        "shortCode": "A208710",
        "codeName": "바이오로그디바이스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7142760008",
        "shortCode": "A142760",
        "codeName": "바이오리더스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065940009",
        "shortCode": "A065940",
        "codeName": "바이오빌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086820008",
        "shortCode": "A086820",
        "codeName": "바이오솔루션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038460002",
        "shortCode": "A038460",
        "codeName": "바이오스마트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7281310003",
        "shortCode": "A281310",
        "codeName": "바이오시네틱스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7044480002",
        "shortCode": "A044480",
        "codeName": "바이오제네틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7216400002",
        "shortCode": "A216400",
        "codeName": "바이오코아",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7086040003",
        "shortCode": "A086040",
        "codeName": "바이오톡스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7199290008",
        "shortCode": "A199290",
        "codeName": "바이오프로테크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7032980005",
        "shortCode": "A032980",
        "codeName": "바이온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7222160004",
        "shortCode": "A222160",
        "codeName": "바이옵트로",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7043150002",
        "shortCode": "A043150",
        "codeName": "바텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003610003",
        "shortCode": "A003610",
        "codeName": "방림",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7267790004",
        "shortCode": "A267790",
        "codeName": "배럴",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001340009",
        "shortCode": "A001340",
        "codeName": "백광산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014580005",
        "shortCode": "A014580",
        "codeName": "백광소재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7046310009",
        "shortCode": "A046310",
        "codeName": "백금T&A",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035150002",
        "shortCode": "A035150",
        "codeName": "백산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036620003",
        "shortCode": "A036620",
        "codeName": "버추얼텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066410002",
        "shortCode": "A066410",
        "codeName": "버킷스튜디오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002410009",
        "shortCode": "A002410",
        "codeName": "범양건영",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7019010008",
        "shortCode": "A019010",
        "codeName": "베뉴지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7177350006",
        "shortCode": "A177350",
        "codeName": "베셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7299910000",
        "shortCode": "A299910",
        "codeName": "베스파",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7096300009",
        "shortCode": "A096300",
        "codeName": "베트남개발1",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007210008",
        "shortCode": "A007210",
        "codeName": "벽산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7225530005",
        "shortCode": "A225530",
        "codeName": "보광산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7250000007",
        "shortCode": "A250000",
        "codeName": "보라티알",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002760007",
        "shortCode": "A002760",
        "codeName": "보락",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014100002",
        "shortCode": "A014100",
        "codeName": "보령메디앙스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003850005",
        "shortCode": "A003850",
        "codeName": "보령제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006910004",
        "shortCode": "A006910",
        "codeName": "보성파워텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000890004",
        "shortCode": "A000890",
        "codeName": "보해양조",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7226340008",
        "shortCode": "A226340",
        "codeName": "본느",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7206950008",
        "shortCode": "A206950",
        "codeName": "볼빅",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7003000007",
        "shortCode": "A003000",
        "codeName": "부광약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001270008",
        "shortCode": "A001270",
        "codeName": "부국증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001271006",
        "shortCode": "A001275",
        "codeName": "부국증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7026940007",
        "shortCode": "A026940",
        "codeName": "부국철강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014470009",
        "shortCode": "A014470",
        "codeName": "부방",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015350002",
        "shortCode": "A015350",
        "codeName": "부산가스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011390002",
        "shortCode": "A011390",
        "codeName": "부산산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005030002",
        "shortCode": "A005030",
        "codeName": "부산주공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008470007",
        "shortCode": "A008470",
        "codeName": "부스타",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7100120005",
        "shortCode": "A100120",
        "codeName": "뷰웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066980004",
        "shortCode": "A066980",
        "codeName": "브레인콘텐츠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064480007",
        "shortCode": "A064480",
        "codeName": "브리지텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7251630000",
        "shortCode": "A251630",
        "codeName": "브이원텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263920001",
        "shortCode": "A263920",
        "codeName": "블러썸엠앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033560004",
        "shortCode": "A033560",
        "codeName": "블루콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7126340009",
        "shortCode": "A126340",
        "codeName": "비나텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7121800007",
        "shortCode": "A121800",
        "codeName": "비덴트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7148140007",
        "shortCode": "A148140",
        "codeName": "비디아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7100220003",
        "shortCode": "A100220",
        "codeName": "비상교육",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7200780005",
        "shortCode": "A200780",
        "codeName": "비씨월드제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7141000000",
        "shortCode": "A141000",
        "codeName": "비아트론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090460007",
        "shortCode": "A090460",
        "codeName": "비에이치",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083650002",
        "shortCode": "A083650",
        "codeName": "비에이치아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215050006",
        "shortCode": "A215050",
        "codeName": "비엔디생활건강",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7271780009",
        "shortCode": "A271780",
        "codeName": "비엔에프코퍼레이션",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7086670007",
        "shortCode": "A086670",
        "codeName": "비엠티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138580006",
        "shortCode": "A138580",
        "codeName": "비즈니스온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7082920000",
        "shortCode": "A082920",
        "codeName": "비츠로셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054220009",
        "shortCode": "A054220",
        "codeName": "비츠로시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042370007",
        "shortCode": "A042370",
        "codeName": "비츠로테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032850000",
        "shortCode": "A032850",
        "codeName": "비트컴퓨터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101140002",
        "shortCode": "A101140",
        "codeName": "비티원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7148780000",
        "shortCode": "A148780",
        "codeName": "비플라이소프트",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7238200000",
        "shortCode": "A238200",
        "codeName": "비피도",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093190007",
        "shortCode": "A093190",
        "codeName": "빅솔론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065450009",
        "shortCode": "A065450",
        "codeName": "빅텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7210120002",
        "shortCode": "A210120",
        "codeName": "빅텐츠",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7005180005",
        "shortCode": "A005180",
        "codeName": "빙그레",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7072950009",
        "shortCode": "A072950",
        "codeName": "빛샘전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7143240000",
        "shortCode": "A143240",
        "codeName": "사람인에이치알",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003960002",
        "shortCode": "A003960",
        "codeName": "사조대림",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008040008",
        "shortCode": "A008040",
        "codeName": "사조동아원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007160005",
        "shortCode": "A007160",
        "codeName": "사조산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014710008",
        "shortCode": "A014710",
        "codeName": "사조씨푸드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006090005",
        "shortCode": "A006090",
        "codeName": "사조오양",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7100090000",
        "shortCode": "A100090",
        "codeName": "삼강엠앤티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005090006",
        "shortCode": "A005090",
        "codeName": "삼광글라스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7122350002",
        "shortCode": "A122350",
        "codeName": "삼기오토모티브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014970008",
        "shortCode": "A014970",
        "codeName": "삼륭물산",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018310003",
        "shortCode": "A018310",
        "codeName": "삼목에스폼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053700001",
        "shortCode": "A053700",
        "codeName": "삼보모터스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009620006",
        "shortCode": "A009620",
        "codeName": "삼보산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023600000",
        "shortCode": "A023600",
        "codeName": "삼보판지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7111870002",
        "shortCode": "A111870",
        "codeName": "삼본전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001470004",
        "shortCode": "A001470",
        "codeName": "삼부토건",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006400006",
        "shortCode": "A006400",
        "codeName": "삼성SDI",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006401004",
        "shortCode": "A006405",
        "codeName": "삼성SDI우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006660005",
        "shortCode": "A006660",
        "codeName": "삼성공조",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7309930006",
        "shortCode": "A309930",
        "codeName": "삼성머스트스팩3호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7028260008",
        "shortCode": "A028260",
        "codeName": "삼성물산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR702826K016",
        "shortCode": "A02826K",
        "codeName": "삼성물산우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7207940008",
        "shortCode": "A207940",
        "codeName": "삼성바이오로직스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032830002",
        "shortCode": "A032830",
        "codeName": "삼성생명",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7291230001",
        "shortCode": "A291230",
        "codeName": "삼성스팩2호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018260000",
        "shortCode": "A018260",
        "codeName": "삼성에스디에스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7028050003",
        "shortCode": "A028050",
        "codeName": "삼성엔지니어링",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009150004",
        "shortCode": "A009150",
        "codeName": "삼성전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009151002",
        "shortCode": "A009155",
        "codeName": "삼성전기우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005930003",
        "shortCode": "A005930",
        "codeName": "삼성전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005931001",
        "shortCode": "A005935",
        "codeName": "삼성전자우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001360007",
        "shortCode": "A001360",
        "codeName": "삼성제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010140002",
        "shortCode": "A010140",
        "codeName": "삼성중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010141000",
        "shortCode": "A010145",
        "codeName": "삼성중공우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016360000",
        "shortCode": "A016360",
        "codeName": "삼성증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7068290006",
        "shortCode": "A068290",
        "codeName": "삼성출판사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7029780004",
        "shortCode": "A029780",
        "codeName": "삼성카드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000810002",
        "shortCode": "A000810",
        "codeName": "삼성화재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000811000",
        "shortCode": "A000815",
        "codeName": "삼성화재우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006110001",
        "shortCode": "A006110",
        "codeName": "삼아알미늄",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009300005",
        "shortCode": "A009300",
        "codeName": "삼아제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7145990008",
        "shortCode": "A145990",
        "codeName": "삼양사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7145991006",
        "shortCode": "A145995",
        "codeName": "삼양사우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003230000",
        "shortCode": "A003230",
        "codeName": "삼양식품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7225190008",
        "shortCode": "A225190",
        "codeName": "삼양옵틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002170009",
        "shortCode": "A002170",
        "codeName": "삼양통상",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7272550005",
        "shortCode": "A272550",
        "codeName": "삼양패키징",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000070003",
        "shortCode": "A000070",
        "codeName": "삼양홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000071001",
        "shortCode": "A000075",
        "codeName": "삼양홀딩스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002810000",
        "shortCode": "A002810",
        "codeName": "삼영무역",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7054540000",
        "shortCode": "A054540",
        "codeName": "삼영엠텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065570004",
        "shortCode": "A065570",
        "codeName": "삼영이엔씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005680004",
        "shortCode": "A005680",
        "codeName": "삼영전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003720000",
        "shortCode": "A003720",
        "codeName": "삼영화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023000003",
        "shortCode": "A023000",
        "codeName": "삼원강재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7073640005",
        "shortCode": "A073640",
        "codeName": "삼원테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004380002",
        "shortCode": "A004380",
        "codeName": "삼익THK",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002450005",
        "shortCode": "A002450",
        "codeName": "삼익악기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032280000",
        "shortCode": "A032280",
        "codeName": "삼일",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002290005",
        "shortCode": "A002290",
        "codeName": "삼일기업공사",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000520007",
        "shortCode": "A000520",
        "codeName": "삼일제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009770009",
        "shortCode": "A009770",
        "codeName": "삼정펄프",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7037460003",
        "shortCode": "A037460",
        "codeName": "삼지전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032750002",
        "shortCode": "A032750",
        "codeName": "삼진",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054090006",
        "shortCode": "A054090",
        "codeName": "삼진엘앤디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005500004",
        "shortCode": "A005500",
        "codeName": "삼진제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000250001",
        "shortCode": "A000250",
        "codeName": "삼천당제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004690004",
        "shortCode": "A004690",
        "codeName": "삼천리",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024950008",
        "shortCode": "A024950",
        "codeName": "삼천리자전거",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038500005",
        "shortCode": "A038500",
        "codeName": "삼표시멘트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017480005",
        "shortCode": "A017480",
        "codeName": "삼현철강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001880004",
        "shortCode": "A001880",
        "codeName": "삼호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010960003",
        "shortCode": "A010960",
        "codeName": "삼호개발",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7046390001",
        "shortCode": "A046390",
        "codeName": "삼화네트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004450003",
        "shortCode": "A004450",
        "codeName": "삼화왕관",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009470006",
        "shortCode": "A009470",
        "codeName": "삼화전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011230000",
        "shortCode": "A011230",
        "codeName": "삼화전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001820000",
        "shortCode": "A001820",
        "codeName": "삼화콘덴서",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000390005",
        "shortCode": "A000390",
        "codeName": "삼화페인트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7027580000",
        "shortCode": "A027580",
        "codeName": "상보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038540001",
        "shortCode": "A038540",
        "codeName": "상상인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307870006",
        "shortCode": "A307870",
        "codeName": "상상인이안1호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101000008",
        "shortCode": "A101000",
        "codeName": "상상인인더스트리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001290006",
        "shortCode": "A001290",
        "codeName": "상상인증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7041650003",
        "shortCode": "A041650",
        "codeName": "상신브레이크",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7091580001",
        "shortCode": "A091580",
        "codeName": "상신이디피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263810004",
        "shortCode": "A263810",
        "codeName": "상신전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089980007",
        "shortCode": "A089980",
        "codeName": "상아프론테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042940007",
        "shortCode": "A042940",
        "codeName": "상지카일룸",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042600007",
        "shortCode": "A042600",
        "codeName": "새로닉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7075180000",
        "shortCode": "A075180",
        "codeName": "새론오토모티브",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7263540007",
        "shortCode": "A263540",
        "codeName": "샘코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007540008",
        "shortCode": "A007540",
        "codeName": "샘표",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7248170003",
        "shortCode": "A248170",
        "codeName": "샘표식품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7038070009",
        "shortCode": "A038070",
        "codeName": "서린바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006730006",
        "shortCode": "A006730",
        "codeName": "서부T&D",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079650008",
        "shortCode": "A079650",
        "codeName": "서산",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7100660000",
        "shortCode": "A100660",
        "codeName": "서암기계공업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007860000",
        "shortCode": "A007860",
        "codeName": "서연",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7200880003",
        "shortCode": "A200880",
        "codeName": "서연이화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012860003",
        "shortCode": "A012860",
        "codeName": "서연전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019770007",
        "shortCode": "A019770",
        "codeName": "서연탑메탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017390006",
        "shortCode": "A017390",
        "codeName": "서울가스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7043710003",
        "shortCode": "A043710",
        "codeName": "서울리거",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7046890000",
        "shortCode": "A046890",
        "codeName": "서울반도체",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004410007",
        "shortCode": "A004410",
        "codeName": "서울식품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004411005",
        "shortCode": "A004415",
        "codeName": "서울식품우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7063170005",
        "shortCode": "A063170",
        "codeName": "서울옥션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7027040005",
        "shortCode": "A027040",
        "codeName": "서울전자통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018680009",
        "shortCode": "A018680",
        "codeName": "서울제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7021050000",
        "shortCode": "A021050",
        "codeName": "서원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7093920007",
        "shortCode": "A093920",
        "codeName": "서원인텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7189860000",
        "shortCode": "A189860",
        "codeName": "서전기전",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7178320008",
        "shortCode": "A178320",
        "codeName": "서진시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122690001",
        "shortCode": "A122690",
        "codeName": "서진오토모티브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140070004",
        "shortCode": "A140070",
        "codeName": "서플러스글로벌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011370004",
        "shortCode": "A011370",
        "codeName": "서한",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065710006",
        "shortCode": "A065710",
        "codeName": "서호전기",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008490005",
        "shortCode": "A008490",
        "codeName": "서흥",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7035890003",
        "shortCode": "A035890",
        "codeName": "서희건설",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003100005",
        "shortCode": "A003100",
        "codeName": "선광",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123420002",
        "shortCode": "A123420",
        "codeName": "선데이토즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007610009",
        "shortCode": "A007610",
        "codeName": "선도전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7067370007",
        "shortCode": "A067370",
        "codeName": "선바이오",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7171090004",
        "shortCode": "A171090",
        "codeName": "선익시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7136490000",
        "shortCode": "A136490",
        "codeName": "선진",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002820009",
        "shortCode": "A002820",
        "codeName": "선창산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014620009",
        "shortCode": "A014620",
        "codeName": "성광벤드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037350006",
        "shortCode": "A037350",
        "codeName": "성도이엔지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014910004",
        "shortCode": "A014910",
        "codeName": "성문전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014911002",
        "shortCode": "A014915",
        "codeName": "성문전자우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003080009",
        "shortCode": "A003080",
        "codeName": "성보화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004980009",
        "shortCode": "A004980",
        "codeName": "성신양회",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004981007",
        "shortCode": "A004985",
        "codeName": "성신양회우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011300001",
        "shortCode": "A011300",
        "codeName": "성안",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7081580003",
        "shortCode": "A081580",
        "codeName": "성우전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045300001",
        "shortCode": "A045300",
        "codeName": "성우테크론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015750003",
        "shortCode": "A015750",
        "codeName": "성우하이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000180000",
        "shortCode": "A000180",
        "codeName": "성창기업지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7080470008",
        "shortCode": "A080470",
        "codeName": "성창오토텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043260009",
        "shortCode": "A043260",
        "codeName": "성호전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002420008",
        "shortCode": "A002420",
        "codeName": "세기상사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7053060000",
        "shortCode": "A053060",
        "codeName": "세동",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017510009",
        "shortCode": "A017510",
        "codeName": "세명전기",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214310005",
        "shortCode": "A214310",
        "codeName": "세미콘라이트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004360004",
        "shortCode": "A004360",
        "codeName": "세방",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004361002",
        "shortCode": "A004365",
        "codeName": "세방우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004490009",
        "shortCode": "A004490",
        "codeName": "세방전지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011560000",
        "shortCode": "A011560",
        "codeName": "세보엠이씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001430008",
        "shortCode": "A001430",
        "codeName": "세아베스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7306200007",
        "shortCode": "A306200",
        "codeName": "세아제강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003030004",
        "shortCode": "A003030",
        "codeName": "세아제강지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7019440007",
        "shortCode": "A019440",
        "codeName": "세아특수강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7058650003",
        "shortCode": "A058650",
        "codeName": "세아홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7013000005",
        "shortCode": "A013000",
        "codeName": "세우글로벌",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7100700004",
        "shortCode": "A100700",
        "codeName": "세운메디칼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7234100006",
        "shortCode": "A234100",
        "codeName": "세원",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024830002",
        "shortCode": "A024830",
        "codeName": "세원물산",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091090001",
        "shortCode": "A091090",
        "codeName": "세원셀론텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7021820006",
        "shortCode": "A021820",
        "codeName": "세원정공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7067830000",
        "shortCode": "A067830",
        "codeName": "세이브존I&C",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033530007",
        "shortCode": "A033530",
        "codeName": "세종공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7135270007",
        "shortCode": "A135270",
        "codeName": "세종머티리얼즈",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7258830009",
        "shortCode": "A258830",
        "codeName": "세종메디칼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036630002",
        "shortCode": "A036630",
        "codeName": "세종텔레콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039310008",
        "shortCode": "A039310",
        "codeName": "세중",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7075580001",
        "shortCode": "A075580",
        "codeName": "세진중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7067770008",
        "shortCode": "A067770",
        "codeName": "세진티에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053450003",
        "shortCode": "A053450",
        "codeName": "세코닉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7234340008",
        "shortCode": "A234340",
        "codeName": "세틀뱅크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7027970003",
        "shortCode": "A027970",
        "codeName": "세하",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7145210001",
        "shortCode": "A145210",
        "codeName": "세화아이엠씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7252500004",
        "shortCode": "A252500",
        "codeName": "세화피앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051980001",
        "shortCode": "A051980",
        "codeName": "센트럴바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049180003",
        "shortCode": "A049180",
        "codeName": "셀루메드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7299660001",
        "shortCode": "A299660",
        "codeName": "셀리드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7268600004",
        "shortCode": "A268600",
        "codeName": "셀리버리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7108860008",
        "shortCode": "A108860",
        "codeName": "셀바스AI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208370007",
        "shortCode": "A208370",
        "codeName": "셀바스헬스케어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7258250000",
        "shortCode": "A258250",
        "codeName": "셀젠텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7068270008",
        "shortCode": "A068270",
        "codeName": "셀트리온",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7068760008",
        "shortCode": "A068760",
        "codeName": "셀트리온제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091990002",
        "shortCode": "A091990",
        "codeName": "셀트리온헬스케어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053110003",
        "shortCode": "A053110",
        "codeName": "소리바다",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032680001",
        "shortCode": "A032680",
        "codeName": "소프트센",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032681009",
        "shortCode": "A032685",
        "codeName": "소프트센우",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7210610002",
        "shortCode": "A210610",
        "codeName": "소프트캠프",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7066910001",
        "shortCode": "A066910",
        "codeName": "손오공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043100007",
        "shortCode": "A043100",
        "codeName": "솔고바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7154040000",
        "shortCode": "A154040",
        "codeName": "솔루에타",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035610005",
        "shortCode": "A035610",
        "codeName": "솔본",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036830008",
        "shortCode": "A036830",
        "codeName": "솔브레인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7230980005",
        "shortCode": "A230980",
        "codeName": "솔트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004430005",
        "shortCode": "A004430",
        "codeName": "송원산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7086980000",
        "shortCode": "A086980",
        "codeName": "쇼박스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7050960004",
        "shortCode": "A050960",
        "codeName": "수산아이앤티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017550005",
        "shortCode": "A017550",
        "codeName": "수산중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7084180009",
        "shortCode": "A084180",
        "codeName": "수성",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7253840003",
        "shortCode": "A253840",
        "codeName": "수젠텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002200004",
        "shortCode": "A002200",
        "codeName": "수출포장",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7185190006",
        "shortCode": "A185190",
        "codeName": "수프로",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7058530007",
        "shortCode": "A058530",
        "codeName": "슈펙스비앤피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7236200002",
        "shortCode": "A236200",
        "codeName": "슈프리마",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094840006",
        "shortCode": "A094840",
        "codeName": "슈프리마에이치큐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7192440006",
        "shortCode": "A192440",
        "codeName": "슈피겐코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7099440000",
        "shortCode": "A099440",
        "codeName": "스맥",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053210001",
        "shortCode": "A053210",
        "codeName": "스카이라이프",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033790007",
        "shortCode": "A033790",
        "codeName": "스카이문스테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7159910009",
        "shortCode": "A159910",
        "codeName": "스킨앤스킨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115570004",
        "shortCode": "A115570",
        "codeName": "스타플렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7258540004",
        "shortCode": "A258540",
        "codeName": "스템랩",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7253450001",
        "shortCode": "A253450",
        "codeName": "스튜디오드래곤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008800005",
        "shortCode": "A008800",
        "codeName": "스튜디오썸머",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013810007",
        "shortCode": "A013810",
        "codeName": "스페코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049830003",
        "shortCode": "A049830",
        "codeName": "승일",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7020710000",
        "shortCode": "A020710",
        "codeName": "시공테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033170002",
        "shortCode": "A033170",
        "codeName": "시그네틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7260870001",
        "shortCode": "A260870",
        "codeName": "시그넷이브이",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7048870000",
        "shortCode": "A048870",
        "codeName": "시너지이노베이션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025320003",
        "shortCode": "A025320",
        "codeName": "시노펙스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7134790005",
        "shortCode": "A134790",
        "codeName": "시디즈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7269620001",
        "shortCode": "A269620",
        "codeName": "시스웍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131090003",
        "shortCode": "A131090",
        "codeName": "시큐브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7232830000",
        "shortCode": "A232830",
        "codeName": "시큐센",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7016590002",
        "shortCode": "A016590",
        "codeName": "신대양제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7029530003",
        "shortCode": "A029530",
        "codeName": "신도리코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004970000",
        "shortCode": "A004970",
        "codeName": "신라교역",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001000009",
        "shortCode": "A001000",
        "codeName": "신라섬유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025870007",
        "shortCode": "A025870",
        "codeName": "신라에스지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215600008",
        "shortCode": "A215600",
        "codeName": "신라젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065350001",
        "shortCode": "A065350",
        "codeName": "신성델타테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011930005",
        "shortCode": "A011930",
        "codeName": "신성이엔지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005390000",
        "shortCode": "A005390",
        "codeName": "신성통상",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004170007",
        "shortCode": "A004170",
        "codeName": "신세계",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7035510007",
        "shortCode": "A035510",
        "codeName": "신세계 I&C",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034300004",
        "shortCode": "A034300",
        "codeName": "신세계건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7031430002",
        "shortCode": "A031430",
        "codeName": "신세계인터내셔날",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7031440001",
        "shortCode": "A031440",
        "codeName": "신세계푸드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006880009",
        "shortCode": "A006880",
        "codeName": "신송홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7056000003",
        "shortCode": "A056000",
        "codeName": "신스타임즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002800001",
        "shortCode": "A002800",
        "codeName": "신신제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307180000",
        "shortCode": "A307180",
        "codeName": "신영스팩4호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7323280008",
        "shortCode": "A323280",
        "codeName": "신영스팩5호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005800008",
        "shortCode": "A005800",
        "codeName": "신영와코루",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001720002",
        "shortCode": "A001720",
        "codeName": "신영증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001721000",
        "shortCode": "A001725",
        "codeName": "신영증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009270000",
        "shortCode": "A009270",
        "codeName": "신원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009271008",
        "shortCode": "A009275",
        "codeName": "신원우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017000001",
        "shortCode": "A017000",
        "codeName": "신원종합개발",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002700003",
        "shortCode": "A002700",
        "codeName": "신일산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012790002",
        "shortCode": "A012790",
        "codeName": "신일제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138070008",
        "shortCode": "A138070",
        "codeName": "신진에스엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019170000",
        "shortCode": "A019170",
        "codeName": "신풍제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7019171008",
        "shortCode": "A019175",
        "codeName": "신풍제약우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002870004",
        "shortCode": "A002870",
        "codeName": "신풍제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005450002",
        "shortCode": "A005450",
        "codeName": "신한",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7293940003",
        "shortCode": "A293940",
        "codeName": "신한알파리츠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7257730002",
        "shortCode": "A257730",
        "codeName": "신한제3호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7277480000",
        "shortCode": "A277480",
        "codeName": "신한제4호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7323230003",
        "shortCode": "A323230",
        "codeName": "신한제5호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7055550008",
        "shortCode": "A055550",
        "codeName": "신한지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001770007",
        "shortCode": "A001770",
        "codeName": "신화실업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7056700008",
        "shortCode": "A056700",
        "codeName": "신화인터텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7187270004",
        "shortCode": "A187270",
        "codeName": "신화콘텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004080008",
        "shortCode": "A004080",
        "codeName": "신흥",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7243840006",
        "shortCode": "A243840",
        "codeName": "신흥에스이씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7108320003",
        "shortCode": "A108320",
        "codeName": "실리콘웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7222800005",
        "shortCode": "A222800",
        "codeName": "심텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036710002",
        "shortCode": "A036710",
        "codeName": "심텍홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7160980009",
        "shortCode": "A160980",
        "codeName": "싸이맥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217330000",
        "shortCode": "A217330",
        "codeName": "싸이토젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7102280005",
        "shortCode": "A102280",
        "codeName": "쌍방울",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003410008",
        "shortCode": "A003410",
        "codeName": "쌍용양회",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003411006",
        "shortCode": "A003415",
        "codeName": "쌍용양회우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010280006",
        "shortCode": "A010280",
        "codeName": "쌍용정보통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003620002",
        "shortCode": "A003620",
        "codeName": "쌍용차",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004770004",
        "shortCode": "A004770",
        "codeName": "써니전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7217320001",
        "shortCode": "A217320",
        "codeName": "썬테크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7122800006",
        "shortCode": "A122800",
        "codeName": "썬텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208640003",
        "shortCode": "A208640",
        "codeName": "썸에이지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7222420002",
        "shortCode": "A222420",
        "codeName": "쎄노텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037760006",
        "shortCode": "A037760",
        "codeName": "쎄니트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7136510005",
        "shortCode": "A136510",
        "codeName": "쎄미시스코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7099320004",
        "shortCode": "A099320",
        "codeName": "쎄트렉아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049960008",
        "shortCode": "A049960",
        "codeName": "쎌바이오텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7050890003",
        "shortCode": "A050890",
        "codeName": "쏠리드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066790007",
        "shortCode": "A066790",
        "codeName": "씨씨에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7222080004",
        "shortCode": "A222080",
        "codeName": "씨아이에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004920005",
        "shortCode": "A004920",
        "codeName": "씨아이테크",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7236030003",
        "shortCode": "A236030",
        "codeName": "씨알푸드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7103660007",
        "shortCode": "A103660",
        "codeName": "씨앗",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7245450002",
        "shortCode": "A245450",
        "codeName": "씨앤에스링크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7264660002",
        "shortCode": "A264660",
        "codeName": "씨앤지하이테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7112610001",
        "shortCode": "A112610",
        "codeName": "씨에스윈드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7115530008",
        "shortCode": "A115530",
        "codeName": "씨엔플러스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225330000",
        "shortCode": "A225330",
        "codeName": "씨엠에스에듀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115480006",
        "shortCode": "A115480",
        "codeName": "씨유메디칼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7189330004",
        "shortCode": "A189330",
        "codeName": "씨이랩",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7096530001",
        "shortCode": "A096530",
        "codeName": "씨젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KYG2114A1094",
        "shortCode": "A900120",
        "codeName": "씨케이에이치",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101240000",
        "shortCode": "A101240",
        "codeName": "씨큐브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7047920004",
        "shortCode": "A047920",
        "codeName": "씨트리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7189540008",
        "shortCode": "A189540",
        "codeName": "씨티네트웍스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7060590007",
        "shortCode": "A060590",
        "codeName": "씨티씨바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036170009",
        "shortCode": "A036170",
        "codeName": "씨티젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7260930003",
        "shortCode": "A260930",
        "codeName": "씨티케이코스메틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013990007",
        "shortCode": "A013990",
        "codeName": "아가방컴퍼니",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123860009",
        "shortCode": "A123860",
        "codeName": "아나패스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025980004",
        "shortCode": "A025980",
        "codeName": "아난티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008700007",
        "shortCode": "A008700",
        "codeName": "아남전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7058220005",
        "shortCode": "A058220",
        "codeName": "아리온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7125210005",
        "shortCode": "A125210",
        "codeName": "아모그린텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002790004",
        "shortCode": "A002790",
        "codeName": "아모레G",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002791002",
        "shortCode": "A002795",
        "codeName": "아모레G우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7090430000",
        "shortCode": "A090430",
        "codeName": "아모레퍼시픽",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7090431008",
        "shortCode": "A090435",
        "codeName": "아모레퍼시픽우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7052710001",
        "shortCode": "A052710",
        "codeName": "아모텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7074430000",
        "shortCode": "A074430",
        "codeName": "아미노로직스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092040005",
        "shortCode": "A092040",
        "codeName": "아미코젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083930008",
        "shortCode": "A083930",
        "codeName": "아바코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7149950008",
        "shortCode": "A149950",
        "codeName": "아바텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036010007",
        "shortCode": "A036010",
        "codeName": "아비코전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002030005",
        "shortCode": "A002030",
        "codeName": "아세아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7183190008",
        "shortCode": "A183190",
        "codeName": "아세아시멘트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002310001",
        "shortCode": "A002310",
        "codeName": "아세아제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7050860006",
        "shortCode": "A050860",
        "codeName": "아세아텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7246720007",
        "shortCode": "A246720",
        "codeName": "아스타",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067390005",
        "shortCode": "A067390",
        "codeName": "아스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7127710002",
        "shortCode": "A127710",
        "codeName": "아시아경제",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7267850006",
        "shortCode": "A267850",
        "codeName": "아시아나IDT",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7020560009",
        "shortCode": "A020560",
        "codeName": "아시아나항공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7154030001",
        "shortCode": "A154030",
        "codeName": "아시아종묘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7227610003",
        "shortCode": "A227610",
        "codeName": "아우딘퓨쳐스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7143160000",
        "shortCode": "A143160",
        "codeName": "아이디스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054800008",
        "shortCode": "A054800",
        "codeName": "아이디스홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122900004",
        "shortCode": "A122900",
        "codeName": "아이마켓코리아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7099190001",
        "shortCode": "A099190",
        "codeName": "아이센스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7289010001",
        "shortCode": "A289010",
        "codeName": "아이스크림에듀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214430001",
        "shortCode": "A214430",
        "codeName": "아이쓰리시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7040910002",
        "shortCode": "A040910",
        "codeName": "아이씨디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7068940006",
        "shortCode": "A068940",
        "codeName": "아이씨케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052860004",
        "shortCode": "A052860",
        "codeName": "아이앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010780005",
        "shortCode": "A010780",
        "codeName": "아이에스동서",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7069920007",
        "shortCode": "A069920",
        "codeName": "아이에스이커머스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038880001",
        "shortCode": "A038880",
        "codeName": "아이에이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122050008",
        "shortCode": "A122050",
        "codeName": "아이엘사이언스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7101390003",
        "shortCode": "A101390",
        "codeName": "아이엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7226350007",
        "shortCode": "A226350",
        "codeName": "아이엠텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078860004",
        "shortCode": "A078860",
        "codeName": "아이오케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114810005",
        "shortCode": "A114810",
        "codeName": "아이원스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7031310006",
        "shortCode": "A031310",
        "codeName": "아이즈비전",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7185490000",
        "shortCode": "A185490",
        "codeName": "아이진",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7059100008",
        "shortCode": "A059100",
        "codeName": "아이컴포넌트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7149010001",
        "shortCode": "A149010",
        "codeName": "아이케이세미콘",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7175250000",
        "shortCode": "A175250",
        "codeName": "아이큐어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052460003",
        "shortCode": "A052460",
        "codeName": "아이크래프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7119830008",
        "shortCode": "A119830",
        "codeName": "아이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7124500000",
        "shortCode": "A124500",
        "codeName": "아이티센",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7223220005",
        "shortCode": "A223220",
        "codeName": "아이피몬스터",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7027360007",
        "shortCode": "A027360",
        "codeName": "아주IB투자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033660002",
        "shortCode": "A033660",
        "codeName": "아주캐피탈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032080004",
        "shortCode": "A032080",
        "codeName": "아즈텍WB",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013310008",
        "shortCode": "A013310",
        "codeName": "아진산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7059120006",
        "shortCode": "A059120",
        "codeName": "아진엑스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067160002",
        "shortCode": "A067160",
        "codeName": "아프리카TV",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001540004",
        "shortCode": "A001540",
        "codeName": "안국약품",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053800009",
        "shortCode": "A053800",
        "codeName": "안랩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7251280004",
        "shortCode": "A251280",
        "codeName": "안지오랩",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7065660003",
        "shortCode": "A065660",
        "codeName": "안트로젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7271400004",
        "shortCode": "A271400",
        "codeName": "알로이스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7001780006",
        "shortCode": "A001780",
        "codeName": "알루코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7260660006",
        "shortCode": "A260660",
        "codeName": "알리코제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131370009",
        "shortCode": "A131370",
        "codeName": "알서포트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140670001",
        "shortCode": "A140670",
        "codeName": "알에스오토메이션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7096610001",
        "shortCode": "A096610",
        "codeName": "알에프세미",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7061040002",
        "shortCode": "A061040",
        "codeName": "알에프텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7148250004",
        "shortCode": "A148250",
        "codeName": "알엔투테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7196170005",
        "shortCode": "A196170",
        "codeName": "알테오젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123750002",
        "shortCode": "A123750",
        "codeName": "알톤스포츠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7085810000",
        "shortCode": "A085810",
        "codeName": "알티캐스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7117670000",
        "shortCode": "A117670",
        "codeName": "알파홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7293780003",
        "shortCode": "A293780",
        "codeName": "압타바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7267810000",
        "shortCode": "A267810",
        "codeName": "앙츠",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7018250001",
        "shortCode": "A018250",
        "codeName": "애경산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7161000005",
        "shortCode": "A161000",
        "codeName": "애경유화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7196300008",
        "shortCode": "A196300",
        "codeName": "애니젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7205500002",
        "shortCode": "A205500",
        "codeName": "액션스퀘어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052790003",
        "shortCode": "A052790",
        "codeName": "액토즈소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131400004",
        "shortCode": "A131400",
        "codeName": "액트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7290740000",
        "shortCode": "A290740",
        "codeName": "액트로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7238090005",
        "shortCode": "A238090",
        "codeName": "앤디포스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092600006",
        "shortCode": "A092600",
        "codeName": "앤씨앤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7266170000",
        "shortCode": "A266170",
        "codeName": "앤유엔터테인먼트",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7174900001",
        "shortCode": "A174900",
        "codeName": "앱클론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7255440000",
        "shortCode": "A255440",
        "codeName": "야스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7030960009",
        "shortCode": "A030960",
        "codeName": "양지사",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7102120003",
        "shortCode": "A102120",
        "codeName": "어보브반도체",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7224810002",
        "shortCode": "A224810",
        "codeName": "엄지하우스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7041590001",
        "shortCode": "A041590",
        "codeName": "에너전트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019990001",
        "shortCode": "A019990",
        "codeName": "에너토크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011090008",
        "shortCode": "A011090",
        "codeName": "에넥스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7208890004",
        "shortCode": "A208890",
        "codeName": "에듀파트너",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7041440009",
        "shortCode": "A041440",
        "codeName": "에버다임",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7270660004",
        "shortCode": "A270660",
        "codeName": "에브리봇",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7038680005",
        "shortCode": "A038680",
        "codeName": "에스넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217480003",
        "shortCode": "A217480",
        "codeName": "에스디생명공학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7121890008",
        "shortCode": "A121890",
        "codeName": "에스디시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7030270003",
        "shortCode": "A030270",
        "codeName": "에스마크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7097780001",
        "shortCode": "A097780",
        "codeName": "에스맥",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7073070005",
        "shortCode": "A073070",
        "codeName": "에스모",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042110007",
        "shortCode": "A042110",
        "codeName": "에스씨디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065420002",
        "shortCode": "A065420",
        "codeName": "에스아이리소스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7270210008",
        "shortCode": "A270210",
        "codeName": "에스알바이오텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7103230009",
        "shortCode": "A103230",
        "codeName": "에스앤더블류",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7260970009",
        "shortCode": "A260970",
        "codeName": "에스앤디",
        "marketName": "KONEX"
    },
    {
        "fullCode": "HK0000055043",
        "shortCode": "A900080",
        "codeName": "에스앤씨엔진그룹",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101490001",
        "shortCode": "A101490",
        "codeName": "에스앤에스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095910006",
        "shortCode": "A095910",
        "codeName": "에스에너지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7275630002",
        "shortCode": "A275630",
        "codeName": "에스에스알",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7031330004",
        "shortCode": "A031330",
        "codeName": "에스에이엠티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060540002",
        "shortCode": "A060540",
        "codeName": "에스에이티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7158300004",
        "shortCode": "A158300",
        "codeName": "에스에이티이엔지",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7112240007",
        "shortCode": "A112240",
        "codeName": "에스에프씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7056190002",
        "shortCode": "A056190",
        "codeName": "에스에프에이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080000003",
        "shortCode": "A080000",
        "codeName": "에스엔유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7160600003",
        "shortCode": "A160600",
        "codeName": "에스엔텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086460003",
        "shortCode": "A086460",
        "codeName": "에스엔피제네틱스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7005850003",
        "shortCode": "A005850",
        "codeName": "에스엘",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7246250005",
        "shortCode": "A246250",
        "codeName": "에스엘에스바이오",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7041510009",
        "shortCode": "A041510",
        "codeName": "에스엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7299670000",
        "shortCode": "A299670",
        "codeName": "에스엠비나",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7007820004",
        "shortCode": "A007820",
        "codeName": "에스엠코어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7109610006",
        "shortCode": "A109610",
        "codeName": "에스와이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012750006",
        "shortCode": "A012750",
        "codeName": "에스원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7080440001",
        "shortCode": "A080440",
        "codeName": "에스제이케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217910009",
        "shortCode": "A217910",
        "codeName": "에스제이켐",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7224020008",
        "shortCode": "A224020",
        "codeName": "에스케이씨에스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7096630009",
        "shortCode": "A096630",
        "codeName": "에스코넥",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069510006",
        "shortCode": "A069510",
        "codeName": "에스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041910001",
        "shortCode": "A041910",
        "codeName": "에스텍파마",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7234300002",
        "shortCode": "A234300",
        "codeName": "에스트래픽",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039440003",
        "shortCode": "A039440",
        "codeName": "에스티아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7098660004",
        "shortCode": "A098660",
        "codeName": "에스티오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052020005",
        "shortCode": "A052020",
        "codeName": "에스티큐브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7237690003",
        "shortCode": "A237690",
        "codeName": "에스티팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7050760008",
        "shortCode": "A050760",
        "codeName": "에스폴리텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7288620008",
        "shortCode": "A288620",
        "codeName": "에스퓨얼셀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058610007",
        "shortCode": "A058610",
        "codeName": "에스피지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043340009",
        "shortCode": "A043340",
        "codeName": "에쎈테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023960008",
        "shortCode": "A023960",
        "codeName": "에쓰씨엔지니어링",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7298690009",
        "shortCode": "A298690",
        "codeName": "에어부산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7054630009",
        "shortCode": "A054630",
        "codeName": "에이디칩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7200710002",
        "shortCode": "A200710",
        "codeName": "에이디테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140910001",
        "shortCode": "A140910",
        "codeName": "에이리츠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7078520004",
        "shortCode": "A078520",
        "codeName": "에이블씨엔씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7298380007",
        "shortCode": "A298380",
        "codeName": "에이비엘바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7203400007",
        "shortCode": "A203400",
        "codeName": "에이비온",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7003800000",
        "shortCode": "A003800",
        "codeName": "에이스침대",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088800008",
        "shortCode": "A088800",
        "codeName": "에이스테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241840008",
        "shortCode": "A241840",
        "codeName": "에이스토리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138360003",
        "shortCode": "A138360",
        "codeName": "에이씨티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039230008",
        "shortCode": "A039230",
        "codeName": "에이아이비트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7050320001",
        "shortCode": "A050320",
        "codeName": "에이앤티앤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7312610009",
        "shortCode": "A312610",
        "codeName": "에이에프더블류",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015260003",
        "shortCode": "A015260",
        "codeName": "에이엔피",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7234070001",
        "shortCode": "A234070",
        "codeName": "에이원알폼",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7072990005",
        "shortCode": "A072990",
        "codeName": "에이치시티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7044990000",
        "shortCode": "A044990",
        "codeName": "에이치엔에스하이텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7176440006",
        "shortCode": "A176440",
        "codeName": "에이치엔티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7028300002",
        "shortCode": "A028300",
        "codeName": "에이치엘비",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067630004",
        "shortCode": "A067630",
        "codeName": "에이치엘비생명과학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043220003",
        "shortCode": "A043220",
        "codeName": "에이치엘비파워",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7239610009",
        "shortCode": "A239610",
        "codeName": "에이치엘사이언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7044780005",
        "shortCode": "A044780",
        "codeName": "에이치케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7071670004",
        "shortCode": "A071670",
        "codeName": "에이테크솔루션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045660008",
        "shortCode": "A045660",
        "codeName": "에이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7224110007",
        "shortCode": "A224110",
        "codeName": "에이텍티앤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7021080007",
        "shortCode": "A021080",
        "codeName": "에이티넘인베스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089530000",
        "shortCode": "A089530",
        "codeName": "에이티세미콘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7207490004",
        "shortCode": "A207490",
        "codeName": "에이펙스인텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7109960005",
        "shortCode": "A109960",
        "codeName": "에이프로젠 H&G",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007460009",
        "shortCode": "A007460",
        "codeName": "에이프로젠 KIC",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003060001",
        "shortCode": "A003060",
        "codeName": "에이프로젠제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7089970008",
        "shortCode": "A089970",
        "codeName": "에이피티씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7230240004",
        "shortCode": "A230240",
        "codeName": "에치에프알",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064510001",
        "shortCode": "A064510",
        "codeName": "에코마이스터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7230360000",
        "shortCode": "A230360",
        "codeName": "에코마케팅",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038870002",
        "shortCode": "A038870",
        "codeName": "에코바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7128540002",
        "shortCode": "A128540",
        "codeName": "에코캡",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086520004",
        "shortCode": "A086520",
        "codeName": "에코프로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7247540008",
        "shortCode": "A247540",
        "codeName": "에코프로비엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038110003",
        "shortCode": "A038110",
        "codeName": "에코플라스틱",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7073540007",
        "shortCode": "A073540",
        "codeName": "에프알텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064850001",
        "shortCode": "A064850",
        "codeName": "에프앤가이드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7064090004",
        "shortCode": "A064090",
        "codeName": "에프앤리퍼블릭",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036810000",
        "shortCode": "A036810",
        "codeName": "에프에스티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7173940008",
        "shortCode": "A173940",
        "codeName": "에프엔씨엔터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083500009",
        "shortCode": "A083500",
        "codeName": "에프엔에스테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054940002",
        "shortCode": "A054940",
        "codeName": "엑사이엔씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR8840090003",
        "shortCode": "A950130",
        "codeName": "엑세스바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7205100001",
        "shortCode": "A205100",
        "codeName": "엑셈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092870005",
        "shortCode": "A092870",
        "codeName": "엑시콘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067570002",
        "shortCode": "A067570",
        "codeName": "엔브이에이치코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140610007",
        "shortCode": "A140610",
        "codeName": "엔솔바이오사이언스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7101400000",
        "shortCode": "A101400",
        "codeName": "엔시트론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036570000",
        "shortCode": "A036570",
        "codeName": "엔씨소프트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7217820000",
        "shortCode": "A217820",
        "codeName": "엔에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138250006",
        "shortCode": "A138250",
        "codeName": "엔에스쇼핑",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7031860000",
        "shortCode": "A031860",
        "codeName": "엔에스엔",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7224760009",
        "shortCode": "A224760",
        "codeName": "엔에스컴퍼니",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7256840000",
        "shortCode": "A256840",
        "codeName": "엔에이치스팩11호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7273060004",
        "shortCode": "A273060",
        "codeName": "엔에이치스팩12호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7310840004",
        "shortCode": "A310840",
        "codeName": "엔에이치스팩13호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7319400008",
        "shortCode": "A319400",
        "codeName": "엔에이치스팩14호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208860007",
        "shortCode": "A208860",
        "codeName": "엔지스테크널러지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7183490002",
        "shortCode": "A183490",
        "codeName": "엔지켐생명과학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7085310001",
        "shortCode": "A085310",
        "codeName": "엔케이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7182400002",
        "shortCode": "A182400",
        "codeName": "엔케이맥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009810003",
        "shortCode": "A009810",
        "codeName": "엔케이물산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7206400004",
        "shortCode": "A206400",
        "codeName": "엔터메이트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069410009",
        "shortCode": "A069410",
        "codeName": "엔텔스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7048830004",
        "shortCode": "A048830",
        "codeName": "엔피케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7096870001",
        "shortCode": "A096870",
        "codeName": "엘디티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7276240009",
        "shortCode": "A276240",
        "codeName": "엘리비젼",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KYG5307W1015",
        "shortCode": "A900140",
        "codeName": "엘브이엠씨홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7061970000",
        "shortCode": "A061970",
        "codeName": "엘비세미콘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138690003",
        "shortCode": "A138690",
        "codeName": "엘아이에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7290650001",
        "shortCode": "A290650",
        "codeName": "엘앤씨바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066970005",
        "shortCode": "A066970",
        "codeName": "엘앤에프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7156100000",
        "shortCode": "A156100",
        "codeName": "엘앤케이바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7311060008",
        "shortCode": "A311060",
        "codeName": "엘에이티",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7073110009",
        "shortCode": "A073110",
        "codeName": "엘엠에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083310003",
        "shortCode": "A083310",
        "codeName": "엘오티베큠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037950003",
        "shortCode": "A037950",
        "codeName": "엘컴텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7170920003",
        "shortCode": "A170920",
        "codeName": "엘티씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058630005",
        "shortCode": "A058630",
        "codeName": "엠게임",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058970005",
        "shortCode": "A058970",
        "codeName": "엠로",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7019590009",
        "shortCode": "A019590",
        "codeName": "엠벤처투자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7097520001",
        "shortCode": "A097520",
        "codeName": "엠씨넥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7179290002",
        "shortCode": "A179290",
        "codeName": "엠아이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225860006",
        "shortCode": "A225860",
        "codeName": "엠앤씨생명과학",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7009780008",
        "shortCode": "A009780",
        "codeName": "엠에스씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123040008",
        "shortCode": "A123040",
        "codeName": "엠에스오토텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7251960001",
        "shortCode": "A251960",
        "codeName": "엠에프엠코리아",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7032790008",
        "shortCode": "A032790",
        "codeName": "엠젠플러스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033160003",
        "shortCode": "A033160",
        "codeName": "엠케이전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7204020002",
        "shortCode": "A204020",
        "codeName": "엠코르셋",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7259630002",
        "shortCode": "A259630",
        "codeName": "엠플러스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115960007",
        "shortCode": "A115960",
        "codeName": "연우",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090740002",
        "shortCode": "A090740",
        "codeName": "연이정보통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014440002",
        "shortCode": "A014440",
        "codeName": "영보화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007530009",
        "shortCode": "A007530",
        "codeName": "영신금속",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7143540003",
        "shortCode": "A143540",
        "codeName": "영우디에스피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7111770004",
        "shortCode": "A111770",
        "codeName": "영원무역",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009970005",
        "shortCode": "A009970",
        "codeName": "영원무역홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036180008",
        "shortCode": "A036180",
        "codeName": "영인프런티어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003520004",
        "shortCode": "A003520",
        "codeName": "영진약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000670000",
        "shortCode": "A000670",
        "codeName": "영풍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036560001",
        "shortCode": "A036560",
        "codeName": "영풍정밀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006740005",
        "shortCode": "A006740",
        "codeName": "영풍제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012280004",
        "shortCode": "A012280",
        "codeName": "영화금속",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7265560003",
        "shortCode": "A265560",
        "codeName": "영화테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012160008",
        "shortCode": "A012160",
        "codeName": "영흥철강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036000008",
        "shortCode": "A036000",
        "codeName": "예림당",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053280004",
        "shortCode": "A053280",
        "codeName": "예스24",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015360001",
        "shortCode": "A015360",
        "codeName": "예스코홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7122640006",
        "shortCode": "A122640",
        "codeName": "예스티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7179720008",
        "shortCode": "A179720",
        "codeName": "옐로페이",
        "marketName": "KONEX"
    },
    {
        "fullCode": "HK0000312568",
        "shortCode": "A900300",
        "codeName": "오가닉티코스메틱",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045060001",
        "shortCode": "A045060",
        "codeName": "오공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080520000",
        "shortCode": "A080520",
        "codeName": "오디텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007310006",
        "shortCode": "A007310",
        "codeName": "오뚜기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079440004",
        "shortCode": "A079440",
        "codeName": "오렌지라이프",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039830005",
        "shortCode": "A039830",
        "codeName": "오로라",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7046120002",
        "shortCode": "A046120",
        "codeName": "오르비텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014940001",
        "shortCode": "A014940",
        "codeName": "오리엔탈정공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002630002",
        "shortCode": "A002630",
        "codeName": "오리엔트바이오",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7065500001",
        "shortCode": "A065500",
        "codeName": "오리엔트정공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7271560005",
        "shortCode": "A271560",
        "codeName": "오리온",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001800002",
        "shortCode": "A001800",
        "codeName": "오리온홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010470003",
        "shortCode": "A010470",
        "codeName": "오리콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053980009",
        "shortCode": "A053980",
        "codeName": "오상자이엘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052420007",
        "shortCode": "A052420",
        "codeName": "오성첨단소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241790005",
        "shortCode": "A241790",
        "codeName": "오션브릿지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039200001",
        "shortCode": "A039200",
        "codeName": "오스코텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7226400000",
        "shortCode": "A226400",
        "codeName": "오스테오닉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7031510001",
        "shortCode": "A031510",
        "codeName": "오스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7048260004",
        "shortCode": "A048260",
        "codeName": "오스템임플란트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138080007",
        "shortCode": "A138080",
        "codeName": "오이솔루션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080580004",
        "shortCode": "A080580",
        "codeName": "오킨스전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067170001",
        "shortCode": "A067170",
        "codeName": "오텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7173130006",
        "shortCode": "A173130",
        "codeName": "오파스넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049480007",
        "shortCode": "A049480",
        "codeName": "오픈베이스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7226950004",
        "shortCode": "A226950",
        "codeName": "올릭스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7057540007",
        "shortCode": "A057540",
        "codeName": "옴니시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7057680001",
        "shortCode": "A057680",
        "codeName": "옴니텔",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123010001",
        "shortCode": "A123010",
        "codeName": "옵토팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7082210006",
        "shortCode": "A082210",
        "codeName": "옵트론텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7109080002",
        "shortCode": "A109080",
        "codeName": "옵티시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7153710009",
        "shortCode": "A153710",
        "codeName": "옵티팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052770005",
        "shortCode": "A052770",
        "codeName": "와이디온라인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7057030009",
        "shortCode": "A057030",
        "codeName": "와이비엠넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122990005",
        "shortCode": "A122990",
        "codeName": "와이솔",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7232140004",
        "shortCode": "A232140",
        "codeName": "와이아이케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067900001",
        "shortCode": "A067900",
        "codeName": "와이엔텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7155650005",
        "shortCode": "A155650",
        "codeName": "와이엠씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7251370003",
        "shortCode": "A251370",
        "codeName": "와이엠티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066430000",
        "shortCode": "A066430",
        "codeName": "와이오엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7193250008",
        "shortCode": "A193250",
        "codeName": "와이제이엠게임즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019210004",
        "shortCode": "A019210",
        "codeName": "와이지-원",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122870009",
        "shortCode": "A122870",
        "codeName": "와이지엔터테인먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079000006",
        "shortCode": "A079000",
        "codeName": "와토스코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7070960000",
        "shortCode": "A070960",
        "codeName": "용평리조트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7114630007",
        "shortCode": "A114630",
        "codeName": "우노앤컴퍼니",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7316140003",
        "shortCode": "A316140",
        "codeName": "우리금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032820003",
        "shortCode": "A032820",
        "codeName": "우리기술",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041190000",
        "shortCode": "A041190",
        "codeName": "우리기술투자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115440000",
        "shortCode": "A115440",
        "codeName": "우리넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004720009",
        "shortCode": "A004720",
        "codeName": "우리들제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7118000009",
        "shortCode": "A118000",
        "codeName": "우리들휴브레인",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7046970000",
        "shortCode": "A046970",
        "codeName": "우리로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7082850009",
        "shortCode": "A082850",
        "codeName": "우리바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215360009",
        "shortCode": "A215360",
        "codeName": "우리산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7072470008",
        "shortCode": "A072470",
        "codeName": "우리산업홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7073560005",
        "shortCode": "A073560",
        "codeName": "우리손에프앤지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7153490008",
        "shortCode": "A153490",
        "codeName": "우리이앤엘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037400009",
        "shortCode": "A037400",
        "codeName": "우리조명",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010050003",
        "shortCode": "A010050",
        "codeName": "우리종금",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7101170009",
        "shortCode": "A101170",
        "codeName": "우림기계",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006980007",
        "shortCode": "A006980",
        "codeName": "우성사료",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7066590001",
        "shortCode": "A066590",
        "codeName": "우수AMS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017370008",
        "shortCode": "A017370",
        "codeName": "우신시스템",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7046940003",
        "shortCode": "A046940",
        "codeName": "우원개발",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215380007",
        "shortCode": "A215380",
        "codeName": "우정바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065680001",
        "shortCode": "A065680",
        "codeName": "우주일렉트로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7105840003",
        "shortCode": "A105840",
        "codeName": "우진",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7018620005",
        "shortCode": "A018620",
        "codeName": "우진비앤지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010400000",
        "shortCode": "A010400",
        "codeName": "우진아이엔에스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7049800006",
        "shortCode": "A049800",
        "codeName": "우진플라임",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016880007",
        "shortCode": "A016880",
        "codeName": "웅진",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7095720009",
        "shortCode": "A095720",
        "codeName": "웅진씽크빅",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7103130001",
        "shortCode": "A103130",
        "codeName": "웅진에너지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7021240007",
        "shortCode": "A021240",
        "codeName": "웅진코웨이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005820006",
        "shortCode": "A005820",
        "codeName": "원림",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7278380001",
        "shortCode": "A278380",
        "codeName": "원바이오젠",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7032940009",
        "shortCode": "A032940",
        "codeName": "원익",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7240810002",
        "shortCode": "A240810",
        "codeName": "원익IPS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7074600008",
        "shortCode": "A074600",
        "codeName": "원익QnC",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7104830005",
        "shortCode": "A104830",
        "codeName": "원익머트리얼즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014190003",
        "shortCode": "A014190",
        "codeName": "원익큐브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7030530000",
        "shortCode": "A030530",
        "codeName": "원익홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012620001",
        "shortCode": "A012620",
        "codeName": "원일특강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7216280008",
        "shortCode": "A216280",
        "codeName": "원텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7008370009",
        "shortCode": "A008370",
        "codeName": "원풍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008290009",
        "shortCode": "A008290",
        "codeName": "원풍물산",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101160000",
        "shortCode": "A101160",
        "codeName": "월덱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095270005",
        "shortCode": "A095270",
        "codeName": "웨이브일렉트로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010600005",
        "shortCode": "A010600",
        "codeName": "웰바이오텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7065950008",
        "shortCode": "A065950",
        "codeName": "웰크론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114190002",
        "shortCode": "A114190",
        "codeName": "웰크론강원",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7076080001",
        "shortCode": "A076080",
        "codeName": "웰크론한텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7196700009",
        "shortCode": "A196700",
        "codeName": "웹스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069080000",
        "shortCode": "A069080",
        "codeName": "웹젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053580007",
        "shortCode": "A053580",
        "codeName": "웹케시",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7071460000",
        "shortCode": "A071460",
        "codeName": "위니아딤채",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7044340008",
        "shortCode": "A044340",
        "codeName": "위닉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7112040001",
        "shortCode": "A112040",
        "codeName": "위메이드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065370009",
        "shortCode": "A065370",
        "codeName": "위세아이텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7140660002",
        "shortCode": "A140660",
        "codeName": "위월드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7038620001",
        "shortCode": "A038620",
        "codeName": "위즈코프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7299900001",
        "shortCode": "A299900",
        "codeName": "위지윅스튜디오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036090009",
        "shortCode": "A036090",
        "codeName": "위지트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7136540002",
        "shortCode": "A136540",
        "codeName": "윈스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7097800007",
        "shortCode": "A097800",
        "codeName": "윈팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7192390003",
        "shortCode": "A192390",
        "codeName": "윈하이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7313760001",
        "shortCode": "A313760",
        "codeName": "윌링스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008600009",
        "shortCode": "A008600",
        "codeName": "윌비스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "HK0000449303",
        "shortCode": "A900340",
        "codeName": "윙입푸드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033270000",
        "shortCode": "A033270",
        "codeName": "유나이티드제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014830004",
        "shortCode": "A014830",
        "codeName": "유니드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036200004",
        "shortCode": "A036200",
        "codeName": "유니셈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018000000",
        "shortCode": "A018000",
        "codeName": "유니슨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000910000",
        "shortCode": "A000910",
        "codeName": "유니온",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7047400007",
        "shortCode": "A047400",
        "codeName": "유니온머티리얼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7203450002",
        "shortCode": "A203450",
        "codeName": "유니온커뮤니티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011330008",
        "shortCode": "A011330",
        "codeName": "유니켐",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7077500007",
        "shortCode": "A077500",
        "codeName": "유니퀘스트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011320009",
        "shortCode": "A011320",
        "codeName": "유니크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086390002",
        "shortCode": "A086390",
        "codeName": "유니테스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241690007",
        "shortCode": "A241690",
        "codeName": "유니테크노",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7142210004",
        "shortCode": "A142210",
        "codeName": "유니트론텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7121060008",
        "shortCode": "A121060",
        "codeName": "유니포인트",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7048430003",
        "shortCode": "A048430",
        "codeName": "유라테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7206650004",
        "shortCode": "A206650",
        "codeName": "유바이오로직스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089850002",
        "shortCode": "A089850",
        "codeName": "유비벨록스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084440007",
        "shortCode": "A084440",
        "codeName": "유비온",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7032620007",
        "shortCode": "A032620",
        "codeName": "유비케어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7264450008",
        "shortCode": "A264450",
        "codeName": "유비쿼스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078070000",
        "shortCode": "A078070",
        "codeName": "유비쿼스홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002920007",
        "shortCode": "A002920",
        "codeName": "유성기업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024800005",
        "shortCode": "A024800",
        "codeName": "유성티엔에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000700005",
        "shortCode": "A000700",
        "codeName": "유수홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7054930003",
        "shortCode": "A054930",
        "codeName": "유신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7252370002",
        "shortCode": "A252370",
        "codeName": "유쎌",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7069330009",
        "shortCode": "A069330",
        "codeName": "유아이디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049520000",
        "shortCode": "A049520",
        "codeName": "유아이엘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7287410005",
        "shortCode": "A287410",
        "codeName": "유안타제3호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7313750002",
        "shortCode": "A313750",
        "codeName": "유안타제4호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003470002",
        "shortCode": "A003470",
        "codeName": "유안타증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003471000",
        "shortCode": "A003475",
        "codeName": "유안타증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7056090004",
        "shortCode": "A056090",
        "codeName": "유앤아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011690005",
        "shortCode": "A011690",
        "codeName": "유양디앤유",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7263770000",
        "shortCode": "A263770",
        "codeName": "유에스티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7072130008",
        "shortCode": "A072130",
        "codeName": "유엔젤",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000220004",
        "shortCode": "A000220",
        "codeName": "유유제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000221002",
        "shortCode": "A000225",
        "codeName": "유유제약1우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000222000",
        "shortCode": "A000227",
        "codeName": "유유제약2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7195990007",
        "shortCode": "A195990",
        "codeName": "유지인트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023410004",
        "shortCode": "A023410",
        "codeName": "유진기업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7056080005",
        "shortCode": "A056080",
        "codeName": "유진로봇",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7321260002",
        "shortCode": "A321260",
        "codeName": "유진스팩4호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084370006",
        "shortCode": "A084370",
        "codeName": "유진테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001200005",
        "shortCode": "A001200",
        "codeName": "유진투자증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7178780003",
        "shortCode": "A178780",
        "codeName": "유테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7221800006",
        "shortCode": "A221800",
        "codeName": "유투바이오",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7179900006",
        "shortCode": "A179900",
        "codeName": "유티아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263050007",
        "shortCode": "A263050",
        "codeName": "유틸렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000100008",
        "shortCode": "A000100",
        "codeName": "유한양행",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000101006",
        "shortCode": "A000105",
        "codeName": "유한양행우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003460003",
        "shortCode": "A003460",
        "codeName": "유화증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003461001",
        "shortCode": "A003465",
        "codeName": "유화증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7191410000",
        "shortCode": "A191410",
        "codeName": "육일씨엔에쓰",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7008730004",
        "shortCode": "A008730",
        "codeName": "율촌화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008250003",
        "shortCode": "A008250",
        "codeName": "이건산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039020003",
        "shortCode": "A039020",
        "codeName": "이건홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025820002",
        "shortCode": "A025820",
        "codeName": "이구산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7060230000",
        "shortCode": "A060230",
        "codeName": "이그잭스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067920009",
        "shortCode": "A067920",
        "codeName": "이글루시큐리티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7044960003",
        "shortCode": "A044960",
        "codeName": "이글벳",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7302430004",
        "shortCode": "A302430",
        "codeName": "이노메트리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7279060008",
        "shortCode": "A279060",
        "codeName": "이노벡스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7214320004",
        "shortCode": "A214320",
        "codeName": "이노션",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7073490005",
        "shortCode": "A073490",
        "codeName": "이노와이어리스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7215790007",
        "shortCode": "A215790",
        "codeName": "이노인스트루먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7246960009",
        "shortCode": "A246960",
        "codeName": "이노테라피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088390000",
        "shortCode": "A088390",
        "codeName": "이녹스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7272290008",
        "shortCode": "A272290",
        "codeName": "이녹스첨단소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053350005",
        "shortCode": "A053350",
        "codeName": "이니텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7258610005",
        "shortCode": "A258610",
        "codeName": "이더블유케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041520008",
        "shortCode": "A041520",
        "codeName": "이라이콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054210000",
        "shortCode": "A054210",
        "codeName": "이랜텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065440000",
        "shortCode": "A065440",
        "codeName": "이루온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088260005",
        "shortCode": "A088260",
        "codeName": "이리츠코크렙",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7139480008",
        "shortCode": "A139480",
        "codeName": "이마트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036260008",
        "shortCode": "A036260",
        "codeName": "이매진아시아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115610008",
        "shortCode": "A115610",
        "codeName": "이미지스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7323210005",
        "shortCode": "A323210",
        "codeName": "이베스트이안스팩1호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078020005",
        "shortCode": "A078020",
        "codeName": "이베스트투자증권",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208850008",
        "shortCode": "A208850",
        "codeName": "이비테크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7080010002",
        "shortCode": "A080010",
        "codeName": "이상네트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086890001",
        "shortCode": "A086890",
        "codeName": "이수앱지스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007660004",
        "shortCode": "A007660",
        "codeName": "이수페타시스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005950001",
        "shortCode": "A005950",
        "codeName": "이수화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7015020001",
        "shortCode": "A015020",
        "codeName": "이스타코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7047560008",
        "shortCode": "A047560",
        "codeName": "이스트소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "HK0000057197",
        "shortCode": "A900110",
        "codeName": "이스트아시아홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067010009",
        "shortCode": "A067010",
        "codeName": "이씨에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093230001",
        "shortCode": "A093230",
        "codeName": "이아이디",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7223310004",
        "shortCode": "A223310",
        "codeName": "이에스브이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241510007",
        "shortCode": "A241510",
        "codeName": "이에스산업",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7052190006",
        "shortCode": "A052190",
        "codeName": "이에스에이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7226360006",
        "shortCode": "A226360",
        "codeName": "이엑스티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101360006",
        "shortCode": "A101360",
        "codeName": "이엔드디",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7102710001",
        "shortCode": "A102710",
        "codeName": "이엔에프테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094190006",
        "shortCode": "A094190",
        "codeName": "이엘케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7063760003",
        "shortCode": "A063760",
        "codeName": "이엘피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123570004",
        "shortCode": "A123570",
        "codeName": "이엠넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095190005",
        "shortCode": "A095190",
        "codeName": "이엠코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091120006",
        "shortCode": "A091120",
        "codeName": "이엠텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7232530006",
        "shortCode": "A232530",
        "codeName": "이엠티",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7102460003",
        "shortCode": "A102460",
        "codeName": "이연제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039030002",
        "shortCode": "A039030",
        "codeName": "이오테크닉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088290002",
        "shortCode": "A088290",
        "codeName": "이원컴포텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084680008",
        "shortCode": "A084680",
        "codeName": "이월드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7181340001",
        "shortCode": "A181340",
        "codeName": "이즈미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035810001",
        "shortCode": "A035810",
        "codeName": "이지바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090850009",
        "shortCode": "A090850",
        "codeName": "이지웰페어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7099750002",
        "shortCode": "A099750",
        "codeName": "이지케어텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092130004",
        "shortCode": "A092130",
        "codeName": "이크레더블",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016250003",
        "shortCode": "A016250",
        "codeName": "이테크건설",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7096040001",
        "shortCode": "A096040",
        "codeName": "이트론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7134060003",
        "shortCode": "A134060",
        "codeName": "이퓨쳐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001840008",
        "shortCode": "A001840",
        "codeName": "이화공영",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000760009",
        "shortCode": "A000760",
        "codeName": "이화산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024810004",
        "shortCode": "A024810",
        "codeName": "이화전기",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7014990006",
        "shortCode": "A014990",
        "codeName": "인디에프",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7041830001",
        "shortCode": "A041830",
        "codeName": "인바디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079950002",
        "shortCode": "A079950",
        "codeName": "인베니아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7277410007",
        "shortCode": "A277410",
        "codeName": "인산가",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060150000",
        "shortCode": "A060150",
        "codeName": "인선이엔티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033230004",
        "shortCode": "A033230",
        "codeName": "인성정보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006490007",
        "shortCode": "A006490",
        "codeName": "인스코비",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7037330008",
        "shortCode": "A037330",
        "codeName": "인지디스플레",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023800006",
        "shortCode": "A023800",
        "codeName": "인지컨트롤스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034590000",
        "shortCode": "A034590",
        "codeName": "인천도시가스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7211050000",
        "shortCode": "A211050",
        "codeName": "인카금융서비스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7083640003",
        "shortCode": "A083640",
        "codeName": "인콘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7216050005",
        "shortCode": "A216050",
        "codeName": "인크로스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049070006",
        "shortCode": "A049070",
        "codeName": "인탑스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7119610004",
        "shortCode": "A119610",
        "codeName": "인터로조",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7158310003",
        "shortCode": "A158310",
        "codeName": "인터불스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017250002",
        "shortCode": "A017250",
        "codeName": "인터엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7129260006",
        "shortCode": "A129260",
        "codeName": "인터지스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7240340000",
        "shortCode": "A240340",
        "codeName": "인터코스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7108790007",
        "shortCode": "A108790",
        "codeName": "인터파크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035080001",
        "shortCode": "A035080",
        "codeName": "인터파크홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051370005",
        "shortCode": "A051370",
        "codeName": "인터플렉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064290000",
        "shortCode": "A064290",
        "codeName": "인텍플러스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7189300007",
        "shortCode": "A189300",
        "codeName": "인텔리안테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7150840007",
        "shortCode": "A150840",
        "codeName": "인트로메딕",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7048530000",
        "shortCode": "A048530",
        "codeName": "인트론바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023810005",
        "shortCode": "A023810",
        "codeName": "인팩",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7175140003",
        "shortCode": "A175140",
        "codeName": "인포마크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115310005",
        "shortCode": "A115310",
        "codeName": "인포바인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039290002",
        "shortCode": "A039290",
        "codeName": "인포뱅크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041020009",
        "shortCode": "A041020",
        "codeName": "인프라웨어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7247300007",
        "shortCode": "A247300",
        "codeName": "인프라웨어테크놀러지",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7071200000",
        "shortCode": "A071200",
        "codeName": "인피니트헬스케어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101930006",
        "shortCode": "A101930",
        "codeName": "인화정공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7249420001",
        "shortCode": "A249420",
        "codeName": "일동제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000230003",
        "shortCode": "A000230",
        "codeName": "일동홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7013360003",
        "shortCode": "A013360",
        "codeName": "일성건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003120003",
        "shortCode": "A003120",
        "codeName": "일성신약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7068330000",
        "shortCode": "A068330",
        "codeName": "일신바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003200003",
        "shortCode": "A003200",
        "codeName": "일신방직",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007110000",
        "shortCode": "A007110",
        "codeName": "일신석재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7058450008",
        "shortCode": "A058450",
        "codeName": "일야",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007570005",
        "shortCode": "A007570",
        "codeName": "일양약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007571003",
        "shortCode": "A007575",
        "codeName": "일양약품우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008500001",
        "shortCode": "A008500",
        "codeName": "일정실업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7019540004",
        "shortCode": "A019540",
        "codeName": "일지테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7081000002",
        "shortCode": "A081000",
        "codeName": "일진다이아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7020760005",
        "shortCode": "A020760",
        "codeName": "일진디스플",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7020150009",
        "shortCode": "A020150",
        "codeName": "일진머티리얼즈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7103590006",
        "shortCode": "A103590",
        "codeName": "일진전기",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7094820008",
        "shortCode": "A094820",
        "codeName": "일진파워",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015860000",
        "shortCode": "A015860",
        "codeName": "일진홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7226320000",
        "shortCode": "A226320",
        "codeName": "잇츠한불",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR8840110108",
        "shortCode": "A950140",
        "codeName": "잉글우드랩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049550007",
        "shortCode": "A049550",
        "codeName": "잉크테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7230400004",
        "shortCode": "A230400",
        "codeName": "자비스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7043910009",
        "shortCode": "A043910",
        "codeName": "자연과환경",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7234920007",
        "shortCode": "A234920",
        "codeName": "자이글",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033240003",
        "shortCode": "A033240",
        "codeName": "자화전자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7174880005",
        "shortCode": "A174880",
        "codeName": "장원테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049630007",
        "shortCode": "A049630",
        "codeName": "재영솔루텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000950006",
        "shortCode": "A000950",
        "codeName": "전방",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7120780002",
        "shortCode": "A120780",
        "codeName": "전우정밀",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7110020005",
        "shortCode": "A110020",
        "codeName": "전진바이오팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065530008",
        "shortCode": "A065530",
        "codeName": "전파기지국",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208140004",
        "shortCode": "A208140",
        "codeName": "정다운",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7022220008",
        "shortCode": "A022220",
        "codeName": "정산애강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7040420002",
        "shortCode": "A040420",
        "codeName": "정상제이엘에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045510005",
        "shortCode": "A045510",
        "codeName": "정원엔시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065620007",
        "shortCode": "A065620",
        "codeName": "제낙스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217190008",
        "shortCode": "A217190",
        "codeName": "제너셈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095700001",
        "shortCode": "A095700",
        "codeName": "제넥신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7072520000",
        "shortCode": "A072520",
        "codeName": "제넨바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7122310006",
        "shortCode": "A122310",
        "codeName": "제노레이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066830001",
        "shortCode": "A066830",
        "codeName": "제노텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7187420005",
        "shortCode": "A187420",
        "codeName": "제노포커스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225220003",
        "shortCode": "A225220",
        "codeName": "제놀루션",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7123330003",
        "shortCode": "A123330",
        "codeName": "제닉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7159580000",
        "shortCode": "A159580",
        "codeName": "제로투세븐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7147830004",
        "shortCode": "A147830",
        "codeName": "제룡산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033100009",
        "shortCode": "A033100",
        "codeName": "제룡전기",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079370003",
        "shortCode": "A079370",
        "codeName": "제우스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054950001",
        "shortCode": "A054950",
        "codeName": "제이브이엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7096690003",
        "shortCode": "A096690",
        "codeName": "제이스테판",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090470006",
        "shortCode": "A090470",
        "codeName": "제이스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7137950002",
        "shortCode": "A137950",
        "codeName": "제이씨케미칼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033320003",
        "shortCode": "A033320",
        "codeName": "제이씨현시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7194370003",
        "shortCode": "A194370",
        "codeName": "제이에스코퍼레이션",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7026040006",
        "shortCode": "A026040",
        "codeName": "제이에스티나",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7126880004",
        "shortCode": "A126880",
        "codeName": "제이엔케이히터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033050006",
        "shortCode": "A033050",
        "codeName": "제이엠아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094970001",
        "shortCode": "A094970",
        "codeName": "제이엠티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058420001",
        "shortCode": "A058420",
        "codeName": "제이웨이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025620006",
        "shortCode": "A025620",
        "codeName": "제이준코스메틱",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036420008",
        "shortCode": "A036420",
        "codeName": "제이콘텐트리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035480003",
        "shortCode": "A035480",
        "codeName": "제이테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089790000",
        "shortCode": "A089790",
        "codeName": "제이티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7030000004",
        "shortCode": "A030000",
        "codeName": "제일기획",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7052670007",
        "shortCode": "A052670",
        "codeName": "제일바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7271980005",
        "shortCode": "A271980",
        "codeName": "제일약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001560002",
        "shortCode": "A001560",
        "codeName": "제일연마",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023440001",
        "shortCode": "A023440",
        "codeName": "제일제강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038010005",
        "shortCode": "A038010",
        "codeName": "제일테크노스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002620003",
        "shortCode": "A002620",
        "codeName": "제일파마홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7080220007",
        "shortCode": "A080220",
        "codeName": "제주반도체",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006220008",
        "shortCode": "A006220",
        "codeName": "제주은행",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7089590004",
        "shortCode": "A089590",
        "codeName": "제주항공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7229000005",
        "shortCode": "A229000",
        "codeName": "젠큐릭스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7082270000",
        "shortCode": "A082270",
        "codeName": "젬백스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7044060002",
        "shortCode": "A044060",
        "codeName": "조광ILI",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004910006",
        "shortCode": "A004910",
        "codeName": "조광페인트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004700001",
        "shortCode": "A004700",
        "codeName": "조광피혁",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001550003",
        "shortCode": "A001550",
        "codeName": "조비",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000480004",
        "shortCode": "A000480",
        "codeName": "조선내화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7120030002",
        "shortCode": "A120030",
        "codeName": "조선선재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034940007",
        "shortCode": "A034940",
        "codeName": "조아제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101730000",
        "shortCode": "A101730",
        "codeName": "조이맥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7067000000",
        "shortCode": "A067000",
        "codeName": "조이시티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7018470005",
        "shortCode": "A018470",
        "codeName": "조일알미늄",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002600005",
        "shortCode": "A002600",
        "codeName": "조흥",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7185750007",
        "shortCode": "A185750",
        "codeName": "종근당",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7063160006",
        "shortCode": "A063160",
        "codeName": "종근당바이오",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001630003",
        "shortCode": "A001630",
        "codeName": "종근당홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033340001",
        "shortCode": "A033340",
        "codeName": "좋은사람들",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036930006",
        "shortCode": "A036930",
        "codeName": "주성엔지니어링",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7044380004",
        "shortCode": "A044380",
        "codeName": "주연테크",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7239340003",
        "shortCode": "A239340",
        "codeName": "줌인터넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7072020001",
        "shortCode": "A072020",
        "codeName": "중앙백신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000440008",
        "shortCode": "A000440",
        "codeName": "중앙에너비스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054180005",
        "shortCode": "A054180",
        "codeName": "중앙오션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7228760005",
        "shortCode": "A228760",
        "codeName": "지노믹트리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7314130006",
        "shortCode": "A314130",
        "codeName": "지놈앤컴퍼니",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7043610005",
        "shortCode": "A043610",
        "codeName": "지니뮤직",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7263860009",
        "shortCode": "A263860",
        "codeName": "지니언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208350009",
        "shortCode": "A208350",
        "codeName": "지란지교시큐리티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114570005",
        "shortCode": "A114570",
        "codeName": "지스마트글로벌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7299480004",
        "shortCode": "A299480",
        "codeName": "지앤이헬스케어",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7051160000",
        "shortCode": "A051160",
        "codeName": "지어소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053050001",
        "shortCode": "A053050",
        "codeName": "지에스이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7119850006",
        "shortCode": "A119850",
        "codeName": "지엔씨에너지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065060006",
        "shortCode": "A065060",
        "codeName": "지엔코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7204840003",
        "shortCode": "A204840",
        "codeName": "지엘팜텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013870001",
        "shortCode": "A013870",
        "codeName": "지엠비코리아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7018290007",
        "shortCode": "A018290",
        "codeName": "지엠피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7071320006",
        "shortCode": "A071320",
        "codeName": "지역난방공사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7135160000",
        "shortCode": "A135160",
        "codeName": "지오씨",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7111820007",
        "shortCode": "A111820",
        "codeName": "지와이커머스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010580009",
        "shortCode": "A010580",
        "codeName": "지코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7035000009",
        "shortCode": "A035000",
        "codeName": "지투알",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7106080005",
        "shortCode": "A106080",
        "codeName": "지투하이소닉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115450009",
        "shortCode": "A115450",
        "codeName": "지트리비앤티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7219750007",
        "shortCode": "A219750",
        "codeName": "지티지웰니스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7088790001",
        "shortCode": "A088790",
        "codeName": "진도",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7018120006",
        "shortCode": "A018120",
        "codeName": "진로발효",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7109820001",
        "shortCode": "A109820",
        "codeName": "진매트릭스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086060001",
        "shortCode": "A086060",
        "codeName": "진바이오텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036890002",
        "shortCode": "A036890",
        "codeName": "진성티이씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003780004",
        "shortCode": "A003780",
        "codeName": "진양산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007370000",
        "shortCode": "A007370",
        "codeName": "진양제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010640001",
        "shortCode": "A010640",
        "codeName": "진양폴리",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7100250000",
        "shortCode": "A100250",
        "codeName": "진양홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7051630002",
        "shortCode": "A051630",
        "codeName": "진양화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7272450008",
        "shortCode": "A272450",
        "codeName": "진에어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011000007",
        "shortCode": "A011000",
        "codeName": "진원생명과학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002780005",
        "shortCode": "A002780",
        "codeName": "진흥기업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002782001",
        "shortCode": "A002787",
        "codeName": "진흥기업2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002781003",
        "shortCode": "A002785",
        "codeName": "진흥기업우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7233990001",
        "shortCode": "A233990",
        "codeName": "질경이",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7085660009",
        "shortCode": "A085660",
        "codeName": "차바이오텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KYG210AT1036",
        "shortCode": "A900040",
        "codeName": "차이나그레이트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009310004",
        "shortCode": "A009310",
        "codeName": "참엔지니어링",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7094850005",
        "shortCode": "A094850",
        "codeName": "참좋은여행",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004650008",
        "shortCode": "A004650",
        "codeName": "창해에탄올",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7278280003",
        "shortCode": "A278280",
        "codeName": "천보",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000650002",
        "shortCode": "A000650",
        "codeName": "천일고속",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7140290008",
        "shortCode": "A140290",
        "codeName": "청광종건",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7096240007",
        "shortCode": "A096240",
        "codeName": "청담러닝",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013720008",
        "shortCode": "A013720",
        "codeName": "청보산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012600003",
        "shortCode": "A012600",
        "codeName": "청호컴넷",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7066360009",
        "shortCode": "A066360",
        "codeName": "체리부로",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033250002",
        "shortCode": "A033250",
        "codeName": "체시스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7047820006",
        "shortCode": "A047820",
        "codeName": "초록뱀",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094360005",
        "shortCode": "A094360",
        "codeName": "칩스앤미디어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016920001",
        "shortCode": "A016920",
        "codeName": "카스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7220250005",
        "shortCode": "A220250",
        "codeName": "카이노스메드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7035720002",
        "shortCode": "A035720",
        "codeName": "카카오",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7042000000",
        "shortCode": "A042000",
        "codeName": "카페24",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006380000",
        "shortCode": "A006380",
        "codeName": "카프로",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7071850002",
        "shortCode": "A071850",
        "codeName": "캐스텍코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7180400004",
        "shortCode": "A180400",
        "codeName": "캔서롭",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7050110006",
        "shortCode": "A050110",
        "codeName": "캠시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7109070003",
        "shortCode": "A109070",
        "codeName": "컨버즈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "HK0000341732",
        "shortCode": "A900310",
        "codeName": "컬러레이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078340007",
        "shortCode": "A078340",
        "codeName": "컴투스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307930008",
        "shortCode": "A307930",
        "codeName": "컴퍼니케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7205290000",
        "shortCode": "A205290",
        "codeName": "케미메디",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7263700007",
        "shortCode": "A263700",
        "codeName": "케어랩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214370009",
        "shortCode": "A214370",
        "codeName": "케어젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7221980006",
        "shortCode": "A221980",
        "codeName": "케이디켐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043290006",
        "shortCode": "A043290",
        "codeName": "케이맥",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7317030005",
        "shortCode": "A317030",
        "codeName": "케이비17호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001620004",
        "shortCode": "A001620",
        "codeName": "케이비아이동국실업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7250930005",
        "shortCode": "A250930",
        "codeName": "케이비제10호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7258790005",
        "shortCode": "A258790",
        "codeName": "케이비제11호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7323940007",
        "shortCode": "A323940",
        "codeName": "케이비제18호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7192250009",
        "shortCode": "A192250",
        "codeName": "케이사인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7029460003",
        "shortCode": "A029460",
        "codeName": "케이씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7115500001",
        "shortCode": "A115500",
        "codeName": "케이씨에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7281820001",
        "shortCode": "A281820",
        "codeName": "케이씨텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7089150007",
        "shortCode": "A089150",
        "codeName": "케이씨티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025880006",
        "shortCode": "A025880",
        "codeName": "케이씨피드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093320000",
        "shortCode": "A093320",
        "codeName": "케이아이엔엑스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060900008",
        "shortCode": "A060900",
        "codeName": "케이알피앤이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7073010001",
        "shortCode": "A073010",
        "codeName": "케이에스피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7105330005",
        "shortCode": "A105330",
        "codeName": "케이엔더블유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039420005",
        "shortCode": "A039420",
        "codeName": "케이엘넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083550004",
        "shortCode": "A083550",
        "codeName": "케이엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7032500001",
        "shortCode": "A032500",
        "codeName": "케이엠더블유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225430008",
        "shortCode": "A225430",
        "codeName": "케이엠제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7145270005",
        "shortCode": "A145270",
        "codeName": "케이탑리츠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7064820004",
        "shortCode": "A064820",
        "codeName": "케이프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7256940008",
        "shortCode": "A256940",
        "codeName": "케이피에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024880007",
        "shortCode": "A024880",
        "codeName": "케이피에프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042040006",
        "shortCode": "A042040",
        "codeName": "케이피엠테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054410006",
        "shortCode": "A054410",
        "codeName": "케이피티유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217600006",
        "shortCode": "A217600",
        "codeName": "켐온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089010003",
        "shortCode": "A089010",
        "codeName": "켐트로닉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7220260004",
        "shortCode": "A220260",
        "codeName": "켐트로스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052400009",
        "shortCode": "A052400",
        "codeName": "코나아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033110008",
        "shortCode": "A033110",
        "codeName": "코너스톤네트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094860004",
        "shortCode": "A094860",
        "codeName": "코닉글로리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7046070009",
        "shortCode": "A046070",
        "codeName": "코다코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7047770003",
        "shortCode": "A047770",
        "codeName": "코데즈컴바인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078940004",
        "shortCode": "A078940",
        "codeName": "코드네이처",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080530009",
        "shortCode": "A080530",
        "codeName": "코디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7224060004",
        "shortCode": "A224060",
        "codeName": "코디엠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078650009",
        "shortCode": "A078650",
        "codeName": "코렌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7104540000",
        "shortCode": "A104540",
        "codeName": "코렌텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7027050004",
        "shortCode": "A027050",
        "codeName": "코리아나",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007811003",
        "shortCode": "A007815",
        "codeName": "코리아써우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007810005",
        "shortCode": "A007810",
        "codeName": "코리아써키트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR700781K015",
        "shortCode": "A00781K",
        "codeName": "코리아써키트2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7101670008",
        "shortCode": "A101670",
        "codeName": "코리아에스이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123410003",
        "shortCode": "A123410",
        "codeName": "코리아에프티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7152330007",
        "shortCode": "A152330",
        "codeName": "코리아오토글라스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003690005",
        "shortCode": "A003690",
        "codeName": "코리안리",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7036690006",
        "shortCode": "A036690",
        "codeName": "코맥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049430002",
        "shortCode": "A049430",
        "codeName": "코메론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7183300003",
        "shortCode": "A183300",
        "codeName": "코미코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041960006",
        "shortCode": "A041960",
        "codeName": "코미팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7089890008",
        "shortCode": "A089890",
        "codeName": "코세스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009730003",
        "shortCode": "A009730",
        "codeName": "코센",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7189350002",
        "shortCode": "A189350",
        "codeName": "코셋",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7192820009",
        "shortCode": "A192820",
        "codeName": "코스맥스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7044820009",
        "shortCode": "A044820",
        "codeName": "코스맥스비티아이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7222040008",
        "shortCode": "A222040",
        "codeName": "코스맥스엔비티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241710003",
        "shortCode": "A241710",
        "codeName": "코스메카코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005070008",
        "shortCode": "A005070",
        "codeName": "코스모신소재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005420005",
        "shortCode": "A005420",
        "codeName": "코스모화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7069110005",
        "shortCode": "A069110",
        "codeName": "코스온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7071950000",
        "shortCode": "A071950",
        "codeName": "코아스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7166480004",
        "shortCode": "A166480",
        "codeName": "코아스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045970001",
        "shortCode": "A045970",
        "codeName": "코아시아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7029960002",
        "shortCode": "A029960",
        "codeName": "코엔텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002020006",
        "shortCode": "A002020",
        "codeName": "코오롱",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003070000",
        "shortCode": "A003070",
        "codeName": "코오롱글로벌",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003071008",
        "shortCode": "A003075",
        "codeName": "코오롱글로벌우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7144620002",
        "shortCode": "A144620",
        "codeName": "코오롱머티리얼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7102940004",
        "shortCode": "A102940",
        "codeName": "코오롱생명과학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002021004",
        "shortCode": "A002025",
        "codeName": "코오롱우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7120110002",
        "shortCode": "A120110",
        "codeName": "코오롱인더",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7120111000",
        "shortCode": "A120115",
        "codeName": "코오롱인더우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR8840120008",
        "shortCode": "A950160",
        "codeName": "코오롱티슈진",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7138490008",
        "shortCode": "A138490",
        "codeName": "코오롱플라스틱",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7033290008",
        "shortCode": "A033290",
        "codeName": "코웰패션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7056360001",
        "shortCode": "A056360",
        "codeName": "코위버",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7121850002",
        "shortCode": "A121850",
        "codeName": "코이즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015710007",
        "shortCode": "A015710",
        "codeName": "코콤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052330008",
        "shortCode": "A052330",
        "codeName": "코텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7126600006",
        "shortCode": "A126600",
        "codeName": "코프라",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7200130003",
        "shortCode": "A200130",
        "codeName": "콜마비앤에이치",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7031820004",
        "shortCode": "A031820",
        "codeName": "콤텍시스템",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7225650001",
        "shortCode": "A225650",
        "codeName": "쿠첸",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7192400000",
        "shortCode": "A192400",
        "codeName": "쿠쿠홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7284740008",
        "shortCode": "A284740",
        "codeName": "쿠쿠홈시스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7060280005",
        "shortCode": "A060280",
        "codeName": "큐렉소",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015590003",
        "shortCode": "A015590",
        "codeName": "큐로",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7040350001",
        "shortCode": "A040350",
        "codeName": "큐로컴",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051780005",
        "shortCode": "A051780",
        "codeName": "큐로홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115180002",
        "shortCode": "A115180",
        "codeName": "큐리언트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7182360008",
        "shortCode": "A182360",
        "codeName": "큐브엔터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066310004",
        "shortCode": "A066310",
        "codeName": "큐에스아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7136660008",
        "shortCode": "A136660",
        "codeName": "큐엠씨",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7016600009",
        "shortCode": "A016600",
        "codeName": "큐캐피탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7264900002",
        "shortCode": "A264900",
        "codeName": "크라운제과",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR726490K013",
        "shortCode": "A26490K",
        "codeName": "크라운제과우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005740006",
        "shortCode": "A005740",
        "codeName": "크라운해태홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005741004",
        "shortCode": "A005745",
        "codeName": "크라운해태홀딩스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7215570003",
        "shortCode": "A215570",
        "codeName": "크로넥스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7043590009",
        "shortCode": "A043590",
        "codeName": "크로바하이텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7114120009",
        "shortCode": "A114120",
        "codeName": "크루셜텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7110790003",
        "shortCode": "A110790",
        "codeName": "크리스에프앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7083790006",
        "shortCode": "A083790",
        "codeName": "크리스탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KYG2115T1076",
        "shortCode": "A900250",
        "codeName": "크리스탈신소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045520004",
        "shortCode": "A045520",
        "codeName": "크린앤사이언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214150005",
        "shortCode": "A214150",
        "codeName": "클래시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7237880000",
        "shortCode": "A237880",
        "codeName": "클리오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7139670004",
        "shortCode": "A139670",
        "codeName": "키네마스터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7020120002",
        "shortCode": "A020120",
        "codeName": "키다리스튜디오",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7311270003",
        "shortCode": "A311270",
        "codeName": "키움제5호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039490008",
        "shortCode": "A039490",
        "codeName": "키움증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012170007",
        "shortCode": "A012170",
        "codeName": "키위미디어그룹",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7054780002",
        "shortCode": "A054780",
        "codeName": "키이스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7219130002",
        "shortCode": "A219130",
        "codeName": "타이거일렉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7180060006",
        "shortCode": "A180060",
        "codeName": "탑선",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7065130007",
        "shortCode": "A065130",
        "codeName": "탑엔지니어링",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7015890007",
        "shortCode": "A015890",
        "codeName": "태경산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006890008",
        "shortCode": "A006890",
        "codeName": "태경화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023160005",
        "shortCode": "A023160",
        "codeName": "태광",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003240009",
        "shortCode": "A003240",
        "codeName": "태광산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011280005",
        "shortCode": "A011280",
        "codeName": "태림포장",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7053620001",
        "shortCode": "A053620",
        "codeName": "태양",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004100004",
        "shortCode": "A004100",
        "codeName": "태양금속",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004101002",
        "shortCode": "A004105",
        "codeName": "태양금속우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7116100009",
        "shortCode": "A116100",
        "codeName": "태양기계",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7009410002",
        "shortCode": "A009410",
        "codeName": "태영건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009411000",
        "shortCode": "A009415",
        "codeName": "태영건설우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7044490001",
        "shortCode": "A044490",
        "codeName": "태웅",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001420009",
        "shortCode": "A001420",
        "codeName": "태원물산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007980006",
        "shortCode": "A007980",
        "codeName": "태평양물산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7191420009",
        "shortCode": "A191420",
        "codeName": "테고사이언스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7182690008",
        "shortCode": "A182690",
        "codeName": "테라셈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066700006",
        "shortCode": "A066700",
        "codeName": "테라젠이텍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7095610002",
        "shortCode": "A095610",
        "codeName": "테스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131970006",
        "shortCode": "A131970",
        "codeName": "테스나",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7055490007",
        "shortCode": "A055490",
        "codeName": "테이팩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7308700004",
        "shortCode": "A308700",
        "codeName": "테크엔",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7089030001",
        "shortCode": "A089030",
        "codeName": "테크윙",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7258050004",
        "shortCode": "A258050",
        "codeName": "테크트랜스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7054450002",
        "shortCode": "A054450",
        "codeName": "텔레칩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091440008",
        "shortCode": "A091440",
        "codeName": "텔레필드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7078000007",
        "shortCode": "A078000",
        "codeName": "텔코웨어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7200230001",
        "shortCode": "A200230",
        "codeName": "텔콘RF제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214420002",
        "shortCode": "A214420",
        "codeName": "토니모리",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7215480005",
        "shortCode": "A215480",
        "codeName": "토박스코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051360006",
        "shortCode": "A051360",
        "codeName": "토비스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045340007",
        "shortCode": "A045340",
        "codeName": "토탈소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7108230004",
        "shortCode": "A108230",
        "codeName": "톱텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7079970000",
        "shortCode": "A079970",
        "codeName": "투비소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7199800004",
        "shortCode": "A199800",
        "codeName": "툴젠",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7105550008",
        "shortCode": "A105550",
        "codeName": "트루윈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7026150003",
        "shortCode": "A026150",
        "codeName": "특수건설",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7117730002",
        "shortCode": "A117730",
        "codeName": "티로보틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033830001",
        "shortCode": "A033830",
        "codeName": "티비씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7228180006",
        "shortCode": "A228180",
        "codeName": "티씨엠생명과학",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7064760002",
        "shortCode": "A064760",
        "codeName": "티씨케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7246710008",
        "shortCode": "A246710",
        "codeName": "티앤알바이오팹",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7277880001",
        "shortCode": "A277880",
        "codeName": "티에스아이",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7131290009",
        "shortCode": "A131290",
        "codeName": "티에스이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019180009",
        "shortCode": "A019180",
        "codeName": "티에이치엔",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7062860002",
        "shortCode": "A062860",
        "codeName": "티엘아이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091810002",
        "shortCode": "A091810",
        "codeName": "티웨이항공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004870002",
        "shortCode": "A004870",
        "codeName": "티웨이홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7191600006",
        "shortCode": "A191600",
        "codeName": "티케이씨",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7104480009",
        "shortCode": "A104480",
        "codeName": "티케이케미칼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7309900009",
        "shortCode": "A309900",
        "codeName": "티티씨디펜스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7081150005",
        "shortCode": "A081150",
        "codeName": "티플랙스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7130740004",
        "shortCode": "A130740",
        "codeName": "티피씨글로벌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217880004",
        "shortCode": "A217880",
        "codeName": "틸론",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7084730001",
        "shortCode": "A084730",
        "codeName": "팅크웨어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7046210001",
        "shortCode": "A046210",
        "codeName": "파나진",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7034230003",
        "shortCode": "A034230",
        "codeName": "파라다이스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033540006",
        "shortCode": "A033540",
        "codeName": "파라텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043200005",
        "shortCode": "A043200",
        "codeName": "파루",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7217950005",
        "shortCode": "A217950",
        "codeName": "파마리서치바이오",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7214450009",
        "shortCode": "A214450",
        "codeName": "파마리서치프로덕트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7208340000",
        "shortCode": "A208340",
        "codeName": "파멥신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005690003",
        "shortCode": "A005690",
        "codeName": "파미셀",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7177830007",
        "shortCode": "A177830",
        "codeName": "파버나인",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037070000",
        "shortCode": "A037070",
        "codeName": "파세코",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7150900009",
        "shortCode": "A150900",
        "codeName": "파수닷컴",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7037030004",
        "shortCode": "A037030",
        "codeName": "파워넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7047310008",
        "shortCode": "A047310",
        "codeName": "파워로직스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7266870005",
        "shortCode": "A266870",
        "codeName": "파워풀엑스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7170790000",
        "shortCode": "A170790",
        "codeName": "파이오링크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123260002",
        "shortCode": "A123260",
        "codeName": "파인넥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7049120009",
        "shortCode": "A049120",
        "codeName": "파인디앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038950002",
        "shortCode": "A038950",
        "codeName": "파인디지털",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7278990007",
        "shortCode": "A278990",
        "codeName": "파인이엠텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7106240005",
        "shortCode": "A106240",
        "codeName": "파인테크닉스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131760001",
        "shortCode": "A131760",
        "codeName": "파인텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7065690000",
        "shortCode": "A065690",
        "codeName": "파커스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7140860008",
        "shortCode": "A140860",
        "codeName": "파크시스템스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7091700005",
        "shortCode": "A091700",
        "codeName": "파트론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7194510004",
        "shortCode": "A194510",
        "codeName": "파티게임즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7038160008",
        "shortCode": "A038160",
        "codeName": "팍스넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7202960001",
        "shortCode": "A202960",
        "codeName": "판도라티비",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7032800005",
        "shortCode": "A032800",
        "codeName": "판타지오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7043090000",
        "shortCode": "A043090",
        "codeName": "팜스웰바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036580009",
        "shortCode": "A036580",
        "codeName": "팜스코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7027710003",
        "shortCode": "A027710",
        "codeName": "팜스토리",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7225590009",
        "shortCode": "A225590",
        "codeName": "패션플랫폼",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054300009",
        "shortCode": "A054300",
        "codeName": "팬스타엔터프라이즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7068050004",
        "shortCode": "A068050",
        "codeName": "팬엔터테인먼트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7028670008",
        "shortCode": "A028670",
        "codeName": "팬오션",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7222110009",
        "shortCode": "A222110",
        "codeName": "팬젠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010820009",
        "shortCode": "A010820",
        "codeName": "퍼스텍",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016800005",
        "shortCode": "A016800",
        "codeName": "퍼시스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7263750002",
        "shortCode": "A263750",
        "codeName": "펄어비스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7251970000",
        "shortCode": "A251970",
        "codeName": "펌텍코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001020007",
        "shortCode": "A001020",
        "codeName": "페이퍼코리아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7327610002",
        "shortCode": "A327610",
        "codeName": "펨토바이오메드",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7087010005",
        "shortCode": "A087010",
        "codeName": "펩트론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7090080003",
        "shortCode": "A090080",
        "codeName": "평화산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7043370006",
        "shortCode": "A043370",
        "codeName": "평화정공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010770006",
        "shortCode": "A010770",
        "codeName": "평화홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7227420007",
        "shortCode": "A227420",
        "codeName": "포레스팅블록체인",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7119500007",
        "shortCode": "A119500",
        "codeName": "포메탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7016670002",
        "shortCode": "A016670",
        "codeName": "포비스티앤씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7056730005",
        "shortCode": "A056730",
        "codeName": "포스링크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7022100002",
        "shortCode": "A022100",
        "codeName": "포스코 ICT",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7058430000",
        "shortCode": "A058430",
        "codeName": "포스코강판",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009520008",
        "shortCode": "A009520",
        "codeName": "포스코엠텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7047050000",
        "shortCode": "A047050",
        "codeName": "포스코인터내셔널",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003670007",
        "shortCode": "A003670",
        "codeName": "포스코케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7189690001",
        "shortCode": "A189690",
        "codeName": "포시에스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7256630005",
        "shortCode": "A256630",
        "codeName": "포인트엔지니어링",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7141020008",
        "shortCode": "A141020",
        "codeName": "포티스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007630007",
        "shortCode": "A007630",
        "codeName": "폴루스바이오팜",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7290720002",
        "shortCode": "A290720",
        "codeName": "푸드나무",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005670005",
        "shortCode": "A005670",
        "codeName": "푸드웰",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7094940004",
        "shortCode": "A094940",
        "codeName": "푸른기술",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7007330004",
        "shortCode": "A007330",
        "codeName": "푸른저축은행",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017810003",
        "shortCode": "A017810",
        "codeName": "풀무원",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7093380004",
        "shortCode": "A093380",
        "codeName": "풍강",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7023900004",
        "shortCode": "A023900",
        "codeName": "풍국주정",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7103140000",
        "shortCode": "A103140",
        "codeName": "풍산",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005810007",
        "shortCode": "A005810",
        "codeName": "풍산홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7195440003",
        "shortCode": "A195440",
        "codeName": "퓨전데이타",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7214270001",
        "shortCode": "A214270",
        "codeName": "퓨쳐스트림네트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7220100002",
        "shortCode": "A220100",
        "codeName": "퓨쳐켐",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7035200005",
        "shortCode": "A035200",
        "codeName": "프럼파스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7203690003",
        "shortCode": "A203690",
        "codeName": "프로스테믹스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7303360002",
        "shortCode": "A303360",
        "codeName": "프로테옴텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7053610002",
        "shortCode": "A053610",
        "codeName": "프로텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053160008",
        "shortCode": "A053160",
        "codeName": "프리엠스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7075130005",
        "shortCode": "A075130",
        "codeName": "플랜티넷",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7222670002",
        "shortCode": "A222670",
        "codeName": "플럼라인생명과학",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7023770001",
        "shortCode": "A023770",
        "codeName": "플레이위드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7300080009",
        "shortCode": "A300080",
        "codeName": "플리토",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7150440006",
        "shortCode": "A150440",
        "codeName": "피노텍",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7032580003",
        "shortCode": "A032580",
        "codeName": "피델릭스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051380004",
        "shortCode": "A051380",
        "codeName": "피씨디렉트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7241820000",
        "shortCode": "A241820",
        "codeName": "피씨엘",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7237750005",
        "shortCode": "A237750",
        "codeName": "피앤씨테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7131390007",
        "shortCode": "A131390",
        "codeName": "피앤이솔루션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054340005",
        "shortCode": "A054340",
        "codeName": "피앤텔",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024850000",
        "shortCode": "A024850",
        "codeName": "피에스엠씨",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7319660007",
        "shortCode": "A319660",
        "codeName": "피에스케이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7031980006",
        "shortCode": "A031980",
        "codeName": "피에스케이홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002230001",
        "shortCode": "A002230",
        "codeName": "피에스텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7242350007",
        "shortCode": "A242350",
        "codeName": "피엔아이컴퍼니",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7239890007",
        "shortCode": "A239890",
        "codeName": "피엔에이치테크",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7137400008",
        "shortCode": "A137400",
        "codeName": "피엔티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7128660008",
        "shortCode": "A128660",
        "codeName": "피제이메탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006140008",
        "shortCode": "A006140",
        "codeName": "피제이전자",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7087600003",
        "shortCode": "A087600",
        "codeName": "픽셀플러스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7057880007",
        "shortCode": "A057880",
        "codeName": "필로시스헬스케어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7033180001",
        "shortCode": "A033180",
        "codeName": "필룩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7064800006",
        "shortCode": "A064800",
        "codeName": "필링크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7161580006",
        "shortCode": "A161580",
        "codeName": "필옵틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7270520000",
        "shortCode": "A270520",
        "codeName": "하나금융10호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7284620002",
        "shortCode": "A284620",
        "codeName": "하나금융11호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7261200000",
        "shortCode": "A261200",
        "codeName": "하나금융9호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086790003",
        "shortCode": "A086790",
        "codeName": "하나금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7099340002",
        "shortCode": "A099340",
        "codeName": "하나니켈1호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7099350001",
        "shortCode": "A099350",
        "codeName": "하나니켈2호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7067310003",
        "shortCode": "A067310",
        "codeName": "하나마이크론",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7307160002",
        "shortCode": "A307160",
        "codeName": "하나머스트제6호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7166090001",
        "shortCode": "A166090",
        "codeName": "하나머티리얼즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7293480000",
        "shortCode": "A293480",
        "codeName": "하나제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039130000",
        "shortCode": "A039130",
        "codeName": "하나투어",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7136480001",
        "shortCode": "A136480",
        "codeName": "하림",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7003380003",
        "shortCode": "A003380",
        "codeName": "하림지주",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7172580003",
        "shortCode": "A172580",
        "codeName": "하이골드12호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7153360003",
        "shortCode": "A153360",
        "codeName": "하이골드3호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7159650001",
        "shortCode": "A159650",
        "codeName": "하이골드8호",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7149980005",
        "shortCode": "A149980",
        "codeName": "하이로닉",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7013030002",
        "shortCode": "A013030",
        "codeName": "하이록코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7126700004",
        "shortCode": "A126700",
        "codeName": "하이비젼시스템",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7200470003",
        "shortCode": "A200470",
        "codeName": "하이셈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7071090005",
        "shortCode": "A071090",
        "codeName": "하이스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7317240000",
        "shortCode": "A317240",
        "codeName": "하이제4호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7221840002",
        "shortCode": "A221840",
        "codeName": "하이즈항공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7106190002",
        "shortCode": "A106190",
        "codeName": "하이텍팜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7019490002",
        "shortCode": "A019490",
        "codeName": "하이트론",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000080002",
        "shortCode": "A000080",
        "codeName": "하이트진로",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000082008",
        "shortCode": "A000087",
        "codeName": "하이트진로2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000140004",
        "shortCode": "A000140",
        "codeName": "하이트진로홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000141002",
        "shortCode": "A000145",
        "codeName": "하이트진로홀딩스우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7066130006",
        "shortCode": "A066130",
        "codeName": "하츠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7152550000",
        "shortCode": "A152550",
        "codeName": "한국ANKOR유전",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004590006",
        "shortCode": "A004590",
        "codeName": "한국가구",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7036460004",
        "shortCode": "A036460",
        "codeName": "한국가스공사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039340005",
        "shortCode": "A039340",
        "codeName": "한국경제TV",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005430004",
        "shortCode": "A005430",
        "codeName": "한국공항",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7071050009",
        "shortCode": "A071050",
        "codeName": "한국금융지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7071051007",
        "shortCode": "A071055",
        "codeName": "한국금융지주우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034950006",
        "shortCode": "A034950",
        "codeName": "한국기업평가",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010040004",
        "shortCode": "A010040",
        "codeName": "한국내화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025540006",
        "shortCode": "A025540",
        "codeName": "한국단자",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7222980005",
        "shortCode": "A222980",
        "codeName": "한국맥널티",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7226610004",
        "shortCode": "A226610",
        "codeName": "한국비엔씨",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7004090007",
        "shortCode": "A004090",
        "codeName": "한국석유",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025550005",
        "shortCode": "A025550",
        "codeName": "한국선재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002960003",
        "shortCode": "A002960",
        "codeName": "한국쉘석유",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023890007",
        "shortCode": "A023890",
        "codeName": "한국아트라스비엑스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7017890005",
        "shortCode": "A017890",
        "codeName": "한국알콜",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7080720006",
        "shortCode": "A080720",
        "codeName": "한국유니온제약",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7123890006",
        "shortCode": "A123890",
        "codeName": "한국자산신탁",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7015760002",
        "shortCode": "A015760",
        "codeName": "한국전력",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7063570006",
        "shortCode": "A063570",
        "codeName": "한국전자금융",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7041460007",
        "shortCode": "A041460",
        "codeName": "한국전자인증",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7006200000",
        "shortCode": "A006200",
        "codeName": "한국전자홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7101680007",
        "shortCode": "A101680",
        "codeName": "한국정밀기계",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039740006",
        "shortCode": "A039740",
        "codeName": "한국정보공학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053300000",
        "shortCode": "A053300",
        "codeName": "한국정보인증",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7025770009",
        "shortCode": "A025770",
        "codeName": "한국정보통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7271740003",
        "shortCode": "A271740",
        "codeName": "한국제5호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7281410001",
        "shortCode": "A281410",
        "codeName": "한국제6호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7291210003",
        "shortCode": "A291210",
        "codeName": "한국제7호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7310870001",
        "shortCode": "A310870",
        "codeName": "한국제8호스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002300002",
        "shortCode": "A002300",
        "codeName": "한국제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009540006",
        "shortCode": "A009540",
        "codeName": "한국조선해양",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023350002",
        "shortCode": "A023350",
        "codeName": "한국종합기술",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025890005",
        "shortCode": "A025890",
        "codeName": "한국주강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000970004",
        "shortCode": "A000970",
        "codeName": "한국주철관",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7104700000",
        "shortCode": "A104700",
        "codeName": "한국철강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017960006",
        "shortCode": "A017960",
        "codeName": "한국카본",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7023760002",
        "shortCode": "A023760",
        "codeName": "한국캐피탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054040001",
        "shortCode": "A054040",
        "codeName": "한국컴퓨터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7050540004",
        "shortCode": "A050540",
        "codeName": "한국코퍼레이션",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7161890009",
        "shortCode": "A161890",
        "codeName": "한국콜마",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024720005",
        "shortCode": "A024720",
        "codeName": "한국콜마홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7021650007",
        "shortCode": "A021650",
        "codeName": "한국큐빅",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7161390000",
        "shortCode": "A161390",
        "codeName": "한국타이어앤테크놀로지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7053590006",
        "shortCode": "A053590",
        "codeName": "한국테크놀로지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000240002",
        "shortCode": "A000240",
        "codeName": "한국테크놀로지그룹",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034830000",
        "shortCode": "A034830",
        "codeName": "한국토지신탁",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007280001",
        "shortCode": "A007280",
        "codeName": "한국특수형강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7168490001",
        "shortCode": "A168490",
        "codeName": "한국패러랠",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7037230000",
        "shortCode": "A037230",
        "codeName": "한국팩키지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010100006",
        "shortCode": "A010100",
        "codeName": "한국프랜지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7047810007",
        "shortCode": "A047810",
        "codeName": "한국항공우주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7123690000",
        "shortCode": "A123690",
        "codeName": "한국화장품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003350006",
        "shortCode": "A003350",
        "codeName": "한국화장품제조",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7030520001",
        "shortCode": "A030520",
        "codeName": "한글과컴퓨터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7052600004",
        "shortCode": "A052600",
        "codeName": "한네트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011500006",
        "shortCode": "A011500",
        "codeName": "한농화성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7002390003",
        "shortCode": "A002390",
        "codeName": "한독",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014790000",
        "shortCode": "A014790",
        "codeName": "한라",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7092460005",
        "shortCode": "A092460",
        "codeName": "한라IMS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7060980000",
        "shortCode": "A060980",
        "codeName": "한라홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7222810004",
        "shortCode": "A222810",
        "codeName": "한류AI센터",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039670005",
        "shortCode": "A039670",
        "codeName": "한류타임즈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053690004",
        "shortCode": "A053690",
        "codeName": "한미글로벌",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7042700005",
        "shortCode": "A042700",
        "codeName": "한미반도체",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008930000",
        "shortCode": "A008930",
        "codeName": "한미사이언스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7128940004",
        "shortCode": "A128940",
        "codeName": "한미약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7047080007",
        "shortCode": "A047080",
        "codeName": "한빛소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009240003",
        "shortCode": "A009240",
        "codeName": "한샘",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7020000006",
        "shortCode": "A020000",
        "codeName": "한섬",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003680006",
        "shortCode": "A003680",
        "codeName": "한성기업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7105630008",
        "shortCode": "A105630",
        "codeName": "한세실업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7069640001",
        "shortCode": "A069640",
        "codeName": "한세엠케이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016450009",
        "shortCode": "A016450",
        "codeName": "한세예스24홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010420008",
        "shortCode": "A010420",
        "codeName": "한솔PNS",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009180001",
        "shortCode": "A009180",
        "codeName": "한솔로지스틱스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7070300009",
        "shortCode": "A070300",
        "codeName": "한솔시큐어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7221610009",
        "shortCode": "A221610",
        "codeName": "한솔씨앤피",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7070590005",
        "shortCode": "A070590",
        "codeName": "한솔인티큐브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7213500002",
        "shortCode": "A213500",
        "codeName": "한솔제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014680003",
        "shortCode": "A014680",
        "codeName": "한솔케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004710000",
        "shortCode": "A004710",
        "codeName": "한솔테크닉스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004150009",
        "shortCode": "A004150",
        "codeName": "한솔홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7025750001",
        "shortCode": "A025750",
        "codeName": "한솔홈데코",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7226440006",
        "shortCode": "A226440",
        "codeName": "한송네오텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7042520007",
        "shortCode": "A042520",
        "codeName": "한스바이오메드",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7004960001",
        "shortCode": "A004960",
        "codeName": "한신공영",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011700002",
        "shortCode": "A011700",
        "codeName": "한신기계",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7078350006",
        "shortCode": "A078350",
        "codeName": "한양디지텍",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7045100005",
        "shortCode": "A045100",
        "codeName": "한양이엔지",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001750009",
        "shortCode": "A001750",
        "codeName": "한양증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001751007",
        "shortCode": "A001755",
        "codeName": "한양증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7018880005",
        "shortCode": "A018880",
        "codeName": "한온시스템",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009420001",
        "shortCode": "A009420",
        "codeName": "한올바이오파마",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7014130009",
        "shortCode": "A014130",
        "codeName": "한익스프레스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7046110003",
        "shortCode": "A046110",
        "codeName": "한일네트웍스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7024740003",
        "shortCode": "A024740",
        "codeName": "한일단조",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005860002",
        "shortCode": "A005860",
        "codeName": "한일사료",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7300720000",
        "shortCode": "A300720",
        "codeName": "한일시멘트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7123840001",
        "shortCode": "A123840",
        "codeName": "한일진공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002220002",
        "shortCode": "A002220",
        "codeName": "한일철강",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006390009",
        "shortCode": "A006390",
        "codeName": "한일현대시멘트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003300001",
        "shortCode": "A003300",
        "codeName": "한일홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7007770001",
        "shortCode": "A007770",
        "codeName": "한일화학",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7051600005",
        "shortCode": "A051600",
        "codeName": "한전KPS",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7052690005",
        "shortCode": "A052690",
        "codeName": "한전기술",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7130660004",
        "shortCode": "A130660",
        "codeName": "한전산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7107640005",
        "shortCode": "A107640",
        "codeName": "한중엔시에스",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7002320000",
        "shortCode": "A002320",
        "codeName": "한진",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7097230007",
        "shortCode": "A097230",
        "codeName": "한진중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003480001",
        "shortCode": "A003480",
        "codeName": "한진중공업홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7180640005",
        "shortCode": "A180640",
        "codeName": "한진칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR718064K016",
        "shortCode": "A18064K",
        "codeName": "한진칼우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005110002",
        "shortCode": "A005110",
        "codeName": "한창",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079170007",
        "shortCode": "A079170",
        "codeName": "한창산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7009460007",
        "shortCode": "A009460",
        "codeName": "한창제지",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7086960002",
        "shortCode": "A086960",
        "codeName": "한컴MDS",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7054920004",
        "shortCode": "A054920",
        "codeName": "한컴시큐어",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7077280006",
        "shortCode": "A077280",
        "codeName": "한컴지엠디",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002680007",
        "shortCode": "A002680",
        "codeName": "한탑",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7066110008",
        "shortCode": "A066110",
        "codeName": "한프",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000880005",
        "shortCode": "A000880",
        "codeName": "한화",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR700088K015",
        "shortCode": "A00088K",
        "codeName": "한화3우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7027390004",
        "shortCode": "A027390",
        "codeName": "한화갤러리아타임월드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7088350004",
        "shortCode": "A088350",
        "codeName": "한화생명",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000370007",
        "shortCode": "A000370",
        "codeName": "한화손해보험",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7265920009",
        "shortCode": "A265920",
        "codeName": "한화수성스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7317320000",
        "shortCode": "A317320",
        "codeName": "한화에스비아이스팩",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7012450003",
        "shortCode": "A012450",
        "codeName": "한화에어로스페이스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7264290008",
        "shortCode": "A264290",
        "codeName": "한화에이스스팩3호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7279410005",
        "shortCode": "A279410",
        "codeName": "한화에이스스팩4호",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000881003",
        "shortCode": "A000885",
        "codeName": "한화우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009830001",
        "shortCode": "A009830",
        "codeName": "한화케미칼",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7009831009",
        "shortCode": "A009835",
        "codeName": "한화케미칼우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003530003",
        "shortCode": "A003530",
        "codeName": "한화투자증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003531001",
        "shortCode": "A003535",
        "codeName": "한화투자증권우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7102210002",
        "shortCode": "A102210",
        "codeName": "해덕파워웨이",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7220630008",
        "shortCode": "A220630",
        "codeName": "해마로푸드서비스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7195870001",
        "shortCode": "A195870",
        "codeName": "해성디에스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7034810002",
        "shortCode": "A034810",
        "codeName": "해성산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7076610005",
        "shortCode": "A076610",
        "codeName": "해성옵틱스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7101530004",
        "shortCode": "A101530",
        "codeName": "해태제과식품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7220180004",
        "shortCode": "A220180",
        "codeName": "핸디소프트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7143210003",
        "shortCode": "A143210",
        "codeName": "핸즈코퍼레이션",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "HK0000214814",
        "shortCode": "A900270",
        "codeName": "헝셩그룹",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084990001",
        "shortCode": "A084990",
        "codeName": "헬릭스미스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000720003",
        "shortCode": "A000720",
        "codeName": "현대건설",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7267270007",
        "shortCode": "A267270",
        "codeName": "현대건설기계",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000721001",
        "shortCode": "A000725",
        "codeName": "현대건설우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7170030001",
        "shortCode": "A170030",
        "codeName": "현대공업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005440003",
        "shortCode": "A005440",
        "codeName": "현대그린푸드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7086280005",
        "shortCode": "A086280",
        "codeName": "현대글로비스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7064350002",
        "shortCode": "A064350",
        "codeName": "현대로템",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7079430005",
        "shortCode": "A079430",
        "codeName": "현대리바트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7012330007",
        "shortCode": "A012330",
        "codeName": "현대모비스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010620003",
        "shortCode": "A010620",
        "codeName": "현대미포조선",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7048410005",
        "shortCode": "A048410",
        "codeName": "현대바이오",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069960003",
        "shortCode": "A069960",
        "codeName": "현대백화점",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004560009",
        "shortCode": "A004560",
        "codeName": "현대비앤지스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004561007",
        "shortCode": "A004565",
        "codeName": "현대비앤지스틸우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016790008",
        "shortCode": "A016790",
        "codeName": "현대사료",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011760006",
        "shortCode": "A011760",
        "codeName": "현대상사",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011200003",
        "shortCode": "A011200",
        "codeName": "현대상선",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004310009",
        "shortCode": "A004310",
        "codeName": "현대약품",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7126560002",
        "shortCode": "A126560",
        "codeName": "현대에이치씨엔",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7017800004",
        "shortCode": "A017800",
        "codeName": "현대엘리베이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7307950006",
        "shortCode": "A307950",
        "codeName": "현대오토에버",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7011210002",
        "shortCode": "A011210",
        "codeName": "현대위아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7267260008",
        "shortCode": "A267260",
        "codeName": "현대일렉트릭",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004020004",
        "shortCode": "A004020",
        "codeName": "현대제철",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7267250009",
        "shortCode": "A267250",
        "codeName": "현대중공업지주",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005380001",
        "shortCode": "A005380",
        "codeName": "현대차",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005382007",
        "shortCode": "A005387",
        "codeName": "현대차2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005383005",
        "shortCode": "A005389",
        "codeName": "현대차3우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7005381009",
        "shortCode": "A005385",
        "codeName": "현대차우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7001500008",
        "shortCode": "A001500",
        "codeName": "현대차증권",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7227840006",
        "shortCode": "A227840",
        "codeName": "현대코퍼레이션홀딩스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7039010004",
        "shortCode": "A039010",
        "codeName": "현대통신",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7001450006",
        "shortCode": "A001450",
        "codeName": "현대해상",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7057050007",
        "shortCode": "A057050",
        "codeName": "현대홈쇼핑",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7204990006",
        "shortCode": "A204990",
        "codeName": "현성바이탈",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7092300003",
        "shortCode": "A092300",
        "codeName": "현우산업",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7053660007",
        "shortCode": "A053660",
        "codeName": "현진소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7011080009",
        "shortCode": "A011080",
        "codeName": "형지I&C",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7093240000",
        "shortCode": "A093240",
        "codeName": "형지엘리트",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003010006",
        "shortCode": "A003010",
        "codeName": "혜인",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7111110003",
        "shortCode": "A111110",
        "codeName": "호전실업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008770000",
        "shortCode": "A008770",
        "codeName": "호텔신라",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7008771008",
        "shortCode": "A008775",
        "codeName": "호텔신라우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7060560000",
        "shortCode": "A060560",
        "codeName": "홈센타홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7064240005",
        "shortCode": "A064240",
        "codeName": "홈캐스트",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7039610001",
        "shortCode": "A039610",
        "codeName": "화성밸브",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7002460004",
        "shortCode": "A002460",
        "codeName": "화성산업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7013520002",
        "shortCode": "A013520",
        "codeName": "화승알앤에이",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7241590009",
        "shortCode": "A241590",
        "codeName": "화승엔터프라이즈",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7006060008",
        "shortCode": "A006060",
        "codeName": "화승인더",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7010690006",
        "shortCode": "A010690",
        "codeName": "화신",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7126640002",
        "shortCode": "A126640",
        "codeName": "화신정공",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7086250008",
        "shortCode": "A086250",
        "codeName": "화신테크",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7204630008",
        "shortCode": "A204630",
        "codeName": "화이브라더스코리아",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7133820001",
        "shortCode": "A133820",
        "codeName": "화인베스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7061250007",
        "shortCode": "A061250",
        "codeName": "화일약품",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7134780006",
        "shortCode": "A134780",
        "codeName": "화진",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010660009",
        "shortCode": "A010660",
        "codeName": "화천기계",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000850008",
        "shortCode": "A000850",
        "codeName": "화천기공",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7016580003",
        "shortCode": "A016580",
        "codeName": "환인제약",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7032560005",
        "shortCode": "A032560",
        "codeName": "황금에스티",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7004800009",
        "shortCode": "A004800",
        "codeName": "효성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7094280005",
        "shortCode": "A094280",
        "codeName": "효성ITX",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7097870000",
        "shortCode": "A097870",
        "codeName": "효성오앤비",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7298040007",
        "shortCode": "A298040",
        "codeName": "효성중공업",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7298050006",
        "shortCode": "A298050",
        "codeName": "효성첨단소재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7298020009",
        "shortCode": "A298020",
        "codeName": "효성티앤씨",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7298000001",
        "shortCode": "A298000",
        "codeName": "효성화학",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7093370005",
        "shortCode": "A093370",
        "codeName": "후성",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7050090000",
        "shortCode": "A050090",
        "codeName": "휘닉스소재",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7081660003",
        "shortCode": "A081660",
        "codeName": "휠라코리아",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7290270008",
        "shortCode": "A290270",
        "codeName": "휴네시온",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005870001",
        "shortCode": "A005870",
        "codeName": "휴니드",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7284420007",
        "shortCode": "A284420",
        "codeName": "휴럼",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7090710005",
        "shortCode": "A090710",
        "codeName": "휴림로봇",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7205470008",
        "shortCode": "A205470",
        "codeName": "휴마시스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7115160004",
        "shortCode": "A115160",
        "codeName": "휴맥스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7028080000",
        "shortCode": "A028080",
        "codeName": "휴맥스홀딩스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7200670008",
        "shortCode": "A200670",
        "codeName": "휴메딕스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7212310007",
        "shortCode": "A212310",
        "codeName": "휴벡셀",
        "marketName": "KONEX"
    },
    {
        "fullCode": "KR7079980009",
        "shortCode": "A079980",
        "codeName": "휴비스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7065510000",
        "shortCode": "A065510",
        "codeName": "휴비츠",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7005010004",
        "shortCode": "A005010",
        "codeName": "휴스틸",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7243070000",
        "shortCode": "A243070",
        "codeName": "휴온스",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7084110006",
        "shortCode": "A084110",
        "codeName": "휴온스글로벌",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7145020004",
        "shortCode": "A145020",
        "codeName": "휴젤",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7069260008",
        "shortCode": "A069260",
        "codeName": "휴켐스",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7024060006",
        "shortCode": "A024060",
        "codeName": "흥구석유",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7010240000",
        "shortCode": "A010240",
        "codeName": "흥국",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7189980006",
        "shortCode": "A189980",
        "codeName": "흥국에프엔비",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7000540005",
        "shortCode": "A000540",
        "codeName": "흥국화재",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000542001",
        "shortCode": "A000547",
        "codeName": "흥국화재2우B",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7000541003",
        "shortCode": "A000545",
        "codeName": "흥국화재우",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7003280005",
        "shortCode": "A003280",
        "codeName": "흥아해운",
        "marketName": "KOSPI"
    },
    {
        "fullCode": "KR7037440005",
        "shortCode": "A037440",
        "codeName": "희림",
        "marketName": "KOSDAQ"
    },
    {
        "fullCode": "KR7238490007",
        "shortCode": "A238490",
        "codeName": "힘스",
        "marketName": "KOSDAQ"
    },
    {
        "shortCode": "A145850",
        "codeName": "TREX 펀더멘탈 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A097750",
        "codeName": "TREX 중소형가치",
        "marketName": "ETF"
    },
    {
        "shortCode": "A108590",
        "codeName": "TREX 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292150",
        "codeName": "TIGER TOP10",
        "marketName": "ETF"
    },
    {
        "shortCode": "A248270",
        "codeName": "TIGER S&P글로벌헬스케어(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A269370",
        "codeName": "TIGER S&P글로벌인프라(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A310970",
        "codeName": "TIGER MSCI Korea TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A289250",
        "codeName": "TIGER MSCI KOREA ESG유니버설",
        "marketName": "ETF"
    },
    {
        "shortCode": "A289260",
        "codeName": "TIGER MSCI KOREA ESG리더스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A138530",
        "codeName": "TIGER LG그룹+펀더멘털",
        "marketName": "ETF"
    },
    {
        "shortCode": "A228820",
        "codeName": "TIGER KTOP30",
        "marketName": "ETF"
    },
    {
        "shortCode": "A307620",
        "codeName": "TIGER KRX300선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A307610",
        "codeName": "TIGER KRX300레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292160",
        "codeName": "TIGER KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A091210",
        "codeName": "TIGER KRX100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300610",
        "codeName": "TIGER K게임",
        "marketName": "ETF"
    },
    {
        "shortCode": "A228790",
        "codeName": "TIGER 화장품",
        "marketName": "ETF"
    },
    {
        "shortCode": "A138540",
        "codeName": "TIGER 현대차그룹+펀더멘털",
        "marketName": "ETF"
    },
    {
        "shortCode": "A143860",
        "codeName": "TIGER 헬스케어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A277650",
        "codeName": "TIGER 코스피중형주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A277640",
        "codeName": "TIGER 코스피대형주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A210780",
        "codeName": "TIGER 코스피고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A277630",
        "codeName": "TIGER 코스피",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261060",
        "codeName": "TIGER 코스닥150IT",
        "marketName": "ETF"
    },
    {
        "shortCode": "A250780",
        "codeName": "TIGER 코스닥150선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261070",
        "codeName": "TIGER 코스닥150바이오테크",
        "marketName": "ETF"
    },
    {
        "shortCode": "A267300",
        "codeName": "TIGER 코스닥150로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A233160",
        "codeName": "TIGER 코스닥150 레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A232080",
        "codeName": "TIGER 코스닥150",
        "marketName": "ETF"
    },
    {
        "shortCode": "A245360",
        "codeName": "TIGER 차이나HSCEI",
        "marketName": "ETF"
    },
    {
        "shortCode": "A217780",
        "codeName": "TIGER 차이나CSI300인버스(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A204480",
        "codeName": "TIGER 차이나CSI300레버리지(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A192090",
        "codeName": "TIGER 차이나CSI300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A117690",
        "codeName": "TIGER 차이나항셍25",
        "marketName": "ETF"
    },
    {
        "shortCode": "A307520",
        "codeName": "TIGER 지주회사",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266140",
        "codeName": "TIGER 지속배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A157500",
        "codeName": "TIGER 증권",
        "marketName": "ETF"
    },
    {
        "shortCode": "A302210",
        "codeName": "TIGER 중장기국채선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A302200",
        "codeName": "TIGER 중장기국채선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A302190",
        "codeName": "TIGER 중장기국채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292130",
        "codeName": "TIGER 중소형성장",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292140",
        "codeName": "TIGER 중소형가치",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292120",
        "codeName": "TIGER 중소형",
        "marketName": "ETF"
    },
    {
        "shortCode": "A150460",
        "codeName": "TIGER 중국소비테마",
        "marketName": "ETF"
    },
    {
        "shortCode": "A248260",
        "codeName": "TIGER 일본TOPIX헬스케어(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A195920",
        "codeName": "TIGER 일본TOPIX(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292590",
        "codeName": "TIGER 일본엔선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292580",
        "codeName": "TIGER 일본엔선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292570",
        "codeName": "TIGER 일본엔선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292560",
        "codeName": "TIGER 일본엔선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A241180",
        "codeName": "TIGER 일본니케이225",
        "marketName": "ETF"
    },
    {
        "shortCode": "A123310",
        "codeName": "TIGER 인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A236350",
        "codeName": "TIGER 인도니프티50레버리지(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A225060",
        "codeName": "TIGER 이머징마켓MSCI레버리지(합..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A307510",
        "codeName": "TIGER 의료기기",
        "marketName": "ETF"
    },
    {
        "shortCode": "A091220",
        "codeName": "TIGER 은행",
        "marketName": "ETF"
    },
    {
        "shortCode": "A245350",
        "codeName": "TIGER 유로스탁스배당30",
        "marketName": "ETF"
    },
    {
        "shortCode": "A225050",
        "codeName": "TIGER 유로스탁스레버리지(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A195930",
        "codeName": "TIGER 유로스탁스50(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A130680",
        "codeName": "TIGER 원유선물Enhanced(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A217770",
        "codeName": "TIGER 원유선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261140",
        "codeName": "TIGER 우선주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A227570",
        "codeName": "TIGER 우량가치",
        "marketName": "ETF"
    },
    {
        "shortCode": "A228800",
        "codeName": "TIGER 여행레저",
        "marketName": "ETF"
    },
    {
        "shortCode": "A157490",
        "codeName": "TIGER 소프트웨어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A138520",
        "codeName": "TIGER 삼성그룹펀더멘털",
        "marketName": "ETF"
    },
    {
        "shortCode": "A329200",
        "codeName": "TIGER 부동산인프라고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A170350",
        "codeName": "TIGER 베타플러스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A211560",
        "codeName": "TIGER 배당성장",
        "marketName": "ETF"
    },
    {
        "shortCode": "A098560",
        "codeName": "TIGER 방송통신",
        "marketName": "ETF"
    },
    {
        "shortCode": "A091230",
        "codeName": "TIGER 반도체",
        "marketName": "ETF"
    },
    {
        "shortCode": "A228810",
        "codeName": "TIGER 미디어컨텐츠",
        "marketName": "ETF"
    },
    {
        "shortCode": "A225030",
        "codeName": "TIGER 미국S&P500선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A143850",
        "codeName": "TIGER 미국S&P500선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A225040",
        "codeName": "TIGER 미국S&P500레버리지(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A182480",
        "codeName": "TIGER 미국MSCI리츠(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A305080",
        "codeName": "TIGER 미국채10년선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261120",
        "codeName": "TIGER 미국달러선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261110",
        "codeName": "TIGER 미국달러선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A329750",
        "codeName": "TIGER 미국달러단기채권액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A245340",
        "codeName": "TIGER 미국다우존스30",
        "marketName": "ETF"
    },
    {
        "shortCode": "A203780",
        "codeName": "TIGER 미국나스닥바이오",
        "marketName": "ETF"
    },
    {
        "shortCode": "A133690",
        "codeName": "TIGER 미국나스닥100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A147970",
        "codeName": "TIGER 모멘텀",
        "marketName": "ETF"
    },
    {
        "shortCode": "A174350",
        "codeName": "TIGER 로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A123320",
        "codeName": "TIGER 레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A105010",
        "codeName": "TIGER 라틴35",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292100",
        "codeName": "TIGER 대형성장",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292110",
        "codeName": "TIGER 대형가치",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253990",
        "codeName": "TIGER 대만TAIEX선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A157450",
        "codeName": "TIGER 단기통안채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A272580",
        "codeName": "TIGER 단기채권액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A182490",
        "codeName": "TIGER 단기선진하이일드(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A137610",
        "codeName": "TIGER 농산물선물Enhanced(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139320",
        "codeName": "TIGER 금은선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139310",
        "codeName": "TIGER 금속선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A276000",
        "codeName": "TIGER 글로벌자원생산기업(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A275980",
        "codeName": "TIGER 글로벌4차산업혁신기술(합성..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A302170",
        "codeName": "TIGER 국채선물3년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A302180",
        "codeName": "TIGER 국채선물10년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A114820",
        "codeName": "TIGER 국채3년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A160580",
        "codeName": "TIGER 구리실물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A319640",
        "codeName": "TIGER 골드선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A237440",
        "codeName": "TIGER 경기방어채권혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139280",
        "codeName": "TIGER 경기방어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A217790",
        "codeName": "TIGER 가격조정",
        "marketName": "ETF"
    },
    {
        "shortCode": "A305540",
        "codeName": "TIGER 2차전지테마",
        "marketName": "ETF"
    },
    {
        "shortCode": "A310960",
        "codeName": "TIGER 200TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A243880",
        "codeName": "TIGER 200IT레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A289480",
        "codeName": "TIGER 200커버드콜ATM",
        "marketName": "ETF"
    },
    {
        "shortCode": "A166400",
        "codeName": "TIGER 200커버드콜5%OTM",
        "marketName": "ETF"
    },
    {
        "shortCode": "A315270",
        "codeName": "TIGER 200커뮤니케이션서비스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A243890",
        "codeName": "TIGER 200에너지화학레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252710",
        "codeName": "TIGER 200선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A267770",
        "codeName": "TIGER 200선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252000",
        "codeName": "TIGER 200동일가중",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139260",
        "codeName": "TIGER 200 IT",
        "marketName": "ETF"
    },
    {
        "shortCode": "A227540",
        "codeName": "TIGER 200 헬스케어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139240",
        "codeName": "TIGER 200 철강소재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139230",
        "codeName": "TIGER 200 중공업",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139250",
        "codeName": "TIGER 200 에너지화학",
        "marketName": "ETF"
    },
    {
        "shortCode": "A227560",
        "codeName": "TIGER 200 생활소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A227550",
        "codeName": "TIGER 200 산업재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139270",
        "codeName": "TIGER 200 금융",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139290",
        "codeName": "TIGER 200 경기소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139220",
        "codeName": "TIGER 200 건설",
        "marketName": "ETF"
    },
    {
        "shortCode": "A102110",
        "codeName": "TIGER 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292500",
        "codeName": "SMART KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A220130",
        "codeName": "SMART 중국본토 중소형 CSI500(합..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A208470",
        "codeName": "SMART 선진국MSCI World(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295040",
        "codeName": "SMART 200TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A168300",
        "codeName": "KTOP 코스피50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A100910",
        "codeName": "KOSEF KRX100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A331910",
        "codeName": "KOSEF Fn중소형",
        "marketName": "ETF"
    },
    {
        "shortCode": "A122260",
        "codeName": "KOSEF 통안채1년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A153270",
        "codeName": "KOSEF 코스피100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291620",
        "codeName": "KOSEF 코스닥150선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291630",
        "codeName": "KOSEF 코스닥150선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291610",
        "codeName": "KOSEF 코스닥150선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A316670",
        "codeName": "KOSEF 코스닥150",
        "marketName": "ETF"
    },
    {
        "shortCode": "A260270",
        "codeName": "KOSEF 저PBR가중",
        "marketName": "ETF"
    },
    {
        "shortCode": "A200250",
        "codeName": "KOSEF 인도Nifty50(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A104520",
        "codeName": "KOSEF 블루칩",
        "marketName": "ETF"
    },
    {
        "shortCode": "A260200",
        "codeName": "KOSEF 배당바이백Plus",
        "marketName": "ETF"
    },
    {
        "shortCode": "A139660",
        "codeName": "KOSEF 미국달러선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A225800",
        "codeName": "KOSEF 미국달러선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A230480",
        "codeName": "KOSEF 미국달러선물 인버스2X(합성..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A138230",
        "codeName": "KOSEF 미국달러선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A130730",
        "codeName": "KOSEF 단기자금",
        "marketName": "ETF"
    },
    {
        "shortCode": "A114470",
        "codeName": "KOSEF 국고채3년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A167860",
        "codeName": "KOSEF 국고채10년레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A148070",
        "codeName": "KOSEF 국고채10년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A104530",
        "codeName": "KOSEF 고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A294400",
        "codeName": "KOSEF 200TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253230",
        "codeName": "KOSEF 200선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253240",
        "codeName": "KOSEF 200선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253250",
        "codeName": "KOSEF 200선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A152280",
        "codeName": "KOSEF 200 선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A069660",
        "codeName": "KOSEF 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A271050",
        "codeName": "KODEX WTI원유선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261220",
        "codeName": "KODEX WTI원유선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A329670",
        "codeName": "KODEX TRF7030",
        "marketName": "ETF"
    },
    {
        "shortCode": "A329660",
        "codeName": "KODEX TRF5050",
        "marketName": "ETF"
    },
    {
        "shortCode": "A329650",
        "codeName": "KODEX TRF3070",
        "marketName": "ETF"
    },
    {
        "shortCode": "A315930",
        "codeName": "KODEX Top5PlusTR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A269420",
        "codeName": "KODEX S&P글로벌인프라(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A275300",
        "codeName": "KODEX MSCI퀄리티",
        "marketName": "ETF"
    },
    {
        "shortCode": "A275290",
        "codeName": "KODEX MSCI밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A275280",
        "codeName": "KODEX MSCI모멘텀",
        "marketName": "ETF"
    },
    {
        "shortCode": "A278540",
        "codeName": "KODEX MSCI Korea TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A289040",
        "codeName": "KODEX MSCI KOREA ESG유니버설",
        "marketName": "ETF"
    },
    {
        "shortCode": "A156080",
        "codeName": "KODEX MSCI Korea",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291890",
        "codeName": "KODEX MSCI EM선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A229720",
        "codeName": "KODEX KTOP30",
        "marketName": "ETF"
    },
    {
        "shortCode": "A306960",
        "codeName": "KODEX KRX300선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A306950",
        "codeName": "KODEX KRX300레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292190",
        "codeName": "KODEX KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266370",
        "codeName": "KODEX IT",
        "marketName": "ETF"
    },
    {
        "shortCode": "A296710",
        "codeName": "KODEX FnKorea50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A325010",
        "codeName": "KODEX Fn성장",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291660",
        "codeName": "KODEX China H선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A204450",
        "codeName": "KODEX China H 레버리지(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A099140",
        "codeName": "KODEX China H",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266420",
        "codeName": "KODEX 헬스케어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A298770",
        "codeName": "KODEX 한국대만IT프리미어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266410",
        "codeName": "KODEX 필수소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A247800",
        "codeName": "KODEX 턴어라운드투자",
        "marketName": "ETF"
    },
    {
        "shortCode": "A244660",
        "codeName": "KODEX 퀄리티Plus",
        "marketName": "ETF"
    },
    {
        "shortCode": "A138920",
        "codeName": "KODEX 콩선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A237350",
        "codeName": "KODEX 코스피100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A226490",
        "codeName": "KODEX 코스피",
        "marketName": "ETF"
    },
    {
        "shortCode": "A251340",
        "codeName": "KODEX 코스닥150선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A233740",
        "codeName": "KODEX 코스닥150 레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A229200",
        "codeName": "KODEX 코스닥 150",
        "marketName": "ETF"
    },
    {
        "shortCode": "A279540",
        "codeName": "KODEX 최소변동성",
        "marketName": "ETF"
    },
    {
        "shortCode": "A117680",
        "codeName": "KODEX 철강",
        "marketName": "ETF"
    },
    {
        "shortCode": "A102970",
        "codeName": "KODEX 증권",
        "marketName": "ETF"
    },
    {
        "shortCode": "A283580",
        "codeName": "KODEX 중국본토CSI300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A169950",
        "codeName": "KODEX 중국본토 A50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A273130",
        "codeName": "KODEX 종합채권(AA-이상)액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A091180",
        "codeName": "KODEX 자동차",
        "marketName": "ETF"
    },
    {
        "shortCode": "A101280",
        "codeName": "KODEX 일본TOPIX100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A114800",
        "codeName": "KODEX 인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A091170",
        "codeName": "KODEX 은행",
        "marketName": "ETF"
    },
    {
        "shortCode": "A144600",
        "codeName": "KODEX 은선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A140710",
        "codeName": "KODEX 운송",
        "marketName": "ETF"
    },
    {
        "shortCode": "A117460",
        "codeName": "KODEX 에너지화학",
        "marketName": "ETF"
    },
    {
        "shortCode": "A256750",
        "codeName": "KODEX 심천ChiNext(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A247790",
        "codeName": "KODEX 성장투자",
        "marketName": "ETF"
    },
    {
        "shortCode": "A251350",
        "codeName": "KODEX 선진국MSCI World",
        "marketName": "ETF"
    },
    {
        "shortCode": "A213610",
        "codeName": "KODEX 삼성그룹밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A102780",
        "codeName": "KODEX 삼성그룹",
        "marketName": "ETF"
    },
    {
        "shortCode": "A140700",
        "codeName": "KODEX 보험",
        "marketName": "ETF"
    },
    {
        "shortCode": "A244670",
        "codeName": "KODEX 밸류Plus",
        "marketName": "ETF"
    },
    {
        "shortCode": "A237370",
        "codeName": "KODEX 배당성장채권혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A211900",
        "codeName": "KODEX 배당성장",
        "marketName": "ETF"
    },
    {
        "shortCode": "A325020",
        "codeName": "KODEX 배당가치",
        "marketName": "ETF"
    },
    {
        "shortCode": "A091160",
        "codeName": "KODEX 반도체",
        "marketName": "ETF"
    },
    {
        "shortCode": "A244580",
        "codeName": "KODEX 바이오",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266360",
        "codeName": "KODEX 미디어&엔터테인먼트",
        "marketName": "ETF"
    },
    {
        "shortCode": "A218420",
        "codeName": "KODEX 미국S&P에너지(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A200030",
        "codeName": "KODEX 미국S&P산업재(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A185680",
        "codeName": "KODEX 미국S&P바이오(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A200040",
        "codeName": "KODEX 미국S&P금융(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A276970",
        "codeName": "KODEX 미국S&P고배당커버드콜(합성..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A219480",
        "codeName": "KODEX 미국S&P500선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A200020",
        "codeName": "KODEX 미국S&P IT(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A314250",
        "codeName": "KODEX 미국FANG플러스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A304670",
        "codeName": "KODEX 미국채울트라30년선물인버스..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A304660",
        "codeName": "KODEX 미국채울트라30년선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A308620",
        "codeName": "KODEX 미국채10년선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A280930",
        "codeName": "KODEX 미국러셀2000(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261260",
        "codeName": "KODEX 미국달러선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261270",
        "codeName": "KODEX 미국달러선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261250",
        "codeName": "KODEX 미국달러선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261240",
        "codeName": "KODEX 미국달러선물",
        "marketName": "ETF"
    },
    {
        "shortCode": "A304940",
        "codeName": "KODEX 미국나스닥100선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A244620",
        "codeName": "KODEX 모멘텀Plus",
        "marketName": "ETF"
    },
    {
        "shortCode": "A321410",
        "codeName": "KODEX 멀티에셋하이인컴(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A122630",
        "codeName": "KODEX 레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A214980",
        "codeName": "KODEX 단기채권PLUS",
        "marketName": "ETF"
    },
    {
        "shortCode": "A153130",
        "codeName": "KODEX 단기채권",
        "marketName": "ETF"
    },
    {
        "shortCode": "A273140",
        "codeName": "KODEX 단기변동금리부채권액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A102960",
        "codeName": "KODEX 기계장비",
        "marketName": "ETF"
    },
    {
        "shortCode": "A276990",
        "codeName": "KODEX 글로벌4차산업로보틱스(합성..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292770",
        "codeName": "KODEX 국채선물3년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A176950",
        "codeName": "KODEX 국채선물10년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A152380",
        "codeName": "KODEX 국채선물10년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A114260",
        "codeName": "KODEX 국고채3년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A138910",
        "codeName": "KODEX 구리선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A280940",
        "codeName": "KODEX 골드선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A132030",
        "codeName": "KODEX 골드선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A279530",
        "codeName": "KODEX 고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266390",
        "codeName": "KODEX 경기소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300950",
        "codeName": "KODEX 게임산업",
        "marketName": "ETF"
    },
    {
        "shortCode": "A117700",
        "codeName": "KODEX 건설",
        "marketName": "ETF"
    },
    {
        "shortCode": "A247780",
        "codeName": "KODEX 가치투자",
        "marketName": "ETF"
    },
    {
        "shortCode": "A271060",
        "codeName": "KODEX 3대농산물선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A305720",
        "codeName": "KODEX 2차전지산업",
        "marketName": "ETF"
    },
    {
        "shortCode": "A278530",
        "codeName": "KODEX 200TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252670",
        "codeName": "KODEX 200선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A284430",
        "codeName": "KODEX 200미국채혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252650",
        "codeName": "KODEX 200동일가중",
        "marketName": "ETF"
    },
    {
        "shortCode": "A223190",
        "codeName": "KODEX 200가치저변동",
        "marketName": "ETF"
    },
    {
        "shortCode": "A226980",
        "codeName": "KODEX 200 중소형",
        "marketName": "ETF"
    },
    {
        "shortCode": "A069500",
        "codeName": "KODEX 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A277540",
        "codeName": "KINDEX S&P아시아TOP50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A226380",
        "codeName": "KINDEX 한류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A261920",
        "codeName": "KINDEX 필리핀MSCI(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A305050",
        "codeName": "KINDEX 코스피",
        "marketName": "ETF"
    },
    {
        "shortCode": "A251890",
        "codeName": "KINDEX 코스닥(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A272910",
        "codeName": "KINDEX 중장기국공채액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A114460",
        "codeName": "KINDEX 중기국고채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A219900",
        "codeName": "KINDEX 중국본토CSI300레버리지(합..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A168580",
        "codeName": "KINDEX 중국본토CSI300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A205720",
        "codeName": "KINDEX 일본TOPIX인버스(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A196030",
        "codeName": "KINDEX 일본TOPIX레버리지(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A238720",
        "codeName": "KINDEX 일본Nikkei225(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A145670",
        "codeName": "KINDEX 인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A256440",
        "codeName": "KINDEX 인도네시아MSCI(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A316300",
        "codeName": "KINDEX 싱가포르리츠",
        "marketName": "ETF"
    },
    {
        "shortCode": "A322150",
        "codeName": "KINDEX 스마트하이베타",
        "marketName": "ETF"
    },
    {
        "shortCode": "A322120",
        "codeName": "KINDEX 스마트퀄리티",
        "marketName": "ETF"
    },
    {
        "shortCode": "A272230",
        "codeName": "KINDEX 스마트밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A272220",
        "codeName": "KINDEX 스마트모멘텀",
        "marketName": "ETF"
    },
    {
        "shortCode": "A322130",
        "codeName": "KINDEX 스마트로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A108450",
        "codeName": "KINDEX 삼성그룹섹터가중",
        "marketName": "ETF"
    },
    {
        "shortCode": "A131890",
        "codeName": "KINDEX 삼성그룹동일가중",
        "marketName": "ETF"
    },
    {
        "shortCode": "A245710",
        "codeName": "KINDEX 베트남VN30(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A143460",
        "codeName": "KINDEX 밸류대형",
        "marketName": "ETF"
    },
    {
        "shortCode": "A211260",
        "codeName": "KINDEX 배당성장",
        "marketName": "ETF"
    },
    {
        "shortCode": "A309230",
        "codeName": "KINDEX 미국WideMoat가치주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A181480",
        "codeName": "KINDEX 미국다우존스리츠(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A280320",
        "codeName": "KINDEX 미국4차산업인터넷(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291130",
        "codeName": "KINDEX 멕시코MSCI(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A152500",
        "codeName": "KINDEX 레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A265690",
        "codeName": "KINDEX 러시아MSCI(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A190620",
        "codeName": "KINDEX 단기통안채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A299080",
        "codeName": "KINDEX 국채선물3년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A299070",
        "codeName": "KINDEX 국채선물10년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A232590",
        "codeName": "KINDEX 골드선물 인버스2X(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A225130",
        "codeName": "KINDEX 골드선물 레버리지(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A332500",
        "codeName": "KINDEX 200TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A105190",
        "codeName": "KINDEX 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A241390",
        "codeName": "KBSTAR V&S셀렉트밸류채권혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A234310",
        "codeName": "KBSTAR V&S셀렉트밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A307020",
        "codeName": "KBSTAR KRX300선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A319870",
        "codeName": "KBSTAR KRX300미국달러선물혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A307010",
        "codeName": "KBSTAR KRX300레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292050",
        "codeName": "KBSTAR KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300310",
        "codeName": "KBSTAR KQ모멘텀밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300300",
        "codeName": "KBSTAR KQ모멘텀로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A270800",
        "codeName": "KBSTAR KQ고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A326240",
        "codeName": "KBSTAR IT플러스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A290130",
        "codeName": "KBSTAR ESG사회책임투자",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253290",
        "codeName": "KBSTAR 헬스케어채권혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253280",
        "codeName": "KBSTAR 헬스케어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A302450",
        "codeName": "KBSTAR 코스피",
        "marketName": "ETF"
    },
    {
        "shortCode": "A275750",
        "codeName": "KBSTAR 코스닥150선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A278240",
        "codeName": "KBSTAR 코스닥150선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A270810",
        "codeName": "KBSTAR 코스닥150",
        "marketName": "ETF"
    },
    {
        "shortCode": "A183700",
        "codeName": "KBSTAR 채권혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A250730",
        "codeName": "KBSTAR 차이나HSCEI(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A291680",
        "codeName": "KBSTAR 차이나H선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A283930",
        "codeName": "KBSTAR 지주회사",
        "marketName": "ETF"
    },
    {
        "shortCode": "A272570",
        "codeName": "KBSTAR 중장기국공채액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300290",
        "codeName": "KBSTAR 중소형모멘텀밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300280",
        "codeName": "KBSTAR 중소형모멘텀로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A281990",
        "codeName": "KBSTAR 중소형고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A136340",
        "codeName": "KBSTAR 중기우량회사채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A310080",
        "codeName": "KBSTAR 중국MSCI China선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A174360",
        "codeName": "KBSTAR 중국본토대형주CSI100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A183710",
        "codeName": "KBSTAR 주식혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A196220",
        "codeName": "KBSTAR 일본TOPIX레버리지(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A140580",
        "codeName": "KBSTAR 우량업종",
        "marketName": "ETF"
    },
    {
        "shortCode": "A140570",
        "codeName": "KBSTAR 수출주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A219390",
        "codeName": "KBSTAR 미국S&P원유생산기업(합성 ..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A267500",
        "codeName": "KBSTAR 미국장기국채선물인버스2X(..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A267450",
        "codeName": "KBSTAR 미국장기국채선물인버스(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A267490",
        "codeName": "KBSTAR 미국장기국채선물레버리지(..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A267440",
        "codeName": "KBSTAR 미국장기국채선물(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252720",
        "codeName": "KBSTAR 모멘텀밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252730",
        "codeName": "KBSTAR 모멘텀로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A315960",
        "codeName": "KBSTAR 대형고배당10TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A196230",
        "codeName": "KBSTAR 단기통안채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A272560",
        "codeName": "KBSTAR 단기국공채액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A326230",
        "codeName": "KBSTAR 내수주플러스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A276650",
        "codeName": "KBSTAR 글로벌4차산업IT(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295020",
        "codeName": "KBSTAR 국채선물10년인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295000",
        "codeName": "KBSTAR 국채선물10년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A282000",
        "codeName": "KBSTAR 국고채3년선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A114100",
        "codeName": "KBSTAR 국고채3년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266160",
        "codeName": "KBSTAR 고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A300640",
        "codeName": "KBSTAR 게임테마",
        "marketName": "ETF"
    },
    {
        "shortCode": "A105780",
        "codeName": "KBSTAR 5대그룹주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A285000",
        "codeName": "KBSTAR 200IT",
        "marketName": "ETF"
    },
    {
        "shortCode": "A315480",
        "codeName": "KBSTAR 200커뮤니케이션서비스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A285020",
        "codeName": "KBSTAR 200철강소재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A285010",
        "codeName": "KBSTAR 200중공업",
        "marketName": "ETF"
    },
    {
        "shortCode": "A284990",
        "codeName": "KBSTAR 200에너지화학",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252420",
        "codeName": "KBSTAR 200선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252410",
        "codeName": "KBSTAR 200선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A252400",
        "codeName": "KBSTAR 200선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A287330",
        "codeName": "KBSTAR 200생활소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A287320",
        "codeName": "KBSTAR 200산업재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A284980",
        "codeName": "KBSTAR 200금융",
        "marketName": "ETF"
    },
    {
        "shortCode": "A290080",
        "codeName": "KBSTAR 200고배당커버드콜ATM",
        "marketName": "ETF"
    },
    {
        "shortCode": "A287310",
        "codeName": "KBSTAR 200경기소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A287300",
        "codeName": "KBSTAR 200건설",
        "marketName": "ETF"
    },
    {
        "shortCode": "A148020",
        "codeName": "KBSTAR 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A332940",
        "codeName": "HANARO MSCI Korea TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A304760",
        "codeName": "HANARO KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A322400",
        "codeName": "HANARO e커머스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A306530",
        "codeName": "HANARO 코스닥150선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A304770",
        "codeName": "HANARO 코스닥150",
        "marketName": "ETF"
    },
    {
        "shortCode": "A306540",
        "codeName": "HANARO 단기통안채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A314700",
        "codeName": "HANARO 농업융복합산업",
        "marketName": "ETF"
    },
    {
        "shortCode": "A322410",
        "codeName": "HANARO 고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A332930",
        "codeName": "HANARO 200TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A306520",
        "codeName": "HANARO 200선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A304780",
        "codeName": "HANARO 200선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A293180",
        "codeName": "HANARO 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292730",
        "codeName": "FOCUS KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A285690",
        "codeName": "FOCUS ESG리더스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A269530",
        "codeName": "ARIRANG S&P글로벌인프라",
        "marketName": "ETF"
    },
    {
        "shortCode": "A309170",
        "codeName": "ARIRANG KRX300IT",
        "marketName": "ETF"
    },
    {
        "shortCode": "A309210",
        "codeName": "ARIRANG KRX300헬스케어",
        "marketName": "ETF"
    },
    {
        "shortCode": "A309200",
        "codeName": "ARIRANG KRX300자유소비재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A309190",
        "codeName": "ARIRANG KRX300산업재",
        "marketName": "ETF"
    },
    {
        "shortCode": "A309180",
        "codeName": "ARIRANG KRX300금융",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292750",
        "codeName": "ARIRANG KRX300",
        "marketName": "ETF"
    },
    {
        "shortCode": "A278420",
        "codeName": "ARIRANG ESG우수기업",
        "marketName": "ETF"
    },
    {
        "shortCode": "A328370",
        "codeName": "ARIRANG 코스피TR",
        "marketName": "ETF"
    },
    {
        "shortCode": "A301440",
        "codeName": "ARIRANG 코스피중형주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A122090",
        "codeName": "ARIRANG 코스피50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A227830",
        "codeName": "ARIRANG 코스피",
        "marketName": "ETF"
    },
    {
        "shortCode": "A301410",
        "codeName": "ARIRANG 코스닥150선물인버스",
        "marketName": "ETF"
    },
    {
        "shortCode": "A301400",
        "codeName": "ARIRANG 코스닥150",
        "marketName": "ETF"
    },
    {
        "shortCode": "A266550",
        "codeName": "ARIRANG 중형주저변동50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A280920",
        "codeName": "ARIRANG 주도업종",
        "marketName": "ETF"
    },
    {
        "shortCode": "A239660",
        "codeName": "ARIRANG 우량회사채50 1년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A256450",
        "codeName": "ARIRANG 심천차이넥스트(합성)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A195980",
        "codeName": "ARIRANG 신흥국MSCI(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A238670",
        "codeName": "ARIRANG 스마트베타Quality채권혼..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A222180",
        "codeName": "ARIRANG 스마트베타 Value",
        "marketName": "ETF"
    },
    {
        "shortCode": "A222200",
        "codeName": "ARIRANG 스마트베타 Quality",
        "marketName": "ETF"
    },
    {
        "shortCode": "A222190",
        "codeName": "ARIRANG 스마트베타 Momentum",
        "marketName": "ETF"
    },
    {
        "shortCode": "A236460",
        "codeName": "ARIRANG 스마트베타 LowVOL",
        "marketName": "ETF"
    },
    {
        "shortCode": "A195970",
        "codeName": "ARIRANG 선진국MSCI(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A269540",
        "codeName": "ARIRANG 미국S&P500(H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A332620",
        "codeName": "ARIRANG 미국장기우량회사채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A332610",
        "codeName": "ARIRANG 미국단기우량회사채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A213630",
        "codeName": "ARIRANG 미국다우존스고배당주(합..",
        "marketName": "ETF"
    },
    {
        "shortCode": "A287180",
        "codeName": "ARIRANG 미국나스닥기술주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A278620",
        "codeName": "ARIRANG 단기채권액티브",
        "marketName": "ETF"
    },
    {
        "shortCode": "A190160",
        "codeName": "ARIRANG 단기유동성",
        "marketName": "ETF"
    },
    {
        "shortCode": "A263190",
        "codeName": "ARIRANG 단기우량채권",
        "marketName": "ETF"
    },
    {
        "shortCode": "A189400",
        "codeName": "ARIRANG 글로벌MSCI(합성 H)",
        "marketName": "ETF"
    },
    {
        "shortCode": "A298340",
        "codeName": "ARIRANG 국채선물3년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A289670",
        "codeName": "ARIRANG 국채선물10년",
        "marketName": "ETF"
    },
    {
        "shortCode": "A251600",
        "codeName": "ARIRANG 고배당주채권혼합",
        "marketName": "ETF"
    },
    {
        "shortCode": "A161510",
        "codeName": "ARIRANG 고배당주",
        "marketName": "ETF"
    },
    {
        "shortCode": "A251590",
        "codeName": "ARIRANG 고배당저변동50",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295880",
        "codeName": "ARIRANG 200퀄리티",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253160",
        "codeName": "ARIRANG 200선물인버스2X",
        "marketName": "ETF"
    },
    {
        "shortCode": "A253150",
        "codeName": "ARIRANG 200선물레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295840",
        "codeName": "ARIRANG 200밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295860",
        "codeName": "ARIRANG 200모멘텀",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295890",
        "codeName": "ARIRANG 200로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A295820",
        "codeName": "ARIRANG 200동일가중",
        "marketName": "ETF"
    },
    {
        "shortCode": "A152100",
        "codeName": "ARIRANG 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A215620",
        "codeName": "흥국 S&P코리아로우볼",
        "marketName": "ETF"
    },
    {
        "shortCode": "A140950",
        "codeName": "파워 코스피100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A176710",
        "codeName": "파워 중기국고채",
        "marketName": "ETF"
    },
    {
        "shortCode": "A275540",
        "codeName": "파워 스마트밸류",
        "marketName": "ETF"
    },
    {
        "shortCode": "A192720",
        "codeName": "파워 고배당저변동성",
        "marketName": "ETF"
    },
    {
        "shortCode": "A152870",
        "codeName": "파워 200",
        "marketName": "ETF"
    },
    {
        "shortCode": "A211210",
        "codeName": "마이티 코스피고배당",
        "marketName": "ETF"
    },
    {
        "shortCode": "A159800",
        "codeName": "마이티 코스피100",
        "marketName": "ETF"
    },
    {
        "shortCode": "A292340",
        "codeName": "마이티 200커버드콜ATM레버리지",
        "marketName": "ETF"
    },
    {
        "shortCode": "A137930",
        "codeName": "마이다스 200커버드콜5%OTM",
        "marketName": "ETF"
    }
]
