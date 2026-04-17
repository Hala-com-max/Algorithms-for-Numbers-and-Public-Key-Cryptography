from Bignum import add, str_to_bignum, bignum_to_str

if __name__ == "__main__":
    a = str_to_bignum("123456789")
    b = str_to_bignum("987654321")

    result = add(a, b)
    print("Result:", bignum_to_str(result))