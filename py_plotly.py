import plotly.offline as po
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px

po.init_notebook_mode(connected=True)

#https://plot.ly/python/bar-charts/
def ChartBar(x_list, y_list, title = ""):
    fig = go.Figure(
        data=[go.Bar(x=x_list, y=y_list, color='lifeExp')],
        layout_title_text=title
    )
    po.iplot(fig)

def ChartBarExp(data, xLabel, yLabel, colorLabel=None):
    fig = px.bar(data, x=xLabel, y=xLabel, color=colorLabel)
    fig.show()