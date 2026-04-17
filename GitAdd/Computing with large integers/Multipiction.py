from Bignum import str_to_bignum, bignum_to_str, mult

if __name__ == "__main__":
    a = str_to_bignum("100")
    b = str_to_bignum("100")

res = mult(a, b)
print(bignum_to_str(res))