import os 
os.system("cls")
a = input(" a sonni kiriting:")
dct = {k: a.count(k) for k in set(a)}
dct = dict(sorted(dct.items(), key=lambda n: n[0]))
for k, v in dct.items():
    print(f'{k} - {v}')