# chapter 7
# 共享坐标轴

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False



t = np.arange(0.05, 10.0, 0.01)
s1 = np.exp(t)
s2 = np.cos(t)


fig, ax = plt.subplots() # 默认一行一列
ax.plot(t, s1, c='b',ls='--',label='$\exp(x)$')
ax.set_xlabel('x-axis') # 设置x坐标轴
ax.set_ylabel('以e为底数的指数函数', color='b') # 设置y坐标轴
ax.tick_params('y', colors='b') # y坐标轴的刻度


## 关键，共享x坐标轴
ax2 = ax.twinx()

ax2.plot(t, s2, c='g', ls=":",label='$\cos(x)$')

ax2.set_ylabel('余弦函数',color='r') #  设置y坐标轴
ax2.tick_params('y', colors='r')

plt.legend()
plt.title('共享x轴')
plt.show()




### 共享不同子图的坐标轴
# 调整subplots中的sharex或sharey参数

# sharex与sharey的取值共有4中，row\col\all\none，其中all和none分别等同与true和false


x1 = np.linspace(0,2*np.pi,100)
y1 = np.sin(x1)

x2 = np.linspace(0,4,100)
y2 = np.random.randn(100)

x3 = np.linspace(0,2*np.pi,100)
y3 = np.cos(x3**2)

x4 = np.linspace(0,4,10)
y4 = np.power(x4,2)

fig, ax = plt.subplots(2,2,sharex=False,sharey=False)

ax[0,0].plot(x1,y1)
ax[0,1].scatter(x2,y2)
ax[1,0].plot(x3,y3)
ax[1,1].scatter(x4,y4)

plt.show()



## 去掉子图之间的间隙
# fig.subplots_adjust(hspace=0, # 去掉水平间隙
# 					vspace=0) # 去掉竖直间隙


# 情况三 共享个别子区域的坐标轴


### 共享不同子图的坐标轴
# 调整subplots中的sharex或sharey参数

# sharex与sharey的取值共有4中，row\col\all\none，其中all和none分别等同与true和false


x1 = np.linspace(-10,2*np.pi,100)
y1 = np.sin(x1)

x2 = np.linspace(0,4,100)
y2 = np.random.randn(100)

x3 = np.linspace(0,2*np.pi,100)
y3 = np.cos(x3**2)

x4 = np.linspace(0,4,10)
y4 = np.power(x4,2)

# fig, ax = plt.subplots(2,2)
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223,sharey=ax2)  # 2与3共享y轴
ax4 = plt.subplot(224,sharex=ax1) # 1与4 共享x轴


ax1.plot(x1,y1)
ax2.scatter(x2,y2)
ax3.plot(x3,y3)
ax4.scatter(x4,y4)


plt.show()

