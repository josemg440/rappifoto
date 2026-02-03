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
codex/create-photo-capture-application-in-python-7k87yc
Despues de guardar una foto, la camara queda abierta para tomar mas.

Al abrir la camara se muestra un recuadro con borde rojo (doble de alto) en el tercio derecho de la ventana. Coloca el papel con el numero dentro de ese recuadro para mejorar la lectura.
=======
codex/create-photo-capture-application-in-python-8v3xzd
Despues de guardar una foto, la camara queda abierta para tomar mas.

Al abrir la camara se muestra un recuadro con borde amarillo (doble de alto) en el tercio derecho de la ventana. Coloca el papel con el numero dentro de ese recuadro para mejorar la lectura.
=======

Al abrir la camara se muestra un recuadro con borde amarillo en el tercio derecho de la ventana. Coloca el papel con el numero dentro de ese recuadro para mejorar la lectura.
 main
main

La imagen se guarda en el Escritorio con el formato:

```
<numero>_YYYYMMDD_HHMMSS.jpg
```

codex/create-photo-capture-application-in-python-7k87yc
El OCR busca el patron `ID` seguido de un numero de 10 digitos dentro del recuadro. Si no se detecta, se usa `sin_numero`.
=======
Si no se detecta ningun numero, se usa `sin_numero`.
main

## Actualizar el codigo (git)

Si ya hiciste cambios y quieres subirlos a tu repositorio:

```bash
git status -sb
git add .
git commit -m "Describe tu cambio"
git push
```

Para bajar los cambios en la carpeta que descargaste en tu Mac (tu clon local):

```bash
git pull
```

Si trabajas en una rama distinta, usa `git push -u origin <tu-rama>` la primera vez, y luego `git pull` desde esa misma rama.
