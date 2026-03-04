while 1 > 0:
    def calc_parser(number_one, number_two, operation):
        if operation == 1:
            result = number_one + number_two
            print(str(number_one) + " + " + str(number_two) + " = " + str(result))
        elif operation == 2:
            result = number_one - number_two
            print(str(number_one) + " - " + str(number_two) + " = " + str(result))
        elif operation == 3:
            result = number_one * number_two
            print(str(number_one) + " * " + str(number_two) + " = " + str(result))
        elif operation == 4:
            if number_two == 0:
                print("Error")
            else:
                result = number_one / number_two
                print(str(number_one) + " / " + str(number_two) + " = " + str(result))

        else:
            print("Error")
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))
    operation = int(input("1. +\n2. -\n3. *\n4. /\n"))
    
    calc_parser(number_one, number_two, operation)