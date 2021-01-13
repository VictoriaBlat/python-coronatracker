import requests
from datetime import timedelta
import datetime
import json


class Request():

    def __init__(self, country, number_of_days=7): #5
        self.Country = country
        self.Number_of_Days = number_of_days #5
        self.Data = self.getinfo()
        self.range = self.getRange()


    def getinfo(self):
        covid_url = "https://api.covid19api.com/total/dayone/country/"
        api_url = covid_url + self.Country
        get_url = requests.get(api_url)
        data = get_url.json()
        return data

    def getRange(self):
        time_today=datetime.date.today()
        delta=time_today - timedelta(days =self.Number_of_Days +1)
        date_span=[]
        for day in self.Data:
            if(str((day['Date']).split("T")[0])>str(delta)): #checkt ob das datum sich in unserem Zeitraum befindet
                date_span.append(day)
        return date_span

    def printData(self): #visualisierung
        print("Land:",  self.range[0]['Country'])
        for day in self.range:

            print("Datum:", (day["Date"]).split("T")[0],"Aktive Fälle:", day['Active'],"Bestätigte Fälle:", day['Confirmed'], "Es sind gestorben:", day['Deaths'], "Genossen:",
                  day['Recovered'])
           # print(len(self.range))  # printed die datensätze für den Zeintraum und check nochmal wie viele es sind


"""abfrage1 = Request("spain",4)
abfrage2 = Request("germany",2)
abfrage1.printData()
abfrage2.printData()"""
