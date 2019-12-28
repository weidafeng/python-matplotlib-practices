# chapter-1： matplotlib图表组成元素
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 3.5, 100) # Returns num evenly spaced samples, calculated over the interval [start, stop].
y = np.sin(x)

y1 = np.random.randn(100) # Return a sample (or samples) from the "standard normal" distribution.

plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')
plt.legend()
plt.show()

'''
matplotlib.iines.Line2D.set_linestyle

linestyle		description
'-'or 'solid' 	solid line
'--'or'dashed'	dashed line
'-.'or'dash_dot'	dash-dotted line
':'or'dotted'	dotted line
'None'		draw nothing
' '			draw nothing
''			draw nothing
'''
plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')
plt.scatter(x, y1, label='scatter figure', marker="*")

## xlim 
plt.xlim(0, 1)
plt.ylim(0, 1)

## xlabel
plt.xlabel('x-axis')
plt.show()


## grid 刻度线
plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')

plt.grid(color='r', linestyle=':')
plt.show()

## axhline 水平参考线
plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')
plt.legend()

plt.axhline(y=0.5,
			color='r',
			xmin=0.5,
			xmax=1,
			linestyle='--',
			linewidth=2)
'''
xmin : scalar, optional, default: 0
Should be between 0 and 1, 0 being the far left of the plot, 1 the far right of the plot.
xmax : scalar, optional, default: 1
Should be between 0 and 1, 0 being the far left of the plot, 1 the far right of the plot.
'''
plt.axvline(4, ymin=0.6,ymax=0.8,color='g',linestyle=":",linewidth=2)
plt.show()


## axvspan 竖直参考区域
plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')

plt.legend()
plt.axvspan(xmin=4, # 起始位置
			xmax=6,	# 终止位置
			ymin=0,
			ymax=0.6,
			facecolor='y', # 填充颜色
			alpha=0.3) # 填充透明度

plt.axhspan(ymin=0,ymax=0.6,xmin=4,xmax=6,facecolor='g',alpha=0.3)
plt.show()




## annotate 指向型文本注释
plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')
plt.legend()

plt.annotate(s='maximum', # 注释文本
			xy=(np.pi/2, 1.0), # 被注释图像内容的位置坐标 （箭头指向的地方，即需要标注的坐标点）
			xytext=((np.pi/2)+1.0, 0.8), # 注释文本的位置坐标（箭头开始指的地方，即放置注释文本的地方）
			color='b',	# 注释文本的颜色
			arrowprops=dict(arrowstyle='->', connectionstyle='arc3',color='b')) # 箭头的属性字典
plt.show()


## text 无指向性文本注释
plt.plot(x, y, 
	ls='-.', # 折线图的线条风格
 	lw=2,   # 折线图的线宽
 	label='plot figure')
plt.legend()
plt.title('y=sin(x)')
plt.text(x=np.pi, y=0.0, s='y=sin(x)', weight='bold', color='b')
plt.show()
