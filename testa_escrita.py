arquivo = open("dados/contatos.csv", encoding="latin_1", mode="a+")

arquivo.write("1,Silvio,silvio@silvio.com.br\n")
arquivo.write("2,Camila,camila@camila.com.br\n")

arquivo.flush()

arquivo.seek(0)

for linha in arquivo:
    print(linha, end="")