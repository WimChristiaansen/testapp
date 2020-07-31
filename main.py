#own code import
from coordinates import address_to_coordinates
from loadtile import loading_tile
from checkboundaries import check_bounds
from API import get_polygon
from server import MyHttpRequestHandler
import requests
#import of external library functions
import rasterio as rio
from rasterio.mask import mask
import plotly.graph_objects as go



#Check for address coordinates
address = str(input("Give an address in Flanders: "))
x, y = address_to_coordinates(address)
print(str(x) + " " + str(y) + " are the coordinates for your address.")

#Check boundaries dictionairy for right tile
tile_number = check_bounds(x, y)
print("Your address is on tile number " + str(tile_number))

#load dsm and dtm tiles, calculating and writing chm
tile = requests.get("http://localhost:3000/tile_" + str(tile_number) + ".tif", stream=True)
dsm = rio.open(tile)
#get polygon from API
pg = get_polygon(address)
print(pg)

#mask dataset with polygon shape
crop_img, crop_transform = mask(dataset=dsm, shapes=pg, crop=True, indexes=1, nodata=0, filled=True)
print(crop_img)

#visualize data
fig = go.Figure(data=[go.Surface(z=crop_img)])

fig.update_layout(title='CHM', autosize=True)

fig.show()


