import string
input=open('input.txt','r')
output=open('output.txt','w')
L=input.read().split()
def bsort(L):
    for j in range(len(L)-1):
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                temp=L[i]
                L[i]=L[i+1]
                L[i+1]=temp
    return L
L=bsort(L)
output.write(' '.join(L))
output.close()
print 'test'
