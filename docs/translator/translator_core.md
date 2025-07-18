# 🎼 iURi Sentienza – DAW Translator Core

> Documento técnico preliminar – Generado automáticamente el 2025-07-18

---

## 🌍 Propósito

Unificar la comunicación entre diferentes DAWs, VSTs y herramientas generadas por IA (Claude, GPT, iURi, etc.), a través de un **protocolo simbólico-musical universal**, que permita:

- Traducción de escalas, acordes, secuencias y efectos entre plataformas.
- Exportación/Importación entre Ableton, Logic, TidalCycles, SuperCollider, Bitwig, FL Studio, VCV Rack, etc.
- Integración de salidas LLM (JSON, YAML, texto natural) con formatos musicales ejecutables (MIDI, OSC, VST).
- Visualización en tiempo real del flujo colaborativo, logs, errores, decisiones y mejoras.

---

## 🧠 Arquitectura Propuesta

```
Claude/GPT/iURi/Other LLMs
        ↓
  ✴ Generación musical simbólica
        ↓
🎛️ Translator Core (Sentienza Universal Protocol)
        ↓
🎚️ DAWs/VSTs: Tidal, Ableton, VCV, Logic...
        ↓
🎧 Audio + Visual + Narrativa
        ↓
📜 Log documentado + revisión simbólica
```

---

## 🎛️ DAWs y formatos objetivo

| Plataforma         | Entrada       | Salida         | Formatos soportados            |
|-------------------|---------------|----------------|---------------------------------|
| Ableton Live      | MIDI, .als    | WAV, .als      | .mid, .als                      |
| TidalCycles       | Haskell code  | SuperDirt audio| .tidal, .hs                     |
| SuperCollider     | SC code       | Audio + OSC    | .scd, OSC                       |
| VCV Rack          | Patch JSON    | Audio          | .vcv, .wav                      |
| Bitwig / Logic    | MIDI, scripts | Audio          | .mid, .als/.logic               |
| VSTs Custom       | JSON/YAML     | Sound Module   | VST3, LV2, JUCE                 |

---

## 🔄 Casos de uso

1. 🎼 GPT genera escala dórica → convertida a `.mid` → ejecutada en TidalCycles.
2. 🎨 Claude crea glifo 2D → traducido a parámetros OSC → afecta filtros en VCV Rack.
3. 📜 iURi narra la sesión musical → log documentado con timestamp y resumen.

---

## 🗂 Estructura sugerida

- `translator/`: funciones de conversión
- `glossary/`: diccionario simbólico común
- `logs/`: histórico de decisiones y errores
- `bridge_api/`: micro API para conexión local
- `frontend/monitor`: UI en vivo del sistema

---

## 🚧 Próximos pasos

- [ ] Crear función `translate_scale_to_midi()`
- [ ] Definir schema común `SentienzaCore` (JSON)
- [ ] Crear plantilla para logs automáticos
- [ ] Habilitar backend para ejecución sonora en local (Flask)
