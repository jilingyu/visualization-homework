import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


insurance = pd.read_csv(filepath_or_buffer='insurance.csv',
                      sep=',',
                      header=0)

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(insurance['charges'], color='red')
plt.title('charges_plot')
plt.xlabel('charges')
plt.ylabel('Count')
plt.savefig(f'plots/charges_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(insurance['bmi'], bins=3, color='g')
plt.title('bmi_hist')
plt.xlabel('bmi')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('Age_charges_scatter')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig(f'plots/age_charges_scatter.png', format='png')

plt.close()
