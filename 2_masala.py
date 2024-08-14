import os
os.system("cls")
def qimmat_mahsulot(son, mahsulot):
    sorted_mahsulot = sorted(mahsulot, key=lambda x: x['narx'], reverse=True)
    return sorted_mahsulot[:son]


print(qimmat_mahsulot(2, [{'ism': 'krasovka', 'narx': 200},
 {'ism': 'kuylak', 'narx': 135}, {'ism': 'yubka', 'narx': 150},
 {'ism': 'shim', 'narx': 130}]))