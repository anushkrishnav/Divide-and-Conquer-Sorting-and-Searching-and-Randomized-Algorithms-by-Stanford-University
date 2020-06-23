import time
def mergesort(values):
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = mergesort(left) 
        right = mergesort(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]:
                values.append(left[0])
                left.pop(0) 
            else: 
                values.append(right[0])
                right.pop(0) 
  
        for i in left: 
            values.append(i)
        for i in right: 
            values.append(i) 
    return values 

def main():
    list1=[5,4,1,8,7,2,6,3]
    print('unsorted set \n',list1)
    print('sorted set \n ',mergesort(list1))

if __name__ == "__main__":
    main()