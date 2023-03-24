sum=0
num2=1
num3=1
fib_num=1
while fib_num<=4000000:
    
    num3=fib_num
    fib_num=fib_num+num2
    if fib_num//2*2==fib_num:
        sum+=fib_num
    num2=num3      
print(sum)
