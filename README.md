#### PYTHON PROJECT
[Pythonanywhere主页](http://fangqiao07.pythonanywhere.com/?)

- 整个交互网站11个页面url组成，项目依赖FLASk，pyecharts等；
- 项目启动命令：python app.py
### 首页
- 交互网页的首页是2014-2017城市绿化覆盖率的中国地图。
-首页的上方有一个单选选择器，其中有“数据总览”、“GDP”、“pop”三个选项。
子页面

### 页面
- 三个子页面分别对应“数据总览”、“GDP”、“pop”。
- 有两个下拉框：前面一个下拉框：分别对应“中国分省人均碳排”、“城市绿化覆盖率”、“中国分省单位GDP碳排”的交互数据图表；后面一个下拉框：分别对应2014-2017各年各省份gdp与城市建设区面积。

### python档描述
- python文件夹里面有.ida文件夹、static文件夹、templates文件夹、app.py文件以及各类数据文档。
## app.py
- 用到列表循环，for循环等等。
- 运用到数据结构嵌套适合在子页面中嵌套出现数据交互图和数据图表。
- 利用判断语句判断用户点击的是什么从而跳转到相应界面。
- 在python档中赋予不同html文件不同的跳转地址并且开展出不同功能，实现python文档与html文档的数据交互。

### web app 动作描述
- 主页面的三个单选选择器，选择不同的选项可以直接跳转到三个不同的子页面。
- 两个下拉框时选择相应那行信息并点击“选择”即可跳转至对应页面，此多页面有地图、折线图、曲线图等多种呈现方式


