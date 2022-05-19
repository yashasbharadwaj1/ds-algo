
class Solution:
    def longestCommonPrefix(self, arr, n):
        
        if(n==0):
            return -1
        if(n==1):
            return arr[0] 
        arr.sort()
        end=min(len(arr[0]),len(arr[n-1]))
        i=0
        if arr[0][0] != arr[n-1][0]:
            return -1
            
                   
        while(i<end and arr[0][i] == arr[n-1][i]):
            i+=1 
        prefix = arr[0][0:i]
        return prefix
        
         



if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))

 
