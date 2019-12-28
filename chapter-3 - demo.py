# chapter 3
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

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

