from django.shortcuts import render
from collections import Counter
import pandas as pd
import plotly.graph_objects as go


def readfile(): #function to read the csv file

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


    # null_data = data[data.isnull().any(axis=1)] # find where is the missing data #na null
    # missing_values = len(null_data)

def index(request):
    readfile()

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

def project2(request):
    
    df = pd.read_csv('E:\PROGRAMMING\Repositories\itd112\itd112\media\Iligan City Falls.csv')
    df['text'] = df['name']

    fig = go.Figure(data=go.Scattergeo(
            lon = df['longitude'],
            lat = df['latitude'],
            text = df['text'],
            mode = 'markers',
            marker=dict(
            color='#B76DF5',
            size=8,
            line=dict(
                color='#4C286A',
                width=2
            )
        )
            ))

    fig.update_geos(
    coastlinecolor="RebeccaPurple",
    coastlinewidth = 1.5,
    landcolor="LightGreen",
    showocean=True, oceancolor="LightBlue",
    lakecolor = "Blue"
)


    # focus point
    lat_foc = 8.1627541
    lon_foc = 124.2322989

    fig.update_layout(
        geo = dict(
            projection_scale=40, #this is kind of like zoom
            center=dict(lat=lat_foc, lon=lon_foc), #this will center on the point
        ),
        margin = dict(l=0, r=0, b=0, t=0),
        height = 500,
    )

    fig.update_layout (paper_bgcolor = "#F1F1F1")


    # Generate the SVG plot as an HTML div element
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'figure': plot_div,
    }
    return  render(request, 'project2.html', context)


def project3(request):
    filename = 'E:\PROGRAMMING\Repositories\itd112\itd112\media\Covid.csv'
    dataset = pd.read_csv(filename)
    # print(data.head())

    fig = go.Figure(data=[
        go.Bar(name='Confirmed', x=dataset['Country'], y=dataset['Confirmed']),
        go.Bar(name='Deaths', x=dataset['Country'], y=dataset['Deaths']),
        go.Bar(name='Recovered', x=dataset['Country'], y=dataset['Recovered']),
    ])
    # Change the bar mode
    fig.update_layout(
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor = "#F1F1F1",
        # width = 800,
        # height = 500,

        )

    # Generate the SVG plot as an HTML div element
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'figure': plot_div,
    }
    return  render(request, 'project3.html', context)
