num1 = 19
num2 = 5
num3 =  17

ans = (num1 % num2) + num3
print(ans)

str1 = "ThisIsMoonjang"
str2 = "InhaUnivLIONS"

print(str1[1:3] * 2 + str2[8:14])

animals = {'조류' : 'duck' , '파충류' : 'turtle' , '어류' : 'fish'}
animals['포유류'] = 'cat'
cute = animals.get('포유류')
print(cute) 

fruits = {'사과' : 'Apple', '바나나': "Banana", "체리" : 'Cherry', '딸기' : 'Strawberry'}
print(fruits)
del fruits['사과']
del fruits['바나나']
del fruits['체리']
del fruits['딸기']
print(fruits)