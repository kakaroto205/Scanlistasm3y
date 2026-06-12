
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   🔥 VERIFICADOR IPTV ULTRA EFICIENTE - VERSIÓN 4.0 TURBO 🔥        ║
║                                                                       ║
║           Creado por: Maestro de la Calamidad                        ║
║          Versión 4.0 TURBO - Máxima Eficiencia y Velocidad           ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple, Set
from urllib.parse import urlparse, parse_qs
from collections import deque
import threading

# ==================== AUTO-INSTALACIÓN OPTIMIZADA ====================
def auto_install_requirements():
    """Instalación paralela y optimizada de dependencias"""
    packages = ['requests', 'urllib3', 'colorama', 'fake-useragent']
    
    print("\n🚀 Instalación ultra-rápida de dependencias...\n")
    
    missing = []
    for pkg in packages:
        try:
            __import__(pkg.replace('-', '_'))
            print(f"✅ {pkg:20} [\033[92mOK\033[0m]")
        except ImportError:
            missing.append(pkg)
    
    if missing:
        print(f"\n📦 Instalando {len(missing)} paquetes...")
        cmd = f"{sys.executable} -m pip install {' '.join(missing)} --quiet --disable-pip-version-check"
        os.system(cmd)
        print("✅ Instalación completada\n")
    time.sleep(0.3)

auto_install_requirements()

# Importaciones
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
from queue import Queue, Empty

try:
    from fake_useragent import UserAgent
    ua = UserAgent()
except:
    ua = None

init(autoreset=True)

# ==================== CONFIGURACIÓN OPTIMIZADA ====================
FUENTE_URL = "https://pastebin.com/raw/6wsQSeFD"

# Proxies API optimizadas (solo las más rápidas)
PROXY_APIS = [
    'https://api.proxyscrape.com/v2/?request=get&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all',
    'https://www.proxy-list.download/api/v1/get?type=http',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
]

USER_AGENTS_CACHE = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
]

# ==================== COLORES ====================
class C:
    """Clase de colores simplificada"""
    H = Fore.CYAN + Style.BRIGHT
    S = Fore.GREEN + Style.BRIGHT
    W = Fore.YELLOW + Style.BRIGHT
    E = Fore.RED + Style.BRIGHT
    I = Fore.BLUE + Style.BRIGHT
    M = Fore.MAGENTA + Style.BRIGHT
    R = Style.RESET_ALL

# ==================== GESTOR DE PROXIES EFICIENTE ====================
class GestorProxiesRapido:
    """Gestor de proxies optimizado con caché y threading"""
    
    def __init__(self):
        self.proxies = deque()
        self.proxies_fallidos = set()
        self.lock = threading.Lock()
        self.usar_proxies = False
        
    def descargar_proxies_paralelo(self):
        """Descarga proxies en paralelo para máxima velocidad"""
        print(f"\n{C.I}🌐 Descargando proxies (modo turbo)...{C.R}")
        
        def fetch(url):
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}', r.text)
            except:
                pass
            return []
        
        with ThreadPoolExecutor(max_workers=len(PROXY_APIS)) as executor:
            futures = [executor.submit(fetch, url) for url in PROXY_APIS]
            all_proxies = []
            for future in as_completed(futures):
                all_proxies.extend(future.result())
        
        # Eliminar duplicados y crear deque
        self.proxies = deque(set(all_proxies))
        
        if len(self.proxies) > 0:
            print(f"{C.S}✅ {len(self.proxies)} proxies cargados{C.R}\n")
            self.usar_proxies = True
        else:
            print(f"{C.W}⚠️  Sin proxies. Modo directo.{C.R}\n")
        
        time.sleep(0.3)
    
    def obtener_proxy(self) -> Optional[Dict]:
        """Obtiene proxy con rotación thread-safe"""
        if not self.usar_proxies or not self.proxies:
            return None
        
        with self.lock:
            # Buscar proxy no fallido
            for _ in range(min(10, len(self.proxies))):
                proxy = self.proxies[0]
                self.proxies.rotate(-1)
                
                if proxy not in self.proxies_fallidos:
                    return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        
        return None
    
    def marcar_fallido(self, proxy_dict: Dict):
        """Marca proxy como fallido thread-safe"""
        if proxy_dict and 'http' in proxy_dict:
            with self.lock:
                self.proxies_fallidos.add(proxy_dict['http'].replace('http://', ''))

# ==================== ANIMACIÓN MINIMALISTA ====================
class Anim:
    """Animación optimizada"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧']
    idx = 0
    
    @classmethod
    def get(cls):
        frame = cls.frames[cls.idx % len(cls.frames)]
        cls.idx += 1
        return frame
    
    @classmethod
    def barra(cls, actual, total, ancho=50):
        """Barra de progreso optimizada"""
        pct = (actual / total * 100) if total > 0 else 0
        llenos = int((actual / total) * ancho) if total > 0 else 0
        vacios = ancho - llenos
        return f"[{C.S}{'█' * llenos}{C.R}{Fore.WHITE}{'░' * vacios}{C.R}] {pct:5.1f}% ({actual}/{total})"

# ==================== DETECTOR IPTV OPTIMIZADO ====================
class DetectorIPTV:
    """Detector ultra-rápido con patrones compilados"""
    
    # Patrones pre-compilados para máxima velocidad
    PATRONES = {
        'm3u_get': re.compile(r'(https?://[^\s]+/get\.php\?[^\s]+)', re.I),
        'm3u_api': re.compile(r'(https?://[^\s]+/player_api\.php\?[^\s]+)', re.I),
        'm3u8': re.compile(r'(https?://[^\s]+\.m3u8?)', re.I),
        'm3u_path': re.compile(r'(https?://[^\s]+/[^/]+/[^/]+/\d+)', re.I),
        'generic': re.compile(r'(https?://[^\s<>"]+(?:m3u|iptv|stream|live))', re.I),
    }
    
    @classmethod
    def extraer_todas(cls, texto: str) -> List[Tuple[str, str]]:
        """Extracción ultra-rápida con patrones pre-compilados"""
        listas = {}
        for tipo, patron in cls.PATRONES.items():
            for match in patron.finditer(texto):
                url = match.group(1)
                if url not in listas:
                    listas[url] = tipo
        return list(listas.items())
    
    @staticmethod
    def extraer_creds(url: str) -> Optional[Dict]:
        """Extracción rápida de credenciales"""
        try:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            datos = {
                'url_completa': url,
                'host': f"{parsed.scheme}://{parsed.netloc}",
                'username': params.get('username', [''])[0],
                'password': params.get('password', [''])[0],
                'tipo': 'xtream' if 'player_api' in url else 'm3u',
                'protocolo': parsed.scheme,
                'puerto': parsed.port or (80 if parsed.scheme == 'http' else 443)
            }
            
            # Extracción alternativa de la ruta
            if not datos['username']:
                parts = [p for p in parsed.path.split('/') if p]
                if len(parts) >= 2:
                    if len(parts[0]) >= 4 and len(parts[1]) >= 4:
                        datos['username'] = parts[0]
                        datos['password'] = parts[1]
            
            # M3U8 directo
            if url.endswith('.m3u8') or url.endswith('.m3u'):
                datos['username'] = 'directo'
                datos['password'] = 'sin_creds'
                datos['tipo'] = 'm3u8'
            
            return datos if datos['username'] else None
        except:
            return None

# ==================== CACHE DE SESIONES ====================
class CacheSesiones:
    """Caché de sesiones HTTP para reutilización"""
    
    def __init__(self, max_size=10):
        self.sessions = Queue(maxsize=max_size)
        self.lock = threading.Lock()
        
        # Pre-crear sesiones
        for _ in range(max_size):
            s = requests.Session()
            s.headers.update({'Connection': 'keep-alive'})
            self.sessions.put(s)
    
    def obtener(self):
        """Obtiene sesión del pool"""
        try:
            return self.sessions.get_nowait()
        except Empty:
            s = requests.Session()
            s.headers.update({'Connection': 'keep-alive'})
            return s
    
    def devolver(self, session):
        """Devuelve sesión al pool"""
        try:
            self.sessions.put_nowait(session)
        except:
            session.close()

# ==================== VERIFICADOR ULTRA EFICIENTE ====================
class VerificadorTurbo:
    """Verificador ultra-optimizado con todas las mejoras de eficiencia"""
    
    def __init__(self):
        self.listas_validas = []
        self.listas_analizadas = 0
        self.listas_rechazadas = 0
        self.objetivo_alcanzado = False
        self.max_listas = 0
        self.lock = threading.Lock()
        
        # Componentes optimizados
        self.gestor_proxies = GestorProxiesRapido()
        self.detector = DetectorIPTV
        self.cache_sesiones = CacheSesiones(max_size=10)
        self.stats_tipo = {}
        
        # Caché de user agents
        self.ua_cache = USER_AGENTS_CACHE.copy()
        self.ua_idx = 0
    
    def banner(self):
        """Banner optimizado"""
        print(f"""
{C.H}╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   {C.S}🚀 VERIFICADOR IPTV ULTRA EFICIENTE - VERSIÓN 4.0 TURBO 🚀{C.H}       ║
║                                                                       ║
║           {C.M}Creado por: Maestro de la Calamidad{C.H}                        ║
║          {C.S}Versión 4.0 TURBO - Máxima Eficiencia{C.H}                      ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝{C.R}

{C.I}[⚡] Sistema Ultra-Eficiente Activado
[⚡] Procesamiento Paralelo Optimizado: 10 Threads
[⚡] Caché de Sesiones HTTP: Habilitado
[⚡] Proxies Rotativos: Modo Turbo
[⚡] Detección con Patrones Pre-Compilados{C.R}
""")
    
    def obtener_ua(self) -> str:
        """Obtiene user agent del caché"""
        if ua:
            try:
                return ua.random
            except:
                pass
        
        ua_str = self.ua_cache[self.ua_idx % len(self.ua_cache)]
        self.ua_idx += 1
        return ua_str
    
    def verificar_rapido(self, url: str, session: requests.Session) -> Tuple[bool, Optional[str]]:
        """Verificación ultra-rápida con early exit"""
        verificaciones = 0
        proxy_usado = None
        
        for _ in range(2):  # Reducido a 2 intentos para velocidad
            if self.objetivo_alcanzado:
                return False, None
            
            proxy = self.gestor_proxies.obtener_proxy()
            
            try:
                r = session.get(
                    url,
                    headers={'User-Agent': self.obtener_ua()},
                    proxies=proxy,
                    timeout=6,  # Reducido timeout
                    stream=True
                )
                
                if r.status_code == 200:
                    # Solo leer primeros 500 bytes
                    content = next(r.iter_content(500), b'').decode('utf-8', errors='ignore')
                    
                    # Verificación rápida
                    if any(x in content for x in ['#EXTM3U', '#EXTINF', '.ts']):
                        verificaciones += 1
                        proxy_usado = proxy.get('http', 'Directo') if proxy else 'Directo'
                        
                        # Early exit si ya es válido
                        if verificaciones >= 1:
                            return True, proxy_usado
                
                r.close()
            except:
                if proxy:
                    self.gestor_proxies.marcar_fallido(proxy)
            
            time.sleep(0.2)
        
        return verificaciones >= 1, proxy_usado
    
    def contar_canales_rapido(self, url: str) -> int:
        """Conteo rápido de canales (solo muestra)"""
        try:
            session = self.cache_sesiones.obtener()
            r = session.get(url, timeout=5, stream=True)
            
            if r.status_code == 200:
                # Leer solo primeros 10KB para estimación
                content = next(r.iter_content(10240), b'').decode('utf-8', errors='ignore')
                count = content.count('#EXTINF')
                
                # Extrapolación aproximada
                if count > 0 and len(content) < 10240:
                    return count
                elif count > 0:
                    return count * 5  # Estimación
            
            r.close()
            self.cache_sesiones.devolver(session)
        except:
            pass
        
        return 0
    
    def descargar_fuente(self) -> List[Tuple[str, str]]:
        """Descarga optimizada de fuente"""
        print(f"{C.I}📥 Descargando fuente...{C.R}")
        
        try:
            r = requests.get(FUENTE_URL, timeout=15)
            if r.status_code == 200:
                listas = self.detector.extraer_todas(r.text)
                
                # Contar por tipo
                tipos = {}
                for _, tipo in listas:
                    tipos[tipo] = tipos.get(tipo, 0) + 1
                
                print(f"\n{C.S}✅ {len(listas)} listas detectadas{C.R}")
                print(f"{C.I}📊 Tipos: {', '.join(f'{t}:{c}' for t,c in tipos.items())}{C.R}\n")
                
                return listas
            else:
                print(f"{C.E}❌ Error: {r.status_code}{C.R}")
                return []
        except Exception as e:
            print(f"{C.E}❌ Error: {e}{C.R}")
            return []
    
    def mostrar_stats(self, total: int):
        """Estadísticas iniciales"""
        print(f"{C.H}{'='*70}")
        print(f"📊 ESTADÍSTICAS")
        print(f"{'='*70}{C.R}")
        print(f"{C.I}  URLs detectadas : {C.S}{total}{C.R}")
        print(f"{C.I}  Objetivo        : {C.S}{self.max_listas}{C.R}")
        print(f"{C.I}  Threads         : {C.S}10 (optimizado){C.R}")
        print(f"{C.I}  Proxies         : {C.S}{len(self.gestor_proxies.proxies)}{C.R}")
        print(f"{C.H}{'='*70}{C.R}\n")
    
    def mostrar_lista(self, datos: Dict, num: int):
        """Muestra lista encontrada (compacto)"""
        print(f"\n{C.S}✅ #{num} | {datos['host'][:40]}... | {datos['tipo']} | {datos['canales']} canales{C.R}")
    
    def procesar(self, url_tipo: Tuple[str, str]) -> Optional[Dict]:
        """Procesamiento optimizado"""
        if self.objetivo_alcanzado:
            return None
        
        url, tipo = url_tipo
        
        with self.lock:
            self.listas_analizadas += 1
        
        session = self.cache_sesiones.obtener()
        
        es_valida, proxy = self.verificar_rapido(url, session)
        
        self.cache_sesiones.devolver(session)
        
        if es_valida:
            datos = self.detector.extraer_creds(url)
            if datos:
                datos['tipo_lista'] = tipo
                datos['canales'] = self.contar_canales_rapido(url)
                datos['proxy_usado'] = proxy
                datos['fecha'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                with self.lock:
                    self.stats_tipo[tipo] = self.stats_tipo.get(tipo, 0) + 1
                
                return datos
        
        with self.lock:
            self.listas_rechazadas += 1
        
        return None
    
    def actualizar_progreso(self):
        """Actualización de progreso optimizada"""
        barra = Anim.barra(len(self.listas_validas), self.max_listas, 50)
        frame = Anim.get()
        
        print(f"\r{C.I}{frame}{C.R} {barra} | "
              f"{C.W}Analizadas:{self.listas_analizadas}{C.R} | "
              f"{C.E}Rechazadas:{self.listas_rechazadas}{C.R}",
              end='', flush=True)
    
    def verificar_paralelo(self, listas: List[Tuple[str, str]], max_listas: int):
        """Verificación paralela ultra-optimizada con 10 threads"""
        self.max_listas = max_listas
        self.mostrar_stats(len(listas))
        
        print(f"{C.H}🚀 INICIANDO VERIFICACIÓN TURBO...{C.R}\n")
        
        with ThreadPoolExecutor(max_workers=10) as executor:  # Aumentado a 10 threads
            futures = {executor.submit(self.procesar, lista): lista for lista in listas}
            
            for future in as_completed(futures):
                self.actualizar_progreso()
                
                if len(self.listas_validas) >= max_listas:
                    self.objetivo_alcanzado = True
                    
                    for f in futures:
                        if not f.done():
                            f.cancel()
                    
                    print(f"\n\n{C.S}🎯 ¡OBJETIVO ALCANZADO!{C.R}\n")
                    break
                
                try:
                    resultado = future.result()
                    if resultado:
                        self.listas_validas.append(resultado)
                        self.mostrar_lista(resultado, len(self.listas_validas))
                except:
                    pass
        
        print("\n")
    
    def mostrar_resumen(self):
        """Resumen final"""
        tasa = (len(self.listas_validas) / self.listas_analizadas * 100) if self.listas_analizadas > 0 else 0
        
        print(f"\n{C.H}{'='*70}")
        print(f"📊 RESUMEN FINAL")
        print(f"{'='*70}{C.R}")
        print(f"{C.I}  Analizadas : {C.S}{self.listas_analizadas}{C.R}")
        print(f"{C.I}  Válidas    : {C.S}{len(self.listas_validas)}{C.R}")
        print(f"{C.I}  Rechazadas : {C.E}{self.listas_rechazadas}{C.R}")
        print(f"{C.I}  Tasa éxito : {C.S}{tasa:.1f}%{C.R}")
        
        if self.stats_tipo:
            print(f"\n{C.I}  Por tipo:{C.R}")
            for tipo, count in self.stats_tipo.items():
                print(f"{C.M}    • {tipo:12} : {count}{C.R}")
        
        print(f"{C.H}{'='*70}{C.R}\n")
    
    def guardar(self):
        """Guardado optimizado"""
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        print(f"{C.I}💾 Guardando...{C.R}\n")
        
        # JSON
        f_json = f"iptv_validas_{ts}.json"
        with open(f_json, 'w', encoding='utf-8') as f:
            json.dump(self.listas_validas, f, indent=2, ensure_ascii=False)
        print(f"{C.S}  ✓ {f_json}{C.R}")
        
        # TXT
        f_txt = f"iptv_validas_{ts}.txt"
        with open(f_txt, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("LISTAS IPTV VERIFICADAS - VERSIÓN 4.0 TURBO\n")
            f.write(f"By: Maestro de la Calamidad | {datetime.now()}\n")
            f.write("="*70 + "\n\n")
            
            for i, lst in enumerate(self.listas_validas, 1):
                f.write(f"\nLISTA #{i}\n" + "-"*70 + "\n")
                f.write(f"URL       : {lst['url_completa']}\n")
                f.write(f"Host      : {lst['host']}\n")
                f.write(f"Tipo      : {lst['tipo_lista']}\n")
                f.write(f"Usuario   : {lst['username']}\n")
                f.write(f"Password  : {lst['password']}\n")
                f.write(f"Canales   : {lst['canales']}\n")
                f.write(f"Proxy     : {lst['proxy_usado']}\n")
                f.write(f"Fecha     : {lst['fecha']}\n")
            
            f.write(f"\n{'='*70}\n")
            f.write("By: Maestro de la Calamidad - Versión 4.0 TURBO\n")
            f.write("="*70 + "\n")
        
        print(f"{C.S}  ✓ {f_txt}{C.R}")
        
        # M3U
        f_m3u = f"iptv_compiladas_{ts}.m3u"
        with open(f_m3u, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            f.write(f"# By: Maestro de la Calamidad - Turbo {datetime.now()}\n\n")
            for lst in self.listas_validas:
                f.write(f"# {lst['tipo_lista']} | {lst['canales']} canales\n")
                f.write(f"{lst['url_completa']}\n\n")
        
        print(f"{C.S}  ✓ {f_m3u}{C.R}\n")
        
        print(f"{C.H}{'='*70}{C.R}")
        print(f"{C.M}  📁 {f_json}\n  📁 {f_txt}\n  📁 {f_m3u}{C.R}")
        print(f"{C.H}{'='*70}{C.R}\n")
    
    def ejecutar(self):
        """Ejecución principal"""
        self.banner()
        
        # Descargar proxies en paralelo
        self.gestor_proxies.descargar_proxies_paralelo()
        
        # Solicitar cantidad
        while True:
            try:
                print(f"{C.W}🎯 ¿Cuántas listas válidas? (1-50):{C.R}", end=' ')
                n = int(input())
                if 1 <= n <= 50:
                    print(f"{C.S}✓ Objetivo: {n} listas{C.R}\n")
                    break
                print(f"{C.E}❌ Rango: 1-50{C.R}\n")
            except ValueError:
                print(f"{C.E}❌ Número inválido{C.R}\n")
        
        # Descargar fuente
        listas = self.descargar_fuente()
        if not listas:
            print(f"{C.E}❌ Sin listas{C.R}")
            return
        
        # Verificar
        self.verificar_paralelo(listas, n)
        
        # Resumen
        self.mostrar_resumen()
        
        # Guardar
        if self.listas_validas:
            self.guardar()
            
            print(f"{C.M}")
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║              ✨ By: Maestro de la Calamidad ✨                       ║")
            print("║                 Versión 4.0 TURBO - 2026                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            print(f"{C.R}")
        else:
            print(f"{C.E}❌ Sin listas válidas{C.R}")

def main():
    """Main optimizado"""
    try:
        VerificadorTurbo().ejecutar()
    except KeyboardInterrupt:
        print(f"\n\n{C.W}⚠️  Interrumpido{C.R}")
    except Exception as e:
        print(f"\n{C.E}❌ Error: {e}{C.R}")

if __name__ == "__main__":
    main()