import json
import os
from datetime import datetime, date, timedelta

# --- CONFIGURACIÓN ---
DB_FILE = "inquisidor_db.json"
VERSION = "1.1"

class Inquisidor:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(DB_FILE):
            return []
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []

    def save_data(self):
        with open(DB_FILE, 'w') as f:
            json.dump(self.data, f, indent=4, default=str)

    def registrar_dia(self, fecha_str=None, es_backup=False):
        """Registra los datos del día. Si fecha_str es None, usa hoy."""
        if not fecha_str:
            fecha_str = str(date.today())
            print(f"\n--- REGISTRO DIARIO ({fecha_str}) ---")
        else:
            print(f"\n--- BACKUP MODE ({fecha_str}) ---")

        # Verificar si ya existe
        for entry in self.data:
            if entry['fecha'] == fecha_str:
                print("⚠️ Ya existe un registro para esta fecha.")
                overwrite = input("¿Sobreescribir? (s/n): ").lower()
                if overwrite != 's': return
                self.data.remove(entry)
                break

        # Métrica 1 y 2 (Simplificadas en Nivel de Productividad/Realismo Base)
        try:
            friccion = float(input("1. Nivel de Fricción (0-3): "))
            prod_base = float(input("2. % Realismo Base percibido (0-100): "))
        except ValueError:
            print("Error: Introduce números válidos.")
            return

        # Métrica 3: Autoobservación (Reemplaza aburrimiento)
        print("\n3. Autoobservación (Mínimo 15 min de percepción pura)")
        ao_input = input("¿Has reflexionado objetivamente hoy? (s/n): ").lower()
        auto_observacion = True if ao_input == 's' else False

        # Nueva Métrica: Contador de Idealismos
        try:
            idealismos = int(input("4. ¿Cuántos idealismos detectaste hoy?: "))
        except ValueError:
            idealismos = 0

        nuevo_registro = {
            "fecha": fecha_str,
            "friccion": friccion,
            "realismo_base": prod_base,
            "auto_observacion": auto_observacion,
            "idealismos": idealismos,
            "es_backup": es_backup
        }

        self.data.append(nuevo_registro)
        self.data.sort(key=lambda x: x['fecha']) # Mantener orden cronológico
        self.save_data()
        print("✅ Datos guardados.")

    def registrar_backup(self):
        print("\n--- MODO BACKUP ---")
        fecha_input = input("Introduce la fecha a recuperar (YYYY-MM-DD): ")
        try:
            datetime.strptime(fecha_input, "%Y-%m-%d")
            self.registrar_dia(fecha_str=fecha_input, es_backup=True)
        except ValueError:
            print("Formato de fecha incorrecto.")

    def calcular_estadisticas(self):
        if not self.data:
            print("No hay datos registrados.")
            return

        # Filtrar mes actual
        mes_actual = str(date.today())[:7] # YYYY-MM
        registros_mes = [r for r in self.data if r['fecha'].startswith(mes_actual)]
        
        if not registros_mes:
            print(f"No hay datos para {mes_actual}")
            return

        # CÁLCULOS
        total_dias = len(registros_mes)
        suma_realismo_base = sum(r['realismo_base'] for r in registros_mes)
        media_base = suma_realismo_base / total_dias
        
        # Penalización por Idealismos (1% del total mensual por cada uno)
        total_idealismos = sum(r.get('idealismos', 0) for r in registros_mes)
        penalizacion_idealismos = total_idealismos * 1.0 

        # Factor Disciplina (Autoobservación)
        # Objetivo: 2 veces por semana.
        # Estimación aproximada: Dias transcurridos / 7 * 2
        semanas_transcurridas = max(1, datetime.now().day / 7)
        objetivo_ao = semanas_transcurridas * 2
        total_ao = sum(1 for r in registros_mes if r['auto_observacion'])
        
        factor_disciplina = 1.0
        msg_disciplina = "CUMPLIDO"
        if total_ao < objetivo_ao:
            factor_disciplina = 0.75 # Castigo del 25%
            msg_disciplina = f"FALLIDO ({total_ao}/{int(objetivo_ao)})"

        # FÓRMULA FINAL
        realismo_final = (media_base * factor_disciplina) - penalizacion_idealismos
        
        print(f"\n=== INFORME MENSUAL ({mes_actual}) ===")
        print(f"📅 Días registrados: {total_dias}")
        print(f"🧠 Realismo Base Promedio: {media_base:.2f}%")
        print(f"👁️ Autoobservación: {msg_disciplina} -> Factor {factor_disciplina}")
        print(f"🦄 Idealismos Totales: {total_idealismos} -> Penalización -{penalizacion_idealismos}%")
        print("-" * 30)
        print(f"📊 REALISMO TOTAL: {realismo_final:.2f}%")

    def menu(self):
        while True:
            print(f"\n--- INQUISIDOR v{VERSION} ---")
            print("1. Registrar Hoy")
            print("2. Registrar Idealismo Rápido (Hoy)")
            print("3. Modo Backup (Registrar pasado)")
            print("4. Ver Estadísticas Mensuales")
            print("5. Salir")
            op = input("Elige: ")

            if op == '1': self.registrar_dia()
            elif op == '2': self.idealismo_rapido()
            elif op == '3': self.registrar_backup()
            elif op == '4': self.calcular_estadisticas()
            elif op == '5': break

    def idealismo_rapido(self):
        """Suma 1 idealismo al día de hoy sin pedir el resto de datos"""
        hoy = str(date.today())
        encontrado = False
        for r in self.data:
            if r['fecha'] == hoy:
                r['idealismos'] = r.get('idealismos', 0) + 1
                encontrado = True
                print(f"🦄 Idealismo añadido. Total hoy: {r['idealismos']}")
                break
        
        if not encontrado:
            print("⚠️ No has iniciado el día. Creando registro básico...")
            nuevo = {
                "fecha": hoy, "friccion": 0, "realismo_base": 100, 
                "auto_observacion": False, "idealismos": 1, "es_backup": False
            }
            self.data.append(nuevo)
            print("Registro creado con 1 idealismo. Recuerda rellenar el resto luego.")
        
        self.save_data()

if __name__ == "__main__":
    app = Inquisidor()
    app.menu()