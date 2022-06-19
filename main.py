#============================주사위 변수 무작위 선정============================
import random
dice=[1,2,3,4,5,6]
d1=random.choice(dice)
d2=random.choice(dice)
d3=random.choice(dice)
d4=random.choice(dice)
d5=random.choice(dice)
dicelist=[d1,d2,d3,d4,d5]
print("====================\n{}".format(dicelist))
num_lim=int(0)
allowlist=[]
allowlist_f=[]
choice=str()
#============================function============================
def once():
  if dicelist.count("1")>0:
    allowlist_f = allowlist.append("once")

def deuces():
  if dicelist.count("2")>0:
    allowlist_f = allowlist.append("deuces")

def threes():
  if dicelist.count("3")>0:
    allowlist_f = allowlist.append("threes")

def fours():
  if dicelist.count("4")>0:
    allowlist_f = allowlist.append("fours")

def fives():
  if dicelist.count("5")>0:
    allowlist_f = allowlist.append("fives")

def sixes():
  if dicelist.count("6")>0:
    allowlist_f = allowlist.append("sixes")

def chance():
  allowlist_f = allowlist.append("chance")

def four_of_a_kind():
  if dicelist.count("1")>4 or dicelist.count("2")>4 or dicelist.count("3")>4 or dicelist.count("4")>4 or dicelist.count("5")>4 or dicelist.count("6")>4:
    allowlist_f = allowlist.append("four_of_a_kind")

def full_house():
  if dicelist.count("1")==3 and dicelist.count("2")==2 or dicelist.count("1")==3 and dicelist.count("3")==2 or dicelist.count("1")==3 and dicelist.count("3")==2 or dicelist.count("1")==3 and dicelist.count("4")==2 or dicelist.count("1")==3 and dicelist.count("5")==2 or dicelist.count("1")==3 and dicelist.count("6")==2 or dicelist.count("2")==3 and dicelist.count("1")==2 or dicelist.count("2")==3 and dicelist.count("2")==2 or dicelist.count("2")==3 and dicelist.count("3")==2 or dicelist.count("2")==3 and dicelist.count("4")==2 or dicelist.count("2")==3 and dicelist.count("5")==2 or dicelist.count("2")==3 and dicelist.count("6")==2 or dicelist.count("3")==3 and dicelist.count("1")==2 or dicelist.count("3")==3 and dicelist.count("2")==2 or dicelist.count("3")==3 and dicelist.count("3")==2 or dicelist.count("3")==3 and dicelist.count("4")==2 or dicelist.count("3")==3 and dicelist.count("5")==2 or dicelist.count("3")==3 and dicelist.count("6")==2 or dicelist.count("4")==3 and dicelist.count("1")==2 or dicelist.count("4")==3 and dicelist.count("2")==2 or dicelist.count("4")==3 and dicelist.count("3")==2 or dicelist.count("4")==3 and dicelist.count("4")==2 or dicelist.count("4")==3 and dicelist.count("5")==2 or dicelist.count("4")==3 and dicelist.count("6")==2 or dicelist.count("5")==3 and dicelist.count("1")==2 or dicelist.count("5")==3 and dicelist.count("2")==2 or dicelist.count("5")==3 and dicelist.count("3")==2 or dicelist.count("5")==3 and dicelist.count("4")==2 or dicelist.count("5")==3 and dicelist.count("5")==2 or dicelist.count("5")==3 and dicelist.count("6")==2 or dicelist.count("6")==3 and dicelist.count("1")==2 or dicelist.count("6")==3 and dicelist.count("2")==2 or dicelist.count("6")==3 and dicelist.count("3")==2 or dicelist.count("6")==3 and dicelist.count("4")==2 or dicelist.count("6")==3 and dicelist.count("5")==2 or dicelist.count("6")==3 and dicelist.count("6")==2:
    allowlist_f = allowlist.append("full_house")

def yacht():
  if dicelist.count("1")==5 or dicelist.count("2")==5 or dicelist.count("3")==5 or dicelist.count("4")==5 or dicelist.count("5")==5 or dicelist.count("6")==5:
    allowlist_f = allowlist.append("yacht")

def large_straight():
  if dicelist.sort[0]==1 and dicelist.sort[1]==2 and dicelist.sort[2]==3 and dicelist.sort[3]==4 and dicelist.sort[4]==5 or dicelist.sort[0]==2 and dicelist.sort[1]==3 and dicelist.sort[2]==4 and dicelist.sort[3]==5 and dicelist.sort[4]==6:
    allowlist_f = allowlist.append("large_straight")

#============================main code============================
while num_lim<4:
  a,b,c,d,e=map(int,input("====================\n킵할 주사위를 1, 굴릴 주사위를 0으로 공백을 두어 구분하여 나타내시오\n====================\n").split())
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
  print("====================\n{}".format(dicelist))
  num_lim+=1
  if num_lim==4:
    print("====================\n{}으로 결정되었습니다.\n====================\n".format(dicelist))
  if a==1 and b==1 and c==1 and d==1 and e==1:
    str_a=input("====================\n{}으로 결정하시겠습니까? \n====================\n(예/아니오)\n====================\n".format(dicelist))
    if str_a=="예":
      print("====================\n{}으로 결정되었습니다.\n====================\n".format(dicelist))
      num_lim+=4
dicelist=str(dicelist)
#============================function_call============================
chance()
once()
deuces()
threes()
fours()
fives()
sixes()
four_of_a_kind()
full_house()
yacht()
#============================last============================
choice=input("====================\n득점 방법을 선택하세요\n====================\n{}\n====================\n".format(allowlist))
if choice=="1":
  print("{} 으로 결정하겠습니다.".format(allowlist[0]))
elif choice=="2":
  print("{} 으로 결정하겠습니다.".format(allowlist[1]))
elif choice=="3":
  print("{} 으로 결정하겠습니다.".format(allowlist[2]))
elif choice=="4":
  print("{} 으로 결정하겠습니다.".format(allowlist[3]))
elif choice=="5":
  print("{} 으로 결정하겠습니다.".format(allowlist[4]))
elif choice=="6":
  print("{} 으로 결정하겠습니다.".format(allowlist[5]))
elif choice=="7":
  print("{} 으로 결정하겠습니다.".format(allowlist[6]))
elif choice=="8":
  print("{} 으로 결정하겠습니다.".format(allowlist[7]))
#8번 이상은 생각하지 않는다.
