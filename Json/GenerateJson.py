import json
import os.path

from Config.JsonConfig import JSON_NAME
from DB.CityDataSqlDriver import CityDataSqlDriver


class GenerateJson:
    def __init__(self):
        self.sqlDriver = CityDataSqlDriver()

    def convert2Json(self):
        cityJsonArray = []
        cities = self.sqlDriver.queryServiceCity()
        if os.path.exists(r'./JsonFile/' + JSON_NAME):
            os.remove(r'./JsonFile/' + JSON_NAME)
        for city in cities:
            cityJson = json.dumps(city.toDic(), ensure_ascii=False)
            cityJsonArray.append(cityJson)
        first_item = True
        with open(r'./JsonFile/' + JSON_NAME, 'w', encoding='utf-8') as out:
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

