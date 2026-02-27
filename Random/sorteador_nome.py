import random
import numpy as np

nomes = ["Yuri", "Takeda", "Pedro", "Rafael", "Gabriel", "Rodolfo"]
vies = [0.1, 0.2, 0.05, 0.15, 0.1, 0.4]

print(np.random.choice(nomes, 5, True, p=vies))