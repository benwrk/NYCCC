from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime, dateutil
import pandas
import numpy
import matplotlib
import cufflinks
import plotly
import plotly.offline
import plotly.graph_objs

def home(request):
    cufflinks.go_offline()
    plotly.offline.init_notebook_mode()

    url = 'https://data.cityofnewyork.us/resource/h9gi-nx95.json'
    collisions = pandas.read_json(url)

    title_str = ''

    if 'from' in request.GET:
        collisions = collisions[collisions['date'] >= request.GET['from']]
        title_str = 'From ' + request.GET['from'] + ' to '
        if 'to' not in request.GET:
            title_str = title_str + 'present'
    if 'to' in request.GET:
        collisions = collisions[collisions['date'] <= request.GET['to']]
        title_str = title_str + request.GET['to']
        if 'from' not in request.GET:
            title_str = 'Before ' + title_str
    
    contributing_factors = pandas.concat([collisions.contributing_factor_vehicle_1,
        collisions.contributing_factor_vehicle_2,
        collisions.contributing_factor_vehicle_3,
        collisions.contributing_factor_vehicle_4,
        collisions.contributing_factor_vehicle_5])

    vccf_dataframe = pandas.DataFrame({
        'vcounts': contributing_factors.value_counts()
    })

    if request.GET.get('no_unspecified', 'False') == 'True':
        vccf_dataframe = vccf_dataframe[vccf_dataframe.index != 'Unspecified']

    vccf_figure = {
        'data': [
            {
                'labels': vccf_dataframe.index,
                'values': vccf_dataframe.vcounts,
                'type': 'pie',
                'name': 'Factors',
                'hoverinfo':'label+percent+name+value',
                'hole': .3,
                'type': 'pie'
            }
        ],
        'layout': {
            'title': 'New York City<br>Vehicles Collisions Contributing Factors<br>' + title_str,
            'annotations': [
                {
                    'font': {
                        'size': 20
                    },
                    'showarrow': False,
                    'text': 'Factors',
                }
            ]
        }
    }

    vccf_plot = plotly.offline.plot(vccf_figure, auto_open=False, output_type='div')

    return render(request, 'index.html', { 'graph': vccf_plot })
