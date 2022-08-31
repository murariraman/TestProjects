# # # # # # # 2 time revision here

# # # # # # # all fundamental data types like int float double complex string are immutable

# # # # # # #x=257
# # # # # # #y=257

# # # # # # #print(x is y)

# # # # # # # x=[10,20,30,40,35]
# # # # # # # b=bytes(x)
# # # # # # # print(b)

# # # # # # # for number in b:
# # # # # # #     print(number)


# # # # # # # bytearray

# # # # # # # listone=[10,20,30,40,50]
# # # # # # # newbytes=bytes(listone)
# # # # # # # print((bytes(listone)))
# # # # # # # for number in bytes(listone):

# # # # # # #     print(number)

# # # # # # # # item assignment is not supported on bytes 

# # # # # # # newbytes[0]=55

# # # # # # # print(newbytes)



# # # # # # # bytearray is mutable where as bytes is not mutable 
# # # # # # # item assignment is supported in bytearray and not in bytes

# # # # # # # from traceback import print_tb


# # # # # # # listtwo=[22, 55, 45, 99]

# # # # # # # newbytearray=bytearray(listtwo)

# # # # # # # for number in newbytearray:
# # # # # # #     print(number)

# # # # # # # newbytearray[2]=199
# # # # # # # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# # # # # # # for numberone in newbytearray:
# # # # # # #     print(numberone)

# # # # # # # compulsory the value should be between 0 to 256

# # # # # # listone=[]

# # # # # # print(type(listone))

# # # # # # listone.append(10)
# # # # # # listone.append(20)
# # # # # # listone.append(30)
# # # # # # listone.append(40)
# # # # # # listone.append(50)
# # # # # # listone.append('tara')
# # # # # # listone.append('sitara')
# # # # # # print(listone)

# # # # # # print(listone[-1])
# # # # # # print(listone[0])

# # # # # # # performing the slicing operator

# # # # # # print(listone[1:5])

# # # # # # # performing the negative indexing
# # # # # # print('NEGATIVE INDEX here')

# # # # # # print(listone[-5:-1:1])


# # # # # # defining the tuple data here
# # # # # # list is mutable while tuple is immutable 

# # # # # # from traceback import print_tb


# # # # # # t=(10,20,30,40,50)
# # # # # # print(type(t))

# # # # # # print(t[1:5:2])

# # # # # # # indexing is not supported in tuple

# # # # # # newtuple=12,20,10,33,55,23,'sona','mona', 'lona'

# # # # # # print(type(newtuple))

# # # # # # # tuple does not support indexing 

# # # # # # #newtuple[2]='gautam' # tuple does not support item assignment

# # # # # # print(newtuple)

# # # # # # print(newtuple)

# # # # # # tuple2=('raman', 'suman', 11,23, ['kumar', 'sonu', 11, 23, 45, 11], 'sunny')
# # # # # # print(tuple2)
# # # # # # print(tuple2[4])

# # # # # # defining range data type here

# # # # # r=range(10)

# # # # # print(r[0:10])

# # # # # for i in r:
# # # # #     print(i, end='  ')


# # # # # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# # # # # r[4]=444
# # # # # print(r[4])

# # # # # # item assignment is not supported in range data type

# # # # # defining the set data type here

# # # # # duplicates are not allowed, slicing and indexing is not supported 
# # # # # heterogeneous and growable in nature, represented by {}

# # # # # setone={'one', 'two', 'three', 'four', 'one'}

# # # # # setone.add('patna')
# # # # # setone.remove('two')

# # # # # print(type(setone))

# # # # # print(setone)

# # # # # set and forzen set

# # # # # forzen set is immutable while set is mutable(does not support slicing, indexing)

# # # # newsetone={'one', 'two', 'three', 'four', 'sonam'}

# # # # forzens=frozenset(newsetone)

# # # # print(forzens)

# # # # #forzens[0]=11 # does not support item assignment 

# # # # #print(forzens[0:6]) does not support subscriptable


# # # # whenever there is need of key value pair then we should always
# # # # go for dictionary data type

# # # d={}
# # # newd=()
# # # newdictionary=dict()
# # # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# # # print(type(newd))
# # # print(type(d))
# # # print(type(newdictionary))

# # # # dictionary is the most commonly used data types 

# # # ddatatype={'one': 'summer', 'two': 'winter', 'three':'autumn'}
# # # print(ddatatype)

# # # print(ddatatype['one'])

# # # ddatatype['one']=110

# # # for k,v in ddatatype.items():
# # #     print(k,v)

# # # # adding value with duplicate key then old value will be 
# # # # replaced with new value 

# # print('durga'*3)
# # print(3*'durga')


# # complexonel=complex(10,20)
# # complexone=complex(20,30)

# # print(complexonel+complexone)
# # print(10.1==10.10)
# # # logical operator are and or not
# # print(True and True)
# # print(True or True)
# #print(1 | 10/0)

# print(4 & 5)

# print(4 >> 5)
# print(~4)
# print(~True)
# print(10>>2)

# compound assignment operator is supported in python but increment, decrement 
# is not supported in python


# compound assignment operators = +=, -=, *=, ^=, >>=, <<=

# ternary operator is not available in python here

# two special operators have been defined in python and they are identity operator
# membership operator 


