travelling = input("Are you travelling? yes or no:")

while travelling == 'yes':
    num = int(input("how many number of people are travelling:"))

    for num in range(1,num+1):
        name = input("Name:")
        age = input("Age:")
        sex = input("Male or Female:")

        print(name)
        print(age)
        print(sex)

    travelling = input("Are you forgetting anyone?")