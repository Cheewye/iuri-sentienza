# iURi Sentienza – Backend Render

Este backend simple está listo para ser desplegado en Render.com y mantener el enjambre activo.

## Endpoints

- `/` – Prueba básica para saber si el backend está vivo.

## Uso

1. Subí este repo a GitHub
2. En Render:
   - New Web Service
   - Python
   - Ruta: este repo o carpeta
   - Start Command: `python app.py`
   - Port: `10000`

3. Usá UptimeRobot para hacer ping cada 5 minutos a:

```
https://<TU_RENDERNOMBRE>.onrender.com/
```
