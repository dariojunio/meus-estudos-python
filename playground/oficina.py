class Carros:
  def __init__(self, modelo, placa, manu):
    self.modelo = modelo
    self.placa = placa
    self.manu = manu

  def exibir_dados(self):
    print(f'Modelo: {self.modelo}, Placa: {self.placa}, Tipo de manutencao: {self.manu}')

garagem = []

def cadastrar_carro():
 while True:
    print('\n--- CADASTRO DE VEÍCULO ---')

    modelo_input = input("Modelo do carro (ou 'sair' para encerrar): ")
    
    if modelo_input.lower() == 'sair':
        break
        
    placa_input = input('Placa do carro: ')
    manu_input = input('Tipo de manutencao: ')

    novo_carro = Carros(modelo_input, placa_input, manu_input)

    garagem.append(novo_carro)
    print(f' {modelo_input} adicionado com sucesso!')


def lista_carros():
  print('\n CARROS CADASTRADOS:')

  for carro in garagem:
    carro.exibir_dados()


while True:
    print('\n===== OFICINA DO D9 =====')
    opcao = input("[1] Cadastrar | [2] Ver Lista | [0] Sair: ")

    if opcao == '1':
        cadastrar_carro()
    elif opcao == '2':
        lista_carros()
    elif opcao == '0':
        print("Fechando sistema... Até logo!")
        break
    else:
        print("Opção inválida!")
