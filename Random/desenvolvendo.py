import random
import numpy as np

# coloquei os nomes dentro de um array do numpy porque facilita fazer operacoes depois
nomes = np.array(["yuri", "takeda", "pedro", "rafael", "gabriel", "rodolfo"])

# defini pesos para cada nome (probabilidade diferente para cada um)
vies = np.array([0.1, 0.2, 0.05, 0.15, 0.1, 0.4])

# normalizei os pesos para garantir que a soma seja 1
vies = vies / vies.sum()


def sortear_nomes(qtd=1, reposicao=True):
    # np.random.choice para sortear com base nas probabilidades
    return np.random.choice(nomes, size=qtd, replace=reposicao, p=vies)


def simular_sorteios(quantidade_simulacoes=10000):
    # varios sorteios de uma vez para ver a frequencia real
    resultados = np.random.choice(nomes, size=quantidade_simulacoes, p=vies)

    # np.unique com return_counts conta quantas vezes cada nome apareceu
    valores, contagem = np.unique(resultados, return_counts=True)

    frequencia = contagem / quantidade_simulacoes

    print("\nresultado da simulacao:")
    for nome, freq in zip(valores, frequencia):
        print(f"{nome}: {freq:.2%}")


def ranking_probabilidade():
    # argsort ordena os indices do menor para o maior
    indices = np.argsort(vies)[::-1]  # inverti para ficar do maior para o menor

    print("\nranking por probabilidade:")
    for i in indices:
        print(f"{nomes[i]} -> {vies[i]:.2%}")


def embaralhar_lista():
    # copiei para lista normal porque random.shuffle funciona direto em lista
    lista = nomes.copy().tolist()
    random.shuffle(lista)
    return lista


def gerar_notas_aleatorias():
    # usei distribuicao normal para gerar notas mais realistas
    notas = np.random.normal(loc=7, scale=1.5, size=len(nomes))

    # limitei as notas entre 0 e 10
    notas = np.clip(notas, 0, 10)

    media = np.mean(notas)
    desvio = np.std(notas)

    print("\nnotas aleatorias:")
    for nome, nota in zip(nomes, notas):
        print(f"{nome}: {nota:.2f}")

    print(f"\nmedia da turma: {media:.2f}")
    print(f"desvio padrao: {desvio:.2f}")


def escolher_capitao():
    # random.choices tambem permite usar pesos
    capitao = random.choices(nomes, weights=vies, k=1)[0]
    return capitao


print("sorteio simples:", sortear_nomes(5))
print("lista embaralhada:", embaralhar_lista())
print("capitao escolhido:", escolher_capitao())

ranking_probabilidade()
simular_sorteios(5000)
gerar_notas_aleatorias()