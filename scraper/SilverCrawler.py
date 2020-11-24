from .base import *

class SilverCrawler(InvestingCrawler):
    
    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.formData = {
            "curr_id": 8836,
            "smlID": 300044,
            "header": "Silver Futures Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="silver"
        self.collection = "DailyFuture"
        self.isAmountExist = True