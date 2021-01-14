from main import *
import os
import sqlite3

PATH = os.path.join(os.path.dirname(__file__), 'database_api.sqlite3')


class Database():

    def __init__(self):
        '''
        Stellt Verbindung zur Datenbank her,
        erstellt eine Datenbank datei wenn nicht vorhanden
        '''
        self.connection = sqlite3.connect(PATH)
        try:
            self.newDb()
        except sqlite3.OperationalError:
            pass

    def newDb(self):
        '''Ersellte eine Tabelle für covid Einträge
        '''
        cursor = self.connection.cursor()
        query = f'''
            CREATE TABLE covid_status (
                id INTEGER PRIMARY KEY,
                dates VARCHAR(200),
                active VARCHAR(200),
                confirmed VARCHAR(200),
                deaths VARCHAR(200),
                recovered VARCHAR(200)
            );
            '''
        cursor.execute(query)
        self.connection.commit()


    def insertInDb(self, dates, active, confirmed, deaths, recovered):
        print(dates,active,confirmed,deaths,recovered)
        cursor = self.connection.cursor()
        for val in range(0,len(dates)):
            insert_query = f'''
                INSERT INTO covid_status (dates, active, confirmed, deaths, recovered)
                VALUES ("{dates[val]}", "{active[val]}", "{confirmed[val]}", "{deaths[val]}", "{recovered[val]}");
                '''
            cursor.execute(insert_query)
        self.connection.commit()

database = Database()
#meine_datenbank.insertInDb("1111", "2222", "3333", "4444", "5555")
