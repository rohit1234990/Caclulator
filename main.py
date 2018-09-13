# this is main file


class Calculator(object):
    def add(self):
        a, b = raw_input("Enter two numbers seperated by space : ").split(" ")
        return int(a) + int(b)

    def sub(self):
        a, b = raw_input("Enter two numbers seperated by space : ").split(" ")
        return int(a) - int(b)

    def mul(self):
        a, b = raw_input("Enter two numbers seperated by space : ").split(" ")
        return int(a) * int(b)

    def div(self):
        a, b = raw_input("Enter two numbers seperated by space : ").split(" ")

        if int(b):
            return  int(a) / int(b)
        else:
            return "Divisor can't be zero"




c = Calculator()

while True:
    print "\n1. Addition"
    print "2. Subtraciton"
    print "3. Multiplication"
    print "4. Division"
    print "5. Exit"

    ch = int(raw_input("Your Choice : "))
    if ch == 1:
        print "Result : " + str(c.add())
    elif ch == 2:
        print "Result : " + str(c.sub())
    elif ch == 3:
        print "Result : " + str(c.mul())
    elif ch == 4:
        print "Result : " + str(c.div())
    elif ch == 5:
        break;
    else:
        print "Wrong Choice !!!"