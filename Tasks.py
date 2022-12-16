# Task 1

def Task1():
    try:
        a = int(input("Première valeur\n"))
        b = int(input("Deuxième valeur\n"))
        c = int(input("Troisième valeur\n"))
        max = a
        if b > max:
            max = b
        if c > max:
            max = c
        print("Maximum = ",max)
    except ValueError:
        print('Wrong input')

# Task 2

def Task2():
    try:
        mat1 = int(input("Donner la première note\n"))
        mat2 = int(input("Donner la deuxième note\n"))
        mat3 = int(input("Donner la troisième note\n"))
        if(mat1 > 20 or mat1 < 0 or mat2 < 0 or mat2 > 20 or mat3 < 0 or mat3 > 20):
            return print('Must be between 0 and 20')
        if mat1 <= 5 or mat2 <= 5 or mat3 <= 5:
            return print('Note eliminatoire')        
        moyenne = (mat1 + mat2 + mat3)/3
        if moyenne < 10:
            return print(moyenne, "Failed")
        elif moyenne >= 10 and moyenne < 15:
            return print(moyenne, 'Good')
        elif moyenne  >= 15 and moyenne <= 20:
            return print(moyenne, 'Very good')
    except ValueError:
        print('Wrong input')

# Task 3

def Task3():
    list = []
    sum = 0
    for i in range(0,10):
        myNumber = input('Give me number '+str(i+1)+'\n')
        while (not (myNumber.lstrip('-').isdigit())):
            myNumber = input('A number please : \n')
        list.append(int(myNumber))       
        sum += int(myNumber)
    max = list[0]
    min = list[0]
    for number in list:
        if number > max:
            max = number
        elif number < min:
            min = number
    print("\nLa liste : ",list,"\nLa somme de la liste : ",sum,"\nLe maximum de la liste : ",max,"\nLe minimum de la liste : ",min)


# Task 4

def Task4():
    list = [4,5,-1,-8,0,14,42,-31,21,6,-7,42,-71]
    for i in range(len(list)):
        for j in range(0,(len(list)-1-i)):
            if(list[j] > list[j+1]): 
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print("\nOrdre croissant : ",list)

# Task 5

def Task5():
    l1 = [1,2,3,4,5,6,7,8,9,10]
    user = input('Give me a number\n')
    while not user.lstrip('-').isdigit():
        user = input('A number please : \n')
    response = False
    for element in l1:
        if(int(user) == element):
            response = True
    if response:
        print("Your number is in the list")
    else:
        print("Your number is not in the list")
    
# Task 6

def Task6():
    userInput = input('Type a string :\n')
    count = 0
    for character in userInput: 
        count += 1
    print("There are ",count," characters in the string '",userInput,"'")


