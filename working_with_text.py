import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


xlabel = plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
# The r preceding the title string is important -- it signifies that the string
# is a raw string and not to treat backslashes as python escapes.
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

# All of the text() commands return an matplotlib.text.Text instance. Just as
# with with lines above, you can customize the properties by passing keyword
# arguments into the text functions or using setp():

plt.setp(xlabel, fontsize=14, color='r')
plt.show()
