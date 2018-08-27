import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Grid


def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)


fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs1.tight_layout(fig, rect=[0, 0, 0.5, 1])

gs2 = gridspec.GridSpec(3, 1)

for ss in gs2:
    ax = fig.add_subplot(ss)
    example_plot(ax)
    ax.set_title("")
    ax.set_xlabel("")

ax.set_xlabel("x-label", fontsize=12)

gs2.tight_layout(fig, rect=[0.5, 0, 1, 1], h_pad=0.5)

# We may try to match the top and bottom of two grids ::
top = min(gs1.top, gs2.top)
bottom = max(gs1.bottom, gs2.bottom)

gs1.update(top=top, bottom=bottom)
gs2.update(top=top, bottom=bottom)

# While this should be mostly good enough, adjusting top and bottom may require
# adjustment of hspace also. To update hspace & vspace, we call tight_layout()
# again with updated rect argument. Note that the rect argument specifies the
# area including the ticklabels, etc. Thus, we will increase the bottom (which
# is 0 for the normal case) by the difference between the bottom from above and
# the bottom of each gridspec. Same thing for the top.
top = min(gs1.top, gs2.top)
bottom = max(gs1.bottom, gs2.bottom)

gs1.tight_layout(fig, rect=[None, 0 + (bottom-gs1.bottom),
                            0.5, 1 - (gs1.top-top)])
gs2.tight_layout(fig, rect=[0.5, 0 + (bottom-gs2.bottom),
                            None, 1 - (gs2.top-top)],
                 h_pad=0.5)

# axes_grid1 工具箱也被支持
plt.close('all')
fig = plt.figure()
grid = Grid(fig, rect=111, nrows_ncols=(2, 2),
            axes_pad=0.25, label_mode='L',
            )

for ax in grid:
    example_plot(ax)
ax.title.set_visible(False)

plt.tight_layout()

# 如果你使用 colorbar() 命令创建一个 colorbar，那它会是 Axes 的一个实例，而
# 不是 Subplot，因此 tight_layout 不奏效。使用 Matplotlib v1.1 以上的版本，你可
# 以使用 gridspec 创建一个 Subplot 的 colorbar 实例
plt.close('all')
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

# 关键在于 use_gridspec 参数，使得 colorbar 可以使用 tight_layout 方法
plt.colorbar(im, use_gridspec=True)

plt.tight_layout()

# 另一种方式可以使用 AxesGrid1 工具包来明确地为 colorbar 创建一个 axes
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.close('all')
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

# 将当前 axes 变为可分隔的
divider = make_axes_locatable(plt.gca())
# 在右侧加入一个 axes
cax = divider.append_axes("right", "5%", pad="3%")
# 针对绘制的 im 对象，在 cax 上绘制 colorbar
plt.colorbar(im, cax=cax)

plt.tight_layout()

plt.show()
