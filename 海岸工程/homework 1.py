#題目𝑦 = sin(𝜃)
#1. 𝑦 = − sin(𝜃)
#2. 𝑦 = sin(−𝜃)
#3. 𝑦 = 0.5sin(𝜃)
#4. 𝑦 = −2 sin(3𝜃)
#5. 𝑦 = sin(𝜃/2)
#6. 𝑦 = sin(𝜃 + 𝜋/2)


import numpy as np
import matplotlib.pyplot as plt

# 定義範圍 -2π ≤ θ ≤ 2π
theta = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 計算 y = -sin(θ)
y =np.sin(theta+np.pi/2)

# 繪製圖形
plt.plot(theta, y)
plt.title(r'$y = \sin(\theta+\pi/2)$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$y$')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()