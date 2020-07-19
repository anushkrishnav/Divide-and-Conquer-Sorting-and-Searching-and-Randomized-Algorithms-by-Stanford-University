class QuickSort():
    def __init__(self,arr):
        self.arr=arr
        self.L=0
        self.high=int(len(arr)-1)
    def QuickSort(self):
        a,l,h=self.arr,self.L,self.high
        return self.quickSort(a,l,h)
    def partition(self,arr,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low , high): 
    
            # If current element is smaller than the pivot 
            if   arr[j] < pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
    
    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low  --> Starting index, 
    # high  --> Ending index 
    # Function to do Quick sort 
    def quickSort(self,array,low,high): 
        if low < high: 
    
            # pi is partitioning index, array[p] is now 
            # at right place 
            pi = self.partition(array,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(array, low, pi-1) 
            self.quickSort(array, pi+1, high)
            return array 

a=QuickSort([2,1,5,4,3])
print(a.QuickSort())