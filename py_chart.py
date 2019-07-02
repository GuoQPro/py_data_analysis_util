from pyecharts.charts import Map, Pie, Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


def ChartPie(lable_list, value_list, chart_title = "", radius = None):
    pie_chart = Pie();
    value_pairs = [list(z) for z in zip(lable_list, value_list)];
    pie_chart.add("", value_pairs, radius = radius);
    pie_chart.set_global_opts(title_opts = opts.TitleOpts(title = chart_title))
    return pie_chart;

def ChartWorldMap(lable_list, value_list, chart_title = "", value_min = 0, value_max = 0):
	w_map = Map(init_opts=opts.InitOpts(theme=ThemeType.DARK));
	value_pairs = [list(z) for z in zip(lable_list, value_list)];
	w_map.add("", value_pairs, maptype = "world");
	w_map.set_global_opts(
	    title_opts = opts.TitleOpts(title = chart_title),
	    visualmap_opts = opts.VisualMapOpts(min_ = value_min, max_= value_max, is_piecewise = False),
	)
	w_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False));
	return w_map;


def ChartBar(xlables, y_tag_list, y_value_list, chart_title = "", x_axis = "", y_axis = ""):
    bar_chart = Bar(init_opts=opts.InitOpts(theme = ThemeType.LIGHT));
    bar_chart.add_xaxis(xlables);
    for tag, values in zip(y_tag_list, y_value_list):
        bar_chart.add_yaxis(tag, values);


    bar_chart.set_global_opts(
    		title_opts = opts.TitleOpts(title = chart_title),
    		yaxis_opts = opts.AxisOpts(name = x_axis),
        	xaxis_opts = opts.AxisOpts(name = y_axis),
    	);
    return bar_chart;