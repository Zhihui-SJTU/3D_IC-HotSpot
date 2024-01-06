import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Cu_pillar_8tiers_thickness = [50, 25]
Cu_pillar_8tiers_temperature  = [87.07, 86.75]
Cu_pillar_thickness = [80, 50, 25]
Cu_pillar_4tiers_temperature  = [68.6, 68.41, 68.25]
Cu_pillar_2tiers_temperature  = [59.09, 59.02, 58.96]
Cu_Cu_thickness = [50, 25, 10]
Cu_Cu_8tiers_temperature  = [57.43, 56.98, 56.71]
Cu_Cu_4tiers_temperature  = [55.65, 55.46, 55.34]
Cu_Cu_2tiers_temperature  = [54.5, 54.44, 54.4]
Monolithic_thickness = [0.16]
Monolithic_8tiers_temperature  = [61.6]
Monolithic_4tiers_temperature  = [61.3]
Monolithic_2tiers_temperature  = [61.15]

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

# 2D IC
# Cu_pillar_24mm_temperature  = [50.08, 50.05, 50.03]
# Cu_pillar_17mm_temperature  = [51, 51.02, 51.06]
# Cu_Cu_24mm_temperature  = [50.05, 50.02, 50.01]
# Cu_Cu_17mm_temperature  = [51.06, 51, 50.97]
# Monolithic_24mm_temperature  = [50]
# Monolithic_17mm_temperature  = [50.96]

# plt.plot(Cu_pillar_thickness, Cu_pillar_24mm_temperature, 'bs-', alpha=0.5, linewidth=1, label='Cu_pillar_24mm')
# plt.plot(Cu_pillar_thickness, Cu_pillar_17mm_temperature, 'bo-', alpha=0.5, linewidth=1, label='Cu_pillar_17mm')

# plt.plot(Cu_Cu_thickness, Cu_Cu_24mm_temperature, 'rs-', alpha=0.5, linewidth=1, label='Cu_Cu_24mm')
# plt.plot(Cu_Cu_thickness, Cu_Cu_17mm_temperature, 'ro-', alpha=0.5, linewidth=1, label='Cu_Cu_17mm')

# plt.plot(Monolithic_thickness, Monolithic_24mm_temperature, 'gs-', alpha=0.5, linewidth=1, label='Monolithic_24mm')
# plt.plot(Monolithic_thickness, Monolithic_17mm_temperature, 'go-', alpha=0.5, linewidth=1, label='Monolithic_17mm')

# 2D IC
# 64W
# thickness = [80, 50, 25, 10, 0.16]
# _2DIC_24mm_temperature  = [50.08, 50.05, 50.02, 50.01, 50]
# _2DIC_17mm_temperature  = [51, 51.06, 51, 50.97, 50.96]
# plt.plot(thickness, _2DIC_24mm_temperature, 'bs-', alpha=0.5, linewidth=1, label='2DIC_24mm')
# plt.plot(thickness, _2DIC_17mm_temperature, 'bo-', alpha=0.5, linewidth=1, label='2DIC_17mm')

# 100W
thickness = [80, 50, 25, 10, 0.16]
_2DIC_24mm_temperature  = [52.94, 52.89, 52.85, 52.82, 52.81]
_2DIC_17mm_temperature  = [54.38, 54.46, 54.38, 54.33, 54.31]
plt.plot(thickness, _2DIC_24mm_temperature, 'bs-', alpha=0.5, linewidth=1, label='2DIC_24mm')
plt.plot(thickness, _2DIC_17mm_temperature, 'bo-', alpha=0.5, linewidth=1, label='2DIC_17mm')

fontdict1 = {"size": 17, "color": "k"}
ax.set_xlabel("Die thickness (µm)", fontdict=fontdict1)
ax.set_ylabel("Peak Temperature (°C)", fontdict=fontdict1)
plt.legend()
plt.savefig('plt_PowerC-100um.png', dpi=900, bbox_inches='tight')