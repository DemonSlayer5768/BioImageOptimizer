
from pathlib import Path
from shutil import copy2
from uuid import uuid4


# Directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Directorio donde se almacenarán las imagenes
ORIGINALS_DIR = BASE_DIR / "data" / "images" / "originals"

# Formatos permitidos
SUPPORTED_FORMATS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp"
}


def import_images(file_paths):
    """
    Copia las imagenes seleccionadas al directorio originals.

    Retorna una lista con informacion de cada imagen importada.
    """

    ORIGINALS_DIR.mkdir(parents=True, exist_ok=True)

    imported_images = []

    for file_path in file_paths:

        source = Path(file_path)

        if not source.exists() or source.suffix.lower() not in SUPPORTED_FORMATS:
            continue

        # Identificador unico para evitar sobrescribir archivos
        image_id = str(uuid4())

        # Conservar la extensión original
        destination = ORIGINALS_DIR / f"{image_id}{source.suffix.lower()}"

        try:
            copy2(source, destination)

            imported_images.append({
                "id": image_id,
                "name": source.name,
                "path": str(destination),
                "format": source.suffix.lower()
            })

        except OSError as error:
            print(f"Error al importar {source.name}: {error}")

    return imported_images
