from gs2 import listar_medicos, listar_enderecos_hospitalares, listar_planos_saude, exportar_enderecos_hospitalares_json, consulta_paciente,exportar_planos_saude_json, exportar_medicos_json



     
def menu():
    sintomas = "" 

    while True:
        print("\nBem-vindo(a) à PrevinaTech! Escolha a opção desejada:")
        print("1 - Não está se sentindo bem?")
        print("2 - Marcar consulta")
        print("3 - listar medicos ")
        print("4 - listar_planos_saude")
        print("5 - listar endereço do hospital")
        print("6 - Exportar endereco para JSON")
        print("7 - Exportar plano de saude para JSON")
        print("8 - exportar medicos para json")
        print("0 - Sair")

        opcao = input("Digite o número da opção desejada : ")
        ##OBS: PARA FAZER A LISTAGEM DA COLUNA DO BANCO DE DADOS, VOCÊ SÓ CONSEGUE UMA POR VEZ. EX: SE QUISER CONSULTAR OS PACIENTE,
        ## E EM SEGUIDA OS MEDICOS, TEM QUE RODAR O CODIGO NOVAMENTE, SE NÃO DA ERRO, ISSO ACONTECE PORQUE ESTÃO EM TABELAS DIFERENTES E
        ## E O BANCO DE DADOS ABRE UMA CONSULTA POR VEZ, SEGUIR O MESMO PROCEDIMENTO COM JSON, CASO OCORRA ERRO NAS DEMAIS OPÇÕES, FAÇA O MESMO PROCEDIMENTO.
        
        if opcao == '1':
         sintomas = input("Descreva seus sintomas (separados por vírgula): ")
        if "febre" in sintomas.lower():
         print("Recomendamos que você consulte um médico clínico geral.")
        elif "tosse" in sintomas.lower():
         print("Recomendamos que você consulte um pneumologista.")
        elif "dor de cabeça" in sintomas.lower():
         print("Recomendamos que você consulte um neurologista.")
        elif "dor abdominal" in sintomas.lower():
         print("Recomendamos que você consulte um gastroenterologista.")
        elif "dor nas articulações" in sintomas.lower():
         print("Recomendamos que você consulte um reumatologista.")
        elif "dor nas costas" in sintomas.lower():
         print("Recomendamos que você consulte um ortopedista.")
        elif "falta de ar" in sintomas.lower():
         print("Recomendamos que você consulte um pneumologista.")
         
         print
         
         
         
        elif opcao == "2":
         opcao = input("Escolha o tipo de consulta (online/presencial): ")
         consulta_paciente(opcao)
    
        elif opcao == '3':
            listar_medicos()

    
        elif opcao == '4':
            listar_planos_saude()


        
            
        elif opcao == '6':
           nome_arquivo = input("Digite o nome do arquivo JSON para exportar: ")
           exportar_enderecos_hospitalares_json("enderecos_hospitalares_exportados")
           
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        
        
        elif opcao == "5":
         listar_enderecos_hospitalares()

    
        elif opcao == "7":
            nome_arquivo = input("Digite o nome do arquivo JSON para exportar: ")
            exportar_planos_saude_json("saude") 
 
        elif opcao == "8":
            exportar_medicos_json("nome_do_arquivo")

 
 
 
             
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")



