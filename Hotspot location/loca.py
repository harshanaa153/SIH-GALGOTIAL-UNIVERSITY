import pandas as pd
from opencage.geocoder import OpenCageGeocode
key = "278442d22a4f4c3988607be868b454ac"
geocoder = OpenCageGeocode(key)

addresses_df = pd.read_excel("Addresses.xlsx")

addresses = addresses_df["Addresses"].values.tolist()

latitudes = []
longitudes = []

for address in addresses:
	result = geocoder.geocode(address, no_annotations="1")

	if result and len(result):
		longitude = result[0]['geometry']['lng']
		latitude = result[0]['geometry']['lat']
	else:
		longitude = "N/A"
		latitude = "N/A"

	latitudes.append(latitude)
	longitudes.append(longitude)

addresses_df["latitudes"] = latitudes
addresses_df["longitudes"] = longitudes

addresses_df.to_excel("Addresses_Geocoded.xlsx")
