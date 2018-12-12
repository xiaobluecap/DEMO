guiyuan1020s=['Hashiqi','faming','PIAOCHANGMING','pangzi']
for guiyuan1020 in guiyuan1020s:
    if guiyuan1020=='Hashiqi':    #if条件判断
        print(guiyuan1020.lower())
    else:
        print(guiyuan1020.upper())
print(guiyuan1020s[0].lower()=="hashiqi") #if条件测试
age_0=22
age_1=18
a=age_0>=21 and age_1<=17
b=age_0>=21 or age_1<=17
print(a)
print(b)
if age_1>=18:   #if-else条件判断

    print("You are old enough to buy ticket!")
else:
    print("Sorry,please wait to 18 years old!")
if age_0<=5:   #if-if独立条件判断
    print("You are free to play!")
if age_0>5 and age_0<=18:
    print("You are twenty percent off to buy ticket!")
if age_0>18:
    print("You aren't preferential to buy ticket!")
if age_0>70:
    print("You aren't to play!")