from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import pandas
import numpy
import matplotlib
import cufflinks
import plotly
import plotly.offline
import plotly.graph_objs

# Create your views here.

def home(request):
    cufflinks.go_offline()
    plotly.offline.init_notebook_mode()

    url = 'https://data.cityofnewyork.us/resource/h9gi-nx95.json'
    collisions = pandas.read_json(url)
    contributing_factors = pandas.concat([collisions.contributing_factor_vehicle_1,
            collisions.contributing_factor_vehicle_2,
            collisions.contributing_factor_vehicle_3,
            collisions.contributing_factor_vehicle_4,
            collisions.contributing_factor_vehicle_5])

    temp = pandas.DataFrame({
        'contributing_factors': contributing_factors.value_counts()
    })

    df = temp[temp.index != 'Unspecified']
    df.sort_values(by='contributing_factors', ascending=True)
    data = plotly.graph_objs.Data([
        plotly.graph_objs.Bar(
            y = df.index,
            x = df.contributing_factors,
            orientation = 'h'
        )
    ])

    layout = plotly.graph_objs.Layout(
        height = '1000',
        margin = plotly.graph_objs.Margin(l=300),
        title = 'Vehicles Collisions Contributing Factors'
    )

    fig = plotly.graph_objs.Figure(data=data, layout=layout)
    plot = plotly.offline.plot(fig, auto_open=False, output_type='div')

    return render(request, 'index.html', { 'graph': plot })

#class Graph(TemplateView):
#    template_name = 'graph.html'

#    def get_context_data(self, **kwargs):
#        context = super(Graph, self).get_context_data(**kwargs)

#        x = [-2,0,4,6,7]
#        y = [q**2-q+3 for q in x]
#        trace1 = plotly.graph_objs.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
#                            mode="lines",  name='1st Trace')

#        data=plotly.graph_objs.Data([trace1])
#        layout=plotly.graph_objs.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
#        figure=plotly.graph_objs.Figure(data=data,layout=layout)
#        div = plotly.offline.plot(figure, auto_open=False, output_type='div')

#        context['graph'] = div

#        return context