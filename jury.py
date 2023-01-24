def determin(a,b,c,d):
    return a*d-b*c
def table_jury(p_Z):
    temp = p_Z.copy()
    temp.reverse()
    N = len(p_Z)
    table = [[0 for _ in range(N)] for _ in range(2*N-3)]
    table[0] = temp.copy()
    table[1] = p_Z.copy()
    for i in range(2,2*N -3):
        if(i%2 == 0):
            l = len(temp)-1
            for j in range(l):
                table[i][j]=determin(temp[0],temp[l-j],temp[-1],temp[j])
            temp = table[i].copy()
        else:
            temp_else = temp.copy()
            temp_else.reverse()
            for k in range(len(temp_else)):
                table[i][k] = temp_else[k]
    return table
def Jury(List):
    table = table_jury(List)
    for i in range(len(table)):
        if(i%2 ==0):
            if(i ==0):
                if( abs(table[i][0]) > abs(table[i][-1]) ):return False
            elif( abs(table[i][0]) < abs(table[i][-1]) ):return False
        else:continue
    return True
# make P(z)
def make_p(sorat,makhraj,MAX):
    P = []
    for i in range(1,len(makhraj)+1):
        if(len(sorat)>= i):
            temp = makhraj[-i] + MAX*sorat[-i]
            P.append(temp)
        else:
            P.append(makhraj[-i])
    P.reverse()
    return P
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
#if 4 test jury
P = make_p(sorat,makhraj,MAX)
if ( Jury(P) ):
    P = make_p(sorat,makhraj,MIN)
    if ( Jury(P) ):print(MIN ," < K < ",MAX)
    else:
        while(1):
            MIN = MIN + 0.0001
            New_p = make_p(sorat,makhraj,MIN)
            if (Jury(New_p)):
                print(MIN ," < K < ",MAX)
                break
else:
    while(1):
        MAX = MAX-0.0001
        New_p = make_p(sorat,makhraj,MAX)
        if (Jury(New_p)):
            break
    New_p = make_p(sorat,makhraj,MIN)
    if (Jury(New_p)):
        print(MIN ," < K < ",MAX)
    else:
        while(1):
            MIN = MIN + 0.0001
            New_p = make_p(sorat,makhraj,MIN)
            if (Jury(New_p)):
                print(MIN ," < K < ",MAX)
                break



