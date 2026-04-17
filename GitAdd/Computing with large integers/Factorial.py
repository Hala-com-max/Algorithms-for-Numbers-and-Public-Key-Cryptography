from Bignum import str_to_bignum, bignum_to_str, mult

def factorial(n):
    result = str_to_bignum("1")

    for i in range(2, n + 1):
        result = mult(result, str_to_bignum(str(i)))

    return result

if __name__ == "__main__":
   n1 = 40
   n2 = 30
   res1 = factorial(n1)
   res2 = factorial(n2)
print(f"{n1}! =", bignum_to_str(res1))
print(f"{n2}! =", bignum_to_str(res2))

#40! = 815915283247897734345611269596115894272000000000
#30! = 265252859812191058636308480000000