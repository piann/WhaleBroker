from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime
from .base import *
import random

class NaverDiscussionCrawler(InfoCrawler):

    def __init__(self):
        super().__init__()
        self.baseBoardUrl = "https://finance.naver.com/item/board.nhn"
        self.collection = "DailyHot"


    @tryCatchWrapped
    def getResultData(self, code, fromPage, toPage):
        totalInfoList = []
        if fromPage > toPage:
            logging.error("fromPage value cannot be bigger than toPage value")
            return None
    
        prevInfoListInPage = None

        for pageIdx in range(fromPage, toPage+1):
            infoListInPage = self.parsePage(code,pageIdx)
            
            if pageIdx is not None:
                totalInfoList += infoListInPage
            
            # check if this page is last page
            if infoListInPage == prevInfoListInPage:
                break

            self.breakTime = random.randint(1,4)
            self.setRandomUserAgent()
            time.sleep(self.breakTime)
            prevInfoListInPage = infoListInPage

        candidateMinDate = [infoChunk["time"] for infoChunk in infoListInPage]
        minDatetimeObj = getMinDate(candidateMinDate)
        dateObjList = list(set([infoChunk["time"].date() for infoChunk in totalInfoList]))
        #resultDict format : {datetime.date(2019,3,19):{viewCount:0, replyCount:0}, ...}
        resultDict = {dateObj:{"viewCount":0, "replyCount":0} for dateObj in dateObjList}

        for infoChunk in totalInfoList:
            datetimeObj = infoChunk["time"]
            viewCount = infoChunk["viewCount"]
            replyCount = infoChunk["replyCount"]
            dateObj = datetimeObj.date()
             
            resultDict[dateObj]["viewCount"] += viewCount
            resultDict[dateObj]["replyCount"] += replyCount
        
        
        resultDict.pop(minDatetimeObj.date(),None) # exclude minimum date info bcoz that isn't considered utterly. 
        print(minDatetimeObj)
        print(resultDict)
        return resultDict


    @tryCatchWrapped
    def parsePage(self, code, pageIdx):
        params = {"code":str(code), "page":str(pageIdx)}
        res = self.requestGetWithProxy(self.baseBoardUrl, headers=self.headers, params=params, timeout=15)
        if res is None or res.ok is False:
            logging.error("Some problem in request")
            return None

        html = res.text
        
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.select(
            'table.type2 tr'
        )
        infoSoupList = [row for row in rows if str(row).find("mouseOut") >= 0]
        
        
        dateAndViewSelector = 'td > span.tah'
        replySelector = 'td.title > a > span.tah'
        
        infoDict = []
        print(len(infoSoupList))
        # must consider when endPrice is blank b4 market is closed
        

        for infoSoup in infoSoupList:
            dateAndViewList = infoSoup.select(dateAndViewSelector)
            replyInfo = infoSoup.select(replySelector)
            
            if len(dateAndViewList) > 0:
                # get date info
                dateStr = dateAndViewList[0].text
                year, month, dayAndTime = dateStr.split(".")
                day, time = dayAndTime.split(" ")
                hour, minute = time.split(":") 
                dateObj = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))

                # get view info
                viewCount = int(dateAndViewList[1].text)
                
                # get reply count info
                if len(replyInfo) > 0:
                    tmp = replyInfo[0].text.replace("<b>","").replace("</b>","")
                    replyCount = int(tmp.replace(",","").replace("[","").replace("]",""))    
                else:
                    replyCount = 0
                print(dateObj)
                print(viewCount)
                print(replyCount)

                infoDict.append({"time":dateObj, "viewCount":viewCount , "replyCount":replyCount})


        return infoDict