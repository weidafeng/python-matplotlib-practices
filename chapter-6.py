# chapter 6
# 划分画布

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# subplot2grid(shape, loc, colspan, rowspan)
# 实现非等分画布

plt.subplot2grid((4,4),(0,0), colspan=3) # 整个画布分均为4行4列，从（0，0）开始，占3列
x = np.linspace(0,4,10)
y = np.random.randn(10)
plt.scatter(x,y,c='b')
plt.title('scatter')


plt.subplot2grid((4,4), (0,3)) # 整个画布分均为4行4列，从（0,3）开始，默认占1行1列
plt.title('empty fig')


plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=2) # 整个画布分均为4行4列，从（1,0）开始，占3行2列
plt.plot(range(10), range(10),color='g')
plt.grid(color='gray',alpha=0.4, linestyle=':')
plt.title('line')


plt.subplot2grid((4,4), (2,2), colspan=2)
plt.plot(x, np.sin(x), marker='*',c='r')
plt.title('sin(x)-1')


plt.subplot2grid((4,4), (3,2))
plt.plot(x, np.sin(x), marker='*',c='m')
plt.title('sin(x)-2')


plt.subplot2grid((4,4), (3,3))
plt.plot(x, np.cos(x), marker='*',c='k')
plt.title('cos(x)')
plt.show()