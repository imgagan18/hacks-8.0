import pandas as pd
import geopandas as gpd

def MakeStops(intersections_df, meters=800):
    '''
    INPUT: DataFrame returned from BlocksPerIntersection() function

    OUTPUT: DataFrame
    '''

    # Sort the DataFrame in order of descending population
    iPop_df = intersections_df[intersections_df.iPop > 0].sort_values('iPop', ascending=False)

    stops_indices = []
    served_populations = []
    
    while not iPop_df.empty:
        stop = iPop_df.iloc[0]
        idx = stop.name
        stops_indices.append(idx)
        
        # Identify the exclusion zone
        zone = stop.geometry.buffer(meters)
        
        # Calculate the total population served in the exclusion zone
        reach = iPop_df[iPop_df.geometry.intersects(zone)]['iPop'].sum()
        served_populations.append(reach)
        
        # Filter out intersections within the exclusion zone
        iPop_df = iPop_df[~iPop_df.geometry.intersects(zone)]

    stops_df = intersections_df.loc[stops_indices]
    stops_df['mergedPop'] = served_populations

    return stops_df

