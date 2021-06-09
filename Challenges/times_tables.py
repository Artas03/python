number = int(input("Which times table do you want: "))
for i in range(1,number):
    for j in range(1,number):
        print(i * j, end='\t')
    print('')
    