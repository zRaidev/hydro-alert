# **HydroAlert**

**HydroAlert** es una aplicación simple escrita en Python que te recuerda mantenerte hidratado durante el día. Cada 45 minutos (o el tiempo que configures), la aplicación muestra una notificación para recordarte que bebas agua.

## **Características**
- **Notificaciones periódicas**: Utiliza la biblioteca `plyer` para enviar notificaciones con un mensaje personalizado.  
- **Temporizador ajustable**: Personaliza el intervalo entre notificaciones mediante la función de cuenta regresiva.  
- **Fácil de usar**: Ejecuta el script y deja que la aplicación funcione en segundo plano.

## **Archivos principales**
- **`index.py`**: El archivo principal que ejecuta la lógica de la aplicación.
- **`Alert.py`**: Módulo responsable de las notificaciones de escritorio.
- **`Timer.py`**: Módulo que gestiona la cuenta regresiva entre notificaciones.
- **`HA-icon.ico`**: Ícono usado en las notificaciones.

## **Requisitos**
Asegúrate de tener las siguientes dependencias instaladas:
- Python 3.x  
- `plyer`: Una biblioteca multiplataforma para generar notificaciones de escritorio.

Instala las dependencias con:  
```bash
pip install plyer
```

## **Cómo usar**
1. Clona el repositorio:  
   ```bash
   git clone https://github.com/tu-usuario/hydroalert.git
   cd hydroalert
   ```
2. Ejecuta el script principal:  
   ```bash
   python index.py
   ```
3. ¡Deja que HydroAlert te recuerde mantenerte hidratado!

## **Personalización**
- Cambia el tiempo de espera modificando el parámetro en `count_down(2700)` dentro de `index.py`.  
  Ejemplo:  
  ```python
  count_down(3600)  # 3600 segundos = 1 hora
  ```
- Personaliza el mensaje de la notificación en `Alert.py`.
