# -*- coding: utf-8 -*-
import json
import urllib2

# GEO系统将动态覆盖全球各类飞行受限制的区域，飞行用户将实时获取相关受限资讯，包含但不限于机场、由于一些突发情况（如森林火灾、大型活动等）造成的临时限飞区域、一些永久禁止飞行的区域（如监狱、核工厂等）。
# 此外，用户在部分区域例如野生保护区、人流密集的城镇等允许飞行的区域也可能收到飞行警示。以上这些无法完全自由飞行的区域，都统称为限飞区，包含了警示区、加强警示区、授权区、限高区、禁飞区等。
# GEO系统将默认限制无人机在可能引起安全问题区域起飞或飞行。用户如需在该区域执行飞行，可通过已认证的DJI账户，并准备相关材料申请临时解禁。此项解禁功能并不适用于高度敏感的区域。
# GEO系统仅是参考性质，在一些区域，DJI 大疆创新系统将采用通用管理，选取一些常规的参数划定限飞区，这与您所预备飞行区域的法律法规未必相符。因此，每位用户都有责任需要在飞行前自行查阅并确认相关法律法规，对自身的飞行安全负责。
for lng in range(70, 140, 4):
    for lat in range(4, 54, 4):
        url_temple = "https://www.dji.com/cn/api/geo/areas?lng=%s&lat=%s&country=CN&search_radius=250000&drone=spark&level=%s&zones_mode=total"
        # 包装头部
        firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
                           'connection': "close",
                           'content-type': "application/json;charset=utf-8",
                           'date': "Fri, 03 May 2019 09:04:11 GMT",
                           'transfer-encoding': "chunked",
                           'via': "nw, 1.1 c307613fe3146dad6950808dc74f82f6.cloudfront.net (CloudFront)",
                           'x-amz-cf-id': "wXPZwrzfKzB_RqcNwuiR7uMdUNvfDlmDZFpnz7ARCiXUqIVWBgU7sA==",
                           'x-cache': "Miss from cloudfront",
                           'x-kunkka-proxy-latency': "0",
                           'x-kunkka-upstream-latency': "35",
                           'x-newrelic-app-data': "PxQFU1JaAQoFR1BWBgcDUFwJBBFORDQHUjZKA1ZLVVFHDFYPHiZcTQdZUwRIB1JaXxQSTFReWkkCXU9AAwAGTVYOQRFZXlEfVABWTFYOXwMKURgAFhMXUF8KFRBYXVsDFh5TSxYDEQxRDmcBV1ZAQFwJVQRDT3QHEGRSEhIRUVBEAQUjRVRWFSJeRHwEAAoBVTVdABoUBB4DSwlSBVQCVlQPD01LUhQRAQdXUwAFBl8GVQELUAVRQBwEWQ5LXWk=",
                           'x-protected-by': "ibg-sec",
                           'x-service-from': "geo_service",
                           'x-service-loc': "",
                           'x-service-version': "1.2.3"}
        # 构建请求
        # request = Request(url, headers=firefox_headers)
        url = url_temple % (lng, lat, "1%2C2%2C4%2C7")

        f = file("url.txt", "a+")  # 以追加的方式
        f.write(url)
        f.write("\n")  # 写完通过\n进行换行
        f.close()
        html = urllib2.urlopen(url)
        # 获取数据
        data = html.read()

        f = file("data.txt", "a+")  # 以追加的方式
        f.write(data)
        f.write("\n")  # 写完通过\n进行换行
        f.close()
        # 转换成字典数据
        data_json = json.loads(data)
