#coding=utf-8
# 导入依赖的模块
import xlsxwriter

# 数据准备
datas = (
            ['Rent', 1000],
                ['Gas',  100 ],
                    ['Food', 300 ],
                        ['Gym',  50  ],
                        )

# 创建表格
workbook = xlsxwriter.Workbook('ex02.xlsx')
worksheet = workbook.add_worksheet('data')

# 添加全局格式
bold = workbook.add_format({'bold': True})
# 添加money格式
money = workbook.add_format({'num_format': '$#,##0'})

# 添加表格头，附带格式
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

# 数据表格偏移
row, col = 1, 0
# 添加数据
for item, cost in datas:
        # 按照行列单元格添加数据
        worksheet.write(row, col, item)
        worksheet.write(row, col+1, cost)
        row += 1

# 添加一列求和计数
worksheet.write(row, 0, 'Total',        bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)


# 存储退出
workbook.close()

