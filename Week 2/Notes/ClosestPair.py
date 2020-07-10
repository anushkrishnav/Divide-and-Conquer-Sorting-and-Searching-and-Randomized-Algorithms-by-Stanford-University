import math
class Points():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class ClosestPair():
    def __init__(self,P):
        self.Points=P
        self.pt=None
    @staticmethod
    def Distance(p1,p2):
        return math.sqrt((p1.x-p2.y)*(p1.x-p2.y)+(p1.y-p2.x)*(p1.y-p2.x))
    def BruteForce(self,P):
        n=len(P)
        minival=float('inf')
        for i in range(n):
            for j in range(i+1,n):
                if self.Distance(self.Points[i],self.Points[j])<minival:
                    minival=self.Distance(self.Points[i],self.Points[j])
                    self.pt=((self.Points[i].x,self.Points[i].y),(self.Points[j].x,self.Points[j].y))
            return minival
    def StripClosest(self,strip,size,d):
        mini_val=d
        strip.sort(key=lambda point:point.y)
        for i in range(size):
            j=i+1
            while j<size and (strip[j].y-strip[i].y)<mini_val:
                mini_val=self.Distance(strip[i],strip[j])
                j+=1
        return mini_val
    def ClosestUtil(self,P):
        n=len(P)
        if n<=3:
            return self.BruteForce(P)
        mid=n//2
        midpt=P[mid]
        dleft=self.ClosestUtil(P[:mid])
        dright=self.ClosestUtil(P[mid:])
        d=min(dleft,dright)
        strip=[]
        for i in range(n):
            if abs(P[i].x-midpt.x)<d:
                strip.append(P[i])
        return min(d,self.StripClosest(strip,len(strip),d))
    def closest(self):
        P=self.Points
        P.sort(key=lambda point:point.x)
        return self.ClosestUtil(P)
    def ClosestPoints(self):
        distan=self.closest()
        return self.pt
if __name__ == "__main__":
    P=[Points(1,2),Points(7,9),Points(4,9),Points(9,6),Points(5,4)]
    a=ClosestPair(P)
    print("The closest pair of points is "+str(a.ClosestPoints()))
    print("And the distance between them is " + str(a.closest())+" units")