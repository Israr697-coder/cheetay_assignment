Q2 = """form the largest number possible from the given list"""

def printLargest(arr):
      
    # extended is a empty list for extended list 
    # resultString for calculating our final string
    extended=[] 
    resultString=""
      
    # calculating the length of largest number from given and add 1 for further operation
    l = len(str(max(arr))) + 1
    # print(l)
      
    # iterate given values and 
    # calculating extended values
    for i in arr:
        temp = str(i) * l
          
        # make tuple of extended value and equivalant original value then 
        # append to list
        # print(temp[:l:],i)
        extended.append((temp[:l:], i))
      
    # sort extval in descending order
    extended.sort(reverse = True)
      
    # iterate extended values
    for i in extended:  
        # concatinate original value equivalant
        # to extended value into ans variable
        resultString += str(i[1])
  
    if int(resultString)==0:
        return "0"
    return resultString
  
if __name__== "__main__":
    a = [2,34,53]
    
    print(printLargest(a))
  