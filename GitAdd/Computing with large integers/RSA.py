class BigNum:
    def __init__(self, digits, sign=1):
        self.digits = digits[:]  # least significant first
        self.sign = sign
        self.normalize()

    def normalize(self):
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    @staticmethod
    def from_string(s):
        sign = -1 if s[0] == '-' else 1
        if s[0] in '+-':
            s = s[1:]
        return BigNum([int(c) for c in reversed(s)], sign)

    def __str__(self):
        s = ''.join(map(str, reversed(self.digits)))
        return '-' + s if self.sign < 0 else s

def compare(a, b):
    if len(a.digits) != len(b.digits):
        return len(a.digits) - len(b.digits)
    for i in reversed(range(len(a.digits))):
        if a.digits[i] != b.digits[i]:
            return a.digits[i] - b.digits[i]
    return 0

def add(a, b):
    res = []
    carry = 0
    n = max(len(a.digits), len(b.digits))

    for i in range(n):
        da = a.digits[i] if i < len(a.digits) else 0
        db = b.digits[i] if i < len(b.digits) else 0

        s = da + db + carry
        res.append(s % 10)
        carry = s // 10

    if carry:
        res.append(carry)

    return BigNum(res)

def sub(a, b):
    res = []
    borrow = 0

    for i in range(len(a.digits)):
        da = a.digits[i]
        db = b.digits[i] if i < len(b.digits) else 0

        s = da - db - borrow
        if s < 0:
            s += 10
            borrow = 1
        else:
            borrow = 0

        res.append(s)

    return BigNum(res)

def mult(a, b):
    res = [0] * (len(a.digits) + len(b.digits))

    for i in range(len(a.digits)):
        carry = 0
        for j in range(len(b.digits)):
            tmp = res[i+j] + a.digits[i]*b.digits[j] + carry
            res[i+j] = tmp % 10
            carry = tmp // 10

        res[i+len(b.digits)] += carry

    return BigNum(res)

def mod(a, n):
    r = BigNum(a.digits[:])
    while compare(r, n) >= 0:
        r = sub(r, n)
    return r


def addmod(a, b, n):
    return mod(add(a, b), n)

def multmod(a, b, n):
    return mod(mult(a, b), n)


def expmod(base, exp, n):
    result = BigNum.from_string("1")
    base = mod(base, n)

    while exp > 0:
        if exp % 2 == 1:
            result = mod(mult(result, base), n)

        base = mod(mult(base, base), n)
        exp //= 2

    return result

def int_to_bignum(n):
    return BigNum.from_string(str(n))

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def inversemod(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        raise ValueError("No inverse")
    return x % n

import random

def is_probable_prime(p, t=5):
    if p < 2:
        return False
    for _ in range(t):
        a = random.randint(2, p-2)
        if pow(a, p-1, p) != 1:
            return False
    return True

def genrandomprime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if is_probable_prime(p):
            return p


def keygen(bits=16):
    p = genrandomprime(bits)
    q = genrandomprime(bits)

    n = p * q
    phi = (p-1)*(q-1)

    e = 65537
    d = inversemod(e, phi)

    return n, e, d


def RSAencrypt(m, e, n):
    return pow(m, e, n)


def RSAdecrypt(c, d, n):
    return pow(c, d, n)


def testRSA():
    n, e, d = keygen()

    m = 1234
    c = RSAencrypt(m, e, n)
    m2 = RSAdecrypt(c, d, n)

    print("n =", n)
    print("e =", e)
    print("d =", d)
    print("cipher =", c)
    print("decrypted =", m2)

if __name__ == "__main__":
    testRSA()