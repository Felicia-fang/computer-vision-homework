#encoding: utf-8
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from matplotlib import pyplot as plt
import csv
from datetime import datetime
import matplotlib.ticker as ticker
# 指定文件名，然后使用 with open() as 打开
x=[20 ,28,40 ,50,60]
y=[1,
1,
1,0.93,
0.85

]
# 绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.xticks(range(len(highs)),highs)
plt.plot(x,y, c='blue')
plt.plot(x,y, 'o')
# 设置图形的格式
plt.title("TYHT-PK-VGG", fontsize=24)
plt.xlabel('K', fontsize=16)
plt.ylabel("Precision", fontsize=16)
# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(500))
# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5))
fig.autofmt_xdate()
plt.show()