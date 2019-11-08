from matplotlib import pyplot as plt

print("f(x) = C1x1 + C2x2")
c1 = int(input("C1 = "))
c2 = int(input("C2 = "))
print("f(x) = {}*x1 + {}*x2".format(c1, c2))


def value_in_poin():
    a1 = int(input("A1 = "))
    b1 = int(input("B1 = "))
    d1 = int(input("D1 = "))
    a2 = int(input("A2 = "))
    b2 = int(input("B2 = "))
    d2 = int(input("D2 = "))

    D = a1 * b2 - a2 * b1
    D1 = d1 * b2 - d2 * b1
    D2 = a1 * d2 - a2 * d1
    if D != 0:
        print("{}/{} = {}".format(D1, D, D1 / D))
        print("{}/{} = {}".format(D2, D, D2 / D))
        print("f(x) = {}*{} + {}*{} = {}".format(c1, D1 / D, c2, D2 / D, c1 * (D1 / D) + c2 * (D2 / D)))

value_in_poin()


plt.show()