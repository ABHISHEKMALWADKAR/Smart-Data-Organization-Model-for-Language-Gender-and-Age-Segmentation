import csv
from ipyleaflet import Map, Marker, Polyline
from IPython.display import display

# Create map
m = Map(center=(0, 0), zoom=2)

# Read locations from CSV (latitude,longitude per line)
locations = []
with open("D:\\PYTHON\\SOFTWARE DEVELOPMENT\\Final project\\Sorted data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        lat, lon = map(float, row)
        locations.append((lat, lon))

# Add markers for each location
for lat, lon in locations:
    marker = Marker(location=(lat, lon))
    m.add_layer(marker)

# Optionally, add a polyline connecting the points
if locations:
    polyline = Polyline(locations=locations, color="blue", fill=False)
    m.add_layer(polyline)

display(m)