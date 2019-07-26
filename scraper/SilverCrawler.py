from .base import *

class SilverCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
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
        self.isAmountExist = True