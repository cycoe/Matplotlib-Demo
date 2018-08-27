# GridSpec 对象有它自己的 tight_layout() 方法（pyplot 的 tight_layout 方法也可
# 用）
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"


def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)


plt.close('all')
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)

# 为防止图像显示不全，需要调整 axe。对于 subplots，可通过调整 subplot 的参数实
# 现（通过移动 axe 的边缘来为刻度标签腾出空间）。对于 plt 来说可以使用
# plt.tight_layout() 方法来调整
# 需要注意的是，matplotlib.pyplot.tight_layout() 方法只会调整已经调用（called）
# 过的子图参数，为了能在每次 figure 在被重绘时自动调整，可以使用
# figure.set_tight_layout(True)
plt.tight_layout()

# 当你有很多子图时，你经常能看到不同子图互相重叠的情况
plt.close('all')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

# tight_layout() 方法也能够通过调整空隙大小来最小化这种重叠现象
# 并且能够附带一些控制参数，这些间隔一般来说是按字体大小比例来的
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

# tight_layout() 也能对不同尺寸的子图其作用，只要他们的规格是兼容的
plt.close('all')
fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)

plt.tight_layout()

# 同样的，使用 subplot2grid() 创建的子图也适用
plt.close('all')
fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0))
ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

plt.tight_layout()

# 虽然未经过测试，该方法也同样广泛地适用于外观不是「自动」的子图（比如一些由图
# 像组成的子图
arr = np.arange(100).reshape((10, 10))
plt.close('all')
fig = plt.figure(figsize=(5, 4))

ax = plt.subplot(111)
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()

# **注意**
# - tight_layout() 方法只考虑刻度标签、坐标轴标签和标题。因此其余的元素会被忽略
# 并仍有可能重叠在一起
# - 事实上我们假定了刻度标签、坐标轴标签和标题需要的额外空间对于图像原本的位置
# 是独立的。这一般来说都是满足的。
# - 使用 pad=0 参数有可能会使程序忽视了文字的一部分像素。这目前还是一个不清楚原
# 理的 bug。所以在使用 pad 参数时建议至少将其设为 0.3
plt.close('all')
fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

# 通过提供 rect 参数，可以指定 subplots 绘制的区域
gs1.tight_layout(fig, rect=(0, 0, 0.5, 1))

plt.show()
