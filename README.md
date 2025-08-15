# Gestion-Aerolinea-EFI
EFI Ingenieria de Software

# 🚀 Instalación y Uso - Sistema de Reservas Aéreas

## 📋 Requisitos previos
- Python 3.12 o superior
- Git
- pip (gestor de paquetes Python)
- Virtualenv (opcional pero recomendado)

---

## 📥 Instalación

1️⃣ **Clonar el repositorio**
```bash
git clone git@github.com:SalvadorCoco/Gestion-Aerolinea-EFI.git
cd Gestion-Aerolinea-EFI
```

2️⃣ **Crear y activar el entorno virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3️⃣ **Instalar los requerimientos**
```bash
pip install -r requirements.txt
```

4️⃣ **Correr las migraciones**
```bash
python manage.py migrate
```

5️⃣ **Crear SuperUser (opcional)**
```bash
python manage.py createsuperuser
```

6️⃣ **Iniciar el proyecto**
```bash
python manage.py runserver
```

**Ingresar a:**
http://127.0.0.1:8000
