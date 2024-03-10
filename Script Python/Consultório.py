
dia = str(input("Dia(Ex: seg,ter,qua,qui,sex): "))
if dia == "seg":
    print("""Médicos disponiveis | Especialidades 
    Mauro - Oftalmologista
    Ana - Oftalmologista
    Claudio - Cardiologista
    Carla - Cardiologista
    Aline - Pediatra
    Antônio - Segunda
    Elis - Pediatra
    """)
    print("""Digite
    O - Para saber mais detalhes sobre o serviço de Oftalmologista
    C - Para saber mais detalhes sobre o serviço de Cardiologista 
    P - Para saber mais detalhes sobre o serviço de Pediatra""")
    ser = str(input("Serviço: ")).upper()
    if ser == "O":
        print("""Horários
        Mauro - Manhâ, Tarde e Noite
        Ana - Manhâ e Tarde""")
        
        turno = str(input("Turno(Ex.:Manhã,Tarde ou Noite): ")).title()

        if turno == "Manhâ" :
            profissional = str(input("Profissional: ")).title()
            if profissional == "Mauro":
                print("Sua consulta foi marcada na segunda, para o serviço de Oftalogista com o Dr. Mauro no periodo da Manhâ")
            else:
                print("Sua consulta foi marrcada na segunda, para o serviço de Oftamologista com a Dr(a) Ana no período da Manhâ")
       
        elif turno == "Tarde" :
            profissional = str(input("Profissional: ")).title()

            if profissional == "Mauro":
                print("Sua consulta foi marcada na segunda, para o serviço de Oftalogista com o Dr. Mauro no periodo da Tarde")
    
            else: 
                print("Sua consulta foi marcada na segunda, para o serviço de Oftamologista com a Dr(a) Ana no período da Tarde")

        else:
            print("Sua consulta foi marcada na segunda, para o serviço de Oftamologista com o Dr Mauro no período da Noite")

    elif ser == "C":
        print("""Horários
        Claudio - Manha e Noite
        Carla - Manhâ, Tarde e Noite""")

        turno = str(input("Turno(Ex.:Manhã,Tarde ou Noite): ")).title
        if turno == "Manhâ" :
            profissional = str(input("Profissional: "))
            if profissional == "Claudio":
                print("Sua consulta foi marcada na segunda, para o serviço de Cardiogista com o Dr Claudio no período da Manhâ")
            
            else: 
                print("Sua consulta foi marcada na segunda, para o serviço de Cardiogista com a Dr(a) Carla no período da Manhâ")
        
        elif turno == "Noite":
            profissional = str(input("Profissional: ")).title()
            if profissional == "Claudio":
                print("Sua consulta foi marcada na segunda, para o serviço de Cardiogista com o Dr Claudio no período da Noite")
            else:
                print("Sua consulta foi marcada na segunda, para o serviço de Cardiogista com a Dr(a) Carla no período da Noite")
        
        else:
            print("Sua consulta foi marcada na segunda, para o serviço de Cardiogista com a Dr(a) Carla no período da Tarde")

    else:
        print("""Horários
        Alice - Tarde e Noite
        Antônio - Manhã e Tarde
        Elis - Manhã, Tarde e Noite""")

        turno = str(input("Turno(Ex.:Manhã,Tarde ou Noite): ")).title
        if turno == "Manhã":
            profissional = str(input("Profissional: ")).title
            if profissional == "Antônio" or profissional =="Antonio":
                print("Sua consulta foi marcada naa segunda, para o serviço de Pediatra com o Dr Antônio no período da Manhã")
            
            else :
                print("Sua consulta foi marcada para a segunda, para o serviço de Pediatra com o Dr Elis no período da Manhã")
        elif turno == "Tarde":
            profissional = str(input("Profissional: ")).title
            if profissional == "Alice":
                print("Sua consulta foi marcada para a segunda, para o serviço de Pediatra com a Dr(a) Alice no período da Tarde")

            elif profissional == "Antônio" or profissional == "Antonio":
                print("Sua consulta foi marcada para a segunda, para o serviço de Pediatra com o Dr Antônio no período da Tarde")
            
            else:
                print("Sua consulta foi marcada para a segunda, para o serviço de Pediatra com o Dr Elis no período da Tarde")
        
        else:
            profissional = str(input("Profissional: ")).title
            if profissional == "Alice":
                print("Sua consulta foi marcada para a segunda, para o serviço de Pediatra com a Dr(a) Alice no período da Noite")
            else:
                print("Sua consulta foi marcada para a segunda, para o serviço de Pediatra com o Dr Elis no período da Noite")

elif dia == "ter":
    print("""Médicos disponiveis | Especialidades
    Lucas - Oftalmologista
    Ana - Oftalmologista
    Cláudio - Cardiologista
    Carla - Cardiologista
    Ruan - Pediatra
    """)
    print("""Digite
    O - Para saber mais detalhes sobre o serviço de Oftalmologista
    C - Para saber mais detalhes sobre o serviço de Cardiologista 
    P - Para saber mais detalhes sobre o serviço de Pediatra""")
    ser = str(input("Serviço: ")).upper()
    if ser == "O":
        print("""Horários
        Lucas - Manhã  e Tarde
        Ana - Manhâ e Tarde
        """)
        turno = str(input("Turno: ")).title
        if turno == "Manhâ" :
            profissional = str(input("Profissional: ")).title
            if profissional == "Lucas":
                print("Sua consulta foi marcada na Terça, para o serviço de Oftalmologista com o Dr Lucas no período da Manhã")
            
            else :
                print("Sua consulta foi marcada para a Terça, para o serviço de Pediatra com a Dr(a) Ana no período da Manhã")
            
        else:
            profissional = str(input("Profissional: ")).title
            if profissional == "Lucas":
                print("Sua consulta foi marcada na Terça, para o serviço de Oftalmologista com o Dr Lucas no período da Manhã")
            
            else:
                print("Sua consulta foi marcada na Terça, para o serviço de Oftalmologista com a Dr(a) Ana no período da Tarde")

    elif ser == "C":
        print(""" Horários
        Cláudio - Tarde e Noite
        Carla - Manhâ, Tarde e Noite""")

        turno = str(input("Turno: ")).title
        if turno == "Tarde" :
            profissional = str(input("Profissional: ")).title
            if profissional == "Cláudio" or profissional == "Claudio":
                print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com o Dr Cláudio no período da Tarde")
            
            else:
                print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com a Dr(a) Carla no período da Tarde")
        
        elif turno == "Noite":
            profissional = str(input("Profissional: ")).title
            if profissional == "Claudio" or profissional == "Cláudio":
                print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com o Dr Cláudio no período da Noite")
            
            else:
                print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com a Dr(a) Carla no período da Noite")

        else: 
            print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com o Dr(a) Carla no período da Manhã")
    
            
    else:
        print("""Horários
        Antônio  - Manhâ e Tarde""")
        turno = str(input("Turno: ")).title()
        if turno == "Manhã":
            print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com o Dr Antônio no período da Manhã")
        
        else:
            print("Sua consulta foi marcada na Terça, para o serviço de Cardiologista com o Dr Antônio no período da Tarde")

elif dia == "qua":
    print("""Médicos disponiveis | Especialidades 
    Mauro - Oftalmologista
    Ana - Oftalmologista
    Rita - Cardiologista
    Cláudio -Cardiologista
    Alice - Pediatra
    Antônio - Pediatra
    """)
    print("""Digite
    O - Para saber mais detalhes sobre o serviço de Oftalmologista
    C - Para saber mais detalhes sobre o serviço de Cardiologista 
    P - Para saber mais detalhes sobre o serviço de Pediatra""")
    ser = str(input("Serviço: ")).upper()
    if ser == "O":
        print("""Horários
        Mauro - Manhã e Tarde
        Ana - Manhã e Tarde
        """)
        turno = str(input("Turno: ")).title()
        if turno == "Manhã":
            profissional = str(input("Profissional: ")).title()
            if profissional == "Mauro":
                print("Sua consulta foi marcada na Quarta, para o serviço de Ofitalmologista com o Dr Mauro no período da Manhã")
            
            else:
                print("Sua consulta foi marcada na Quarta, para o serviço de Ofitalmologista com a Dr(a) Ana no período da Manhã")
        
        else:
            profissional = str(input("Profissional: "))
            if profissional == "Mauro":
                print("Sua consulta foi marcada na Quarta, para o serviço de Ofitalmologista com o Dr Mauro no período da Tarde")
            
            else:
                print("Sua consulta foi marcada na Quarta, para o serviço de Ofitalmologista com a Dr(a) Ana no período da Tarde")

    elif  ser == "C":
        print("""Horários
        Rita - Tarde e Noite
        Cláudio - Manhã e Tarde
        """)
        turno = str(input("Turno: ")).title()
        if turno == "Tarde":
            profissional = str(input("Profissional: ").title())
            if profissional == "Rita":
                print("Sua consulta foi marcada na Quarta, para o serviço de Cardiologista com a Dr(a) Rita no período da Tarde.")
            else:
                print("Sua consulta foi marcada na Quarta, para o serviço de Cardiologista com o Dr Cláudio no período da Tarde.")
        
        elif turno == "Manhã":
            print("Sua consulta foi marcada na Quarta, para o serviço de Cardiologista com o Dr Cláudio no período da Manhã.")
        
        else:
            print("Sua consulta foi marcada na Quarta, para o serviço de Cardiologista com a Dr(a) Rita no período da Noite.")
        
    else:
        print("""Horários
        Alice - Tarde e Noite
        Antônio - Manhâ e Tarde
        """)
        turno = str(input("Turno: ")).upper()
        if turno == "Tarde":
            profissional = str(input("Profissional: ")).title() 
            if profissional == "Alice":
                print("Sua consulta foi marcada na Quarta, para o serviço de Pediatra com a Dr(a) Alice no período da Tarde.")
            
            else:
                print("Sua consulta foi marcada na Quarta, para o serviço de Pediatra com o Dr Antônio no período da Tarde.")
        
        elif turno == "Manhã":
            print("Sua consulta foi marcada na Quarta, para o serviço de Pediatra com o Dr Antônio no período da Manhã.")
        
        else:
            print("Sua consulta foi marcada na Quarta, para o serviço de Pediatra com a Dr(a) Alice no período da Noite.")
    

elif dia == "qui":
    print("""Médicos disponiveis | Especialidades
    Lucas - Oftalmologista
    Ana - Oftalmologista
    Rita - Cardiologista
    Ruan - Pediatra
    """)
    print("""Digite
    O - Para saber mais detalhes sobre o serviço de Oftalmologista
    C - Para saber mais detalhes sobre o serviço de Cardiologista 
    P - Para saber mais detalhes sobre o serviço de Pediatra""")
    ser = str(input("Serviço: ")).upper()
    if ser == "O":
        print("""Horários
        Lucas - Manhã e Tarde
        Ana - Manha e Tarde""")
        turno = str(input("Turno: ")).title()
        if turno == "Tarde":
            profissional = str(input("Profissional: ")).title()
            if profissional == "Lucas":
                print("Sua consulta foi marcada na Quinta, para o serviço de Oftalmologista com o Dr Lucas no período da Tarde.")
            
            else:
                print("Sua consulta foi marcada na Quinta, para o serviço de Oftalmologista com a Dr(a) Ana no período da Tarde.")
        
        else:
            profissional = str(input("Profissional: ")).title()
            if profissional == "Lucas":
                print("Sua consulta foi marcada na Quinta, para o serviço de Oftalmologista com o Dr Lucas no período da Manhã.")
            
            else:
                print("Sua consulta foi marcada na Quinta, para o serviço de Oftalmologista com a Dr(a) Ana no período da Manhã.")

    
    elif ser == "C":
        print("""Horários
        Rita - Manhã, tarde e Noite""")
        turno = str(input("Turno: ")).title()
        if turno == "Manhã":
            print("Sua consulta foi marcada na Quinta, para o serviço de Cardiologista com a Dr(a) Rita no período da Manhã.")
        
        elif turno == "Tarde":
            print("Sua consulta foi marcada na Quinta, para o serviço de Cardiologista com a Dr(a) Rita no período da Tarde.")
        
        else:
            print("Sua consulta foi marcada na Quinta, para o serviço de Cardiologista com a Dr(a) Rita no período da Noite.")
    
    else:
        print("""Horários
        Ruan - Manhã e Tarde""")
        turno = str(input("Turno: ")).title()
        if turno == "Manhã":
            print("Sua consulta foi marcada na Quinta, para o serviço de Cardiologista com a Dr(a) Ruan no período da Manhã.")
        
        else:
            print("Sua consulta foi marcada na Quinta, para o serviço de Cardiologista com a Dr(a) Ruan no período da Tarde.")

elif dia == "sex":
    print("""Médicos disponiveis | Especialidades
    Mauro - Oftalmologista
    Lucas - Oftalmologista
    Ana - Oftalmologista
    Rita - Cardiologista
    Alice - Pediatra
    Ruan - Pediatra
    Elis - Pediatra
    """)
    print("""Digite
    O - Para saber mais detalhes sobre o serviço de Oftalmologista
    C - Para saber mais detalhes sobre o serviço de Cardiologista 
    P - Para saber mais detalhes sobre o serviço de Pediatra""")

    ser = str(input("Serviço: ")).upper()
    if ser == "O":
        print("""Horários
        Mauro - Manha e Noite
        Lucas - Tarde e Noite
        Ana - Manha e Tarde""")
        turno = str(input("Turno: ")).title()
        if turno == "Manhã":
            profissional = str(input("Profissional: ")).title()
            if profissional == "Mauro":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Mauro no período da Manhã.")
            
            else: 
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com a Dr(a) Ana no período da Manhã.")
            
        elif turno == "Tarde":
            profissional = str(input("Profissonal: ")).title()
            if profissional == "Lucas":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Lucas no período da Tarde.")
            
            else:
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com a Dr(a) Ana no período da Tarde.")
        
        else:
            profissional = str(input("Profissinal: ")).title()
            if profissional == "Mauro":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Mauro no período da Noite.")
            
            else:
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Lucas no período da Noite.")

    
    elif ser == "C":
        print("""Horários
        Rita - Tarde e Noite""")
        turno = str(input("Turno: "))
        if turno == "Tarde":
            print("Sua consulta foi marcada na Sexta, para o serviço de Cardiologista com a Dr(a) Rita no período da Tarde.")
        
        else:
            print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com a Dr(a) Rita no período da Noite.")
    
    else:
        print("""Horários
        Alice - Tarde e Noite
        Ruan - Manhã e Tarde
        Elis - Manhã, Tarde e Noite""")
        turno = str(input("Turno: ")).title()
        if turno == "Tarde":
            profissional = str(input("Profissional: ")).title()
            if profissional == "Alice":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com a Dr(a) Alice no período da Tarde.")
            
            elif profissional == "Ruan":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Ruan no período da Tarde.")
            
            else:
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Elis no período da Tarde.")
            
        elif turno == "Manhã":
            profissional = str(input("Profissional: ")).title()
            if profissional == "Ruan":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Ruan no período da Manhã.")
            
            else:
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Elis no período da Manhã.")
        
        else:
            profissional = str(input("Profissional: ")).title()
            if profissional == "Ruan":
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com o Dr Ruan no período da Noite.")
            
            else:
                print("Sua consulta foi marcada na Sexta, para o serviço de Pediatra com a Dr(a) Alice no período da Noite.")

else:
    print("Não Trabalhamos nos Fins de Semana ")
