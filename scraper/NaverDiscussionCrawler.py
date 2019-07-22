from .base import *

class NaverDiscussionCrawler(InfoCrawler):

    def __init__(self):
        super().__init__()
        self.baseUrl = "https://finance.naver.com/item/board.nhn"
