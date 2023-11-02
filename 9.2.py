x = int(input("Введите число: "))
a = []
for n in range(1,x+1):
  if [n% i for i in range(1, n)].count(0) == 1:
    a += [n]
print(f"Ваши простые числа от 1 до {n}:", ",".join(list(map(str, a))))
#Рекурсией:
# def prost(n):
#   if n == 2:
#     return [n]
#   else:
#     new_lst = prost(n - 1)
#     if [n% i for i in range(1, n)].count(0) == 1:
#         new_lst.append(n)
#     return  new_lst 
# print(prost(int(input("Введите число: "))))
