no=[15,16,17,18,19,20]
fizzbuzz=[]
fizz=[]
buzz=[]
number=[]
for num in no:
    if num%3==0 and num%5==0:
        fizzbuzz.append(num)
    elif num%3==0:
        fizz.append(num)
    elif num%5==0:
        buzz.append(num)
    elif not num%3==0 and not num%5==0:
        number.append(num)
print("Fizz:",fizz)
print("Buzz:",buzz)
print("FizzBuzz:",fizzbuzz)
print("Numbers:",number)