from django.shortcuts import render
from django.contrib import messages
from collections import Counter
import pandas as pd


def readfile():

    #we have to create those in order to be able to access it around
    # use panda to read the file because i can use DATAFRAME to read the file
    #column;culumn2;column
    global rows,columns,data,my_file,missing_values, attribute
     #read the missing data - checking if there is a null
    missingvalue = ['?', '0', '--']

    my_file = pd.read_csv('E:\PROGRAMMING\Repositories\itd112\itd112\media\doh-epi-dengue-data-2016-2021.csv', 
                                        sep='[:;,|_]',na_values=missingvalue, engine='python')

    attribute = 'Region' #attribute to display in the chart

    data = pd.DataFrame(data=my_file, index=None)

    rows = len(data.axes[0])
    columns = len(data.axes[1])


    null_data = data[data.isnull().any(axis=1)] # find where is the missing data #na null
    missing_values = len(null_data)

def index(request):
    readfile()

    message = 'I found ' + str(rows) + ' rows and ' + str(columns) + ' columns. Missing datas are: ' +str(missing_values)
    messages.warning(request, message)

    dashboard = []
    for x in data[attribute]:
        dashboard.append(x)

    my_dashboard = dict(Counter(dashboard))

    print(my_dashboard)

    keys = my_dashboard.keys()
    values = my_dashboard.values()

    listkeys = []
    listvalues = []

    for x in keys:
        listkeys.append(x)

    for y in values:
        listvalues.append(y)

    print(listkeys)
    print(listvalues)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return  render(request, 'index.html', context)
