#FORMATAÇÃO USANDO f-string###########################################################################
# numero_inteiro = 255
# numero_flutuante = 12345.6789
# texto = "Python"
# casas_decimais = int(input('Digite quantas casas decimais: '))
# #Pode-se adicionar variáveis dentro da formatação, **usando como exemplo o .2f
# # Usando f-strings
# formatado = (
#     f"Alinhado à esquerda : {texto:<10}\n"
#     f"Alinhado à direita  : {texto:>10}\n"
#     f"Centralizado        : {texto:^10}\n"
#     f"Binário             : {numero_inteiro:b}\n"
#     f"Octal               : {numero_inteiro:o}\n"
#     f"Hexadecimal         : {numero_inteiro:x}\n"
#     f"Ponto flutuante     : {numero_flutuante:.2f}\n"
#     f"Ponto flutuante com variável    : {numero_inteiro:.{casas_decimais}f}\n"#**
#     f"Notação científica  : {numero_flutuante:e}\n"
#     f"Percentual          : {0.85:.2%}\n"
#     f"Separadores milhar  : {numero_flutuante:,.2f}\n"
# )

# print(formatado)

#Métodos (a.isnumeric())################################################################################
# String de exemplo
s = "  Hello, World! 12345  "

# Métodos que não aceitam argumentos
print("Original:", repr(s))
print("Uppercase:", s.upper())            # Converte para maiúsculas
print("Lowercase:", s.lower())            # Converte para minúsculas
print("Strip:", s.strip())                # Remove espaços em branco nas extremidades
print("Capitalize:", s.capitalize())      # Capitaliza o primeiro caractere
print("Title:", s.title())                # Capitaliza cada palavra
print("Swapcase:", s.swapcase())          # Troca maiúsculas por minúsculas e vice-versa

# Métodos que aceitam argumentos
print("Replace 'Hello' with 'Hi':", s.replace("Hello", "Hi"))  # Substitui uma substring por outra
print("Count 'l':", s.count('l'))                              # Conta a ocorrência de um caractere
print("Starts with '  Hello':", s.startswith("  Hello"))       # Verifica se a string começa com a substring
print("Ends with '12345  ':", s.endswith("12345  "))           # Verifica se a string termina com a substring
print("Find 'World':", s.find("World"))                        # Encontra a posição de uma substring
print("Index of 'World':", s.index("World"))                   # Encontra a posição de uma substring (gera erro se não encontrar)
print("Split by space:", s.split(" "))                         # Divide a string por um delimitador
print("Join with '-':", "-".join(['Hello', 'World']))          # Junta elementos de uma lista com um delimitador

# Métodos de verificação
print("Is alphanumeric:", s.isalnum())                         # Verifica se a string é alfanumérica
print("Is alphabetic:", s.isalpha())                           # Verifica se a string é alfabética
print("Is digit:", s.isdigit())                                # Verifica se a string contém apenas dígitos
print("Is numeric:", s.isnumeric())                            # Verifica se a string contém apenas caracteres numéricos
print("Is space:", s.isspace())                                # Verifica se a string contém apenas espaços
print("Is title:", s.istitle())                                # Verifica se a string está capitalizada

# Manipulação de espaços em branco
print("Left strip:", s.lstrip())                               # Remove espaços em branco à esquerda
print("Right strip:", s.rstrip())                              # Remove espaços em branco à direita


