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

def P(L):
    Sum =0
    l = len(L)
    for i in range(l):
        Sum += ( (-1)**(l-i-1)) * L[i]     
    if l%2 == 0:
        if Sum < 0 :return False
        else:return True
    else:
        if Sum > 0 : return False
        else : return True

def Jury(List):
    if ( abs(List[0]) < abs(List[-1]) ):
        print("if 1")
        return False
    elif(sum(List)<0):
        print("if 2")
        return False
    elif(P(List)):
        print("if 3")
        return False
    else:
        table = table_jury(List)
        for i in range(len(table)):
            if(i%2 ==0):
                if(i ==0):
                    if( abs(table[i][0]) > abs(table[i][-1]) ):
                        print("if 4")
                        return False
                elif( abs(table[i][0]) < abs(table[i][-1]) ):
                    print("if 4")
                    return False
            else:continue
    return True
        
# p = [1,-1.3,-0.08,0.24]
p = [1.-1.2,0.07,0.3,-0.08]
print(sum(p))
print(Jury(p))