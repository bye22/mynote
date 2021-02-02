# coding=utf-8
#import sys

#reload(sys)

#sys.setdefaultencoding('utf8')

# 引入依赖模块
import xlsxwriter

# 操作数据
data = [20, 45, 26, 18, 45]

# 创建表格
workbook = xlsxwriter.Workbook("ex04.xlsx")
worksheet = workbook.add_worksheet("data")

# 添加数据：一次添加多个数据
worksheet.write_column('A1', data)

# 创建图表
chart = workbook.add_chart({'type': 'line'})
# 图表添加数据
chart.add_series({
        'values': '=data!$A1:$A6',
        'name': '图表线名称',
        'marker': {
           'type': 'circle',
           'size': 8,
           'border': {'color': 'black'},
           'fill': {'color': 'red'}
        },
        'data_labels': {'value': True},
        'trendline': {
           'type': 'polynomial',
           'order': 2,
           'name': '示例趋势线',
           'forward': 0.5,
           'backward': 0.5,
           'display_equation': True,
           'line': {'color': 'red', 'width': 1, 'dash_type': 'long_dash'}
        }
})

worksheet.insert_chart('C1', chart)

workbook.close()
