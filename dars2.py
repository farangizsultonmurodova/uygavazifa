import os,math
os.system("cls")
def Kursatgichlar_ruyxati():
    return input("""
1. Bilet va uning  narxini  qidirish
2. Davlat nomini  qidirish
3. US ga uchadigan va qo'nish vaqti 20:00 va undan oldingi reyslar
4. Dasturdan chiqish
(1-4 oralig'ida son tanlang)
""")


def qidiruv_narxi(bookings):
    foydalanuvchi_narxi = int(input('Narxni kiriting::'))
    lower_bound = foydalanuvchi_narxi - 500
    upper_bound = foydalanuvchi_narxi + 1000
    parvozlar_oraligi = [booking for booking in bookings if lower_bound <= booking['narx'] <= upper_bound]
    for uchish in parvozlar_oraligi:
        print(uchish)


def davlat_qidiruvi(bookings):
    davlat_nomi = input('Davlat nomini kiriting: ')
    uchishlar = [booking for booking in bookings if booking['dep_davlat'] == davlat_nomi]
    for uchish in uchishlar:
        print(uchish)


def parvoz_qidiruvi(bookings):
    parvozlar = []
    for booking in bookings:
        if booking['arr_davlat'] == 'US' or booking['dep_davlat'] == 'US':
            arr_soat, arr_daqiqa = map(int, booking['arr_vaqt'].split(':'))
            if arr_soat < 20 or (arr_soat == 20 and arr_daqiqa == 0):
                parvozlar.append(booking)
    for uchish in parvozlar:
        print(uchish)


with open('booking.txt') as fayl:
    qatorlar = fayl.read().split('\n')

if qatorlar[-1] == '':
    qatorlar = qatorlar[:-1]

bookings = []
for line in qatorlar:
    booking_id, dep_davlat, dep_vaqt, arr_davlat, arr_vaqt, narx = line.strip().split(',')
    bookings.append({
        'booking_id': int(booking_id),
        'dep_davlat': dep_davlat,
        'dep_vaqt': dep_vaqt,
        'arr_davlat': arr_davlat,
        'arr_vaqt': arr_vaqt,
        'narx': float(narx.replace('$', ''))
    })

while True:
    foydalanuvchi = Kursatgichlar_ruyxati()
    if foydalanuvchi == '1':
        qidiruv_narxi(bookings)
    elif foydalanuvchi == '2':
        davlat_qidiruvi(bookings)
    elif foydalanuvchi == '3':
        parvoz_qidiruvi(bookings)
    elif foydalanuvchi == '4':
        print("Dasturdan chiqish:")
        break
    else:
        print("Tanlov noto\'g\'ri: Iltimos 1 dan 4 gacha bo\'lgan sonlardan birini tanlang!!!")
