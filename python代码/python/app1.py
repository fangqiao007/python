import pandas as pd
from flask import Flask
from flask import render_template, request, redirect
from pyecharts.charts import EffectScatter, Bar, Line, WordCloud, Map, Grid
from pyecharts.charts import Scatter
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline

app = Flask(__name__)


@app.route('/data')
def index():
    data1 = pd.read_csv(r"./static/data/china_province_carbon_emission.csv")
    data2 = pd.read_csv(
        r"./static/data/cityms.csv")
    data3 = pd.read_csv(
        r"./static/data/citys.csv")
    data4 = pd.read_csv(
        r"./static/data/greens.csv")
    data1_x = data1.columns.values
    data2_x = data2.columns.values
    data3_x = data3.columns.values
    data4_x = data4.columns.values

    data1_y = data1.values.tolist()
    data2_y = data2.values.tolist()
    data3_y = data3.values.tolist()
    data4_y = data4.values.tolist()
    return render_template("index_1.html", data1_x=data1_x[1:], data2_x=data2_x[1:], data3_x=data3_x[1:],
                           data4_x=data4_x[1:], data1_y=data1_y, data2_y=data2_y, data3_y=data3_y, data4_y=data4_y,
                           a=1)


@app.route('/allGeo')
def index_bar():
    df = pd.read_csv("./static/data/china_province_carbon_emission.csv")
    c = (
        Geo()
            .add_schema(maptype="china")
            .add("碳排(Mt)", list(zip(list(df.province), list(df.emissions.fillna(0)))))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(min_=min(list(df.emissions)), max_=max(list(df.emissions))),
            title_opts=opts.TitleOpts(title="中国分省碳排数据"),
        )
    )
    return render_template('index_1.html',
                           myechart=c.render_embed(),
                           text=''' ''')


@app.route('/gdptp')
def index_bar_every_1_tp():
    df = pd.read_csv("./static/data/china_province_carbon_emission.csv")
    c = (
        Geo()
            .add_schema(maptype="china")
            .add("单位GDP碳排(Mt/亿元)", list(zip(list(df.province), list(df.emissions_per_GDP.fillna(0)))))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            #            visualmap_opts=opts.VisualMapOpts(),
            visualmap_opts=opts.VisualMapOpts(min_=0.07, max_=0.09),
            title_opts=opts.TitleOpts(title="中国分省单位GDP碳排数据"),
        )
    )
    return render_template('index_1.html',
                           myechart=c.render_embed(),
                           text='''
                           ''')


@app.route('/every')
def index_bar_every():
    df = pd.read_csv("./static/data/china_province_carbon_emission.csv")
    c = (
        Geo()
            .add_schema(maptype="china")
            .add("人均碳排(Mt/万人)", list(zip(list(df.province), list(df.emissions_per_POP.fillna(0)))))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            #            visualmap_opts=opts.VisualMapOpts(),
            visualmap_opts=opts.VisualMapOpts(min_=0.05, max_=1),
            title_opts=opts.TitleOpts(title="中国分省人均碳排数据"),
        )
    )
    return render_template('index_1.html',
                           myechart=c.render_embed(),
                           text='''
                           ''')


@app.route('/gdp1')
def index_bar_every_4():
    df = pd.read_csv(r'./static/data/greens.csv')

    df1 = pd.read_csv(r'./static/data/citys.csv')

    df2 = pd.read_csv(r'./static/data/cityms.csv')

    a = list(df.province)
    a1 = list(df1['2017年'])
    b1 = list(df2['2017年'])
    a2 = list(df1['2016年'])
    b2 = list(df2['2016年'])
    a3 = list(df1['2015年'])
    b3 = list(df2['2015年'])
    a4 = list(df1['2014年'])
    b4 = list(df1['2014年'])

    bar = (
        Bar()
            .add_xaxis(a)
            .add_yaxis("2014年各省份GDP", a4)
            .set_global_opts(title_opts=opts.TitleOpts(title="2014年各省份GDP"),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45}))
    )

    line = (
        Line()
            .add_xaxis(a)
            .add_yaxis("2014年城市建成区面积", b4)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2014年城市建成区面积", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
            xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45})
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return render_template('index_1.html',
                           myechart=grid.render_embed(),
                           text='''
                           由图中可以看出各省份的地区生产总值差异很大城市建成区面积各个省份差异也很大，广东、江苏、浙江的城市建成面积最多，西藏、青海等省份最少
                          ''', text1='''由图表可以清晰的看出经济越发达的地区，城市的建成区面积也越多。''')


@app.route('/gdp2')
def index_bar_every_1():
    df = pd.read_csv(r'./static/data/greens.csv')

    df1 = pd.read_csv(r'./static/data/citys.csv')

    df2 = pd.read_csv(r'./static/data/cityms.csv')

    a = list(df.province)
    a1 = list(df1['2017年'])
    b1 = list(df2['2017年'])
    a2 = list(df1['2016年'])
    b2 = list(df2['2016年'])
    a3 = list(df1['2015年'])
    b3 = list(df2['2015年'])
    a4 = list(df1['2014年'])
    b4 = list(df1['2014年'])

    bar = (
        Bar()
            .add_xaxis(a)
            .add_yaxis("2015年各省份GDP", a3)
            .set_global_opts(title_opts=opts.TitleOpts(title="2015年各省份GDP"),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45}))
    )

    line = (
        Line()
            .add_xaxis(a)
            .add_yaxis("2015年城市建成区面积", b3)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2015年城市建成区面积", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
            xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45})
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return render_template('index_1.html',
                           myechart=grid.render_embed(),
                           text='''由图中可以看出各省份的地区生产总值差异很大城市建成区面积各个省份差异也很大，广东、江苏、浙江的城市建成面积最多，西藏、青海等省份最少
                                                    ''', text1='''由图表可以清晰的看出经济越发达的地区，城市的建成区面积也越多。''')


@app.route('/gdp3')
def index_bar_every_2():
    df = pd.read_csv(r'./static/data/greens.csv')

    df1 = pd.read_csv(r'./static/data/citys.csv')

    df2 = pd.read_csv(r'./static/data/cityms.csv')

    a = list(df.province)
    a1 = list(df1['2017年'])
    b1 = list(df2['2017年'])
    a2 = list(df1['2016年'])
    b2 = list(df2['2016年'])
    a3 = list(df1['2015年'])
    b3 = list(df2['2015年'])
    a4 = list(df1['2014年'])
    b4 = list(df1['2014年'])

    bar = (
        Bar()
            .add_xaxis(a)
            .add_yaxis("2016年各省份GDP", a2)
            .set_global_opts(title_opts=opts.TitleOpts(title="2016年各省份GDP"),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45}))
    )

    line = (
        Line()
            .add_xaxis(a)
            .add_yaxis("2016年城市建成区面积", b2)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2016年城市建成区面积", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
            xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45})
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return render_template('index_1.html',
                           myechart=grid.render_embed(),
                           text='''由图中可以看出各省份的地区生产总值差异很大城市建成区面积各个省份差异也很大，广东、江苏、浙江的城市建成面积最多，西藏、青海等省份最少
                                                    ''', text1='''由图表可以清晰的看出经济越发达的地区，城市的建成区面积也越多。''')


@app.route('/gdp4')
def index_bar_every_3():
    df = pd.read_csv(r'./static/data/greens.csv')

    df1 = pd.read_csv(r'./static/data/citys.csv')

    df2 = pd.read_csv(r'./static/data/cityms.csv')

    a = list(df.province)
    a1 = list(df1['2017年'])
    b1 = list(df2['2017年'])
    a2 = list(df1['2016年'])
    b2 = list(df2['2016年'])
    a3 = list(df1['2015年'])
    b3 = list(df2['2015年'])
    a4 = list(df1['2014年'])
    b4 = list(df1['2014年'])

    bar = (
        Bar()
            .add_xaxis(a)
            .add_yaxis("2017年各省份GDP", a1)
            .set_global_opts(title_opts=opts.TitleOpts(title="2017年各省份GDP"),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45}))
    )

    line = (
        Line()
            .add_xaxis(a)
            .add_yaxis("2017年城市建成区面积", b1)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2017年城市建成区面积", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
            xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45})
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return render_template('index_1.html',
                           myechart=grid.render_embed(),
                           text='''由图中可以看出各省份的地区生产总值差异很大城市建成区面积各个省份差异也很大，广东、江苏、浙江的城市建成面积最多，西藏、青海等省份最少
                                                                              ''',
                           text1='''由图表可以清晰的看出经济越发达的地区，城市的建成区面积也越多。''')


@app.route('/wordX')
def word():
    prevention = request.args.get("city")
    if prevention == "1":
        return redirect("/gdp1")
    elif prevention == "2":
        return redirect("/gdp2")
    elif prevention == "3":
        return redirect("/gdp3")
    else:
        return redirect("/gdp4")


@app.route('/wordXxx')
def word1111():
    prevention = request.args.get("city")
    if prevention == "1":
        return redirect("/every")
    elif prevention == "2":
        return redirect("/wordY")
    elif prevention == "3":
        return redirect("/gdptp")


@app.route('/wo')
def word1():
    df = pd.read_csv("./static/data/china_province_carbon_emission.csv")
    prevention = request.args.get("city1", "POP")
    map0 = (
        Bar()
            .add_xaxis(list(df.province))
            .add_yaxis("单位{}碳排".format(prevention), list(zip(list(df.province), list(df["{}".format(prevention)]))))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各省单位碳排".format(prevention)),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return render_template('index_1.html',
                           myechart=map0.render_embed(),
                           text='''
                               ''')


@app.route('/')
def wo_index():
    df = pd.read_csv("./static/data/greens.csv")
    prevention = request.args.get("city1", "emissions")
    tl = Timeline()
    for i in range(2014, 2018):
        map0 = (
            Map()
                .add(
                "城市绿化覆盖率", list(zip(list(df.province), list(df["{}年".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年城市绿化覆盖率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=30, max_=50)

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('index_1.html',
                           myechart=tl.render_embed(),
                           text='''
                               总体上2014年到2017年各省份的城市绿化覆盖率在增加极少的经济欠发达省份如西藏的城市绿化覆盖率在这近四年减少''',
                           text1='''由各年份城市绿化覆盖率图可以知道，经济越发达的省份城市绿化程度更好，如青海、西藏、新疆等省份经济欠发达的省份城市绿化程度相对比较差
东部沿海省份城市的城市绿化覆盖率最高，例如山东、江苏、浙江、福建、广东等省份''')


@app.route('/wordY')
def wordY():
    df = pd.read_csv("./static/data/greens.csv")
    prevention = request.args.get("city1", "emissions")
    tl = Timeline()
    for i in range(2014, 2018):
        map0 = (
            Map()
                .add(
                "城市绿化覆盖率", list(zip(list(df.province), list(df["{}年".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年城市绿化覆盖率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=30, max_=50)

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('index_1.html',
                           myechart=tl.render_embed(),
                           text='''
                               总体上2014年到2017年各省份的城市绿化覆盖率在增加极少的经济欠发达省份如西藏的城市绿化覆盖率在这近四年减少''',
                           text1='''由各年份城市绿化覆盖率图可以知道，经济越发达的省份城市绿化程度更好，如青海、西藏、新疆等省份经济欠发达的省份城市绿化程度相对比较差
东部沿海省份城市的城市绿化覆盖率最高，例如山东、江苏、浙江、福建、广东等省份''')


if __name__ == '__main__':
    app.run(debug=True)
