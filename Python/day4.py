# import json
# a = '{"name": "Bikash", "age":"19"}'
# res = json.loads(a) #converting json to python objects
# print(res)
# print(type(res))

# print(json.dumps(res), type(json.dumps(res))) #converting python objects to json

# print (eval(a), type(eval(a))) #Converting json to python objects

# b = '[1,2,3,4]'
# print(eval(b))  #eval also convers json to list
# print(type(eval(b)))

#practising map
# def A(i):
#     i+=10
#     return i
# a = map(A, [1,2,3])
# print(list(a))

# b = map(lambda x:x+10, [5,9,6])
# print(list(b))

#convert li = ['abc', 'def', 'ghi'] to opt = [['a','b','c'], ['d','e','f'], ['g','h','i']]
# list1 = ['abc', 'def', 'ghi']
# a = [i for i in range (0,len(list1))]
# print(a)


#Q2. x = [5,10,15] and y = [3,6,9]  to opt = [8,16,24]


#Fucntion practices
# def test (*args, **kwargs):
#     print(args[0])
#     val = kwargs.get('a')
#     print(val)

# # test(**{'a':1})
# test(5,6,**{'a':1, 'b':2})

# def add (*args):
#     sum=0
#     for i in range (0,len(args)):
#         sum = sum + args[i]
#     print(sum)   
# add(1,2,3)


li = ['abc', 'def', 'ghi']
a = list(map(list,li))
print(a)
