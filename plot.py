from datetime import datetime
import matplotlib.pyplot as plt 

import numpy as np

x=np.array([date for date in range(2006, 2021)])
y=np.array(storico_papers)

z1 = np.polyfit(x, y, 1)
p = np.poly1d(z1)

fig, ax = plt.subplots(2, figsize=(9, 7), sharex=True, sharey=True)

fig.suptitle('Serie Storica numero di pubblicazioni in Italia', fontsize=16)

fig.text(0.5, 0.04, 'Years', ha='center', fontsize=16)
fig.text(0.04, 0.5, 'Numbers of papers', va='center', rotation='vertical', fontsize=16)

ax[0].plot(x,y,marker="o")
ax[0].plot(x,p(x),"r--")

ax[1].bar(x,y, color ='blue', width = 0.4)
ax[1].plot(x,p(x),"r--")



plt.gcf().set_size_inches(9, 7)
plt.xticks(x)   #visualizzo tutte le date sull'asse x
plt.show()
