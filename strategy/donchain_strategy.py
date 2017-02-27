#coding=utf-8
'''
    唐奇安通道
'''
import sys

import os
cwd = os.getcwd()
if cwd not in sys.path:
    sys.path.insert(0, os.getcwd())

import strategy.istrategy as istrategy
import data_api 

class DonchainStrategy(istrategy.IStrategy):
    def __init__(self, N1, N2):
        self.N1 = N1
        self.N2 = N2

    #返回最小开始索引
    def min_start(self):
        return max(self.N1, self.N2)

    #对某一天返回是否进场点
    def is_entry(self, dataApi, index):
        if dataApi.high(index) == dataApi.hhv(index, self.N1, data_api.KDataType.High):
            return True
        return False

    #对某一天返回是否出场
    def is_exit(self, dataApi, index, enterInfo):
        if dataApi.low(index) == dataApi.llv(index, self.N2, data_api.KDataType.Low):
            return True
        return False

    #进场使用资金比率
    def get_percent(self):
        return 1