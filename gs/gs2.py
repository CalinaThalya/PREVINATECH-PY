import datetime
import json
import oracledb


conexao = oracledb.connect("rm552539/130701@oracle.fiap.com.br/orcl")
cursor = conexao.cursor()

pacientes = []

def listar_medicos():
    try:
        cursor.execute("SELECT * FROM T_PVTC_MEDICO")
        medicos_bd = cursor.fetchall()

        print("\nLista de Médicos:")
        for medico in medicos_bd:
            print(f"ID: {medico[0]}, CRM: {medico[1]}, Especialidade: {medico[2]}, "
                  f"Cadastrado em: {medico[3]}, Usuário: {medico[4]}")

    except oracledb.DatabaseError as e:
        print(f"Erro ao listar médicos: {e}")

    finally:
        cursor.close()
        conexao.close()
        
        
        
def listar_enderecos_hospitalares():
    try:
        cursor.execute("SELECT * FROM T_PVTC_ENDERECO_HOSPITALAR")
        enderecos_bd = cursor.fetchall()

        print("\nLista de Endereços Hospitalares:")
        for endereco in enderecos_bd:
            print(f"ID: {endereco[0]}, Logradouro: {endereco[1]}, Complemento: {endereco[2]}, "
                  f"Cadastrado em: {endereco[3]}, Usuário: {endereco[4]}")

    except oracledb.DatabaseError as e:
        print(f"Erro ao listar endereços hospitalares: {e}")

    finally:
        cursor.close()
        conexao.close()
       


def listar_planos_saude():
    try:
        cursor.execute("SELECT * FROM T_PVTC_PLANO_SAUDE")
        planos_saude_bd = cursor.fetchall()

        print("\nLista de Planos de Saúde:")
        for plano_saude in planos_saude_bd:
            print(f"ID: {plano_saude[0]}, Razão Social: {plano_saude[1]}, Nome Fantasia: {plano_saude[2]}, "
                  f"Plano de Saúde: {plano_saude[3]}, CNPJ: {plano_saude[4]}, Contato: {plano_saude[5]}, "
                  f"Cadastrado em: {plano_saude[6]}, Usuário: {plano_saude[7]}")

    except oracledb.DatabaseError as e:
        print(f"Erro ao listar planos de saúde: {e}")

    finally:
        cursor.close()
        conexao.close()
        
def consulta_paciente(opcao_consulta):
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu CPF: ")
    data_consulta = input("Informe a data da consulta (formato DD/MM/AAAA): ")
    hora_consulta = input("Informe a hora da consulta, atuamos 24horas (formato HH:MM): ")

    try:
        data_hora_consulta = datetime.datetime.strptime(f"{data_consulta} {hora_consulta}", "%d/%m/%Y %H:%M")
    except ValueError:
        print("Erro: Formato de data ou hora incorreto. Use DD/MM/AAAA para data e HH:MM para hora.")
        return

    if opcao_consulta == "online":
        print(f"Consulta online marcada com sucesso para {nome}, {cpf}, {data_hora_consulta.strftime('%d/%m/%Y %H:%M')} .")
    elif opcao_consulta == "presencial":
        print(f"Consulta presencial marcada com sucesso para {nome}, {cpf}, {data_hora_consulta.strftime('%d/%m/%Y %H:%M')}.")
    else:
        print("Opção de consulta inválida. Escolha 'online' ou 'presencial'.")




def default_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    raise TypeError("Type not serializable")

def exportar_enderecos_hospitalares_json(nome_arquivo):
    try:
        cursor.execute("SELECT * FROM T_PVTC_ENDERECO_HOSPITALAR")
        enderecos_hospitalares_bd = cursor.fetchall()

        enderecos_hospitalares_json = []
        for endereco_hospitalar in enderecos_hospitalares_bd:
            endereco_hospitalar_dict = {
                'ID': endereco_hospitalar[0],
                'Logradouro': endereco_hospitalar[1],
                'Complemento': endereco_hospitalar[2],
                'Cadastro em': endereco_hospitalar[3],
                'Usuário': endereco_hospitalar[4]
            }
            enderecos_hospitalares_json.append(endereco_hospitalar_dict)

        with open(nome_arquivo, 'w') as json_file:
            json.dump(enderecos_hospitalares_json, json_file, indent=2)

        print(f"Endereços hospitalares exportados para o arquivo {nome_arquivo}.json com sucesso.")

    except oracledb.DatabaseError as e:
        print(f"Erro ao exportar endereços hospitalares para JSON: {e}")

    finally:
        cursor.close()
        conexao.close()
        
        
        
def default_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    raise TypeError("Type not serializable")

def default_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    raise TypeError("Type not serializable")

cursor = conexao.cursor()

def exportar_planos_saude_json(nome_arquivo):
    try:
        query = "SELECT * FROM T_PVTC_PLANO_SAUDE"
        cursor.execute(query)
        planos_saude_bd = cursor.fetchall()

        planos_saude_json = []
        for plano_saude in planos_saude_bd:
            plano_saude_dict = {
                'ID': plano_saude[0],
                'Razão Social': plano_saude[1],
                'Nome Fantasia': plano_saude[2],
                'Plano de Saúde': plano_saude[3],
                'CNPJ': plano_saude[4],
                'Contato': plano_saude[5],
                'Cadastrado em': plano_saude[6],
                'Usuário': plano_saude[7]
            }
            planos_saude_json.append(plano_saude_dict)

        with open(f"{nome_arquivo}.json", 'w') as json_file:
            json.dump(planos_saude_json, json_file, indent=2, default=default_serializer)

        print(f"Planos de Saúde exportados para o arquivo {nome_arquivo}.json com sucesso.")

    except oracledb.DatabaseError as e:
        print(f"Erro ao exportar Planos de Saúde para JSON: {e}")

    finally:
        cursor.close()
        conexao.close()

def default_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    raise TypeError("Type not serializable")


def exportar_medicos_json(nome_arquivo):
    try:
        cursor = conexao.cursor()

        query = "SELECT * FROM T_PVTC_MEDICO"
        cursor.execute(query)
        medicos_bd = cursor.fetchall()

        medicos_json = []
        for medico in medicos_bd:
            medico_dict = {
                'ID': medico[0],
                'CRM': medico[1],
                'Especialidade': medico[2],
                'Cadastrado_em': medico[3],
                'Usuario': medico[4]
            }
            medicos_json.append(medico_dict)

        with open(f"{nome_arquivo}.json", 'w') as json_file:
            json.dump(medicos_json, json_file, indent=2, default=default_serializer)

        print(f"Médicos exportados para o arquivo {nome_arquivo}.json com sucesso.")

    except oracledb.DatabaseError as e:
        print(f"Erro ao exportar médicos para JSON: {e}")

    finally:
        cursor.close()
        conexao.close()
