import random
dice=[1,2,3,4,5,6]
d1=random.choice(dice)
d2=random.choice(dice)
d3=random.choice(dice)
d4=random.choice(dice)
d5=random.choice(dice)
dicelist=[d1,d2,d3,d4,d5]
print(dicelist)
num_lim=int(0)

while num_lim<4:
  a,b,c,d,e=map(int,input("킵할 주사위를 1, 굴릴 주사위를 0으로 ','를 이용해 구분하여 나타내시오").split(','))
  if a==0:
    dicelist[0]=random.choice(dice)
  if b==0:
    dicelist[1]=random.choice(dice)
  if c==0:
    dicelist[2]=random.choice(dice)
  if d==0:
    dicelist[3]=random.choice(dice)
  if e==0:
    dicelist[4]=random.choice(dice)
  print(dicelist)
  num_lim+=1
  if num_lim==4:
    print("턴을 넘겼습니다!")
  if a==1 and b==1 and c==1 and d==1 and e==1:
    str_a=input("{}으로 결정하시겠습니까?".format(dicelist))
    if str_a=="예":
      print("{}으로 결정되었습니다.".format(dicelist))
      num_lim+=4