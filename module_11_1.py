import random

import matplotlib.pyplot as plt
import numpy as np

l = np.linspace(0, 5)
fig, ax = plt.subplots( figsize= (10, 5), layout= 'constrained')
ax.plot (l, 100-100*0.5**(l), label= 'монетка')
ax.plot(l, 100-100*0.8334**(l), label= 'кубик')
ax.plot(l, 100-100*0.9**(l), label= 'десятигранник')
ax.set_xlabel('Количество')
ax.set_ylabel('Шанс (в %)')
ax.set_title('Шанс получить определенный результат при броске')
ax.legend()
ax.grid(True)
ax.set_yticks(np.arange(0, 100, 10))
plt.show()

fig, axs = plt.subplots(2, 1)
axs[0].plot([-1, 0, 1, 0, -1], [0, 1, 0, -1, 0])
x = np.random.randint(0, 10)
y = np.random.randint(0, 10)
z = np.random.randint(0, 10)
axs[1].scatter([x, y, z], [z, x, y])
plt.show()


import requests as r

r1 = r.options('https://github.com/IronPhilosopher/Homework')
r2 = r.delete('https://github.com/IronPhilosopher/Homework')
r3 = r.get('https://github.com/IronPhilosopher/Homework')
print(r1.text)
print(r2.text)
print(r3.history)
print(r3.status_code)

