import matplotlib.pyplot as plt
import numpy as np

# The uses of the basic text() command above place text at an arbitrary
# position on the Axes. A common use for text is to annotate some feature of
# the plot, and the annotate() method provides helper functionality to make
# annotations easy. In an annotation, there are two points to consider: the
# location being annotated represented by the argument xy and the location of
# the text xytext. Both of these arguments are (x,y) tuples.

# 在 matplotlib 中，可以通过 plt.figure() 创建多个 figure 对象，每个 figure 又
# 可以创建多个 subplot。
# 绘图有两种方法
# 1. 通过函数绘图
# plt.figure(1)
# plt.subplot(111)
# plt.plot(x, y)
# plt.xlim(0, 2) # 通过 plt 的 xlim 方法设置当前 axe 的属性
# plt 会自动 handle 当前的 figure 和 axe，在当前的 axe 上作图，也可通过
# plt.gca() 方法得到当前的 axe 对象，通过 plt.gcf() 方法得到当前的 figure 对象。
# 2. 面对对象绘图
# plt.figure(1)
# axe = subplot(111) # 使用 axe 接收返回的 axe 对象
# axe.plot(x, y)
# axe.set_xlim(0, 2) # 通过 axe 对象的方法设置 axe 的属性
# plt.setp(axe, xlim=(0, 2)) # 或通过 plt.setp() 方法设置对象属性

fig = plt.figure(1)
plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='red', shrink=0.05),
             )

ax = plt.gca()
ax.set_ylim(-2, 2)
plt.show()
