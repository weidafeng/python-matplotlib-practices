# chapter 8
# 坐标轴高阶应用

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


# 移动坐标轴

## 设置刻度范围和刻度标签
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.subplot(211) # 2行1列，指定第二个子图
# 1. 刻度以圆周率形式展示
# 2. 设置合理的范围
plt.xlim(-2*np.pi, 2*np.pi)
plt.xticks([-2*np.pi, -1.5 *np.pi, -np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
		[r'$-2\pi$',r'$-3\pi/2$',r'$-\pi$',r'$\pi/2$',r'$0$',r'$\pi/2$',r'$3\pi/2$',r'$2\pi$'])

plt.plot(x,y_1, label=r'$\sin(x)$')
plt.plot(x,y_2,label=r'$\cos(x)$')
plt.grid(axis='x',color='gray',ls=":")
plt.legend(loc='lower left', bbox_to_anchor=(1,0.5,0.9,0.9))


ax = plt.subplot(212)
# 1. 取消两个轴
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 2. 移动两个轴
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

plt.xlim(-2*np.pi, 2*np.pi) # 这里通过ax设置
plt.xticks([-2*np.pi, -1.5 *np.pi, -np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],  # 这里通过plt设置
		[r'$-2\pi$',r'$-3\pi/2$',r'$-\pi$',r'$\pi/2$',r'$0$',r'$\pi/2$',r'$3\pi/2$',r'$2\pi$'])

plt.plot(x,y_1, label=r'$\sin(x)$')
plt.plot(x,y_2,label=r'$\cos(x)$')
plt.grid(axis='x',color='gray',ls=":")
plt.show()
