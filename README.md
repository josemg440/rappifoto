# RappiFoto

Aplicacion simple en Python que abre la camara del PC, toma una foto, detecta un numero en la imagen, y guarda la foto en el Escritorio con el numero detectado y un timestamp.

## Requisitos

- Python 3.9+
- Una camara disponible
- Tesseract OCR instalado en el sistema

## Instalacion

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows, usa:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

Controles:
- Presiona **ESPACIO** para tomar la foto.
- Presiona **Q** para salir.

Al abrir la camara se muestra un recuadro con borde amarillo en el tercio derecho de la ventana. Coloca el papel con el numero dentro de ese recuadro para mejorar la lectura.

La imagen se guarda en el Escritorio con el formato:

```
<numero>_YYYYMMDD_HHMMSS.jpg
```

Si no se detecta ningun numero, se usa `sin_numero`.
