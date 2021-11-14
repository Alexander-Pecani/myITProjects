p = 0
n = int(input())

while (p*p) < n:
    p = p + 1

if (p*p) == n:
    print (p*p)
else:
    p = p-1
    print (p*p)

# "Guess I learned how to use Git Commands Today!"