from loadtile import loading_tile
import rasterio as rio

boundaries_dsm = {}

for i in range(1, 39294):
    z = loading_tile(i, 'DSM')
    boundaries_dsm[i] = z.rio.bounds()
    print(str(i) + "\n")

with open('bounds_full2.csv', 'w') as f:
    for key in boundaries_dsm.keys():
        f.write("%s,%s\n"%(key,boundaries_dsm[key]))
