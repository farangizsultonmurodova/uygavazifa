import os
os.system("cls")
def nol_bormi(son):
    count=0
    i=0
    while len(son)>i and son[i] =='0':
        count +=1
        i +=1
    return count

a=input(" a sonni kiriting:")
print(nol_bormi(a))