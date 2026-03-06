tarefas = []

def adicionar_tarefa(titulo:str):
    tarefas_dict = {
        "titulo": titulo,
        "concluido": False,
    } 
    tarefas.append(tarefas_dict)
    print(f"\nTarefa '{titulo}' Adicionado a sua lista de tarefas com sucesso!")
    return

def visualizar_tarefa():
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = " ✓ " if tarefa["concluido"] else " "
        tarefa = tarefa["titulo"]
        print(f"{indice}. [{status}] {tarefa}")
    return

def atualizar_tarefa(indice_tarefa:int, nova_tarefa:str):
    indice_tarefa_ajustado = indice_tarefa - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["titulo"] = nova_tarefa
        print(f"Tarefa '{indice_tarefa}'. Atualizada para '{nova_tarefa}'")
    else:
        print("\nDigite um índice válido e correspondente a tarefa acima!")
    return

def completar_tarefa(indice_tarefa:int):
    indice_tarefa_ajustado = indice_tarefa -1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        if tarefas[indice_tarefa_ajustado]["concluido"]:
            print("\nTarefa já concluída!")
            return

        concluir = input("Deseja concluir esta tarefa? (s/n): ")
        if concluir.lower() == "s":
            tarefas[indice_tarefa_ajustado]["concluido"] = True
            indice = indice_tarefa
            print(f"Tarefa '{indice}'. concluída com Sucesso!")
        return
    else:
        print("Indice de tarefa inexistente!")
    return

def deletar_tarefa_concluída():
    for tarefa in tarefas:
        if tarefa["concluido"]:
            print(tarefa["titulo"])
    return

def main():
    
    while True:
        
        
        print("\nBem Vindo ao nosso Sistema de gerenciamento de Tarefas!")
        print("Escolha uma das opções a seguir:")
        print("OPÇÃO 1 - ADICIONAR TAREFA")
        print("OPÇÃO 2 - VISUALIZAR TAREFA")
        print("OPÇÃO 3 - ATUALIZAR TAREFA")
        print("OPÇÃO 4 - COMPLETAR TAREFA")
        print("OPÇÃO 5 - DELETAR TAREFA CONCLUIDA")
        print("OPÇÃO 6 - SAIR\n")
        
        try:
            opcao = int(input("\nDigite o numero da opção que deseja: "))
            
            if opcao == 1:
                titulo = input("\nDigite o titulo da sua tarefa: ")
                
                adicionar_tarefa(titulo)
            
            elif opcao == 2:
                visualizar_tarefa()
            
            elif opcao == 3:
                visualizar_tarefa()
                indice_tarefa = int(input("Digite o índice da tarefa que deseja atualizar: "))
                nova_tarefa = input("Digite o novo nome que deseja dar para esta tarefa: ")
                atualizar_tarefa(indice_tarefa, nova_tarefa)
                
            elif opcao == 4:
                visualizar_tarefa()
                indice_tarefa = int(input("Digite o índice da tarefa que deseja concluir: "))
                completar_tarefa(indice_tarefa)
            
            elif opcao == 5:
                deletar_tarefa_concluída()
            
            elif opcao == 6:
                print("\nObrigado Por Utilizar Nosso Sistema!")
                print("Saindo...")
                break
            
            else:
                print("\nPorfavor digite um número inteiro e que esteja no menu!")
                
        except ValueError:
            print(f"\nPorfavor digite o número que está disponível no menu 1 - 6")
            
if __name__ == "__main__":
    main()