# BioImage Optimizer

Aplicación de escritorio para el procesamiento, optimización y análisis de imágenes, desarrollada en Python utilizando PySide6.

---

## 🎨 Identidad Visual

### Paleta de colores

La interfaz de BioImage Optimizer utiliza una paleta oscura con tonalidades azul marino y detalles en turquesa, buscando una apariencia moderna, minimalista y profesional.

| Nombre     | Uso                                           | Código HEX |
| ---------- | --------------------------------------------- | ---------- |
| Background | Fondo general y ventanas                      | `#0b0f1a`  |
| Surface    | Sidebar, tarjetas y paneles                   | `#111a2e`  |
| Elevated   | Elementos internos y estados Hover            | `#1b2a41`  |
| Border     | Bordes, divisores y elementos activos         | `#2f3e56`  |
| Typography | Texto principal e iconos                      | `#c8d3e0`  |
| Accent     | Indicadores, selección y acciones principales | `#65D6C6`  |

### Referencia visual

| Color      | Vista previa                         | HEX       |
| ---------- | ------------------------------------ | --------- |
| Background | <span style="color:#0b0f1a">■</span> | `#0b0f1a` |
| Surface    | <span style="color:#111a2e">■</span> | `#111a2e` |
| Elevated   | <span style="color:#1b2a41">■</span> | `#1b2a41` |
| Border     | <span style="color:#2f3e56">■</span> | `#2f3e56` |
| Typography | <span style="color:#c8d3e0">■</span> | `#c8d3e0` |
| Accent     | <span style="color:#65D6C6">■</span> | `#65D6C6` |

---

## ⚙️ Comandos de desarrollo

Comandos útiles para configurar y trabajar con el proyecto.

| Descripción             | Comando                                     |
| ----------------------- | ------------------------------------------- |
| Activar entorno virtual | `.\env\Scripts\Activate.ps1`                |
| Abrir Qt Designer       | `pyside6-designer`                          |
| Ver paquetes instalados | `python -m pip list`                        |
| Guardar dependencias    | `python -m pip freeze > requirements.txt`   |
| Instalar dependencias   | `python -m pip install -r requirements.txt` |
| Ejecutar aplicación     | `python main.py`                            |

---

## 📁 Estructura del proyecto

```text
BioImageOptimizer/
│
├── main.py
├── requirements.txt
│
├── ui/
│   ├── MainWindow.ui
│   ├── main_window.py
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── Dashboard.ui
│   │   ├── dashboard.py
│   │   ├── Laboratory.ui
│   │   ├── laboratory.py
│   │   ├── Optimization.ui
│   │   ├── optimization.py
│   │   ├── Binarization.ui
│   │   ├── binarization.py
│   │   ├── Segmentation.ui
│   │   ├── segmentation.py
│   │   ├── Processing.ui
│   │   ├── processing.py
│   │   ├── Restoration.ui
│   │   ├── restoration.py
│   │   ├── Evaluation.ui
│   │   ├── evaluation.py
│   │   ├── History.ui
│   │   ├── history.py
│   │   ├── Settings.ui
│   │   └── settings.py
│   │
│   └── components/
│       ├── __init__.py
│       ├── image_viewer.ui
│       ├── image_viewer.py
│       ├── image_comparator.ui
│       ├── image_comparator.py
│       ├── parameter_panel.ui
│       ├── parameter_panel.py
│       ├── metric_card.ui
│       └── metric_card.py
│
├── algorithms/
│   ├── optimization/
│   ├── binarization/
│   ├── segmentation/
│   ├── processing/
│   └── restoration/
│
├── core/
│   ├── image_manager.py
│   ├── processing_engine.py
│   ├── experiment_manager.py
│   └── metrics.py
│
├── database/
│   └── database.py
│
└── resources/
    ├── icons/
    ├── images/
    └── styles/
```

---

## 🚀 Ejecución del proyecto

1. Clonar el repositorio.
2. Crear un entorno virtual.
3. Activar el entorno virtual.
4. Instalar las dependencias.
5. Ejecutar la aplicación.

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

---

## 📌 Estado del proyecto

En desarrollo.
