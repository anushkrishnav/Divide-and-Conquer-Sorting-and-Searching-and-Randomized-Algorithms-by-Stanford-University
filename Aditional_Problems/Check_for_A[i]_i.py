#Author @anushkrishna
#Problem statement
'''You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero. You want to decide whether or not there is an index i such that A[i] = i. Design the fastest algorithm that you can for solving this problem.'''
class Find_i():
    def __init__(self,arr):
        self.arr=sorted(arr)
        self.n=len(arr)
    def BruteForce(self):
        '''Time Complexity: O(n)'''
        for i in range(self.n):
            if arr[i] is i:
                return i
        return "No such value"
    def BinarySearch(self):
        return self.Bsearch(arr,0,len(arr))
    def Bsearch(self,arr,low,high):
        if high-low==1:
            return "Value doesnt exist"
        if high >= low:
            mid=(low+high)//2
        if mid is arr[mid]:
            return mid
        if mid>arr[mid]:
            return self.Bsearch(arr,low,(mid-1))

        else:
            return self.Bsearch(arr,(mid),high)
if __name__ == "__main__":
    arr=[1,2,3,4,5,6]
    f=Find_i(arr)
    print(f.BinarySearch())