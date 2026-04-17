from Bignum import str_to_bignum, bignum_to_str, add

def fibonacci(n):
    u0 = str_to_bignum("1")
    u1 = str_to_bignum("1")

    if n == 0:
        return u0
    if n == 1:
        return u1

    for n in range(2, n + 1):
        u2 = add(u1, u0)
        u0, u1 = u1, u2

    return u1

if __name__ == "__main__":
    n = 101
    result = fibonacci(n)
    print(f"u_{n} =", bignum_to_str(result))

    #u_101 = 927372692193078999176