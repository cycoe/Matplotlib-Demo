import numpy as np
import matplotlib.pyplot as plt

data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)
}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d'] * 100)

# c means color, s means size
plt.scatter('a', 'b', c='c', s='d', data=data, alpha=1)
plt.show()

print(data['d'])
