# 苏格兰东线、西线与天空岛互动行程

在线分享：[https://mrpixelraf.github.io/scotland-trip/](https://mrpixelraf.github.io/scotland-trip/)。GitHub Pages从`main:/docs`发布。

本页仅做规划与本地交互，不收集个人信息，不发送报名，不保存预算修改，不启动智能体。6人、4晚是模型假设，球位、住宿和共同方案未确认。新增个人信息按公开仓库规则处理。

## 文件与更新

- `trip.json`：12处摄影候选、三条路线、每日活动、球费和酒店说明。
- `places.json`：从OpenStreetMap Nominatim取得的城镇/球场点，含请求来源与OSM ID。
- `roads.json`：OSRM公路几何与模型里程/时间，含实际查询URL和途经点；不含伦敦往返，不能作徒步导航。
- `approach-stats.json`：英格兰北上、机场接驳与还车道路模型；`transport-quotes.json`：目标日期火车、机票、卧铺及整车报价快照与计价条件。
- `basemap.json`、`lakes.json`：Natural Earth 1:10m国界/海岸及湖泊，裁剪苏格兰行程范围、简化并调整D3投影环方向。
- `view.html`：交互视图模板；`index.html`和`docs/index.html`由构建脚本生成，不应手工维护两份不同版本。

更新数据或模板后执行：

```sh
python3 scripts/build-route-artifact.py
```

需要在Codex对话里展示时，可另给`--inline-output`一个本任务有写权限的绝对文件路径。页面使用D3 7.9.0的固定CDN地址；几何和行程数据内嵌，无运行时API请求。直接打开`index.html`需要网络加载D3。所有预算状态仅在当前页面内存，刷新后恢复默认。

按AGENTS.md建个人分支和PR，核对事实、日期、来源、预算与地图后合并。GitHub Pages随后发布新的`docs/index.html`，分享网址保持不变；页面不是自动从Markdown提取资料，改规划时需同步`trip.json`。

## 地图数据来源

获取日2026-09-14至15日。地理坐标用于区域比较，4位小数不代表停车精度。

- [组员原图](https://claude.ai/public/artifacts/fea19929-5477-4189-afa5-a8005c208c0a)：12处点、坐标和逐点到访来源，重新编写整合文字，未复制原图完整应用。
- [Natural Earth countries GeoJSON](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_0_countries.geojson)、[lakes GeoJSON](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_lakes.geojson)，[公有领域条款](https://www.naturalearthdata.com/about/terms-of-use/)。这不是海拔地形图。
- [© OpenStreetMap contributors](https://www.openstreetmap.org/copyright)，点数据查询链接保存在`places.json`。
- [OSRM](https://project-osrm.org/)，原请求和模型时长保存在`roads.json`。西线/天空岛线从Glasgow经Balloch、Crianlarich进山，东线从Perth起；西线另用Oban、Lochgilphead和Tarbert途经点，避免将渡轮当作默认行驶路径。

正式导航仍按住宿/停车入口地址、目标日Traffic Scotland和现场标识；额外景点、接送和延长段重新计算。

## 核验

交互检查覆盖东/西/天空岛线、每日高亮、12处地点、核心两轮/只打一轮/可选九洞、房价与无效输入、996敏感性计算；360、736、1024px明暗主题检查无页面横向溢出。商家价格为已查询费率或明确标注的预算，不是订位确认。

天空岛线以`skye`为数据键，`spotOverrides`仅覆盖该线路的地点说明，保留其他两条路线。页面默认打开天空岛，可用`?route=east`、`?route=west`、`?route=skye`指定首次显示。三线比较用两轮18洞；Sconser为9果岭两圈，未误标世界百佳。第三日路程长与未核定球位已在每日详情明示。

会合点修订后，东线从Perth至10/3住宿地334英里，西线从Glasgow至10/3住宿地359英里；天空岛从Glasgow出发，包含10/4回Glasgow还车，共593英里。起点和末日范围不同，不能直接当作伦敦全程里程比较。30日驾驶时间不包含本人从英格兰北上的前段；详见[铁路会合规划](../../planning/transport-meeting-points.md)。

[天空岛交通比较](https://mrpixelraf.github.io/scotland-trip/?route=skye&view=transport)已加入30日去、4日回的日间火车/飞机，以及29日晚卧铺。票价写明人数，租车写明整车总额和取还时间；可切换七/九座车、球包和普通行李预留。普通航空托运£80为往返预算，不是实价；日间铁路球包接收条件待核。按5人分摊九座车，默认火车£220.50/人，晚班返程£179.50，Glasgow卧铺去加日间回£338.10；均非全包交通价。来源及详细条件见[研究记录](../../planning/skye-transport.md)。
