son = int(input("Sonni kiriting: "))

for qator in range(1, son + 1):
    print(*range(1, qator + 1))


son = 1000
qatorlar_soni = 3

har_qatorga = son // qatorlar_soni
qoldiq = son % qatorlar_soni
boshlanish = 1

for qator in range(qatorlar_soni):
    miqdor = har_qatorga
    if qator < qoldiq:
        miqdor += 1

    tugash = boshlanish + miqdor
    print(*range(boshlanish, tugash))
    boshlanish = tugash
