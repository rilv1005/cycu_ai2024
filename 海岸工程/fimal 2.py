import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Input waveHeight_t120.txt
file = r"C:\Users\User\Desktop\homework\海岸工程\final\waveHeight_5120.txt"
(time, eta) = np.loadtxt(file, unpack=True, skiprows=1)

# 基本參數設定
f_s2 = 1 / (time[1] - time[0])  # 採樣頻率 Hz
N2 = len(time)  # 資料點數
t = np.arange(N2)/f_s2  # 時間軸
print(f"採樣頻率：{f_s2:.2f} Hz, 資料總數：{N2} 筆, 總時間：{(N2 / f_s2):.2f} s")

# 計算 FFT
Y = fft(eta)
# 頻率軸
freq = fftfreq(N2, d=1/f_s2)

# 取前半段頻率(因為對稱性)
half_N = N2//2
freq_half = freq[:half_N]
Y_half = Y[:half_N]

# 計算振幅譜 (Amplitude Spectrum)
amplitude_spectrum = np.abs(Y_half)/(N2/2) # 正規化，以便振幅代表每頻率成分的相對大小

# 時域圖
fig1, ax1 = plt.subplots(layout='constrained', dpi=150)
ax1.plot(time, eta, linewidth=1)
ax1.set_xlabel('Time (s)');
ax1.set_ylabel('Water Surface Elevation (m)')
ax1.grid(axis='y')

# 頻域圖
plt.figure(figsize=(10, 4))
plt.plot(freq_half, amplitude_spectrum, 'r', label='Amplitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Domain')
plt.grid(True)
plt.legend()
plt.xlim(0.0, 1.0)  # 設定 x 軸範圍
plt.tight_layout()

plt.show()