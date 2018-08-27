# sphinx_gallery_thumbnail_number = 10
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# 初始化数据
data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# 设置 plt 属性，使绘图自动布局
# plt.rcParams.update({'figure.autolayout': True})

# 列出所有可用风格
print(plt.style.available)

# 设置风格
# 要在初始化 figure 和 axe 之前
plt.style.use('seaborn')

with plt.xkcd():
    # 新建 subplots
    # figsize 参数指定了子图的长宽
    fig, ax = plt.subplots(figsize=(8, 4))

    # 绘图
    ax.barh(group_names, group_data)

    # 获得 labels 对象
    xlabels = ax.get_xticklabels()
    ylabels = ax.get_yticklabels()

    # 使用 plt.setp 方法设置属性
    # 设置 label 的旋转
    plt.setp(ylabels, rotation=45, horizontalalignment='right')

    # 设置 ax 属性
    ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
           title='Company Revenue')

    # It is possible to draw multiple plot elements on the same instance of
    # axes.Axes. To do this we simply need to call another one of the plot methods
    # on that axes object.

    # Add a vertical line, here we set the style in the function call
    ax.axvline(group_mean, ls='--', color='r')

    # 在右侧标注出新公司
    for group in [3, 5, 8]:
        ax.text(145000, group, "New Company", fontsize=10,
                verticalalignment="center")

    # 重新设置标题位置居中
    ax.title.set(y=1.05)

    # For labels, we can specify custom formatting guidelines in the form of
    # functions by using the ticker.FuncFormatter class. Below we'll define a
    # function that takes an integer as input, and returns a string as an output.
    # 此处直接使用装饰器装饰函数，将其变为一个 formatter 对象
    @FuncFormatter
    def currency(x, pos):
        """The two args are the value and tick position"""
        if x >= 1e6:
            s = '${:1.1f}M'.format(x*1e-6)
        else:
            s = '${:1.0f}K'.format(x*1e-3)
        return s

    # 为 x 轴设置 label formatter
    ax.xaxis.set_major_formatter(currency)

    # 调整图像位置，防止页面元素显示不全
    # 如果使用自动布局，那此条设置会被忽略
    fig.subplots_adjust(right=0.8)

# 显示图像
plt.show()

# 获取支持的导出格式
print(fig.canvas.get_supported_filetypes())

# 保存图像
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
