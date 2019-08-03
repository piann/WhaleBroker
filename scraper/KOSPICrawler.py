from .base import *

class KOSPICrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
        self.formData = {
            "curr_id": 37426,
            "smlID": 2055174,
            "header": "KOSPI Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="KOSPI"
        self.collection = "DailyIndex"
        self.isAmountExist = True