def str_to_bignum(s):
    return [int(c) for c in reversed(s)]

def bignum_to_str(a):
    return ''.join(str(d) for d in reversed(a))

def add(a, b):
    result = []
    carry = 0

    for i in range(max(len(a), len(b))):
        da = a[i] if i < len(a) else 0
        db = b[i] if i < len(b) else 0

        total = da + db + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return result

def mult(a, b):
    result = [0] * (len(a) + len(b))

    for i in range(len(a)):
        carry = 0
        for j in range(len(b)):
            total = result[i + j] + a[i] * b[j] + carry

            result[i + j] = total % 10
            carry = total // 10

        if carry:
            result[i + len(b)] += carry

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result