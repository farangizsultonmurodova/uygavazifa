import os
os.system("cls")
with open('salom.txt') as fayl:
    qatorlar = fayl.read()

qatorlar = qatorlar.replace('\n', '').replace(' ', '')
print(qatorlar)

ong_qol = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', '^', '6', '&', '7', '*', '8', '9', '0', '(', ')', '-', '_', '+', '=']
ong_qol_count = 0
chap_qol = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5']
chap_qol_count = 0

for i in qatorlar:
    if i.lower() in ong_qol:
        ong_qol_count += 1
    elif i.lower() in chap_qol:
        chap_qol_count += 1

print('O\'ng qolda yozilgan harflar soni: ', ong_qol_count)
print('Chap qolda yozilgan harflar soni: ', chap_qol_count)