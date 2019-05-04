# -*- coding: utf-8 -*-
import json
import shapefile
#创建shp文件
w = shapefile.Writer(target="polygon.shp", shapeType=shapefile.POLYGON)
# w.poly(parts=[[[1, 5], [5, 5], [5, 1], [3, 3], [1, 1]]])
# w.field('FIRST_FLD', 'C', '40')
# w.field('SECOND_FLD', 'C', '40')
# w.record('First', 'Polygon')
w.field('name', 'C', '40')
w.field('area_id', 'C', '20')
w.field('country', 'C', '40')
w.field('color', 'C', '10')
f = open("data.txt", "r")

#解析下载的文件
lines = f.readlines()

for line in lines:  # 循环输出读取的内容

    data_json = json.loads(line)
    print line

    for area in data_json['areas']:
        print area['name'], area['area_id'], area['country'], area['color']

        # print area['polygon_points']
        if area['polygon_points'] is not None:
            w.poly(area['polygon_points'])
            w.record(area['name'], area['area_id'], area['country'], area['color'])
        if area['sub_areas'] is not None:
            for sub_area in area['sub_areas']:
                if sub_area['polygon_points'] is not None:
                    try:
                        w.poly(sub_area['polygon_points'])
                        w.record(area['name'], area['area_id'], area['country'], sub_area['color'])
                    except TypeError:
                        print sub_area['polygon_points']

