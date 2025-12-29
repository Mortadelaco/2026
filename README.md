========================================================================
             PROTOCOLO ANTI-IDEALISMO: EL INQUISIDOR (v1.0)
========================================================================

DESCRIPCIÓN:
Este software no es un "tracker de hábitos". Es un espejo digital diseñado 
para medir la discrepancia entre quién crees que eres (Idealismo) y quién 
eres realmente (Realismo).

Mide tres indicadores neurológicos de desintoxicación dopaminérgica:
1. Fricción Voluntaria (Capacidad de hacer lo que no quieres).
2. Ratio Verdad/Discurso (Capacidad de ejecutar lo que piensas).
3. Tolerancia al Aburrimiento (Capacidad de estar sobrio sin estímulos).

NO TIENE INTERFAZ GRÁFICA. NO TIENE COLORES. NO TIENE PIEDAD.

========================================================================
                        INSTALACIÓN EN PC (Windows)
========================================================================

REQUISITOS:
- Tener instalado Python (marcar "Add Python to PATH" al instalar).

INSTRUCCIONES:
1. Crea una carpeta llamada "PROYECTO_REALIDAD".
2. Guarda el script con el nombre "inquisidor.py".
   (¡OJO! Asegúrate de que no se llame "inquisidor.py.txt").
3. Para abrirlo:
   - Opción A: Abre la consola (CMD), ve a la carpeta y escribe: 
     python inquisidor.py
   - Opción B: Crea un acceso directo en el escritorio si lo prefieres.

========================================================================
                    INSTALACIÓN EN MÓVIL (Android + Termux)
========================================================================

Si tienes Termux, tienes el poder. Sigue estos pasos exactos:

1. PREPARACIÓN DEL ENTORNO:
   Abre Termux y escribe estos comandos (uno a uno):
   
   pkg update && pkg upgrade
   pkg install python
   termux-setup-storage
   (Dale a "Permitir" cuando te pida acceso a archivos).

2. LLEVAR EL ARCHIVO AL MÓVIL:
   - Guarda el archivo "inquisidor.py" en la carpeta "Descargas" (Download) 
     de tu móvil.

3. EJECUTARLO:
   Cada vez que quieras usarlo, abre Termux y escribe:
   
   cd /storage/emulated/0/Download
   python inquisidor.py

   (El programa se abrirá igual que en el PC).

========================================================================
                        MANUAL DE OPERACIONES
========================================================================

MODO 1: REGISTRAR DÍA (Hacerlo cada noche)
------------------------------------------
El sistema te hará 3 preguntas. Sé honesto. Si dudas, redondea hacia abajo.

1. KPI FRICCIÓN:
   - Cuenta solo acciones que requirieron fuerza de voluntad activa.
   - Rutinas fáciles NO cuentan.

2. KPI RATIO V/D:
   - Ideas: ¿Cuántos planes, "tengo que hacer" o intenciones tuviste?
   - Acciones: ¿Cuántas ejecutaste físicamente?
   - El sistema calculará tu % de efectividad. 
   - Menos de 50% es patológico (eres un soñador, no un hacedor).

3. KPI ABURRIMIENTO:
   - Minutos totales de "mirar a la pared" sin móvil, música ni pensamientos 
     obsesivos circulares. Silencio real.

MODO 2: VER PROGRESO
--------------------
- Muestra tus medias mensuales.
- Se resetea automáticamente el día 1 de cada mes.
- Te etiqueta como (REALISTA) o (IDEALISTA) según tus resultados.

========================================================================
                        SOLUCIÓN DE PROBLEMAS
========================================================================

ERROR: "Se abre y se cierra rápido" (En PC)
SOLUCIÓN: No hagas doble clic. Abre la terminal (CMD), arrastra el archivo 
dentro y dale a Enter. O ejecútalo escribiendo "python inquisidor.py".

ERROR: "No such file or directory" (En Termux)
SOLUCIÓN: No has escrito bien la ruta de la carpeta ("cd ..."). Asegúrate 
de que el archivo "inquisidor.py" está realmente en la carpeta Descargas.

ADVERTENCIA FINAL:
El archivo "registro_kpi.csv" contiene tu historial.
- NO lo abras con Excel mientras usas el programa.
- NO modifiques los datos pasados para parecer mejor persona.
- Si corrompes el archivo, bórralo y empieza de cero.

"La verdad os hará libres, pero primero os hará miserables."
========================================================================
