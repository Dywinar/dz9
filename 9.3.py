n = int(input("Введите число: "))
a = []
for i in range(1, n+1):
  if n % i == 0:
    a +=[i]
print(f"Список делителей числа {n}:", ",".join(list(map(str, a))))
