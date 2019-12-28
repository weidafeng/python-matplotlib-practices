
# coding: utf-8

# # 《python数据可视化之matplotlib实践》
# 
# ## 查看颜色格式
# 
# http://colorbrewer2.org/#type=sequential&scheme=PuBuGn&n=3

# In[3]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

random_data = np.random.rand(10,10)
plt.pcolor(random_data, cmap='BuPu') # Create a pseudocolor plot of a 2-D array.
plt.colorbar()
plt.show()


# In[4]:


random_data = np.random.rand(10,10)
plt.pcolor(random_data, cmap=mpl.cm.BuPu) # 指定颜色格式colormap的另一种方法
plt.colorbar()
plt.show()


# In[5]:


# 绘制图片的像素值colormap

import scipy.misc
import matplotlib as mpl
import matplotlib.pyplot as plt

ascent = scipy.misc.ascent()  # 调用一张图像示例（numpy array格式）
print(ascent.shape, type(ascent))
plt.imshow(ascent, cmap=mpl.cm.gray)

plt.colorbar()
plt.show()


# In[6]:


plt.imshow(ascent, cmap=mpl.cm.jet)

plt.colorbar()
plt.show()


# In[7]:


plt.imshow(ascent, cmap=mpl.cm.hot)

plt.colorbar()
plt.show()


# In[8]:


demo = plt.imread("overview.png")
plt.imshow(demo)
plt.colorbar()
plt.show()

