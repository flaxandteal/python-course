import geopandas
import folium
from shapely.geometry import Point

def to_geo_dataframe(df):
    """Turn a carpark DataFrame into a GeoDataFrame."""
    
    geometry = [Point(row['LONGITUDE'], row['LATITUDE']) for index, row in df.iterrows()]

    gdf = geopandas.GeoDataFrame(df, geometry=geometry)
    gdf.crs = {'init': 'epsg:4326'}
    
    return gdf


def plot_gdf(filename, gdf):
    """Save an interactive map plot."""
    
    map = folium.Map(
        location=[54.6, -5.90],
        zoom_start=10
    )
    carparks = folium.features.GeoJson(gdf)
    map.add_children(carparks)
    map.save(filename)