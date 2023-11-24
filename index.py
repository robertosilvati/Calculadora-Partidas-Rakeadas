def rankeadas(vitorias, derrotas):
    saldo = vitorias - derrotas

    if vitorias <= 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo, nivel


def obter_numero(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Por favor, insira um número não negativo.")
            else:
                return valor
        except ValueError:
            print("Por favor, insira um número válido.")


def main():
    vitorias = obter_numero("Coloque a quantidade de vitórias aqui: ")
    derrotas = obter_numero("Coloque a quantidade de derrotas aqui: ")
    
    saldo, nivel = rankeadas(vitorias, derrotas)
    
    print(f"O herói tem o saldo {saldo} está no nível {nivel}")


main()
