import numpy as np
import csv

def Correlation_Marks_DaysPresent(data_3):
    Marks = []
    DaysPresent = []

    with open(data_3) as f:
        data = csv.DictReader(f)
        for x in data:
            Marks.append(float(x["Marks In Percentage"]))
            DaysPresent.append(float(x["Days Present"]))

        return{"x":Marks,"y":DaysPresent}

def Calculate_Correlation(data1):
    Correlation = np.corrcoef(data1["x"],data1["y"])
    print("Correlation is equal to: " + str(Correlation[0,1]))

def Main():
    data3 = "./Student Marks vs Days Present.csv"
    data2 = Correlation_Marks_DaysPresent(data3)
    Calculate_Correlation(data2)

Main()