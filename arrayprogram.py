arr=[10,20,30,40,50]
print(arr[0])
print(arr[-1])
print(arr[-2])


brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)



add=['a','b','c']
add.append('d')
print(add)



colors=["violet","indigo","blue","green","yellow","orange","red"]
del colors[4]
colors.remove("blue")
colors.pop(3)
print (colors)



fruits=["apple","banana","mango","grapes","orange"]
fruits[1]="pineapple"
fruits[-1]="guava"
print (fruits)



concat = [1, 2, 3]
a=concat + [4,5,6]
print(a)



repeat=["a"]
repeat=repeat*5
print(repeat)



fruits=["apple","banana","mango","grapes","orange"]
print(fruits[1:4])
print(fruits[ :3])
print(fruits[-4: ])
print(fruits[-3:-1])