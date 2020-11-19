from .base import *

class NASDAQCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
        self.formData = {
            "curr_id": 14958,
            "smlID": 2035302,
            "header": "NASDAQ Composite Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="nasdaq"
        self.collection = "DailyIndex"
        self.isAmountExist = True