# a=[1,2,3]
# b=a
# b.append(4)
# print(a)

# t = (1, 2, [3, 4])
# t[2].append(5)
# print(t)


    # l1=[]

    # for i in range(1,5):
    #     l1.append(int(input("Enter the number:")))

    # def remove_duplicates(l1):
        
    # l2=[]
    # for i in l1:
    #     if i not in l2:
    #         l2.append(i) 
                
    # return l2


    # l3=remove_duplicates(l1)

    # print(l3)
    
# scores = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]

# for name, score in scores:
#     print(f"({name},{score})")


# numbers=[]

# for i in range(1,6):
#     numbers.append(i)
    
# def analyze_number(numbers):
    
#     min=numbers[0]
#     max=numbers[0]
#     sum=0
    
#     for i in numbers:
#         sum=sum+i
        
#         if i<min:
#             min=i
        
#         if i>max:
#             max=i
            
#     avg=sum/len(numbers)
    
#     return min,max,avg

# min,max,avg=analyze_number(numbers)

# print(f"min:{min}, max:{max}, avg:{avg}")


# if 32 > 1:
#     print('inside')
# print('outside')

# flag = 6 > 5
# print(type(flag))

# x = 30
# y = x
# x = 4
# y=x
# print(y)


name="Rohit"
age=25
percentage=90

print(type(name))
print(type(age))
print(type(percentage))


age=int(input("Enter the age:"))

print(age+5)


num=[25,40,18,67,32]

minimun=min(num)
print(minimun)

maximum=max(num)
print(maximum)

total_sum=sum(num)
print(total_sum)

num1=25
print(num1,type(num1))

num2=30.5
print(num2,type(num2))


str="Om Gandhewar"
print(len(str))

num=-125
print(abs(num))


num=78.4567
print(round(num,2))
