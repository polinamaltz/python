# Chauvenet criterion
from scipy.stats import tmean, tstd 
from scipy.special import erfc 

set_ = ((8.02, 8.16, 3.97, 8.64, 0.84, 4.46, 0.81, 7.74, 8.78, 9.26, 20.46, 29.87, 10.38, 25.71),
         (8.02, 8.16, 3.97, 8.64, 0.84, 4.46, 0.81, 7.74, 8.78, 9.26, 20.46, 10.38),
         (8.02, 8.16, 3.97, 8.64, 0.84, 4.46, 0.81, 7.74, 8.78, 9.26, 10.38))

for p in set_:
    n = len(p)
    m = tmean(p)
    std = tstd(p)
    rv = 1 / (2 * n)
    for p_i in (max(p), min(p)):
        erfc_x = erfc(abs(p_i - m) / std)
        print("p =", *p)
        print("{:5} {:2} {:9} {:9} {:9} {:9} {}".format("p_i", "n", "p_mean", "std", "erfc", "r_value", "Chauvenet"))
        print("{:>5.2f} {} {:9.6f} {:9.6f} {:9.6f} {:9.6f} {}".format(p_i, n, m, std, erfc_x, rv, erfc_x < rv))
        print()
