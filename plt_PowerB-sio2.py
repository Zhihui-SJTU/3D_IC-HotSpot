import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Cu_pillar_8tiers_thickness = [50, 25]
Cu_pillar_8tiers_temperature  = [91.81, 92.36]
Cu_pillar_thickness = [80, 50, 25]
Cu_pillar_4tiers_temperature  = [74.7, 74.91, 75.08]
Cu_pillar_2tiers_temperature  = [66.39, 66.4, 66.4]
Cu_Cu_thickness = [50, 25, 10]
Cu_Cu_8tiers_temperature  = [58.77, 59.19, 59.44]
Cu_Cu_4tiers_temperature  = [58.25, 58.38, 58.46]
Cu_Cu_2tiers_temperature  = [57.47, 57.47, 57.47]
Monolithic_thickness = [0.16]
Monolithic_8tiers_temperature  = [103.12]
Monolithic_4tiers_temperature  = [103.33]
Monolithic_2tiers_temperature  = [103.43]

fig, ax = plt.subplots(figsize=(7, 5), dpi=200)
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.07, top=0.95)

plt.plot(Cu_pillar_8tiers_thickness, Cu_pillar_8tiers_temperature, 'b*--', alpha=0.5, linewidth=1, label='Cu_pillar_8tiers')
plt.plot(Cu_pillar_thickness, Cu_pillar_4tiers_temperature, 'bs--', alpha=0.5, linewidth=1, label='Cu_pillar_4tiers')
plt.plot(Cu_pillar_thickness, Cu_pillar_2tiers_temperature, 'bo--', alpha=0.5, linewidth=1, label='Cu_pillar_2tiers')

plt.plot(Cu_Cu_thickness, Cu_Cu_8tiers_temperature, 'r*--', alpha=0.5, linewidth=1, label='Cu_Cu_8tiers')
plt.plot(Cu_Cu_thickness, Cu_Cu_4tiers_temperature, 'rs--', alpha=0.5, linewidth=1, label='Cu_Cu_4tiers')
plt.plot(Cu_Cu_thickness, Cu_Cu_2tiers_temperature, 'ro--', alpha=0.5, linewidth=1, label='Cu_Cu_2tiers')

plt.plot(Monolithic_thickness, Monolithic_8tiers_temperature, 'g*--', alpha=0.5, linewidth=1, label='Monolithic_8tiers')
plt.plot(Monolithic_thickness, Monolithic_4tiers_temperature, 'gs--', alpha=0.5, linewidth=1, label='Monolithic_4tiers')
plt.plot(Monolithic_thickness, Monolithic_2tiers_temperature, 'go--', alpha=0.5, linewidth=1, label='Monolithic_2tiers')

# for a, b in zip(x_axis_data, y_axis_data1):
#     plt.text(a, b, str(b), ha='center', va='bottom', fontsize=8)  #  ha='center', va='top'
# for a, b1 in zip(x_axis_data, y_axis_data2):
#     plt.text(a, b1, str(b1), ha='center', va='bottom', fontsize=8)  
# for a, b2 in zip(x_axis_data, y_axis_data3):
#     plt.text(a, b2, str(b2), ha='center', va='bottom', fontsize=8)

fontdict1 = {"size": 17, "color": "k"}
ax.set_xlabel("Die thickness (µm)", fontdict=fontdict1)
ax.set_ylabel("Peak Temperature (°C)", fontdict=fontdict1)
plt.legend()
plt.savefig('plt_PowerB-sio2.png', dpi=900, bbox_inches='tight')