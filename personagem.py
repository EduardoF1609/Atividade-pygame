class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, ataque=20, defesa=10):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida = max(0, alvo.vida - dano)

        print(f"{self.nome} atacou {alvo.nome}")
        print(f"Dano causado: {dano}")
        print(f"Vida restante de {alvo.nome}: {alvo.vida}")

    def __str__(self):
        return (
        f'Personagem: {self.nome}, '
        f'Idade: {self.idade}, '
        f'Vida: {self.vida}, '
        f'Ataque: {self.ataque}, '
        f'Defesa: {self.defesa}'
    )
