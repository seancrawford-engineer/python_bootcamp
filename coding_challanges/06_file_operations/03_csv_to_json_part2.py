# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
import json
file = open('csv_file.txt','r')
file_contents = [line.strip() for line in file.readlines()]
file.close()
# - process data and convert them into a single JSON object
file_data = []
for line in file_contents:
    line_data = line.split(',')
    club = line_data[0]
    country = line_data[2]
    city = line_data[1]
    line_dict = {"club": club, "country": country, "city": city}
    file_data.append(line_dict)
# - store the JSON object into json_file.txt
file = open('json_file.txt', 'w')
json.dump(file_data,file)
file.close()