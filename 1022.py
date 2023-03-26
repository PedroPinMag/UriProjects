n = int(input())


def calc(nu, m):
    if m == 0:
        return nu
    else:
        return calc(m, nu % m)


while n:
    n -= 1
    n1, x, d1, operator, n2, y, d2 = input().split()
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)

    if operator == "+":
        n3 = n1 * d2 + n2 * d1
        d3 = d1 * d2

    elif operator == "-":
        n3 = n1 * d2 - n2 * d1
        d3 = d1 * d2

    elif operator == "*":
        n3 = n1 * n2
        d3 = d1 * d2

    elif operator == "/":
        n3 = n1 * d2
        d3 = n2 * d1

    print('%d/%d = %d/%d' % (n3, d3, n3 / calc(n3, d3), d3 / calc(n3, d3)))
