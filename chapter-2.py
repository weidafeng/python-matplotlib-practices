# chapter 2
# 使用统计函数绘制简单图形
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# bar 柱状图
x = list(range(1, 10))
y = [3,1,4,5,6,8,9, 7, 2]

plt.bar(x,y,align='center',color='c', tick_label=list('sahfdaksj'), hatch='/')
plt.xlabel("箱子编号")
plt.ylabel("箱子重量")
plt.show()


## barh 水平柱状图
plt.barh(x,y,align='center', color='c', tick_label=list('sahfdaksj'), hatch='/')
plt.xlabel("箱子编号")
plt.ylabel("箱子重量")
plt.show()

## hist 直方图
box_hight = np.random.randint(low=0, high=10,size=100)
bins = range(0,11)
# plt.hist(box_hight, bins)
plt.hist(x=box_hight, bins=bins, histtype='bar', rwidth=1, alpha=0.6)
plt.show()

## pie 饼图
kinds = '简易箱','保鲜箱', '行李箱', '密封箱'
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
sold_nums = [0.05, 0.45, 0.15, 0.35]
plt.pie(x=sold_nums, 
		labels=kinds,
		autopct="%3.1f%%", 
		startangle=60, 
		colors=colors)
plt.show()

## polar 在极坐标系上绘制折线图
bar_slices = 12
theta = np.linspace(start=0.02, stop=2*np.pi,num=bar_slices, endpoint=False	)
r = 30 * np.random.rand(bar_slices)

plt.polar(theta,r,linewidth=2,marker="*", mfc='b',ms=10)
plt.show()

## scatter 绘制气泡图
# 二维数据借助气泡大小展示三维数据
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, s=np.power(10*x + 20*y, 2), cmap=mpl.cm.RdYlBu, marker='o')
plt.show()


## stem 棉签图
# 绘制离散有序数据
x = np.linspace(0.5, 2*np.pi, 20)
y = np.random.randn(20)

plt.stem(x, y, linefmt='-.', markerfmt='o', basefmt='-', label='stem fig')
plt.show()

## boxplot 箱线图
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

x = np.random.randn(100)
plt.boxplot(x)

plt.title('随机数生成器抗干扰能力的稳定性')
plt.xticks([1], ['随机数生成器'])
plt.ylabel('随机数值')

plt.grid(axis="y", ls=":", lw=1, color='gray', alpha=0.4)
plt.show()

## errorbar 绘制误差棒图
# 绘制x或y轴方向的误差范围
x = np.linspace(0.1, 0.6, 6)
y = np.exp(x)
plt.errorbar(x,y, fmt='bo', yerr=0.2,xerr=0.02)
plt.xlim(0, 0.7)
plt.show()