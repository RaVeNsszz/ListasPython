"""A secretária de dra Ivone, Clara, precisa dizer para os pacientes que ligam qual médico irá
atendê-los dependendo do dia que eles quiserem marcar e da especialidade escolhida. Como a
escala de especialidades, de médicos e de dias é muito cheia, seu software irá ajudar a ela dar
essa informação.
Lembre de avisar que não tem médico naquele dia, caso aquele horário não
tenha ninguém na escala.
Mapeie essa escala para seu programa, de tal forma, que ele responda corretamente a Clara:"""

esp = input("Digite a especialidade do médico: [Oftalmologista, Cardiologista e Pediatra] ")
dia = input("Digite o dia para consulta: ")

esp = esp.upper()
dia = dia.upper()

if esp == "OFTALMOLOGISTA":
    if dia == "SEGUNDA":
        print("Disponíveis: Mauro (Manhã, Tarde e Noite) e Ana (Manhã e Tarde). ")
    elif dia == "TERÇA":
        print("Disponíveis: Lucas (Manhã e Tarde) e Ana (Manhã e Tarde). ")
    elif dia == "QUARTA":
        print("Disponíveis: Mauro (Manhã e Tarde) e Ana (Manhã e Tarde). ")
    elif dia == "QUINTA":
        print("Disponíveis: Lucas (Manhã, Tarde e Noite) e Ana (Manhã e Tarde). ")
    elif dia == "SEXTA":
        print("Disponíveis: Mauro (Manhã e Noite), Lucas (Tarde e Noite) e Ana (Manhã e Tarde). ")
    else:
        print("Nenhum médico disponível para esse dia. ")

elif esp == "CARDIOLOGISTA":
    if dia == "SEGUNDA":
        print("Disponíveis: Cláudio (Manhã e Noite) e Carla (Manhã, Tarde e Noite). ")
    elif dia == "TERÇA":
        print("Disóníveis: Cláudio (Tarde e Noite) e Carla (Manhã, Tarde e Noite). ")
    elif dia == "QUARTA":
        print("Disponíveis: Rita (Tarde e Noite) e Cláudio (Manhã e Tarde). ")
    elif dia == "QUINTA":
        print("Disponível: Rita (Manhã, Tarde e Noite). ")
    elif dia == "SEXTA":
        print("Disponivel: Rita (Tarde e Noite). ")
    else:
        print("Nenhum médico disponível para esse dia.. ")

elif esp == "PEDIATRA":
    if dia == "SEGUNDA":
        print("Disponíveis: Alice (Tarde e Noite), Antônio (Manhã e Tarde) e Elis (Manhã, Tarde e Noite). ")
    elif dia == "TERÇA":
        print("Dsiponíveis: Ruan (Manhã e Tarde) e Antônio (Manhã e Tarde). ")
    elif dia == "QUARTA":
        print("Disponíveis: Alice (Tarde e Noite) e Antônio (Manhã e Tarde). ")
    elif dia == "QUINTA":
        print("Disponível: Ruan (Manhã e Tarde). ")
    elif dia == "SEXTA":
        print("Disponíveis: Alice (Tarde e Noite), Ruan (Manhã e Tarde) e Elis (Manhã, Tarde e Noite). ")
    else:
        print("Nenhum médico disponível para esse dia.. ")
else:
    print("Especialidade Inválida. ")