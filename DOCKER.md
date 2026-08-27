# Health Monitor - Docker Setup

## Archivos Agregados

- **Dockerfile**: Configuración para construir la imagen Docker
- **docker-compose.yml**: Orquestación para ejecutar el contenedor
- **.dockerignore**: Archivos excluidos del contexto de build
- **requirements.txt**: Dependencias Python (psutil)

## Cómo Usar

### Opción 1: Con Docker Compose (Recomendado)

```bash
# Construir la imagen
docker-compose build

# Ejecutar la aplicación
docker-compose up

# Ejecutar en background
docker-compose up -d

# Ver logs
docker-compose logs -f health-monitor

# Detener
docker-compose down
```

### Opción 2: Con Docker CLI

```bash
# Construir la imagen
docker build -t health-monitor .

# Ejecutar el contenedor
docker run --rm \
  --privileged \
  -v /sys:/sys:ro \
  -v /proc:/proc:ro \
  -v /dev:/dev:ro \
  health-monitor
```

## Características

- **Imagen base**: Python 3.11-slim (ligera ~150MB)
- **Acceso al sistema host**: Monta `/sys`, `/proc` y `/dev` en modo lectura
- **Privileged mode**: Necesario para acceso completo a información del sistema
- **Reinicio automático**: El contenedor se reinicia si falla (con `docker-compose`)

## Notas

- La aplicación necesita acceso a información del sistema del host para funcionar correctamente
- En entornos de producción, considera ejecutar la aplicación periódicamente con cron o un scheduler similar
- El contenedor está configurado para ejecutarse de forma interactiva (puedes ver el output en tiempo real)

## Troubleshooting

Si la aplicación no lee datos correctamente:
```bash
# Verificar que los volúmenes están correctamente montados
docker inspect <container_id> | grep Mounts
```
