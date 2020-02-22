#this file is used to find the sum of accident victims each part of the day
s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
  data = line.strip().split('\t')
  district, victims = data

  if district != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = district 
    thisValue = 0
  
  # apply the aggregation function
  thisValue += int(victims)

# output the final entry when done
#print(thisKey + '\t' + str(thisValue)+'\n')
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
