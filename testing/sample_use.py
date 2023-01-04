import numpy as np
import pandas as pd
from pysheds.grid import Grid
import geopandas as gpd
from shapely import geometry, ops
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
sns.set_palette('husl')



grid = Grid.from_raster('elevation.tiff')
dem = grid.read_raster('elevation.tiff')

fig, ax = plt.subplots(figsize=(8,6))
plt.imshow(grid.dem, extent=grid.extent, cmap='cubehelix', zorder=1)
plt.colorbar(label='Elevation (m)')
plt.title('Digital elevation map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')