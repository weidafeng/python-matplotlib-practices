# chapter 3
# 绘制统计图形
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 多数据堆叠
x = [1,2,3,4,5]
y1 = [2,4,1,6,3]
y2 = [6,2,3,5,1]

plt.bar(x,y1,bottom=0,label='class A')
plt.bar(x,y2,bottom=y1, label='class B')
plt.grid(True, axis='x', ls=':', color='r', alpha=0.3)
plt.legend()
plt.show()

# 多数据并列
x = np.arange(1,6) ##### 注意，这里不是[1,2,3,4,5]，而是一个列表生成式，因为后面要为每个x做平移
y0 = [0,3,4,2,5]
y1 = [2,4,1,6,3]
y2 = [6,2,3,5,1]

bar_width = 0.35
tick_label = list('ABCDE')

plt.bar(x, y1, width=bar_width, align='center',label='class A', alpha=0.5)
plt.bar(x + bar_width, y2, width=bar_width, align='center',label='class B', alpha=0.5)
plt.legend()
plt.show()


# 堆积折线图 stackplot 
# Draws a stacked area plot.
labels = ['Blue', 'Brown', 'Green']
colors = ['#8da0cb', '#fc8d62', '#66c2a5']
plt.stackplot(x, y0, y1, y2, labels=labels, colors=colors)
plt.legend()
plt.show()


## 间断条形图 broken_barh
# 间断条形图主要是在条形图的基础上绘制，用来可视化定性数据的相同指标在时间维度上的指标值的变换情况
# 实现定性数据的相同指标的变化情况的直观比较

mpl.rcParams['font.sans-serif'] = ['LiSu'] # 隶书字体
mpl.rcParams['axes.unicode_minus'] = False
xrange_1 = [(30,100),(180, 50), (260, 70)] # 30,100表示起点为30， 沿着x轴正方向移动100个单位
yrange_1 = (20,8) # 20,8 表示以20为起点，沿着y轴向上移动8个单位

xrange_2 = [(60,90), (190, 20), (230, 30), (280, 60)]
yrange_2 = (10, 8)
plt.broken_barh(xrange_1, yrange_1, facecolors='#8da0cb')
plt.broken_barh(xrange_2, yrange_2, facecolors='#fc8d62')
plt.xlabel('演出时间')

plt.xticks(np.arange(0, 361, 60))
plt.yticks([15, 25], ['歌剧院A','歌剧院B'])
plt.grid(axis='y', color='gray')
plt.legend()
plt.show()

## 阶梯图 step
## 很像折线图，显示时序数据的波动周期规律
x = np.linspace(0, 10,20)
y = np.sin(x)
plt.plot(x,y,label='y=sin(x)')
plt.step(x,y,where='pre',label='y=step(sin(x))-pre')
plt.step(x,y,where='mid',label='y=step(sin(x))-mid')
plt.step(x,y,where='post',label='y=step(sin(x))-post')
'''where: [ 'pre' | 'post' | 'mid' ]
If 'pre' (the default), the interval from x[i] to x[i+1] has level y[i+1].

If 'post', that interval has level y[i].

If 'mid', the jumps in y occur half-way between the x-values.
'''
plt.legend()
plt.show()


## 堆叠直方图 
## stack=True
score_1 = np.random.randint(0,100,100)
score_2 = np.random.randint(0,100,100)

x = [score_1, score_2]
colors = ['#8dd3c7', '#bebada']
labels = ['class A','class B']

bins = range(0, 101, 10)
plt.hist(x, 	# 输入数据
		bins=bins,  # bins的个数或者bins的边缘范围
		color=colors, 
		rwidth=10, 
		stacked=True,   ### 堆叠直方图的关键
		label=labels)	
plt.xlabel("score")
plt.ylabel("class")
plt.show()


## pie 分裂式饼图
kinds = '简易箱','保鲜箱', '行李箱', '密封箱'
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
sold_nums = [0.05, 0.45, 0.15, 0.35]
explode = (0.1,0.1,0.1,0.1)
plt.pie(x=sold_nums, 
		labels=kinds,
		autopct="%3.1f%%", 
		startangle=60, 
		colors=colors,
		explode=explode)  # 设置偏离半径的百分比
plt.show()


## 案例 绘制内嵌环形饼图
elements = ['面粉','砂糖','奶油','草莓酱','坚果']
weight_1 = [40, 20, 15, 10, 15]
weight_2 = [30, 25, 15, 20, 10]

colormap = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3','#ff7f00']
outer_colors = colormap
inner_colors = colormap

wedges_1, texts_1, autotexts_1 = plt.pie(weight_1, 
	autopct="%3.1f%%", 
	radius=0.7,
	pctdistance=0.6, 
	colors=inner_colors,
	textprops=dict(color='c'),
	wedgeprops=dict(width=0.3,edgecolor='w'))
wedges_2, texts_2, autotexts_2 = plt.pie(weight_2, 
	autopct="%3.1f%%", 
	radius=1,
	pctdistance=0.8, 
	colors=inner_colors,
	textprops=dict(color='c'),
	wedgeprops=dict(width=0.3,edgecolor='w'))
plt.legend(wedges_1,elements, fontsize=12,label='配料表',loc='center left', bbox_to_anchor=(0.91,0,0.3,1))

plt.setp(autotexts_1,size=15,weight='bold')
plt.setp(autotexts_2,size=15,weight='bold')
plt.setp(texts_1, size=12)
plt.title("两种配料表")
plt.show()


## 箱线图
## 用于多组定量数据的分布比较
## 箱线图由一个箱体和箱须组成，第一四分位数，中位数、第二、三四分位数组成箱体
## 箱顶之外的竖直可以理解为离群点
test_1 = np.random.randn(5000)
test_2 = np.random.randn(5000)
test_list = [test_1, test_2]
labels = ["随机数生成器-1","随机数生成器-2"]
colors = ['#793217', "#218731"]

whis = 1.6
width = 0.35

bplot = plt.boxplot(test_list,whis=whis,widths=width, labels=labels, patch_artist=True, sym='o')

for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)

plt.ylabel("随机数值")
plt.title("随机数生成器抗干扰能力的稳定性比较")

plt.grid(axis='y', ls=':',lw=1, color='gray',alpha=0.4)
plt.show()


## 误差棒图

# 应用场景：通过抽检获得样本，对总体参数估计会由于样本的随机性导致估计值出现波动，
# 因此需要用误差置信区间来表示对总体参数估计的可靠范围。

# 误差棒图就可以很好地描述总体参数估计的置信区间。
# 误差棒的计算方法可有很多种：单一数值、置信区间、标准差、标准误差等。
# 可视化展示方式也有很多种：水平误差棒、垂直误差棒、对称误差棒、非对称误差棒等。
x = np.linspace(0.1, 0.6, 10)
y = np.exp(x)

error = 0.05 + 0.15*x

lower_error = error
upper_error = error * 0.3

error_limit = [lower_error, upper_error]

plt.errorbar(x,y, # xy数据点的位置
	yerr=error_limit, # 单一数值的非对称形式误差范围
	fmt='o', # 数据点的标记样式和连接线样式
	ecolor='y',  # 误差棒的线条颜色
	elinewidth=4, # 误差棒的线宽
	ms=5, # 数据点的大小
	mfc='c', # 数据点的颜色
	mec='r', # 数据点的边缘颜色
	capsize=2,capthick=1 # 误差棒边界横杠大小
	)
plt.xlim(0,0.7)
plt.show()


## 案例一 带误差棒的柱状图
# 使统计图形同时可以反映数据测量误差

x = np.arange(5)
y = [100, 82, 39, 92,43]
std_err = [7, 2, 6, 10, 5]

err_attribute = dict(elinewidth=2, ecolor='black', capsize=3)
plt.bar(x, y, color='c',
	width=0.6,
	align='center',
	yerr=std_err,
	error_kw=err_attribute,
	tick_label=list('ABCDE'))



'''
xerr : scalar or array-like, optional
	if not None, will be used to generate errorbar(s) on the bar chart default: None
yerr : scalar or array-like, optional
	if not None, will be used to generate errorbar(s) on the bar chart default: None
'''

plt.title("不同芒果园种植区的单词收割量")
plt.xlabel('芒果种植园区')
plt.ylabel('收割量')

plt.grid(axis='y', linestyle=':', color='gray', alpha=0.4)
plt.show()


## 案例3 带误差棒的多数据并列柱状图
# 可以对比两组数据



x = np.arange(5)
y = [100, 82, 39, 92,43]
y_2 = [83,92,100,53, 25]
std_err = [7, 2, 6, 10, 5]
std_err_2 = [6,5 ,10, 2,7 ]

bar_width = 0.35
err_attribute = dict(elinewidth=2, ecolor='black', capsize=3)

# 第一组
plt.bar(x, y, color='c',
	width=bar_width,
	align='center',
	yerr=std_err,
	error_kw=err_attribute,
	# tick_label=list('ABCDE'),  # 后面统一制定x轴标签
	label='第一组')
# 第二组
plt.bar(x+bar_width,   # 并列摆放
	y_2, color='m',
	width=bar_width,
	align='center',
	yerr=std_err_2,
	error_kw=err_attribute,
	# tick_label=list('ABCDE'),
	label='第二组')
plt.xticks((x + bar_width//2), list('ABCDE'))

plt.title("不同芒果园种植区的单词收割量")
plt.xlabel('芒果种植园区')
plt.ylabel('收割量')

plt.grid(axis='y', linestyle=':', color='gray', alpha=0.4)
plt.show()

