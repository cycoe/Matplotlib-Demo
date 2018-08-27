import matplotlib.pyplot as plt
import numpy as np

# 绘制手绘风格的图
with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Monroe
    # http://xkcd.com/418/

    fig, (ax1, ax2) = plt.subplots(2, 1)
    # 去掉上边和右边的边界
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    ax1.annotate(
        'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -15))

    ax1.plot(data)

    ax1.set_xlabel('time')
    ax1.set_ylabel('my overall health')
    ax1.set_title('"Stove Ownership" from xkcd by Randall Monroe')

    ax2.bar([0, 1], [0, 100], 0.25)
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.xaxis.set_ticks_position('bottom')
    ax2.set_xticks((0, 1))
    ax2.set_xlim((-0.5, 1.5))
    ax2.set_ylim((0, 110))
    ax2.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
    ax2.set_yticks([])
    ax2.set_title('CLAIMS OF SUPERNATURAL POWERS')

fig.tight_layout()
plt.show()
