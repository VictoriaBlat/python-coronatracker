from main import *
import requests

abfrage1 = Request("Spain",4)

class Calculation():
    def __init__(self, request):
        self.Request=request
        self.Population=self.current_population()

    def getInfektionRate(self):
        n=0
        while(len(self.Request.range)>n):
            if n==0:
                print("noch kein wert",self.Request.range[n]['Active'])
                self.Request.range[n]["Daily_infektion_rate"]="kein wert"
            else:
                self.Request.range[n]["Daily_infektion_rate"]=round((self.Request.range[n]['Active'] * 100 / self.Request.range[n - 1]['Active']) - 100,2)
                print("aktive fälle",self.Request.range[n]['Active'])
            n+=1
        for x in self.Request.range:
            print("Infektionsrate",x["Daily_infektion_rate"],"%")

    def current_population(self):
        url = "https://restcountries.eu/rest/v2/all"
        get_url = requests.get(url)
        data = get_url.json()

        for el in data:
            if el["name"]==self.Request.range[0]["Country"]:
                return el["population"]


    def recoveredRatio(self):
        population_size = self.Population

        ratio=round(100/population_size*self.Request.range[-1]['Recovered'],2)
        print("recovered ratio", ratio, "%")
    def infektedRatio(self):
        population_size=self.Population
        ratio=round(100/population_size*self.Request.range[-1]['Active'],2)
        print("Active", ratio, "%")
        if(ratio>0.01):
            print("WARNING!!!!!!!!!")





blub= Calculation(abfrage1)
blub.getInfektionRate()
#blub.recoveredRatio()
#blub.infektedRatio()
#blub.current_population()




