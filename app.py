import re
from datetime import datetime
from pathlib import Path

import cv2
import pytesseract


def get_desktop_path() -> Path:
    desktop = Path.home() / "Desktop"
    return desktop if desktop.exists() else Path.home()


def extract_number(image) -> str:
    config = "--psm 6 -c tessedit_char_whitelist=0123456789"
    text = pytesseract.image_to_string(image, config=config)
    digits = re.findall(r"\d+", text)
    return "_".join(digits) if digits else "sin_numero"


def build_filename(number_text: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{number_text}_{timestamp}.jpg"
    return get_desktop_path() / filename


def main() -> None:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise SystemExit("No se pudo abrir la camara.")

    print("Presiona ESPACIO para tomar la foto. Presiona Q para salir.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer la imagen de la camara.")
            break

        cv2.imshow("Camara", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        if key == ord(" "):
            number_text = extract_number(frame)
            output_path = build_filename(number_text)
            cv2.imwrite(str(output_path), frame)
            print(f"Imagen guardada en: {output_path}")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
