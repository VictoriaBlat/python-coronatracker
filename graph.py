from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from calculation import *
abfrage1 = Request("Spain",10)
blub= Calculation(abfrage1)
infektionen=abfrage1.printData()["aktive"]
dates=abfrage1.printData()["dates"]
#print(infektionen)


root=Tk()
root.title(f"Corona Daten aus den letzten {len(dates)} Tage")
root.geometry("500x500")

def drawGraph():
    
    plt.plot(dates,infektionen)
    plt.ylabel('some numbers')
    plt.show()

    #werte=[7,9,7,23,1,6]
    #plt.hist(werte,1)
    #plt.show()

show_data= Button(root,text="Grafik anzeigen", command=drawGraph )
show_data.pack()

root.mainloop()