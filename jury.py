temp = input('please enter sorat G_z: ')
temp = temp.split(',')
sorat = []
for num in temp:
    sorat.append(float(num))
temp = input('please enter makhraj G_z: ')
temp = temp.split(',')
makhraj = []
for num in temp:
    makhraj.append(float(num))
# print(sorat)
# print(makhraj)
#if_1 : |a0|>|an|
MIN = -(makhraj[0]+makhraj[-1])/sorat[-1]
MAX = (makhraj[0]-makhraj[-1])/sorat[-1]
#if_2 P(1) > 0
temp2 = -sum(makhraj)/sum(sorat)
if(temp2>MIN):MIN = temp2
#if_3 P(-1)>0 ||P(-1)<0
l_makhraj = len(makhraj)
l_sorat = len(sorat)
sum_m =0
print("--------------------------------------------------------")
for i in range(l_makhraj):
    sum_m += ( (-1)**(l_makhraj-i-1)) * makhraj[i] 
sum_s =0
for i in range(l_sorat):
    sum_s += ( (-1)**(l_sorat-i-1)) * sorat[i]
temp2 = -sum_m / sum_s
if(l_makhraj % 2 == 0):  
    if(temp2>MIN):MIN = temp2
else:
    if(temp2 < MAX): MAX = temp2
print(MIN ," < K < ",MAX)
