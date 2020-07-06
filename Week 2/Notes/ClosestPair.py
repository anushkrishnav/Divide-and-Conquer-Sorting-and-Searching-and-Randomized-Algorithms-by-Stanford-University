class ClosestPair():
    def __init__(self,P=[]):
        self.Points=P
        self.Px=sorted(P, key=lambda x: x[0])
        self.Py=sorted(P, key=lambda x: x[1])
    def MergeSort(self,cons='x'):
        array=self.Sort(self.Points,cons)
        return array
    def Sort(self,Points,cons):
        if len(Points) <= 1:
            return Points
        med=len(Points)//2
        left=self.Sort(Points[:med],cons)
        right=self.Sort(Points[med:],cons)
        return self.Merge(left,right,cons)
                
    def Merge(self,left,right,cons):
        l=1
        if cons=='x':
            l=0
        sorte=[]
        i,j,=0,0
        while i < len(left) and j<len(right):
            if left[i][l] <= right[j][l]:
                sorte.append(left[i])
                i+=1
            else:
                sorte.append(right[j])
                j+=1
        while i < len(left):
            sorte.append(left[i])
            i += 1
        while j < len(right):
            sorte.append(right[j])
            j += 1
        return sorte 
    def CountSplitPair(self):
        pass
if __name__ == "__main__":
    P=[[1,2],[7,9],[3,4],[5,6],[4,7]]
    sort=ClosestPair(P)
    print(sort.MergeSort())
    sort.prin()