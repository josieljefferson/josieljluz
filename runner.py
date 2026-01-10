# runner.py
import subprocess
import sys
import threading

def install_requirements():
    """Instala as dependências do requirements.txt"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        sys.exit(1)

def run_app():
    subprocess.run([sys.executable, "app.py"])

def run_epg():
    subprocess.run([sys.executable, "epg.py"])

if __name__ == "__main__":
    # Primeiro instala as dependências
    install_requirements()
    
    # Depois inicia os scripts
    t1 = threading.Thread(target=run_app)
    t2 = threading.Thread(target=run_epg)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
