'''Programa de cadastro de usuario'''
nome=[]
senha=[]
endereco=[]
estado=[]
cidade=[]
cep=[]

cadastroQtde = int(input("Quantos cadastro deseja realizar? "))

for cadastro in range(cadastroQtde):
    nome.append(input("Digite o nome do cliente: "))
    senha.append(int(input("Digite a senha (somente senha numerica): ")))
    endereco.append(input("digite seu endereco: "))
    estado.append(input("Digite o nome do seu Estado: "))
    cidade.append(input("Digite o nome da sua cidade: "))
    cep.append(int(input("Digite seu CEP(sem traço e ponto): ")))
    print(nome,senha,endereco,estado,cidade,cep)
    print()