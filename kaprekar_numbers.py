def convert(num, to_base = 10, from_base = 10):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_num = ''
    n = int(num, from_base)
    while n > 0:
        put = s[n % to_base]
        new_num = ''.join((str(put),new_num))
        n = int(n / to_base)
    return new_num

def kaprekar(n, base):
    num = int(convert(str(n), 10, base))
    num = convert(str(num*num), base, 10)
    for i in range(1,len(num)):
        a = int(num[0:i], base)
        b = int(num[i:len(num)], base)
        if a and b and a+b == int(str(n), base):
            return True
    return False

num_sys = 10
for n in [9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4879, 4950, 5050, 7272, 7777, 9999]:
    print(f'Base {num_sys} number {n} -- {kaprekar(n, num_sys)}')
