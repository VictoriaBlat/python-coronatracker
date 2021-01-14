from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from calculation import *
#abfrage1 = Request("Spain", 10)
#blub = Calculation(abfrage1)
# infektionen = abfrage1.printData()["active"]
# print(infektionen)
#dates = abfrage1.printData()["dates"]

root = Tk()
root.title('Corona Daten') # aus den letzten {len(dates)} Tage"
root.geometry("600x900")
#
corona_img = ImageTk.PhotoImage(Image.open("corona.jpg"))
header = Label(image=corona_img, height=200)
header.pack()

"""def drawGraph():
    plt.plot(dates, infektionen)
    plt.ylabel('some numbers')
    plt.show()"""



def showDataGermany(val):
    days_span=int(days_input.get())
    abfrage1 = Request(val, days_span)
    recovered = Calculation(abfrage1).recoveredRatio()
    print("ration is", recovered)
    ratio1 = Label(root, text=f"recovered ratio  {recovered}", fg='blue')
    ratio1.config(font=('Arial', 10, 'bold'))
    ratio1.place(x=20, y=590)
    infekted_ratio= Calculation(abfrage1).infektedRatio()
    if infekted_ratio>0.01:
        warning= Label(root, text=f"WARNUNG, SEHR HOCHE INFENKTIONSRATE!!", fg='red')
        warning.config(font=('Arial', 20, 'bold'))
        warning.place(x=60, y=610)
    ratio2 = Label(root, text=f"Infekted ratio  {infekted_ratio}", fg='blue')
    ratio2.config(font=('Arial', 10, 'bold'))
    ratio2.place(x=120, y=590)

    #data = abfrage1.printData()
    data= abfrage1.range
    print("start-----------",data,"--------ende")
    #print(infektionen)
    dates = abfrage1.printData()["dates"]
    #print("days", days_input.get())
    for day in data:


        listbox.insert(END, f" {day['Date']} {day['Confirmed']} {day['Active']} {day['Recovered']} {day['Deaths']}")
    #Daily infektion rate
    daily=Calculation(abfrage1).getInfektionRate()
    print("daily", daily)
    for day in daily:
        infos = Label(root, text=f"Daily infekted ratio Tag {daily.index(day)}  {day['Daily_infektion_rate']}", fg='blue')
        infos.config(font=('Arial', 10, 'bold'))
        infos.place(x=20, y=900)
    #######graph logic
    def drawGraph(dates,values):
        plt.plot(dates, values)
        plt.ylabel('some numbers')
        plt.show()

    values_for_graphs=abfrage1.printData()
    days= values_for_graphs["dates"]
    button_active = Button(root, text='Aktiv', width=10, command=lambda:drawGraph(days,values_for_graphs["active"]))
    button_active.place(x=100, y=640)

    button_confirmed = Button(root, text='Bestätigt', width=10, command=lambda:drawGraph(days,values_for_graphs["confirmed"]))
    button_confirmed.place(x=200, y=640)
    button_recovered = Button(root, text='Genesen', width=10, command=lambda:drawGraph(days,values_for_graphs["recovered"]))
    button_recovered.place(x=300, y=640)
    button_death = Button(root, text='Tot', width=10, command=lambda:drawGraph(days,values_for_graphs["deaths"]))
    button_death.place(x=400, y=640)

label = Label(root, text='Corona Information der letzten x Tagen: x =', fg='blue')
label.config(font=('Arial', 10, 'bold'))
label.pack(pady=15)
days_input = Entry(root, text='tage', width=5)
days_input.pack()


label = Label(root, text='Von welchem Land möchtest Du die aktuellen Daten ersehen?', fg='blue')
label.config(font=('Arial', 10, 'bold'))
label.pack(pady=20)
button_DE = Button(root, text='Deutschland', width=10, command=lambda:showDataGermany("Germany"))
button_DE.place(x=95, y=430)
button_AT = Button(root, text='Österreich', width=10, command=lambda:showDataGermany("Austria"))
button_AT.place(x=200, y=430)
button_IT = Button(root, text='Italien', width=10, command=lambda:showDataGermany("Italy"))
button_IT.place(x=300, y=430)
button_ES = Button(root, text='Spanien', width=10, command=lambda:showDataGermany("Spain"))
button_ES.place(x=400, y=430)

### Lable Spalten Listbox
label_listbox = Label(root, text='[Datum] [Bestätigt] [Aktiv] [Genesen] [Tot] [Zuwachs]', width=95, height=5, fg='blue')
label_listbox.config(font=('Arial', 8, 'bold'))
label_listbox.pack(pady=18)
#label_listbox.place(x=10, y=490)


### Listbox mit Scrollbar
scrollbar = Scrollbar(root)
listbox = Listbox(root, width=95, height=5, yscrollcommand = scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.place(x=10, y=505)
scrollbar.pack(side="right", fill="y")



root.mainloop()


