

def lengthOfLongestSubstring(str):
    ans=0
    #str=s
    if len(str) <= 1:
        return len(str)
    n=len(str)
    myset = set();
    j=0
    i=0
    while i < n:
        char1 = str[i]
        if char1 in myset:
            j=removeFromSet(myset,str,char1,j,i)
        myset.add(char1)
        curLength= len(myset)
        if curLength > ans:
            ans=curLength
        i=i+1
    #print("ans" + str(ans))
    return ans
            
 
def removeFromSet(set,arr,ele,prevIndex,arrLength):
     i =prevIndex
     while i <arrLength:
         char = arr[i];
         set.remove(char) 
         if char == ele:
             return i +1
         i=i+1
             
str = "abcabcbb"
print( str)
print(lengthOfLongestSubstring(str))  
print(lengthOfLongestSubstring("bbb"))  
print(lengthOfLongestSubstring("bbaabbcc"))  
              