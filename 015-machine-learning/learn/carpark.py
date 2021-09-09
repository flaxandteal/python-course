#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find the closest carparks to the Computer Science building

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
@license: MIT
"""

import pandas
from sklearn.neighbors import NearestNeighbors

import utils

def closest_carpark(gdf, target):
    X = []
    def extract_points(row):
        X.append([row.geometry.y, row.geometry.x])
        
    gdf.apply(extract_points, axis=1)
    nbrs = NearestNeighbors(n_neighbors=4).fit(X)
    
    Y = [target]
    # This maps multiple targets at once efficiently, but we just need one
    distances_per_Y_row, row_numbers_per_Y_row = nbrs.kneighbors(Y)
    
    distances = distances_per_Y_row[0]
    row_numbers = row_numbers_per_Y_row[0]
    
    # Report distance as a comparison
    reference_distance = distances[0]
    # Why are there two zeroes below? What happens if Y has multiple entries?
    for distance, row_i in zip(distances, row_numbers):
        relative_distance = 100 * (distance / reference_distance - 1)
        row = gdf.iloc[row_i]
        print(row['NAME'], " is ", relative_distance, "percent further than the closest")

        
def run():
    # Load data into variable called "df"
    df = pandas.read_csv('car-park-locations-data.csv', encoding='latin1')
    
    # Because why not?
    # print(df.describe())
    
    # Get a geopandas dataframe, from a normal pandas one
    # gdf = utils.to_geo_dataframe(df)
    
    # Create a plot
    # utils.plot_gdf("output.html", gdf)
    
    # CompSci Building 54.5817428 -5.9374874
    closest_carpark(gdf, [54.5817428, -5.9374874])
    
if __name__ == "__main__":
    run()