from datetime import datetime, timedelta

# Entradas del usuario
materias = []
num_materias = int(input("¿Cuántas materias estás cursando? "))

for _ in range(num_materias):
    nombre = input("\nNombre de la materia: ")
    dificultad = input("Dificultad (alta/media/baja): ").lower()
    entrega_str = input("Fecha de entrega más próxima (formato YYYY-MM-DD): ")
    entrega = datetime.strptime(entrega_str, "%Y-%m-%d")
    materias.append({"nombre": nombre, "dificultad": dificultad, "entrega": entrega})

# Energía por hora (7 AM a 10 PM)
print("\nIngresa tu nivel de energía de 1 a 10 para cada hora:")
energia_horas = {}
for h in range(7, 22):
    nivel = int(input(f"{h}:00 - Nivel de energía: "))
    energia_horas[h] = nivel

# Horarios disponibles para estudiar
horas_disponibles = []
print("\nIndica tus horas disponibles para estudiar (ej. 9 para 9:00 AM). Escribe 'fin' para terminar:")
while True:
    entrada = input("Hora disponible: ")
    if entrada.lower() == 'fin':
        break
    horas_disponibles.append(int(entrada))

# Proceso: asignar horas según dificultad y energía
print("\n📅 Horario sugerido de estudio:\n")

materias_ordenadas = sorted(materias, key=lambda m: (m['entrega'], {"alta": 3, "media": 2, "baja": 1}[m['dificultad']]), reverse=False)

plan_estudio = {}

for materia in materias_ordenadas:
    bloques_asignados = []
    dificultad = materia['dificultad']
    bloques_necesarios = {"alta": 3, "media": 2, "baja": 1}[dificultad]

    # Ordenar las horas disponibles por nivel de energía
    horas_ordenadas = sorted(horas_disponibles, key=lambda h: energia_horas[h], reverse=True)

    for hora in horas_ordenadas:
        if hora not in plan_estudio and len(bloques_asignados) < bloques_necesarios:
            plan_estudio[hora] = materia['nombre']
            bloques_asignados.append(hora)

# Salida: mostrar el plan ordenado por hora
for hora in sorted(plan_estudio):
    print(f"{hora}:00 - {plan_estudio[hora]}")
