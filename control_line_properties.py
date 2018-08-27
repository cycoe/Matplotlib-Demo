import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 50, 1)
y = np.random.randn(50)
z = np.random.random(50)

# plt.plot return matplotlib.lines.Line2D object, is a indexable object
line1, line2 = plt.plot(x, y, x, z)
# 使用 line2D 对象的方法进行控制
line1.set_antialiased(False)
line2.set_alpha(0.5)
# 使用 plt.setp 方法对 line2D 对象进行控制
# 可以对单独一条线控制，也可以对 matplotlib.lines.Line2D object
plt.setp(line1, color='r')
plt.setp(line2, color='m')
plt.setp((line1, line2), linestyle=':', linewidth=1)

# 通过调用不加参数的 setp，可获取当前 line 的属性
plt.setp(line1)

plt.show()
