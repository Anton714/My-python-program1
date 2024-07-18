#task 1

print("Введите любую строку:  ")
print('например: "Самолет" или "Топинамбур" ' )
example=input()

#task 2
print(example[0])

#task 3
print(example[-1])

#task 4
s = len(example)

if s % 2 != 0:
    s=s+1

w = s / 2
if w == 2:
    w=w-1

if w % 2 == 0:
    w = w+1

w=int(w)
r=(example[::-1])
string1=(r[:w])
string2=(string1[::-1])
print(string2)

#task 5
print(example[::-1])

#task 6
print(example[1::2])
print('END')



