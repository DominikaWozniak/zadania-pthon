def potegowanie(podstawa, wykladnik):
    i = 0
    potega=1
    while i < wykladnik:
        i = i + 1
        potega = podstawa * potega
    print(potega)

potegowanie(2, 9)