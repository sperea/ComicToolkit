#!/bin/bash

# Ruta al script de Python (asumiendo que está en el mismo directorio que este script)
PYTHON_SCRIPT="./cbr2cbz.py"

# Verificar si el script de Python existe y es ejecutable
if [ ! -f "$PYTHON_SCRIPT" ] || [ ! -x "$PYTHON_SCRIPT" ]; then
    echo "Error: El script de Python no se encontró o no es ejecutable."
    exit 1
fi

# Recorrer todos los subdirectorios del directorio actual, excluyendo el directorio raíz
find . -type d ! -path . -mindepth 1 | while read dir; do
    echo "Procesando directorio: $dir"
    # Llamar al script de Python para cada subdirectorio
    python3 "$PYTHON_SCRIPT" -d "$dir"
done

echo "Proceso completado."
