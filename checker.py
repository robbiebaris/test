from datetime import datetime

def getTime(array1, array2):
  sec = array2[0] - array1[0]
  ms = array2[1] - array1[1]

  return "Total seconds is: " + str(sec) + " Total microseconds is: " + str(ms)

def input2(array, check):
   getTimeA = [datetime.now().second, datetime.now().microsecond]
   for i, v in enumerate(array):
     if (v == check):
       print "Index of " + str(v) + " is: " + str(i)
       getTimeB = [datetime.now().second, datetime.now().microsecond]
  
       return getTime(getTimeA, getTimeB)
  
   getTimeB = [datetime.now().second, datetime.now().microsecond]

   return getTime(getTimeA, getTimeB)