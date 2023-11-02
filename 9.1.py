a, b = int(input("Введите 1 число: ")), int(input("Введите 2 число: "))
if a == 0 or b == 0:
  print(0)
else:
  for i in range(1, a*b+1):
    if i % a == 0 and i % b == 0:
      print(f"Ваше НОК = {i}")
      break
#это работает, но когда большое число прога думала 10 минут и ничего, в чем прикол.
