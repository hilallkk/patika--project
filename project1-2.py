#-------------1
liste1=[[1, 2], [3, 4], [5, 6, 7]]

def reverse(x):
 x=x[::-1]
 x = [i[::-1] for i in x]
 
 
 return x

#liste1=[[1, 2], [3, 4], [5, 6, 7]]


print(reverse(liste1))



#----------------2
x= [[1,2],[3,4],[5,6,7]]
x=x[::-1]
x=[i[::-1] for i in x]
print(x)
