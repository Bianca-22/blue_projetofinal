import os

def limpar():
    return os.system('cls' if os.name == 'nt' else 'clear')

def avancar():
    return input('\n\nQuando quiser avançar aperte ENTER: ')

