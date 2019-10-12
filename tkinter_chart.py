import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('E:\Python_ML\My Projects\DATA.xlsx')

plt.plot(data['Age'])

plt.show()
