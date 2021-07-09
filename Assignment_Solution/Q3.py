Q3 = """Return Palindromic  string"""

def longestPalin(S):
    palindrome=[]
    # Get total lenght of string
    n = len(S)
     
    # All subStrings of length 1
    # are palindromes
    maxLength = 1
    start = 0

    # Nested loop to mark start
    # and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1
             
            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (S[i + k] != S[j - k]):
                    flag = 0
 
            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1

    for i in range(start, start+maxLength):
        myStr = S[i]
        palindrome.append(myStr)

    return ''.join(palindrome)
   
def timeComplexity():
        """Time complexity: O(n^3).Three nested loops are needed to find the longest 
        palindromic substring in this approach, so the time complexity is O(n^3)."""


if __name__ =="__main__":
    string = "israar"
    print(longestPalin(string))