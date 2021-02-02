#coding=utf-8
# 引入依赖模块
import xlsxwriter

# 数据准备
datas = (
            ['Rent', 1000],
                ['Gas',  100 ],
                    ['Food', 300 ],
                        ['Gym',  50  ],
                        )

# 创建一个Excel文档
workbook = xlsxwriter.Workbook('ex01.xlsx')
# 添加一个工作表
worksheet = workbook.add_worksheet()

# 设置行和列的偏移
row, col = 0, 0

# 开始添加数据
for item, cost in datas:
        # 指定行、列的单元格，添加数据
            worksheet.write(row, col, item)
            worksheet.write(row, col+1, cost)
            # 行增加
            row += 1

# 添加一个计算总数的函数
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

# 关闭文档
workbook.close()

