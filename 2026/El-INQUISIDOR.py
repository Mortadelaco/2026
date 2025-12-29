import csv
import os
import datetime
from datetime import date

# --- CONFIGURACIÓN ---
ARCHIVO_DB = 'registro_kpi.csv'

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def inicializar_db():
    if not os.path.exists(ARCHIVO_DB):
        with open(ARCHIVO_DB, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Fecha', 'Mes', 'Friccion_Eventos', 'Ideas_Pensadas', 'Acciones_Hechas', 'Ratio_RVD', 'Aburrimiento_Min'])

def obtener_fecha_hoy():
    return date.today().strftime("%Y-%m-%d")

def obtener_mes_actual():
    return date.today().strftime("%Y-%m")

def registrar_dia():
    limpiar()
    print("=== INQUISIDOR DIARIO ===")
    print(f"Fecha: {obtener_fecha_hoy()}\n")
    
    try:
        # KPI 1
        print("[KPI 1: FRICCIÓN]")
        print("¿Cuántas veces hiciste algo que NO querías hacer hoy?")
        friccion = int(input(">> Cantidad de eventos: "))
        
        # KPI 2
        print("\n[KPI 2: RATIO VERDAD/DISCURSO]")
        print("¿Cuántas ideas/planes de mejora tuviste?")
        ideas = int(input(">> Ideas: "))
        print("¿Cuántas ejecutaste físicamente?")
        acciones = int(input(">> Acciones: "))
        
        ratio = 0.0
        if ideas > 0:
            ratio = round((acciones / ideas) * 100, 2)
        
        # KPI 3
        print("\n[KPI 3: ABURRIMIENTO]")
        print("¿Cuántos minutos aguantaste sin hacer NADA (sin pantallas)?")
        aburrimiento = int(input(">> Minutos: "))
        
        # Guardar
        with open(ARCHIVO_DB, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                obtener_fecha_hoy(),
                obtener_mes_actual(),
                friccion,
                ideas,
                acciones,
                ratio,
                aburrimiento
            ])
        print(f"\n[REGISTRADO] Tu Ratio de Realidad hoy es: {ratio}%")
        input("Presiona ENTER para salir.")
        
    except ValueError:
        print("\nERROR: Introduce números enteros, no textos ni excusas.")
        input()

def ver_informe_mensual():
    limpiar()
    if not os.path.exists(ARCHIVO_DB):
        print("No hay datos. Registra tu primer día.")
        input()
        return

    print("=== INFORME DE REALIDAD (MEDIA MENSUAL) ===\n")
    
    datos_mes = {} # Diccionario para acumular datos por mes
    
    with open(ARCHIVO_DB, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mes = row['Mes']
            if mes not in datos_mes:
                datos_mes[mes] = {'dias': 0, 'friccion': 0, 'ratio': 0.0, 'aburrimiento': 0}
            
            datos_mes[mes]['dias'] += 1
            datos_mes[mes]['friccion'] += int(row['Friccion_Eventos'])
            datos_mes[mes]['ratio'] += float(row['Ratio_RVD'])
            datos_mes[mes]['aburrimiento'] += int(row['Aburrimiento_Min'])

    print(f"{'MES':<10} | {'FRICCIÓN (Med)':<15} | {'REALISMO (Med)':<15} | {'ABURRIMIENTO (Total)':<20}")
    print("-" * 70)
    
    for mes, data in datos_mes.items():
        dias = data['dias']
        media_friccion = round(data['friccion'] / dias, 1)
        media_ratio = round(data['ratio'] / dias, 1)
        total_aburrimiento = data['aburrimiento']
        
        estado = ""
        if media_ratio < 50: estado = "(IDEALISTA)"
        else: estado = "(REALISTA)"

        print(f"{mes:<10} | {media_friccion:<15} | {media_ratio}% {estado:<10} | {total_aburrimiento} min")
    
    print("\nNota: El sistema calcula la media automáticamente.")
    input("\nPresiona ENTER para volver.")

def menu():
    inicializar_db()
    while True:
        limpiar()
        print("SISTEMA DE CONTROL ANTI-IDEALISMO")
        print("---------------------------------")
        print("1. Registrar Datos de Hoy")
        print("2. Ver Progreso Mensual (Reset Automático)")
        print("3. Salir")
        
        opc = input("\n>> Elige: ")
        
        if opc == '1': registrar_dia()
        elif opc == '2': ver_informe_mensual()
        elif opc == '3': break

if __name__ == "__main__":
    menu()