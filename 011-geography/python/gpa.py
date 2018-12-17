import geopandas
import folium
import folium.plugins as plugins

geo_path = '/tmp/regional-soils-a-xrf.geojson'
rows = []
popups = []

def latlong(row):
  rows.append([row.geometry.y, row.geometry.x])
  popups.append("Fe2 O3: %lf" % row.Fe2O3)

gdf = geopandas.GeoDataFrame.from_file(geo_path).to_crs(epsg='4326')
gdf.apply(latlong, axis=1)

ice_map = folium.Map(location=[55, -6],
  tiles='cartodbpositron', zoom_start=10)
ice_map.add_children(plugins.MarkerCluster(locations=rows, popups=popups))
ice_map.save('soils.html')
