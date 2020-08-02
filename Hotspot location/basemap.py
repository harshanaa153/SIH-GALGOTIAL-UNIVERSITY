import os
import conda
conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel(r'E:\SIH\Addresses_Geocoded.xlsx','Sheet1')

fig = plt.figure(figsize=(12,9))

m = Basemap(projection='mill', llcrnrlat=-90,  urcrnrlat=90, llcrnrlon=-180,  urcrnrlon = 180, resolution = 'c')

m.drawcoastlines()

m.drawparallels(np.arange(-90,90,10),labels=[True,False,False,False])
m.drawmeridians(np.arange(-180,180,30),labels=[0,0,0,1])

sites_lat_y = df['latitudes'].tolist()
sites_lon_x = df['longitudes'].tolist()

colors = ['green', 'darkblue', 'yellow', 'a', 'blue', 'orange']

m.scatter(sites_lon_x,sites_lat_y,latlon=True)
plt.title('Basemap tutorial', fontsize=20)

plt.show()
