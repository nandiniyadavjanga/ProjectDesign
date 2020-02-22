#this file is to find the average of accidents occuring in each month
s = open("02.txt","r")
r = open("03.txt", "w")

counter = 0
thiskey = ""
thisvalue = 0

#splitting the data with tabspace
for line in s:
  data = line.strip().split('\t')
  month, victims = data

  if thiskey == "":
    if month:
      thiskey = month

  # apply the aggregation function
  
  if month == thiskey:
    thisvalue = thisvalue + int(victims)
    counter = counter + 1
   
  else:
    r.write( thiskey + '\t' + str(thisvalue/counter)+'\n')
    
# start over when changing keys
    thiskey = month
    thisvalue = float(victims)
    counter = 1

  # output final entry

r.write( thiskey + '\t' + str(thisvalue/counter)+'\n')

s.close()

r.close()



    