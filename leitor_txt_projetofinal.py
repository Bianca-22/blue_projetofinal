def leitor():
    t = 'intro_projetofinal.txt' #alterar o nome do arquivo txt
    with open(t,encoding = 'utf-8') as file:
        read = file.read()
        print(read)

if __name__ == "__main__":
    leitor()
