list1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list_flatten=[]

def flattenList(list1):
    for i in list1:
        if isinstance(i, list):
            flattenList(i)
        else :
            list_flatten.append(i)
            
flattenList(list1)
print(list_flatten)
