import sqlite3

from PyQt6.QtSql import QSqlDatabase

from Config.DBConfig import DB_TYPE, DB_NAME, TABLE_NAME_SERVICE_CITY, TABLE_NAME_ENCRYPT_INFO, COLUMN_NAME_ENCRYPT_ID, \
    TABLE_NAME_DATA_PROVIDER
from DB.DBConvert import raw2Bean


class CityDataSqlDriver:
    def __init__(self):
        self.encrypts = None
        self.encryptDic = None
        self.providerDic = None
        self.db = None
        self.dbConnect()

    def dbConnect(self):
        self.db = QSqlDatabase.addDatabase(DB_TYPE)
        self.db.setDatabaseName('./DBFile/' + DB_NAME)
        self.queryEncryptDic()
        self.queryProvider()

    def closeDB(self):
        self.db.close()

    def queryEncryptDic(self):
        self.encrypts = {}
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_ENCRYPT_INFO)
        for row in cursorResult:
            self.encrypts[str(row[1])] = row[2]
        conn.close()
        return self.encrypts

    def queryProvider(self):
        self.providers = {}
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_DATA_PROVIDER)
        for row in cursorResult:
            self.providers[str(row[1])] = row[2]
        conn.close()
        return self.providers

    def queryServiceCity(self):
        data_list = []
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_SERVICE_CITY)
        for row in cursorResult:
            data_list.append(raw2Bean((row[0], row[1], row[2], row[3]), self.encrypts, self.providers))
        conn.close()
        return data_list

    def connectDB(self, table_name):
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + table_name)
        return cursorResult

    def deleteServiceCityById(self, serviceId):
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursor.execute('delete from ' + TABLE_NAME_SERVICE_CITY + ' where id= ' + str(serviceId))
        conn.commit()
        cursor.close()
        conn.close()

    def createCityConfigInfo(self, city):
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        sql = 'insert into ' + TABLE_NAME_SERVICE_CITY + '(cityname,encryptTypeId,dataproviderId) values (?,?,?)'
        data = (city[0], city[1], city[2])
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

    def queryCityInfoByCityName(self, cityName):
        data_list = []
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_SERVICE_CITY+' WHERE cityname= \''+cityName+'\'')
        for row in cursorResult:
            data_list.append(raw2Bean((row[0], row[1], row[2], row[3]), self.encrypts, self.providers))
        conn.close()
        return data_list

    def updateCityServiceInfo(self, city):
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        sql = 'update ServiceCity set cityname=?,encryptTypeId=?,dataproviderId=? where id='+str(city[0])
        data = (city[1], city[2], city[3])
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    sqlDriver = CityDataSqlDriver()
    cities = sqlDriver.queryServiceCity()
    # jsonGenerate = GenerateJson()
    # jsonGenerate.convert2Json(cities)
