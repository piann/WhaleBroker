from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime

class BrentOilCrawler(InvestingCrawler):
    
    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.formData = {
            "curr_id": 8833,
            "smlID": 300028,
            "header": "Brent Oil Futures Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName = "brentOil"
        self.collection = "DailyFuture"
        self.isAmountExist = True
 