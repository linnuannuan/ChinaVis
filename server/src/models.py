import pandas as pd
import ndjson
import simplejson
import os
from datetime import date
import time

# PATH_TESTDATA = '../server/data/testdata1231.ndjson'
PATH_TESTDATA = '../server/data/0130'

class Model:
    def __init__(self):
        # get test data

        for root, dirs, files in os.walk(r"C:\Users\jfly\Desktop\ChinaVis2020\ChinaVis\server\data\0131"):
            # print(root, dirs, files)
            data = []
            for file in files:
                # 获取文件所属目录,文件路径,文件名
                file_path = os.path.join(root, file)
                # print(file_path)
                f_data = list(filter(lambda x: x['date']['utc'] == "2020-01-31T06:00:00.000Z", ndjson.load(open(file_path, 'rb'))))


                # 格式化数据
                def get_data(x):  #获取需要的数据
                    a = {}
                    a['coordinates'] = [x['coordinates']['latitude'], x['coordinates']['longitude']]
                    a['country'] = x['country']
                    a['city'] = x['city']
                    a['location'] = x['location']
                    a['parameter'] = x['parameter']
                    a['value'] = x['value']
                    # a['date'
                    # ''] = x['date']['utc']
                    return a

                data = data + list(map(get_data, f_data))
            self.data = pd.DataFrame(data, columns=['coordinates', 'country', 'city', 'location', 'parameter', 'value', 'date'])
            # print(self.data)
        # self.data = ndjson.load(open(PATH_TESTDATA, 'rb'))
        # print(data)

    def getData(self):
        print(len(self.data))
        return simplejson.loads(self.data.to_json(orient="records"))

    def getDataByParam(self, parameter="pm25"):
        c_data = self.data.query('parameter == @parameter')
        print(len(c_data))
        return simplejson.loads(c_data.to_json(orient="records"))

    # 默认地图为全球
    # def getDataByCountry(self, parameter="pm25"):

    # 默认时间对所有时间取平均值
    # def getDataByTime(self, start_time='2019-12-31T00:00:00.000Z', end_time='2020-1-1T00:00:00.000Z'):
    #     cdata = self.data.query('@start_time <= date <= @end_time')
    #     print(cdata)
    #     return cdata




