import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')
data = pd.read_csv(filepath_or_buffer='CIC timelines  - QSW applicants.csv',
                      sep=',',
                      header=4)
print(data.columns)
os.makedirs('plots_for_data', exist_ok=True)
# Plotting line chart
plt.plot(data['APP-PPR'], color='red')
plt.title('APP-PPR')
plt.xlabel('APP-PPR TIME')
plt.ylabel('NUMBER OF PEOPLE WHO GOT APP-PPR')
plt.savefig(f'plots_for_data/plot.png', format='png')
plt.clf()

plt.hist(data['AOR-PPR'], bins=3, color='g')
plt.title('AOR-PPR')
plt.xlabel('AOR-PPR TIME')
plt.ylabel('NUMBER OF PEOPLE WHO GOT AOR-PPR')
plt.savefig(f'plots_for_data/hist.png', format='png')
plt.clf()

plt.scatter(data['APP-PPR'], data['AOR-PPR'], color='b')
plt.title('APP-PPR')
plt.xlabel('AOR-PPR')
plt.ylabel('NUMBER OF PEOPLE WHO GOT APP-PPR')
plt.savefig(f'plots_for_data/scatter.png', format='png')
plt.clf()
