import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def plotMap():    
    proj = ccrs.Robinson(
)

    fig, ax = plt.subplots(subplot_kw=dict(projection=proj), figsize=(12,12))

    ax.set_extent([-180 ,180, -90, 90], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.LAND, facecolor='0.3')
#    ax.add_feature(cfeature.LAKES, alpha=0.9)  
#    ax.add_feature(cfeature.BORDERS, zorder=10)
    ax.add_feature(cfeature.COASTLINE, zorder=10)

#    states_provinces = cfeature.NaturalEarthFeature(
#            category='cultural',  name='admin_1_states_provinces_lines',
#            scale='50m', facecolor='none')
#    ax.add_feature(states_provinces, edgecolor='black', zorder=10)   

    gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth=2, color='black', alpha=0.5, linestyle='--', draw_labels=True)
    gl.top_labels =True 
    gl.left_labels =True 
    gl.right_labels=True
    gl.xlines =True 
    gl.xlocator = mticker.FixedLocator([-180, -120, -60, 0, 60, 120, 180])
    gl.ylocator = mticker.FixedLocator([-90, -60, -30, 0, 30, 60, 90])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    plt.savefig("plot.png")
plotMap()
