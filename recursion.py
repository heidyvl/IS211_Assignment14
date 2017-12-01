import sys


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def gcd(a,b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


def compareTo(s1, s2):
    if s1 < s2:
        return -1
    if s1==s2:
        return 0
    else:
        return int(compareTo(s1[1:],s2[1:])<s1[1:])

    
def main():
    print 'FIBONACCI'
    while True:
            try:
                n = input("Enter Number to fibonacci: ")
            
            except(SyntaxError, ValueError): continue
            print fibonacci(n)
            break
            print 'LOOKING FOR GREATEST COMMON DIVISOR'
            print 'EUCLYDS GCD'
    while True:
            try:
                a= input('Enter first number: ')
            except(SyntaxError, ValueError): continue

            break
    while True:
        try:
            b = input('Enter second number: ')
        except(SyntaxError, ValueError): continue
            
        print gcd(a,b)
        break

    print 'COMPARING STRINGS'
    s1= raw_input('Enter first str: ')
    s2 = raw_input('Enter second str: ')
    print compareTo(s1,s2)

if __name__=='__main__':
    main()
    action = None
    while action != 0 or action !=1:
            try:
                action = input('Press 1 to try again or 0 to quit ')
                if action == 1:
                    main()
                else:
                    sys.exit()
            except (ValueError, SyntaxError):
                continue


