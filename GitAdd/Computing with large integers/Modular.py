from Bignum import str_to_bignum, bignum_to_str, mult

def mod(a, n):
    return str_to_bignum(str(int(bignum_to_str(a)) % int(bignum_to_str(n))))

def expmod(a, b, n):
    result = str_to_bignum("1")
    base = a
    while b > 0:
        if b % 2 == 1:
            result = mod(mult(result, base), n)

        base = mod(mult(base, base), n)
        b = b // 2
    return result
if __name__ == "__main__":
    a = str_to_bignum("2342")
    b = 6762
    n = str_to_bignum("9343")
    res = expmod(a, b, n)
    print(bignum_to_str(res))