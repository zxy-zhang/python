cars=['bwm','audu','toyota','subaru']
cars.sort()
print(cars)                #永久性排序

cars=['bwm','audu','toyota','subaru']
cars.sort(reverse=True)
print(cars)                #按字母顺序相反的顺序排列，同样的也是永久性排序

cars=['bwm','audu','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list：")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)              #使用sorted()对列表进行临时排序

cars=['bwm','audu','toyota','subaru']
print(cars)
cars.reverse()
print(cars)              #倒着打印排序（反转列表元素）
