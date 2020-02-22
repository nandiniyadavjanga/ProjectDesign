#to find the maximum accident victims in each month
s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0
#ctr = 0

for line in s:
  data = line.strip().split('\t')
  month, victims = data

  if month != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    

    # start over when changing keys
    thisKey = month 
    thisValue = 0.0
    
  
  # apply the aggregation function
  if(float(victims)>float(thisValue)):
      thisValue =float(victims)


# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
