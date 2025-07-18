# 🎼 Feature: Sistema Musical Modal

## Descripción
Un generador de escalas musicales y resoluciones armónicas, para ser usado en composición algorítmica y visualización simbólica.

## Funcionalidades esperadas
- Generación de escalas mayores, menores, modos griegos (dórico, frigio, lidio, mixolidio, etc.).
- Posibilidad de definir la tónica (root).
- Generación de resoluciones: suaves, tensas o disonantes.
- Sonar las notas generadas (usando sintes en Python o samples pregrabados).
- Preparar para visualización por glifo en módulos simbólicos.

## Entradas
- `modo`: tipo de escala o modo musical.
- `tónica`: nota raíz.

## Salidas
- Lista de notas.
- Audio de ejemplo.
- Diccionario JSON con metadata para visualización.

## Branch sugerido
`feature/modal-generator`

## Directorio sugerido
- Código: `backend/modal_generator.py`
- Audios: `frontend/audio_samples/`
