# BioImage Optimizer

Aplicación de escritorio desarrollada en Python para importar, explorar y procesar imágenes biomédicas y generales mediante una interfaz gráfica construida con PyQt6/PySide6.

## Funcionalidades

### Panel principal

- Importación de una o varias imágenes.
- Acceso a las secciones de galería, binarización y segmentación.
- Interfaz oscura con navegación lateral.

### Galería

- Visualiza las imágenes originales y procesadas.
- Permite buscar por nombre y filtrar por categoría.
- Importa imágenes a `data/images/originals`.
- Permite seleccionar varias imágenes para eliminar, guardar o modificar su nombre.
- Abre una imagen seleccionada directamente desde la galería.

Formatos admitidos: PNG, JPG, JPEG, BMP, TIFF y WebP.

### Binarización

- Umbral fijo.
- Método de Otsu.
- Método Triangle.
- Umbral adaptativo por media.
- Umbral adaptativo gaussiano.
- Control opcional de inversión del resultado.
- Vista previa configurable.
- Guardado del resultado en `data/images/processed`.

### Segmentación

- Umbralización por rango.
- Umbralización adaptativa.
- Watershed.
- K-means.
- Region Growing mediante selección de una semilla en la imagen.
- SLIC/Superpíxeles.
- Vista previa con actualización diferida.
- Procesamiento en segundo plano para mantener activa la interfaz.
- Guardado del resultado en `data/images/processed`.

## Tecnologías

- Python
- PyQt6 para la aplicación principal
- PySide6 y archivos `.ui` generados con Qt Designer
- NumPy
- SciPy
- scikit-image
- QSS para el diseño visual

## Requisitos

- Windows
- Python 3.11 recomendado
- Entorno virtual de Python

Las dependencias se encuentran en `requirements.txt`.

## Instalación

Desde PowerShell, dentro de la carpeta del proyecto:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecución

Con el entorno virtual activado:

```powershell
python main.py
```

También puede ejecutarse el archivo incluido en el entorno:

```powershell
.\env\Scripts\python.exe main.py
```

## Pruebas

Las pruebas usan `unittest` y cubren los algoritmos de segmentación y el comportamiento del procesamiento en segundo plano.

```powershell
python -m unittest discover -s tests -p "test_*.py"
```

## Comandos útiles

| Acción | Comando |
| --- | --- |
| Activar el entorno virtual | `.\env\Scripts\Activate.ps1` |
| Abrir Qt Designer | `pyside6-designer` |
| Ver paquetes instalados | `python -m pip list` |
| Instalar dependencias | `python -m pip install -r requirements.txt` |
| Actualizar `requirements.txt` | `python -m pip freeze > requirements.txt` |
| Ejecutar la aplicación | `python main.py` |
| Ejecutar las pruebas | `python -m unittest discover -s tests -p "test_*.py"` |

## Estructura del proyecto

```text
BioImageOptimizer/
├── algorithms/
│   ├── binarizacion/
│   │   └── binarizacion.py
│   └── segmentacion/
│       └── segmentacion.py
├── core/
│   ├── image_manager.py
│   └── styles/
│       └── styles_manager.py
├── data/
│   ├── database/
│   │   └── bioimageoptimizer.db
│   └── images/
│       ├── originals/
│       └── processed/
├── resources/
│   ├── Icons/
│   └── styles/
│       ├── global.qss
│       └── components/
├── tests/
│   ├── test_segmentacion.py
│   └── test_segmentacion_worker.py
├── ui/
│   ├── MainWindow.py
│   ├── MainWindow.ui
│   └── pages/
│       ├── Frm_Dashboard.py
│       ├── Frm_Galeria.py
│       ├── Frm_Binarizacion.py
│       └── Frm_Segmentacion.py
├── main.py
├── requirements.txt
└── README.md
```

## Diseño

La interfaz utiliza una paleta oscura basada en azul marino y turquesa.

| Uso | Color |
| --- | --- |
| Fondo principal | `#0b0f1a` |
| Superficies y paneles | `#111a2e` |
| Elementos elevados | `#1b2a41` |
| Bordes y divisores | `#2f3e56` |
| Texto principal | `#c8d3e0` |
| Color de acento | `#65D6C6` |

Los estilos se cargan desde `resources/styles/global.qss` y la carpeta `resources/styles/components`.

## Estado del proyecto

El proyecto se encuentra en desarrollo. Las secciones de panel, galería, binarización y segmentación están implementadas.

La opción de máscara previa aparece deshabilitada en la interfaz hasta que se implemente su persistencia y aplicación.
