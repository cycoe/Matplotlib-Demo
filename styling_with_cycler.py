from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt


# generate some sample data
x = np.linspace(0, 2 * np.pi, 50)
offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])

# 创建样式的 cycler，组合颜色和线的样式
default_cycler = (
    cycler(color=['r', 'g', 'b', 'y']) +
    cycler(linestyle=['-', '--', ':', '-.'])
)
custom_cycler = (
    cycler(color=['c', 'm', 'y', 'k']) +
    cycler(lw=[1, 2, 3, 4])
)

# 此时 cc 是一个迭代器
# cc = (cycler(color=list('rgb')) +
#       cycler(linestyle=['-', '--', '-.']))
# 返回
# {'color': 'r', 'linestyle': '-'}
# {'color': 'g', 'linestyle': '--'}
# {'color': 'b', 'linestyle': '-.'}
#
# cc = (cycler(color=list('rgb')) *
#       cycler(linestyle=['-', '--', '-.']))
# 返回
# {'color': 'r', 'linestyle': '-'}
# {'color': 'r', 'linestyle': '--'}
# {'color': 'r', 'linestyle': '-.'}
# {'color': 'g', 'linestyle': '-'}
# {'color': 'g', 'linestyle': '--'}
# {'color': 'g', 'linestyle': '-.'}
# {'color': 'b', 'linestyle': '-'}
# {'color': 'b', 'linestyle': '--'}
# {'color': 'b', 'linestyle': '-.'}

# 创建多图对象
fig, (ax0, ax1) = plt.subplots(nrows=2)

# 使用 plt.rc 设置样式，并绘制 ax0
plt.rc('lines', linewidth=4)
plt.rc('axes', prop_cycle=default_cycler)
ax0.plot(yy)
ax0.set_title('Set default color cycle to rgby')

# 使用 custom_cycler 设置样式，并绘制 ax1
ax1.set_prop_cycle(custom_cycler)
ax1.plot(yy)
ax1.set_title('Set axe1 color cycle to cmyk')

# Add a bit more space between the two plots
fig.subplots_adjust(hspace=0.3)

plt.show()
