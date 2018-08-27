# How to create grid-shaped combinations of axes.
# subplots()
#     Perhaps the primary function used to create figures and axes. It's also
#     similar to subplot(), but creates and places all axes on the figure at
#     once.
# GridSpec
#     Specifies the geometry of the grid that a subplot will be placed. The
#     number of rows and number of columns of the grid need to be set.
#     Optionally, the subplot layout parameters (e.g., left, right, etc.) can
#     be tuned.
# SubplotSpec
#     Specifies the location of the subplot in the given GridSpec.
# subplot2grid()
#     A helper function that is similar to subplot(), but uses 0-based indexing
#     and let subplot to occupy multiple cells. This function is not covered in
#     this tutorial.

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

# Using subplots() is quite simple. It returns a Figure instance and an array
# of Axes objects.
# fig1, axes1 = plt.subplots(ncols=2, nrows=2)
# fig1.tight_layout()

# 对于 gridspec，你需要独立创建 figure 和 GridSpec 实例，然后将 gridspec 对象
# 作为参数传递给 figure.add_subplot() 方法。其中 gridspec 对象的索引方式与
# Numpy 类似
# fig2 = plt.figure()
# spec2 = gridspec.GridSpec(ncols=2, nrows=2)
# f2_ax1 = fig2.add_subplot(spec2[0, 0])
# f2_ax2 = fig2.add_subplot(spec2[0, 1])
# f2_ax3 = fig2.add_subplot(spec2[1, 0])
# f2_ax4 = fig2.add_subplot(spec2[1, 1])
# fig2.tight_layout()

# 当你想要绘制不同大小的子图时，就需要使用 GridSpec 对象。通过像使用 Numpy
# 一样指定子图占有的行和列，即可按整数比例绘制子图
# fig3 = plt.figure()
# spec3 = gridspec.GridSpec(ncols=3, nrows=3)
# # 创建一个字典用于存储注释的参数
anno_opts = dict(
    xy=(0.5, 0.5),
    xycoords='axes fraction',
    va='center',
    ha='center'
)
# fig3.add_subplot(spec3[0, 0]).annotate('GridSpec[0, 0]', **anno_opts)
# fig3.add_subplot(spec3[0, 1:]).annotate('GridSpec[0, 1:]', **anno_opts)
# fig3.add_subplot(spec3[1:, 0]).annotate('GridSpec[1:, 0]', **anno_opts)
# fig3.add_subplot(spec3[1:, 1:]).annotate('GridSpec[1:, 1:]', **anno_opts)
# fig3.tight_layout()

# 另一种控制子图大小的方法是直接控制网格的大小比例，通过将一个权重列表传入
# GridSpec，获得一个按权重分布的子图网格。既然是比例，那么 [1, 2, 4] 与
# [2, 4, 8] 就是等价的
# fig4 = plt.figure()
# widths = [2, 3, 1.5]
# heights = [1, 3, 2]
# spec4 = gridspec.GridSpec(ncols=3, nrows=3, width_ratios=widths,
#                           height_ratios=heights)
# for row in range(3):
#     for col in range(3):
#         ax = fig4.add_subplot(spec4[row, col])
#         label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
#         ax.annotate(label, **anno_opts)

# fig4.tight_layout()

# 所有 GridSpec 的参数都可以通过 gridspec_kw 参数传递给 plt.subplots 方法
# widths = [2, 3, 1.5]
# heights = [1, 3, 2]
# gs_kw = dict(width_ratios=widths, height_ratios=heights)
# fig5, f5_axes = plt.subplots(ncols=3, nrows=3, gridspec_kw=gs_kw)
# for r, row in enumerate(f5_axes):
#     for c, ax in enumerate(row):
#         label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
#         ax.annotate(label, **anno_opts)

# fig5.tight_layout()

# 当你使用 GridSpec 对象创建子图网格时，可以直接通过布局参数控制子图，类似
# figure.subplots_adjust() 方法
# fig = plt.figure()
# gs1 = gridspec.GridSpec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.2)
# ax1 = fig.add_subplot(gs1[:-1, :])
# ax2 = fig.add_subplot(gs1[-1, :-1])
# ax3 = fig.add_subplot(gs1[-1, -1])

# 使用上述布局调整只影响由该 GridSpec 对象创建的子图，比较左右两幅图有助于理解
# fig = plt.figure()
# gs1 = gridspec.GridSpec(nrows=3, ncols=3, left=0.05, right=0.48,
#                         wspace=0.2)
# ax1 = fig.add_subplot(gs1[:-1, :])
# ax2 = fig.add_subplot(gs1[-1, :-1])
# ax3 = fig.add_subplot(gs1[-1, -1])

# gs2 = gridspec.GridSpec(nrows=3, ncols=3, left=0.55, right=0.98,
#                         hspace=0.2)
# ax4 = fig.add_subplot(gs2[:, :-1])
# ax5 = fig.add_subplot(gs2[:-1, -1])
# ax6 = fig.add_subplot(gs2[-1, -1])

# 使用 SubplotSpec 创建 GridSpec
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2)

gs00 = gridspec.GridSpecFromSubplotSpec(2, 3, subplot_spec=gs0[0])
gs01 = gridspec.GridSpecFromSubplotSpec(3, 2, subplot_spec=gs0[1])

for a in range(2):
    for b in range(3):
        fig.add_subplot(gs00[a, b])
        fig.add_subplot(gs01[b, a])

fig.tight_layout()

plt.show()
