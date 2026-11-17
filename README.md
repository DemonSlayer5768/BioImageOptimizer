# BioImage Optimizer

Aplicación de escritorio para el procesamiento, optimización y análisis de imágenes, desarrollada en Python utilizando PySide6.

---

## 🎨 Identidad Visual

### Paleta de colores

La interfaz de BioImage Optimizer utiliza una paleta oscura con tonalidades azul marino y detalles en turquesa, buscando una apariencia moderna, minimalista y profesional.

| Nombre     | Uso                                           | Código HEX |
| ---------- | --------------------------------------------- | ---------- |
| Background | Fondo general y ventanas                      | #0b0f1a    |
| Surface    | Sidebar, tarjetas y paneles                   | #111a2e    |
| Elevated   | Elementos internos y estados Hover            | #1b2a41    |
| Border     | Bordes, divisores y elementos activos         | #2f3e56    |
| Typography | Texto principal e iconos                      | #c8d3e0    |
| Accent     | Indicadores, selección y acciones principales | #65D6C6    |

### Colores de botones

| Nombre        | Variant    | uso           | color   | dissabled |
| ------------- | ---------- | ------------- | ------- | --------- | --- |
| PrimaryButton | btn_green  | btn_agregar   | #388E3C | #2F3E56   |
| PrimaryButton | btn_blue   | btn_modificar | #42A5F5 | #2F3E56   |
| PrimaryButton | btn_yellow | btn_guardar   | #FFB74D | #2F3E56   |     |
| PrimaryButton | btn_aqua   | cmbs y reset  | #65D6C6 | #2F3E56   |
| PrimaryButton | btn_red    | btn_eliminar  | #EF5350 | #2F3E56   |

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
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── env/                     # entorno virtual local
│
├── algorithms/
│   ├── binarizacion/
│   ├── optimizacion/
│   ├── procesamiento/
│   ├── restauracion/
│   └── segmentacion/
│
├── core/
│
├── data/
│   ├── database/
│   │   └── bioimageoptimizer.db
│   ├── images/
│   ├── originals/
│   ├── processed/
│   └── thumbnails/
│
├── resources/
│   ├── Icons/
│   └── images/
│
├── ui/
│   ├── MainWindow.py
│   ├── MainWindow.ui
│   ├── __pycache__/
│   ├── components/
│   └── pages/
│       ├── Tfrm_Binarizacion.py
│       ├── Tfrm_Binarizacion.ui
│       ├── Tfrm_Configuracion.py
│       ├── Tfrm_Configuracion.ui
│       ├── Tfrm_Dashboard.py
│       ├── Tfrm_Dashboard.ui
│       ├── Tfrm_Evaluacion.py
│       ├── Tfrm_Evaluacion.ui
│       ├── Tfrm_Galeria.py
│       ├── Tfrm_Galeria.ui
│       ├── Tfrm_Historial.py
│       ├── Tfrm_Historial.ui
│       ├── Tfrm_Optimizacion.py
│       ├── Tfrm_Optimizacion.ui
│       ├── Tfrm_Procesamiento.py
│       ├── Tfrm_Procesamiento.ui
│       ├── Tfrm_Restauracion.py
│       ├── Tfrm_Restauracion.ui
│       ├── Tfrm_Segmentacion.py
│       └── Tfrm_Segmentacion.ui
│
└── .git/
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
