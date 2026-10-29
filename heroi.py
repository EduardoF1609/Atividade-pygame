
from personagem import Personagem


class Heroi(Personagem):

    def __init__(self, nome, idade, vida):
        super().__init__(nome, idade, vida, ataque=20, defesa=10)

    def usar_cogumelo(self):
        self.upgrade_vida(20)
        print(f"{self.nome} usou o cogumelo!")

    def __str__(self):
        return (
            f'Herói: {self.nome}, '
            f'Idade: {self.idade}, '
            f'Vida: {self.vida}, '
            f'Ataque: {self.ataque}, '
            f'Defesa: {self.defesa}'
        )
