n = int(input())

def ff(n):
    if n % 2 == 0:
        return n // 2
    else:
        return -(n // 2 + 1)

print(ff(n))
