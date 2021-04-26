import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

yoko = np.array([200,400,600,800,1000])
g_200 = np.array([68.59,68.69,70.03,77.66,79.22])
g_400 = np.array([68.73,68.39,68.16,71.09,73.46])
g_600 = np.array([71.0,69.61,69.39,70.00,72.36])
g_800 = np.array([68.51,69.54,69.91,70.66,71.23])
g_1000 = np.array([69.91,69.59,69.72,70.16,69.71])

# fig = plt.figure(figsize=(4,4))
# ax = fig.add_subplot(111)
# ax.grid()

plt.plot(yoko,g_200,label = "200")
plt.plot(yoko,g_400,label = 400)
plt.plot(yoko,g_600,label = 600)
plt.plot(yoko,g_800,label = 800)
plt.plot(yoko,g_1000,label = 1000)
plt.legend()
plt.show()