import sys
import random

import os
cwd = os.getcwd()
if cwd not in sys.path:
    sys.path.insert(0, os.getcwd())

import ipool.ipool as ipool
import data_api 

class StockPool(ipool.IStockPool):
    #num持有数目
    def __init__(self, num, N1):
        ipool.IStockPool.__init__(self, num, N1)
        pass

    #返回日期date，满足条件的前N个
    def select(self, dataApiList, date):
        tmp = {}
        sortList = []
        for dataApi in dataApiList:
            tmp['key'] = dataApi.get_code()
            tmp['data'] = dataApi        
            sortList.append(tmp)
        random.shuffle(sortList)
        return sortList[:self.num]

    def select_out(self, dataApiList, enterInfoList, date):
        return self.select(dataApiList, date)
