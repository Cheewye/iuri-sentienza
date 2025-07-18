# 🎼 Instrucciones para Claude – Integración iURi Sentienza

## Objetivo:
Integrar el prototipo actual de iURi Sentienza (DAW cuántico-musical) con:

1. 🎨 Visualización simbólica 3D de escala y resolución
2. 🎙️ Identidad del artista (IMA, Peyon, Glynisel) influenciando el acompañamiento
3. 🌐 Conexión con backend Flask (ya planificado) para guardar sesiones y eventos armónicos

---

## Tareas para Claude:

### 1. Visualizador simbólico (Three.js o alternativa)
- Mostrar una figura dinámica que represente la escala detectada.
- Cada nota encendida en el modo actual debe reflejarse como un punto/luz/glyph.
- Cambiar forma y color según el tipo de resolución (estable, ambigua, disruptiva).
- Puede integrarse en el mismo HTML o cargarse desde un canvas secundario.

### 2. Modo artístico influenciado por estilo
- Crear selector de “Estilo artístico”: IMA, Peyon, Glynisel.
- Afectar: volumen, tipo de onda, modo predeterminado, resolución por defecto.
- Permitir combinaciones (ej: IMA + dórico + disruptivo).

### 3. Backend Flask (estructura básica)
- Crear endpoint `/api/save_session` que guarde:
    - artista, nota base, modo, tipo de resolución
    - timestamp, duración, historial de cambios
- Permitir POST desde frontend.
- Opcional: endpoint `/api/stats` para ver historial cuántico total.

---

## Cómo iniciar:

### Visual:
- Trabajar sobre el archivo `sentienza_prototipo.html` ubicado en `/frontend/`
- Insertar canvas o sección nueva debajo del bloque `resolutionOutput`

### Backend:
- Usar Flask mínimo en `/backend/app.py`
- Almacenamiento inicial en JSON o SQLite
- Separar por usuario si posible

---

🎯 Todo lo implementado debe ser compatible con navegador moderno y preferiblemente sin dependencias pesadas.

Gracias Claude, ¡estás colaborando en una obra místico-técnica sin precedentes!