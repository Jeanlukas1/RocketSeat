lista_de_tarefas = []

def adicionar_tarefa(titulo:str, sobre:str):
    """Função de adiciona uma tarefa a uma lista de tarefas, caso a lista esteja vazia, isso é tratado e informado ao 
    Usuário que ele ainda não adicionou nenhuma tarefa na sua lista"""
    
    dicionario_de_tarefas = {
        "titulo": titulo,
        "sobre": sobre,
    }
    
    lista_de_tarefas.append(dicionario_de_tarefas)
    return

def visualizar_tarefa():
    """Função que lista as tarefas adicionada pelo usuário em sua lista"""
    
    if not lista_de_tarefas:
        print("Lista vazia!")
    for tarefa in lista_de_tarefas:
        print(f"""
              Titulo: {tarefa["titulo"]}
              Assunto: {tarefa["sobre"]}
              """)
    return
    
def atualizar_tarefa(titulo:str):
    for tarefa in lista_de_tarefas:
        if titulo in tarefa["titulo"]:
            try:
                pergunta = int(input("""Oque Deseja Atualizar? 
                                        1 - TITULO
                                        2 - ASSUNTO  """))
                if pergunta == 1:
                    novo_titulo = input("Digite um novo titulo para sua tarefa: ")
                    tarefa["titulo"] = novo_titulo
                    
                elif pergunta == 2:
                    novo_assunto = input("Digite um novo assunto para sua tarefa: ")
                    tarefa["sobre"] = novo_assunto
                    
                else:
                    print("Porfavor insira um número inteiro e que esteja dentro das opções!")
                
            except ValueError:
                print("Insira um número inteiro!")
    print("Tarefa não encontrada!")
    return
          
def completar_tarefa(titulo:str):
    for tarefa in lista_de_tarefas:
        if titulo == tarefa["titulo"]:
            concluir_tarefa = input("Deseja concluir esta tarefa? s/n")
            
            if concluir_tarefa == 's':
                lista_de_tarefas.remove(tarefa)
                print(f"tarefa '{titulo}' concluída com sucesso!")
                return
            
    print("Tarefa não encontrada!")
    return

def deletar_tarefa(titulo:str):
    for tarefa in lista_de_tarefas:
        if titulo == tarefa["titulo"]:
            lista_de_tarefas.remove(tarefa)
            print(f"Tarefa com titulo '{titulo}' deletada")
            return
    
    print("Tarefa não encontrada!")
    return


def main():
    
    while True:
        
        print()
        print("Bem Vindo ao nosso Sistema de gerenciamento de Tarefas!")
        print()
        print("Escolha uma das opções a seguir:")
        print("OPÇÃO 1 - ADICIONAR TAREFA")
        print("OPÇÃO 2 - VISUALIZAR TAREFA")
        print("OPÇÃO 3 - ATUALIZAR TAREFA")
        print("OPÇÃO 4 - COMPLETAR TAREFA")
        print("OPÇÃO 5 - DELETAR TAREFA")
        print("OPÇÃO 6 - SAIR")
        print()
        
        try:
            opcao = int(input("Digite o numero da opção que deseja: "))
            
            if opcao == 1:
                titulo = input("Digite o titulo da sua tarefa: ")
                sobre = input("Assunto: ")
                print()
                if not titulo or not sobre:
                    print("Porfavor digite um titulo válido e um assunto")
                    continue
                
                print()
                adicionar_tarefa(titulo, sobre)
                print(f"Tarefa com Titulo: {titulo} adicionada na sua lista de tarefas com sucesso!")
            
            elif opcao == 2:
                visualizar_tarefa()
            
            elif opcao == 3:
                titulo = input("Digite o Titulo da tarefa que deseja atualizar: ")
                atualizar_tarefa(titulo)
                
            elif opcao == 4:
                titulo = input("Digite o titulo da tarefa que deseja concluir: ")
                completar_tarefa(titulo)
            
            elif opcao == 5:
                titulo = input("Digite o titulo da tarefa que deseja deletar: ")
                deletar_tarefa(titulo)
            
            elif opcao == 6:
                print("Obrigado Por Utilizar Nosso Sistema!")
                print("Saindo...")
                break
            
            else:
                print("Porfavor digite um número inteiro e que esteja no menu!")
                
        except ValueError:
            print(f"Porfavor digite o número que está disponível no menu 1 - 6")
            
if __name__ == "__main__":
    main()
    