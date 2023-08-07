no=[15,16,17,18,19,20]
for num in no:
    if num%3==0 and num%5==0:
        print('FizzBuzz',num)
    elif num%3==0:
        print("Fizz",num)
    elif num%5==0:
        print("Buzz",num)
    elif not num%3==0 and not num%5==0:
        print(num)
