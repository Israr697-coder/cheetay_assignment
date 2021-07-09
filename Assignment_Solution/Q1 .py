MAX=256
  
# Function to return the lexicographically
# smallest after swapping all the
# occurrences of any two characters
def chooseandswap(A):
    A=[i for i in string]
    n = len(A)
    i, j=0,0
    # To store the first index of
    # every character of str
    chk=[0 for i in range(MAX)]
    for i in range(MAX):
        chk[i] = -1
  
    # Store the first occurring
    # index every character
    for i in range(n):
  
        # If current character is appearing
        # for the first time in str
        if (chk[ord(A[i])] == -1):
            chk[ord(A[i])] = i
  
    # Starting from the leftmost character
    for  i in range(n):
        flag = False
  
        # For every character smaller than ord(str[i])
        for j in range(ord(A[i])):
  
            # If there is a character in str which is
            # smaller than ord(str[i]) and appears after it
            if (chk[j] > chk[ord(A[i])]):
                flag = True
                break
  
  
        # If the required character pair is found
        if (flag):
            break
  
    # If swapping is possible
    if (i < n):
  
        # Characters to be swapped
        ch1 = (A[i])
        ch2 = chr(j)
  
        # For every character
        for i in range(n):
  
            # Replace every ch1 with ch2
            # and every ch2 with ch1
            if (A[i] == ch1):
                A[i] = ch2
  
            elif (A[i] == ch2):
                A[i] = ch1
  
    return "".join(A)
  

if __name__== "__main__":
    string = "effg"
    print(chooseandswap(string))