# Calculadora-de-estudio
Prototipo Fase 2 - Calculadora de estudio 

Este proyecto corresponde a la **Fase 2 – Prototipado** del curso **CC2005 – Algoritmos y Programación Básica** en la Universidad del Valle de Guatemala.  

El objetivo es ofrecer una herramienta para que los estudiantes puedan **organizar su tiempo de estudio** de acuerdo con:  
- Materias cursadas.  
- Fechas de entrega de tareas y parciales.  
- Nivel de dificultad de cada curso.  
- Horarios disponibles.  
- Nivel de energía a lo largo del día.  

---

## 🚀 Características principales  

- Registro de materias con dificultad y entregas próximas.  
- Horarios disponibles por día de la semana en rangos (ejemplo: `9-12`).  
- Registro de nivel de energía (7:00 – 22:00).  
- Generación automática de un **plan de estudio sugerido** priorizando:  
  - Entregas más próximas.  
  - Materias más difíciles.  
  - Horas de mayor energía.  

---

## 🛠️ Tecnologías utilizadas  

- **Lenguaje:** Python 3.x  
- **Librerías estándar:**  
  - `datetime` para manejo de fechas.  
  - `collections.defaultdict` para organizar horarios.
 
▶️ Ejecución

Ejecutar el programa en la terminal:

python fase2_version final.py


El sistema pedirá:

Número de materias.

Nombre, dificultad y número de entregas por materia.

Horarios disponibles por día de la semana.

Nivel de energía por hora.

Al finalizar, mostrará un plan de estudio sugerido por día.

📊 Ejemplo de salida
Lunes:
  9:00 - Matemáticas
  10:00 - Física

Martes:
  8:00 - Programación
  9:00 - Programación

👥 Equipo de trabajo

María Fernanda Afre Córdova – 251355

Laura Gabriela Sandoval Palma – 251409

María Alejandra Afre Córdova – 251359

📌 Futuras mejoras

Exportar plan de estudio en PDF.

Integración con Google Calendar.

Simplificar registro de energía en bloques (mañana/tarde/noche).

📄 Licencia

Este proyecto es académico y de uso educativo.
