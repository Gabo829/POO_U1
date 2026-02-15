import os
import subprocess
import datetime
from abc import ABC, abstractmethod

# --- 1. PATRÓN STRATEGY PARA EJECUCIÓN ---
class EstrategiaEjecucion(ABC):
    @abstractmethod
    def ejecutar(self, ruta):
        pass

class EjecutorPython(EstrategiaEjecucion):
    def ejecutar(self, ruta):
        ruta_absoluta = os.path.abspath(ruta)
        print(f"\n[SISTEMA] Ejecutando: {os.path.basename(ruta_absoluta)}")
        try:
            if os.name == 'nt':
                # Cambie a os.system con start para abrir en ventana nueva 
                # y devolver el control inmediatamente al programa principal
                os.system(f'start cmd /k python "{ruta_absoluta}"')
            else:
                subprocess.run(['python3', ruta_absoluta], check=True)
        except Exception as e:
            print(f"[-] Error al ejecutar: {e}")

# --- 2. GESTOR DE HISTORIAL ---
class HistorialLogger:
    def __init__(self, archivo="log_actividad.txt"):
        self.archivo = archivo

    def registrar_accion(self, script_nombre):
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.archivo, "a", encoding="utf-8") as f:
                f.write(f"[{fecha}] Ejecutado exitosamente: {script_nombre}\n")
        except:
            pass

# --- 3. CLASE DE DATOS PARA SCRIPTS ---
class ScriptPython:
    def __init__(self, ruta):
        self.ruta = ruta
        self.nombre = os.path.basename(ruta)
        try:
            self.tamanio = os.path.getsize(ruta) / 1024
        except:
            self.tamanio = 0

    def leer_contenido(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return "[-] No se pudo leer el archivo (error de codificacion)."

# --- 4. COMPONENTE DE INTERFAZ (SINGLETON) ---
class InterfazConsola:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(InterfazConsola, cls).__new__(cls)
        return cls._instancia

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def imprimir_menu(self, titulo, opciones):
        # Diseño adaptado a nombres largos de carpetas
        ancho_opciones = max(len(opt) for opt in opciones) if opciones else 0
        ancho = max(ancho_opciones + 15, len(titulo) + 15, 60)

        print("\n" + "╔" + "═"*(ancho-2) + "╗")
        print(f"║ {titulo.center(ancho-4)} ║")
        print("╠" + "═"*(ancho-2) + "╣")
        for i, opt in enumerate(opciones, 1):
            linea = f" [{i}] {opt}"
            print(f"║ {linea.ljust(ancho-4)} ║")
        print(f"║ {' [0] Salir / Volver'.ljust(ancho-4)} ║")
        print("╚" + "═"*(ancho-2) + "╝")

    def solicitar_opcion(self, max_val):
        while True:
            try:
                # Limpiamos espacios y posibles restos de la ejecucion anterior
                entrada = input(f"\n>> Seleccione una opcion (0-{max_val}): ").strip()
                if not entrada: continue
                val = int(entrada)
                if 0 <= val <= max_val: return val
                print(f"[-] Opcion no valida.")
            except ValueError:
                print("[-] Error: Ingrese solo el numero de la opcion.")

# --- 5. CONTROLADOR PRINCIPAL ---
class DashboardOptimizado:
    def __init__(self, ruta_raiz):
        self.ruta_raiz = os.path.abspath(ruta_raiz)
        self.ui = InterfazConsola()
        self.ejecutor = EjecutorPython()
        self.logger = HistorialLogger()

    def iniciar(self):
        while True:
            self.ui.limpiar_pantalla()
            unidades = sorted([d.name for d in os.scandir(self.ruta_raiz) 
                              if d.is_dir() and not d.name.startswith('.')])
            
            if not unidades:
                print(f"[-] No hay carpetas en: {self.ruta_raiz}")
                break

            self.ui.imprimir_menu("PANEL DE CONTROL - PROYECTOS POO", unidades)
            opc = self.ui.solicitar_opcion(len(unidades))
            
            if opc == 0: break
            self.gestionar_subcarpetas(os.path.join(self.ruta_raiz, unidades[opc-1]))

    def gestionar_subcarpetas(self, ruta_unidad):
        while True:
            self.ui.limpiar_pantalla()
            subs = sorted([d.name for d in os.scandir(ruta_unidad) if d.is_dir()])
            
            if not subs:
                input("\n[!] Carpeta vacia. Enter para volver...")
                break

            self.ui.imprimir_menu(f"UNIDAD: {os.path.basename(ruta_unidad)}", subs)
            opc = self.ui.solicitar_opcion(len(subs))
            
            if opc == 0: break
            self.gestionar_scripts(os.path.join(ruta_unidad, subs[opc-1]))

    def gestionar_scripts(self, ruta_carpeta):
        while True:
            self.ui.limpiar_pantalla()
            archivos = sorted([f.name for f in os.scandir(ruta_carpeta) if f.name.endswith('.py')])
            
            if not archivos:
                input("\n[!] Sin scripts .py. Enter para volver...")
                break

            self.ui.imprimir_menu(f"SCRIPTS: {os.path.basename(ruta_carpeta)}", archivos)
            opc = self.ui.solicitar_opcion(len(archivos))
            
            if opc == 0: break
            
            script_obj = ScriptPython(os.path.join(ruta_carpeta, archivos[opc-1]))
            self.ver_y_ejecutar(script_obj)

    def ver_y_ejecutar(self, script_obj):
        self.ui.limpiar_pantalla()
        sep = "=" * 70
        print(sep)
        print(f" LEYENDO: {script_obj.nombre} | Tamaño: {script_obj.tamanio:.2f} KB")
        print(sep)
        print(script_obj.leer_contenido())
        print(sep)
        
        # Corregido: Ahora el input es mas robusto tras una ejecucion
        conf = input("\n¿Ejecutar script? (s/n): ").lower().strip()
        if conf == 's':
            self.logger.registrar_accion(script_obj.nombre)
            self.ejecutor.ejecutar(script_obj.ruta)
            print("\n[INFO] El script se abrio en una ventana nueva.")
        
        print("\nPulse ENTER para volver al menú de scripts...")
        input() # Pausa forzada para recuperar el foco de la terminal

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    app = DashboardOptimizado(BASE_DIR)
    app.iniciar()