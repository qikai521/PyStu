show = filter(lambda x:x%2,range(10))

print(list(filter(lambda x:not(x%3),range(1,100))))

print(list(map(lambda x,y :[x,y] ,[1,3,5],[2,4,6])))