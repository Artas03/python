math = int(input("What is your Maths mark?: "))
phys = int(input("What is your physics mark?: "))
chem = int(input("What is your chemistry mark?: "))

avg = (math + phys + chem) // 3

if avg > 70:
    print("A")
elif avg > 60:
    print("B")
elif avg > 50:
    print("C")
elif avg > 40:
    print("D")
else:
    print("F You failed")