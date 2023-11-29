
MOEX_RATE = [417.42,
             673.72,
             722.81,
             1323.32,
             2216.63,
             2472.38,
             810.922,
             1793.24,
             2209.46,
             1835.14,
             1934.43,
             1967.83,
             1828.06,
             2305.50,
             3042.00,
             3015.71,
             3564.05,
             4887.25,
             5567.28,
             6731.43,
             4170.35]
INFLATION_RATE = [
    15.06,
    11.99,
    11.74,
    10.91,
    9.00,
    11.87,
    13.28,
    8.80,
    8.78,
    6.10,
    6.58,
    6.45,
    11.36,
    12.91,
    5.38,
    2.52,
    4.27,
    03.05,
    4.91,
    8.39,
    11.92]
year = int(input())
proc_izi = float(0)
number = year - 2002
if (year >= 2002) and (year < 2022):
    while True:
        nacho_sum = MOEX_RATE[number] #цыфра массива
        proc_izi += 0.5
        cash = MOEX_RATE[number] * proc_izi * 0.01
        for y in range(2022 - year):
            nacho_sum -= cash
            nacho_sum =nacho_sum*( MOEX_RATE[number+y+1] / MOEX_RATE[number+y])
            cash = cash * (100 + INFLATION_RATE[number+y]) / 100
        if nacho_sum < 0:
            print(proc_izi-0.5)
            break
        if proc_izi > 100:
            print(proc_izi)
            break
else:
    print('throws Exception…')