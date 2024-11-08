k = int(input("Количество дней: ")) 
a = float(input("Расстояние:"))
a_k=a
i = 2
for i in range(1, k):
    a_k += a_k * 0.10
print(a_k) 





