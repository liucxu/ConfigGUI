import json
import os.path

from Config.GitConfig import DEFAULT_GIT_PATH, GIT_TOKEN
from Config.JsonConfig import JSON_NAME
from DB.CityDataSqlDriver import CityDataSqlDriver
from Git.GitRepository import GitRepository


class GenerateJson:
    def __init__(self):
        self.sqlDriver = CityDataSqlDriver()
        self.git = GitRepository(DEFAULT_GIT_PATH, 'https://'+GIT_TOKEN+'@github.com/liucxu/V2IConfig.git')

    def convert2Json(self):
        cityJsonArray = []
        cities = self.sqlDriver.queryServiceCity()
        if os.path.exists(DEFAULT_GIT_PATH + '/' + JSON_NAME):
            os.remove(DEFAULT_GIT_PATH + '/' + JSON_NAME)
        for city in cities:
            cityJson = json.dumps(city.toDic(), ensure_ascii=False)
            cityJsonArray.append(cityJson)
        first_item = True
        with open(DEFAULT_GIT_PATH + '/' + JSON_NAME, 'w', encoding='utf-8') as out:
            out.write('[')
            for item in cityJsonArray:
                if first_item:
                    # out.write(json.dumps(item, ensure_ascii=False))
                    out.write(item)
                    first_item = False
                else:
                    out.write(","+item)
                    # out.write("," + json.dumps(item, ensure_ascii=False))
            out.write("]")
        self.git.sync()

