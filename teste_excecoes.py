try :
    with open("dados/contato.csv", encoding="latin_1") as arquivo :
        for linha in arquivo:
            print(linha, end="")

        arquivo.write("3,Bento José, bento@bento.com.br")

        arquivo.seek(0)
        for linha in arquivo:
            print(linha, end="")

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')

