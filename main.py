import requests
from datetime import timedelta
import datetime
from datenbank import *
import json

class Request():

    def __init__(self, country, number_of_days=7):
        self.Country = country
        self.Number_of_Days = number_of_days                                            #5
        self.Data = self.getinfo()
        self.range = self.getRange()

    def getinfo(self):
        '''Zieht die Daten aus der covid 19 api
        :return json Daten der api'''
        covid_url = "https://api.covid19api.com/total/dayone/country/"
        api_url = covid_url + self.Country
        get_url = requests.get(api_url)
        data = get_url.json()
        return data                                                                     #1

    def getRange(self):
        '''Grenzt die Tage auf den jeweilig eingegebenen wert ein'''
        time_today = datetime.date.today()
        delta = time_today - timedelta(days=self.Number_of_Days + 2)
        date_span = []

        for day in self.Data:
            if(str((day['Date']).split("T")[0]) > str(delta)):                          #checkt ob das datum sich in unserem Zeitraum befindet
                date_span.append(day)

        return date_span

    def printData(self):                                                                # I visualisierung
        print("Land:",  self.range[0]['Country'])
        active=[]
        confirmed=[]
        deaths=[]
        dates=[]
        recovered=[]
        database = Database()
        for day in self.range:
            active.append(day['Active'])
            confirmed.append(day['Confirmed'])
            deaths.append(day['Deaths'])
            recovered.append(day['Recovered'])
            dates.append((day["Date"]).split("T")[0][5:])
            print("Datum:", (day["Date"]).split("T")[0],"Aktive Fälle:", day['Active'],"Bestätigte Fälle:", day['Confirmed'], "Es sind gestorben:", day['Deaths'], "Es sind genesen:", day['Recovered'])

            database.insertInDb(dates, active, confirmed, deaths, recovered)
            # print(len(self.range))  # printed die datensätze für den Zeintraum und check nochmal wie viele es sind
        return {"active":active,"confirmed":confirmed,"deaths":deaths,"recovered":recovered,"dates":dates}

#abfrage = Request("Germany")                                                            # VI Länderauswahl
#abfrage.printData()
