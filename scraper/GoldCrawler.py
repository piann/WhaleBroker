from .base import *

class GoldCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
        self.formData = {
            "curr_id": 8830,
            "smlID": 300004,
            "header": "Gold Futures Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="gold"
        self.collection = "DailyFuture"
        self.isAmountExist = True