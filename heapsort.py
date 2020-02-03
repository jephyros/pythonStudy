
# -*- coding: utf-8 -*- 

def heapsort(data):
    #MaxHeap만들기
    for i in range(int((len(data)-1)/2),-1,-1):        
        max_Heapfiy(data,i,len(data))
    #Downheap 으로 정렬
    #print(f'{0:d} : {data}')
    for i in range(len(data)-1,-1,-1):    
        swap(data,0,i)
        max_Heapfiy(data,0,i)
        #print(str(i) + ":"+ ' '.join(data))
        #print(f'{i:d} : {data}')
        

    

def swap(data,x,y):
    tmp = data[x]
    data[x] = data[y]
    data[y] = tmp

def max_Heapfiy(data,n,heaplength):
    length = heaplength
    leftchild = n*2 + 1 
    rightchild = n*2 + 2
    #자식노드가없으면
    if((length-1) < leftchild):        
        return
        #left child 만 존재하면     
    elif((length-1) == leftchild):
        if(data[n] < data[leftchild]):
            swap(data,n,leftchild)        
    else:
        maxchild = 0
        if(data[leftchild]>data[rightchild]):
            maxchild = leftchild
        else:
            maxchild = rightchild
        
        if(data[n] < data[maxchild]):
            swap(data,n,maxchild)    
            max_Heapfiy(data,maxchild,heaplength)



data_list = [5,4,3,2,1,6]
#data_list = [1,2,3,4]
# for i in range(input()):
#     data_list.append(int(input()))

heapsort(data_list)
print(data_list)


