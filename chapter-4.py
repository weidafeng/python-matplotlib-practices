# chapter 4
# 完善统计图形

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 图例和标题
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y_1 = np.sin(x)
y_2 = np.cos(x)

'''
matplotlib 支持Tex公式输入，格式为：`r$formula$`
r表示该字符串为raw strings，字符串按照Tex规范解析。

对于两个美元符号之间的非数学公式字符串会按照泄题的形式输出，呈现印刷级别的文档效果
'''
plt.plot(x,y_1, label=r'$\sin(x)$')
plt.plot(x,y_2,label=r'$\cos(x)$')
plt.legend(loc='lower left')
plt.title('正弦余弦曲线图')
plt.show()

## 图例样式的调整

x = np.linspace(-1,10,100)
y_1 = np.power(x, 1)
y_2 = np.power(x, 2)
y_3 = np.power(x, 3)

plt.plot(x, y_1, ls='-', lw=2, color='r',label=r"$x^{1}$")
plt.plot(x, y_2, ls='--', lw=2, color='g',label=r"$x^{2}$")
plt.plot(x, y_3, ls='-.', lw=2, color='b',label=r"$x^{3}$")

plt.legend(loc='upper left', 
	bbox_to_anchor=(0.05,0.95),  # 将图例的左上角放在整幅图的（0.05， 0.95处
	ncol=3, #图例分成3列
	title='power function',  # 图例的标题
	shadow=True,
	fancybox=True) # 控制图例圆角或方角
plt.show()


## 标题的样式
plt.plot(x, y_2, ls='--', lw=2, color='g',label=r"$x^{2}$")
plt.legend(title='legend title')
plt.title('center demo')
plt.title('left demo', loc='left', fontdict={'fontsize':6, 'color':'r','family':'Comic Sans MS','style':'oblique'})
plt.title('right demo',loc='right', fontdict={'size':'xx-large', 'color':'b','family':'Times New Roman'})
plt.show()




## 案例3 带图例的饼图
## pie 分裂式饼图
elements = ['简易箱','保鲜箱', '行李箱', '密封箱']
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
sold_nums = [0.05, 0.45, 0.15, 0.35]
explode = (0.1,0.1,0.1,0.1)
wedges, texts, autotexts = plt.pie(x=sold_nums, 
									labels=elements,
									autopct="%3.1f%%",  # 饼图内部显示的数字格式
									startangle=60,  # 偏离角度
									colors=colors,
									explode=explode)  # 设置偏离半径的百分比

plt.legend(wedges, elements, fontsize=12, title='占比', loc='center left', bbox_to_anchor=(0.9,0,0,0))
plt.setp(autotexts,size=15,weight='bold')
plt.setp(texts, size=12)
# Set a property on an artist object.
plt.show()


## 设置刻度范围和刻度标签

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.subplot(211) # 2行1列，指定第一个子图
plt.title('正弦余弦曲线图')
plt.plot(x,y_1, label=r'$\sin(x)$')
plt.plot(x,y_2,label=r'$\cos(x)$')

plt.subplot(212) # 2行1列，指定第二个子图
# 1. 刻度以圆周率形式展示
# 2. 设置合理的范围
plt.xlim(-2*np.pi, 2*np.pi)
plt.xticks([-2*np.pi, -1.5 *np.pi, -np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
		 [r'$-2\pi$',r'$-3\pi/2$',r'$-\pi$',r'$\pi/2$',r'$0$',r'$\pi/2$',r'$3\pi/2$',r'$2\pi$'])

plt.plot(x,y_1, label=r'$\sin(x)$')
plt.plot(x,y_2,label=r'$\cos(x)$')

plt.legend(loc='lower left')
plt.show()


## 设置逆序坐标轴刻度
x = np.arange(1,11,0.5)
y = np.power(x, 2) + 0.7
plt.plot(x,y)
plt.xlim(10 ,1)
plt.show()



## 饼图下面添加表格
# 饼图
elements = ['简易箱','保鲜箱', '行李箱', '密封箱']
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
sold_nums = [0.05, 0.45, 0.15, 0.35]
explode = (0.1,0.1,0.1,0.1)
wedges, texts, autotexts = plt.pie(x=sold_nums, 
									labels=elements,
									autopct="%3.1f%%",  # 饼图内部显示的数字格式
									startangle=60,  # 偏离角度
									colors=colors,
									explode=explode)  # 设置偏离半径的百分比

plt.legend(wedges, elements, fontsize=12, title='占比', loc='center left', bbox_to_anchor=(0.9,0,0,0))
plt.setp(autotexts,size=15,weight='bold')
plt.setp(texts, size=12)
# Set a property on an artist object.

# 添加表格
col_labels = elements
row_labels = ['销量']
values = np.array(sold_nums) * 100 # 即
plt.table(cellText=values,
	cellColours=colors,
	colWidths=[0.1]*4, # 每列的宽度
	colLabels=col_labels, # 每列的标签
	rowLabels=row_labels, # 每行的标签
	loc='bottom', # 表格整体的位置
	rowLoc='center', # 每行元素的样式
	cellLoc='center')
plt.show()










plt.show()