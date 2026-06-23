import os

restaurantes = [{"nome" : "Praça", "categoria" :"Japonesa", "ativo" : False},
                {"nome" : "Pizza Suprema", "categoria" :"Pizaa", "ativo" : True},
                {"nome" : "Cantina", "categoria" :"Italiano", "ativo" : False}]

def exbir_nome_do_programa():
     """Exibe o nome do programa formatado para o usuário"""
     print("𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠\n")

def exibir_opcoes():
    """Exibe as opções do menu para o usuário"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
     """Finaliza o aplicativo"""
     exibir_subtitulo("Finalizar app ")

def voltar_ao_menu_principal(): 
      """Volta ao menu principal"""  
      input("\nDigite uma tecla para voltar ao menu principal.\n")
      main()

def opcao_invalida():
     """Exibe uma mensagem de opção inválida e volta ao menu principal"""
     os.system("clear")
     print("Opção inválida.\n")
     voltar_ao_menu_principal ()

def exibir_subtitulo(texto):
      """Exibe um subtítulo formatado para o usuário"""
      os.system("clear")
      linha = "*" * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      """Cadastra um novo restaurante com nome, categoria e estado inativo por padrão"""
      exibir_subtitulo("Cadastro de novos restaurantes")
      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f"Restaurante '{nome_do_restaurante}' cadastrado com sucesso!\n")
      voltar_ao_menu_principal()

 
def listar_restaurantes():
      """Lista todos os restaurantes cadastrados"""
      exibir_subtitulo("Listando os restaurantes")

      print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")

      for restaurante in restaurantes:
          nome_restaurante = restaurante["nome"]
          categoria = restaurante["categoria"]
          ativo = " ativado" if restaurante["ativo"] else " desativado"
          print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}") 
      voltar_ao_menu_principal()

def alterna_estado_restaurante():
    """Alterna o estado de um restaurante entre ativo e inativo com base no nome fornecido pelo usuário"""
    exibir_subtitulo("Alternar estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            if restaurante["ativo"]:
                mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!"
            else:
                mensagem = f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            
            print(mensagem)          
    if not restaurante_encontrado:
            print("O restaurante não foi encontrado.")         

    voltar_ao_menu_principal()

def escolher_opcao():
    """Lê a opção escolhida pelo usuário e executa a função correspondente"""
    try:
        opcao_escolhida = int(input("Digite a opção desejada: "))

        if   opcao_escolhida == 1:
                cadastrar_novo_restaurante()   
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
                alterna_estado_restaurante()
        elif opcao_escolhida == 4:  
                finalizar_app()
        else:  
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
     """Função principal que inicia o aplicativo e exibe o menu para o usuário"""
     os.system("clear")
     exbir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

if __name__ == "__main__":
       """Verifica se o script está sendo executado diretamente e chama a função principal para iniciar o aplicativo"""
       main()

