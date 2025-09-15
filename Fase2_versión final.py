from datetime import datetime
from collections import defaultdict

materias = []
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

# Paso 1: Materias que desea estudiar
num_materias = int(input("¿Cuántas materias deseas incluir en tu horario de estudio? "))

for _ in range(num_materias):
    nombre = input("\nNombre de la materia: ")
    dificultad = input("Dificultad (alta/media/baja): ").lower()
    
    entregas = []
    cantidad_tareas = int(input(f"¿Cuántas tareas o parciales próximos tienes en {nombre}? "))
    if cantidad_tareas > 0:
        for i in range(cantidad_tareas):
            fecha_str = input(f" - Fecha de entrega #{i+1} (formato YYYY-MM-DD): ")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            entregas.append(fecha)
    
    materias.append({
        "nombre": nombre,
        "dificultad": dificultad,
        "entregas": entregas
    })

# Paso 2: Horarios disponibles por día
horas_disponibles = defaultdict(list)

print("\nIndica tus horarios disponibles por día (formato 9-12 para 9:00 a 12:00). Puedes ingresar varios rangos por día.")
for dia in dias_semana:
    print(f"\n{dia.title()}:")
    while True:
        rango = input(" - Rango disponible (o escribe 'fin' para continuar): ")
        if rango.lower() == "fin":
            break
        try:
            inicio, fin = map(int, rango.split("-"))
            for h in range(inicio, fin):
                horas_disponibles[dia].append(h)
        except:
            print("❌ Formato incorrecto. Usa formato como 9-12.")

# Paso 3: Energía por hora
energia_horas = {}
print("\nIngresa tu nivel de energía por hora (1 a 10, solo entre 7 AM y 10 PM):")
for h in range(7, 22):
    nivel = int(input(f"{h}:00 - Nivel de energía: "))
    energia_horas[h] = nivel

# Paso 4: Asignar bloques de estudio
plan_estudio = defaultdict(list)

# Ordenar materias por fecha más próxima y dificultad
materias_ordenadas = sorted(
    materias,
    key=lambda m: (min(m["entregas"]) if m["entregas"] else datetime.max,
                   {"alta": 3, "media": 2, "baja": 1}[m["dificultad"]])
)

print("\n📅 Plan de estudio sugerido por día:\n")

for dia in dias_semana:
    horas_dia = horas_disponibles[dia]
    horas_ordenadas = sorted(horas_dia, key=lambda h: energia_horas.get(h, 0), reverse=True)
    asignadas = 0

    for materia in materias_ordenadas:
        bloques_necesarios = {"alta": 3, "media": 2, "baja": 1}[materia["dificultad"]]
        bloques_asignados = 0

        for h in horas_ordenadas:
            if all(h != hora for hora, _ in plan_estudio[dia]) and bloques_asignados < bloques_necesarios:
                plan_estudio[dia].append((h, materia["nombre"]))
                bloques_asignados += 1
                asignadas += 1

# Paso 5: Mostrar horario sugerido
for dia in dias_semana:
    print(f"\n{dia.title()}:")
    if not plan_estudio[dia]:
        print("  - No se asignaron sesiones de estudio.")
    else:
        for h, materia in sorted(plan_estudio[dia]):
            print(f"  {h}:00 - {materia}")
