def contar_caracteres():
    entrada = input("Digite uma string: ")
    total_caracteres = len(entrada)
    total_sem_espacos = len(entrada.replace(" ", ""))
    print(f"Total de caracteres (com espaços): {total_caracteres}")
    print(f"Total de caracteres (sem espaços): {total_sem_espacos}")

contar_caracteres()
