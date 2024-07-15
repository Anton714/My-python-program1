# 1st program
print(9**0.5*5)
# 2nd program
print(9.99>9.98 and 1000 != 1000.1)
# 3rd program
print(1234//10%100+5678//10%100)
# 4th program v1
print(int(13.42*100//100)==int(42.13%42*100) or int(13.42%13*100+0.1)==int(42.13*100//100))
# 4th program v2
A=13.42
B=42.13
C=int(str(A)[0:2])
print(C)             # удалить строку / для контроля
D=int(str(A)[3:5])
print(D)             # удалить строку / для контроля
E=int(str(B)[0:2])
print(E)             # удалить строку / для контроля
F=int(str(B)[3:5])
print(F)             # удалить строку / для контроля
print(C==F or D==E)