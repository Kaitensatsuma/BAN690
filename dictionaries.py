with open(txt,'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Location","Longitude","Latitude","Count"])
    for key, count in dict.items():
        location, lat, long = key
        writer.writerow([location,lat,long,count])
