import random

#print(random.sample(range(1,6), 5))

#print([random.randint(1, 100) for i in range(6)])

#print([random.uniform(1, 10) for i in range(5)])

#print([round(random.uniform(1, 10), 2) for i in range(5)])

#print(random.randint(1, 1000001))

#print(np.random.choice(nomes, 5, True, p=vies))

n = (random.randint(1, 1000001))

t = int(input("USER1:\n"))
y = int(input("USER2:\n"))

t2 = t - n
y2 = y - n

if y2 < t2:
    print("USER2 CHEGOU MAIS PROXIMO DO NUMERO SORTEADO\n")
elif t2 < y2:
    print("USER1 CHEGOU MAIS PROXIMO DO NUMERO SORTEADO\n")
else:
    print("EMPATE\n")

print("\n O NUMERO SORTEADO FOI:  ",n)


