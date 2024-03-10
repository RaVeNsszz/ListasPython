print("""Em que turno você estuda:
M para Matutino
V para Vespertino
N para Noturno """)
turno = input("Turno: ").title()
if turno == "M" or turno == "Matutino":
    print("Bom Dia!!!")
elif turno == "V" or turno == "Vespentino":
    print("Boa Tarde!!!")
elif turno == "N" or turno == "Noturno":
    print("Boa Noite!!!")
else:
    print("Turno inválido")