import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error fetching ISS location data")
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    return latitude, longitude

def iss_map():
    lat, lon = iss_location()

    plt.figure(figsize=(8, 6))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='lightgray', lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')

    x, y = m(lon, lat)
    m.plot(x, y, 'ro', markersize=10)
    plt.text(x, y, 'ISS', fontsize=12, ha='left', va='bottom', color='red')

    plt.title('Current Location of the ISS')
    plt.show()

iss_map()
