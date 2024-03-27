#program 1
list1=[10,501,22,37,100,999,87,351]
odd_num=[]
even_num=[]
for num in list1:
    if num % 2==1:
        odd_num.append(num)
    else:
        num % 2==0,
        even_num.append(num)
print("all even numbers:",even_num)
print("all odd numbers:",odd_num)

#program 2
list2=[10,501,22,37,100,999,87,351]
def prime_num(num):
    if num <=1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in list2 if prime_num(num)]

print("Prime numbers:", prime_numbers)


