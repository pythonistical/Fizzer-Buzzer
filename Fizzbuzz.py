user = int(input("Till which number?\t"))
stats_fizzbuzz = 0
stats_fizz = 0
stats_buzz = 0
for a in range(user + 1):
    output = ""
    if a % 3 == 0 and a % 5 == 0:
       output += "fizzbuzz"
       stats_fizzbuzz += 1
       print(output)  
    elif a % 3 == 0:
         output += "fizz"
         stats_fizz += 1
         print(output) 
    elif a % 5 == 0:
         output += "buzz"
         stats_buzz += 1
         print(output) 
    else:
        print(a)

p_fizz = stats_fizz*100/user
p = stats_buzz*100/user
p_fizzbuzz = stats_fizzbuzz*100/user
print(f'buzz appeared {stats_buzz} times, that is about {p}%')
print(f'fizz appeared {stats_fizz} times, that is about {p_fizz}%')
print(f'fizzbuzz appeared {stats_fizzbuzz} times, that is about {p_fizzbuzz}%')
