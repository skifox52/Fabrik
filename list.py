try:
    l1 = [1,2,3,4,5,6,7,8,9,10]
    user = int(input('Give me a number\n'))
    response = False
    for element in l1:
        if(user == element):
            response = True
    print(response)
except ValueError:
    print('Wrong input')