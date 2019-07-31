from .base import *
from ..common import *
import time
import datetime
import requests
import json


class ShortSellCrawler(InfoCrawler):

    def __init__(self):
        super().__init__()
        self.OTPUrl = "https://short.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=SRT%2F02%2F02010100%2Fsrt02010100&name=form&_={0}"
        self.baseUrl = "https://short.krx.co.kr/contents/SRT/99/SRT99000001.jspx"
        self.setRandomUserAgent()
    
    @tryCatchWrapped
    def getResultData(self, code, fromDate, toDate):
        timeVar = int(datetime.datetime.now().timestamp()*1000)
        res = requests.get(self.OTPUrl.format(timeVar), headers=self.headers)
        if res is None or res.ok==False:
            return None
        otp = res.content
        data = {
            "isu_cd": self.getFullCode(code),
            "strt_dd": fromDate.replace("/",""),
            "end_dd": toDate.replace("/",""),
            "pagePath": "/contents/SRT/02/02010100/SRT02010100.jsp",
            "code": otp
        }

        res = requests.post(self.baseUrl, data=data)
        if res.ok is None or res.content == None:
            logging.error("Some problem in request")
            return None

        resultDict = {}
        dumpData = json.loads(res.content)
        infoJsonList = dumpData['block1'] 
        for infoDict in infoJsonList:
            dateStr = infoDict['trd_dd']
            year, month, day = dateStr.split("/")
            dateObj = datetime.datetime(int(year), int(month), int(day))
            transactionValue = infoDict['cvsrtsell_trdval']
            if transactionValue == '-':
                transactionValue = 0
            else:
                transactionValue = int(transactionValue.replace(",",""))
            resultDict[dateObj] = {"tValue":transactionValue}


    @tryCatchWrapped
    def getFullCode(self,shortCode):
        for infoDict in CODE_TABLE:
            if shortCode in infoDict["shortCode"]:
                return infoDict["fullCode"] 
        