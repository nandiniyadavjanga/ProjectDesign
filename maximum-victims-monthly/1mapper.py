#This file is to map the columns
input = open("accidents_2017.csv", "r")
output = open("01.txt", "w")
count = 0

for line in input:
    datalist = line.strip().split(",")
    id, district,weekday, month, day, hour, partoftheday,mild, serious, victims, vehiclesinvolved = datalist
   #writing only required columns into the output file 
    output.write(month + "\t" + victims + "\n")



 
input.close()
output.close()

