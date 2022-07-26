import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('WR 100W.xlsx')

x_1 = df.iloc[2:25, 3]
print(x_1)

y_1 = df.iloc[2:25, 5]
print(y_1)

plt.scatter(x_1, y_1, marker='x')

z = np.polyfit(x_1, y_1, 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(x_1, p(x_1))

plt.xlim([0, 110])
plt.ylim([78, 85])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')

plt.show()