import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_file(path):
  data = pd.read_csv(path)
  df = pd.DataFrame(data)
  return df

# import files


path = '/Users/nathanoliver/Desktop/Python/US_Energy2.0/csv/data.csv'

df = read_file(path)

print(df.columns)


# res_wasted = []
# res_used = []
# res_total = []

# wasted energy

# df1 = df.copy()


# width = .1

# sector = ['residential', 'commercial', 'industrial',
#           'transportation', 'electricity generation']


# energy = ['natural gas', 'petroleum', 'coal', 'biomass']

# color = ['#87ceeb', '#964B00', 'black', 'green']

# df2 = df1[df1['category'] == energy[0]]
# df3 = df1[df1['category'] == energy[1]]
# df4 = df1[df1['category'] == energy[2]]

# factor = 2

# shift = [-.1 * factor, 0, .1 * factor]

# print(shift)


# def reset_index(df):
#     df = df.reset_index(drop=True)

#     return df


# df2 = reset_index(df2)
# df3 = reset_index(df3)
# df4 = reset_index(df4)

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, figsize=(20, 8))

textstr = 'Source: EIA'

plt.text(0.12, 0.025, textstr, fontsize=10, transform=plt.gcf().transFigure)


col1 = ['Natural Gas Consumed by the ',
        'Petroleum Consumed by the ', 'Coal Consumed by the ']
col2 = ['Residential Sector', 'Commercial Sector', 'Industrial Sector',
        'Transportation Sector', 'Electric Power Sector']

title = ['Natural Gas', 'Petroleum', 'Coal']

sector_label = ['Residential', 'Commercial', 'Industrial',
                'Transportation', 'Electricity']


def plot_graph(df, colors, ax, title, col):
  lw = 3
  ax.plot(df['year'], df[col + col2[0]], color=colors[0], linewidth=lw)
  ax.plot(df['year'], df[col + col2[1]], color=colors[1], linewidth=lw)
  ax.plot(df['year'], df[col + col2[2]], color=colors[3], linewidth=lw)
  ax.plot(df['year'], df[col + col2[3]], color=colors[4], linewidth=lw)
  ax.plot(df['year'], df[col + col2[4]],
          color=colors[5], linewidth=lw)
  ax.set_xlim(1949, 2019)
  ax.set_ylim(0, 30000)
  ax.set_title(title)
  ax1.set_ylabel('Energy (Trillion Btu)')
  # ax3.legend(sector_label)
  # ax.set_xticks(np.arange(1949, 2019, 10))
  # ax.set_xticks(np.arange(1950, 2020, 10), 2019)
  # # ax.set_yticks([])
  # ax1.set_yticks(np.arange(0, 35000, 5000))
  # ax.grid(b=None, which='major', axis='both')


# plt.grid(b=None, which='major', axis='both')


# plt.subplots_adjust(wspace=0.1)
plot_graph(df, colors, ax1, title[0], col1[0])
plot_graph(df, colors, ax2, title[1], col1[1])
plot_graph(df, colors, ax3, title[2], col1[2])
fig.suptitle(
    '      US Fossil Fuel Consumption by Sector (1949-2019)', fontsize=20)
plt.text(1, 1, textstr, fontsize=14)


# Residential

plt.text(0.19, 0.255, sector_label[0],
         color=colors[0], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.55, 0.16, sector_label[0],
         color=colors[0], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.7, 0.168, sector_label[0],
         color=colors[0], transform=plt.gcf().transFigure, weight='bold')

# Commercial

plt.text(0.19, 0.153, sector_label[1],
         color=colors[1], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.46, 0.12, sector_label[1],
         color=colors[1], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.7, 0.15, sector_label[1],
         color=colors[1], transform=plt.gcf().transFigure, weight='bold')

# industrial

plt.text(0.215, 0.35, sector_label[2],
         color=colors[3], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.505, 0.37, sector_label[2],
         color=colors[3], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.78, 0.2, sector_label[2],
         color=colors[3], transform=plt.gcf().transFigure, weight='bold')

# Transportation

plt.text(0.265, 0.14, sector_label[3],
         color=colors[4], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.46, 0.69, sector_label[3],
         color=colors[4], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.7, 0.132, sector_label[3],
         color=colors[4], transform=plt.gcf().transFigure, weight='bold')

# Electricity

plt.text(0.255, 0.28, sector_label[4],
         color=colors[5], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.457, 0.23, sector_label[4],
         color=colors[5], transform=plt.gcf().transFigure, weight='bold')

plt.text(0.82, 0.67, sector_label[4],
         color=colors[5], transform=plt.gcf().transFigure, weight='bold')

# fontsize=m_size,

plt.show()
