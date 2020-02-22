s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
  data = line.strip().split('\t')
  partoftheday, victims = data

  if partoftheday != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = partoftheday 
    thisValue = 0
  
  # apply the aggregation function
  thisValue += int(victims)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
