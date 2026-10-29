
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi

def main():
    # Criando personagens e vilões
    heroi = Heroi('Mario', 30, 100)
    npc = Personagem('Luiji', 28, 80)
    vilao = Vilao('Bowser', 45, 120, 'Alta')

    # Usando poção
    heroi.usar_cogumelo()

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.atacar(heroi)

    # Herói ataca o vilão
    heroi.atacar(vilao)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)

    # Mudando nome do NPC
    npc.update_nome('Luigi')
    print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()
