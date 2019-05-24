from pyecharts.charts import Map, Pie
from pyecharts import options as opts

def ChartPie(lable_list = [], value_list = [], title = ""):
    pie_chart = Pie();
    values = [list(z) for z in zip(lable_list, value_list)];
    pie_chart.add("", values);
    pie_chart.set_global_opts(title_opts=opts.TitleOpts(title=title))
    return pie_chart;



