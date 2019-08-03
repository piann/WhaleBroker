from .base import *

class KOSDAQCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
        self.formData = {
            "curr_id": 38016,
            "smlID": 2055462,
            "header": "KOSDAQ Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="KOSDAQ"
        self.collection = "DailyIndex"
        self.isAmountExist = True