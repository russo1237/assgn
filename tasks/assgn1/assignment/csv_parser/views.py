from django.shortcuts import render,render_to_response
from django.http import request,HttpResponse
from prettytable import PrettyTable
import csv,io



# Create your views here.

def csv(request):

    if request.method == "GET":
        return render(request,"csv_parser/output.html")
    csv_file = request.FILES["test"]
    csv_reading = csv_file.read().decode("UTF-8")
    files = io.StringIO(csv_reading)
 
    Lallrows = []
    n = 5
    for line in files:
        Lallrows.append(line)
     
    for i in range(len(Lallrows)):
        Lallrows[i] = Lallrows[i].split(",")
    L5_0 = Lallrows[0]

    title = dict(zip(Lallrows[0],[[] for x in L5_0]))
    count = 0
    
    for i in range(0,len(L5_0)):
        for j in range(1,len(Lallrows)):
            title[Lallrows[0][i]].append(Lallrows[j][i])
            count = count+1

    L1=[]
    for property in L5_0:
        L1.append(title[property])


    count = 0


    x = PrettyTable()
    column_names = Lallrows[0]
    

    for i in range(len(L5_0)):
        x.add_column(column_names[i], L1[i])



    htmlcode = x.get_html_string()
    htmlFile = open("csv_parser/templates/csv_parser/result.html","w")
    init = "<!DOCTYPE html><html><head><style>table,th,td{ border:1px solid black;}</style></head><body>"          
    htmlFile.write(init)
    htmlFile.close()



    htmlT = open("csv_parser/templates/csv_parser/result.html","a+")
    htmlFile = htmlT.write(htmlcode)
    htmlT.close()

    end = open("csv_parser/templates/csv_parser/result.html","a+")
    htmlFile = end.write("</body></html>")
    end.close()
    

    return render(request,"csv_parser/result.html")


            

    if request.method == "POST":
        return render(request,"csv_parser/result.html")
