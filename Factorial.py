class Factorial(object):

    def calculate(self, number):
        if number == 0: 
            return number

        result = 0

        while number > 1:
            nextNumber = number - 1;
            if (result == 0):
                result = (number * nextNumber)
            else:
                result = (result * nextNumber)
            print(result)
            number = nextNumber

        return result