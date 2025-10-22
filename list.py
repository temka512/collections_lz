N=int(input('Здравствуйте! Введите число N:'))
spisok=[0,1]
i=0
k=0
sum=0
while i < (N-2):
  spisok.append(spisok[i]+spisok[i+1])
  i+=1
print('Исходный список:')
print(spisok)
i=0
min=spisok[0]
max=spisok[0]
while i <= (N-1): 
  #print(spisok)
  #print(i)
  if i%2 == 0:
    spisok[i]=spisok[i]*2
  else:
    spisok[i]=spisok[i]**2
  if min >= spisok[i]:
    min=spisok[i]
  if max <= spisok[i]:
    max=spisok[i]
  sum+=spisok[i]
  i+=1
srednee=sum/N
print('Изменённый список:')
print(spisok)
i=0
while i <= (N-1): 
  if spisok[i] > srednee:
    k+=1
  i+=1
print('Минимальный элемент:', min)
print('Максимальный элемент:', max)
print('Длина списка:', len(spisok))
print('Кол-во элементов, большее медианного значения списка:', k)
