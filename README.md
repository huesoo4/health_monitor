# Health Monitor 🖥️

Una herramienta de monitoreo del sistema que proporciona información en tiempo real sobre el estado de hardware y servicios de tu servidor.

## 📋 Características

- **Monitoreo de CPU**: Uso en porcentaje con evaluación de estado
- **Monitoreo de RAM**: Porcentaje de uso y disponibilidad en GB
- **Monitoreo de Disco**: Uso del filesystem raíz y espacio disponible
- **Estado de Servicios**: Verifica si servicios críticos están corriendo
- **Evaluación de Estado**: Clasifica recursos como OK, WARNING o DANGER

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.7+
- pip

### Instalación Local

```bash
# Clonar o descargar el repositorio
cd health_monitor

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python main.py
```

## 📊 Salida de la Aplicación

```
================================
       SYSTEM HEALTH
================================

Hostname: myserver

CPU
Usage: 45.2 %
Status: OK

MEMORY
Usage: 62.5 %
Available: 15.34 GB
Status: OK

DISK /
Usage: 78.9 %
Available: 45.67 GB
Status: WARNING

SERVICES
sshd       running
docker     running
nginx      stopped
cron       running
```

## 📁 Estructura del Proyecto

```
health_monitor/
├── main.py              # Punto de entrada principal
├── requirements.txt     # Dependencias Python
├── services.json        # Configuración de servicios a monitorear
├── README.md            # Este archivo
└── monitor/
    ├── cpu.py          # Monitoreo de CPU
    ├── ram.py          # Monitoreo de memoria RAM
    ├── disk.py         # Monitoreo de disco
    ├── hostname.py     # Obtención del nombre del host
    ├── services.py     # Verificación de estado de servicios
    └── status.py       # Evaluación de estado de recursos
```

## ⚙️ Configuración

### Servicios a Monitorear

Edita `services.json` para agregar o quitar servicios:

```json
{
  "services": [
    "sshd",
    "docker",
    "nginx",
    "cron"
  ]
}
```

## 📈 Niveles de Estado

| Estado | Rango | Significado |
|--------|-------|-------------|
| OK | 0-70% | Recurso disponible, sin problemas |
| WARNING | 70-85% | Recurso bajo, monitorear de cerca |
| DANGER | 85-100% | Recurso crítico, intervención necesaria |
| ERROR | < 0 o > 100 | Error en la lectura de datos |


## 🔧 Dependencias

- **psutil** (5.9.8): Librería para obtener información del sistema

## 📝 Uso Avanzado

### Ejecutar Periódicamente

Para ejecutar el monitoreo cada cierto tiempo, puedes usar:

**Con cron (Linux/Mac):**
```bash
# Cada 5 minutos
*/5 * * * * cd /path/to/health_monitor && python main.py >> health.log 2>&1

# Cada hora
0 * * * * cd /path/to/health_monitor && python main.py >> health.log 2>&1
```

### El script falla localmente

```bash
# Asegúrate de tener psutil instalado
pip install -r requirements.txt

# En algunos sistemas necesitas permisos de administrador para ciertos datos
sudo python main.py
```

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
