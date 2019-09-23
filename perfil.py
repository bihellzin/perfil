import random
import numpy as np

class Perfil:
    def __init__(self):
        probabilidade = np.array(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
             27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
             52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
             77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])
        self.estilo = self.definindoEstilo()
        self.genero = self.definindoGenero(probabilidade)
        self.idade = self.definindoIdade(probabilidade)
        self.estado_civil = None
        self.necessidades = None
        self.pessoas = None
        self.animais = None
        self.altura = None
        self.hobbies = self.definindoHobbies()
        self.espaco = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def leitura(self, file):
        arquivo = open(file, "r")
        arquivo = arquivo.readlines()
        palavras = []
        for palavra in arquivo:
            palavra = palavra.strip()
            palavras.append(palavra)

        return palavras

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def definindoEstilo(self):
        estilos = self.leitura("estilo.txt")
        return random.choice(estilos)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def definindoGenero(self, probabilidade):
        expressao_generos = self.leitura("expressao_genero.txt")
        identidade_generos = self.leitura("identidade_genero.txt")
        p1 = random.choice(probabilidade)
        p2 = random.choice(probabilidade)
        if p1 <= 43:
            expressao_generos = expressao_generos[0]

        elif p1 > 43 and p1 <= 90:
            expressao_generos = expressao_generos[1]

        else:
            expressao_generos = expressao_generos[2]

        if p2 <= 90:
            identidade_generos = identidade_generos[0]

        else:
            identidade_generos = identidade_generos[1]

        return expressao_generos + ' ' + identidade_generos

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def definindoIdade(self, probabilidade):
        pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def definindoHobbies(self):
        hobbies = self.leitura("hobbies.txt")
        h1 = hobbies.pop(random.randint(0, 35))
        h2 = hobbies.pop(random.randint(0, 34))
        h3 = hobbies.pop(random.randint(0, 33))
        return h1 + ', ' + h2 + ' e ' + h3