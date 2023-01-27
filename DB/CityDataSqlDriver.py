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
        self.initEncryptDic()
        self.initProvider()

    def closeDB(self):
        self.db.close()

    def initEncryptDic(self):
        self.encrypts = {}
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_ENCRYPT_INFO)
        for row in cursorResult:
            self.encrypts[str(row[1])] = row[2]
        conn.close()

    def initProvider(self):
        self.providers = {}
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_DATA_PROVIDER)
        for row in cursorResult:
            self.providers[str(row[1])] = row[2]
        conn.close()

    def queryServiceCity(self):
        data_list = []
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + TABLE_NAME_SERVICE_CITY)
        for row in cursorResult:
            data_list.append(raw2Bean((row[1], row[2], row[3]), self.encrypts, self.providers))
        conn.close()
        return data_list

    def connectDB(self, table_name):
        conn = sqlite3.connect('./DBFile/' + DB_NAME)
        cursor = conn.cursor()
        cursorResult = cursor.execute('select * from ' + table_name)
        return cursorResult


if __name__ == '__main__':
    sqlDriver = CityDataSqlDriver()
    sqlDriver.queryServiceCity()
