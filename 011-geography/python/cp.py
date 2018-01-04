import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from owslib.wms import WebMapService

ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
ax.coastlines()

ax.add_wms(wms='http://vmap0.tiles.osgeo.org/wms/vmap0',
           layers=['basic'])

plt.show()
