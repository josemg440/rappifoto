import re
from datetime import datetime
from pathlib import Path

import cv2
import pytesseract


def get_desktop_path() -> Path:
    desktop = Path.home() / "Desktop"
    return desktop if desktop.exists() else Path.home()


def extract_number(image) -> str:
    config = "--psm 6"
    text = pytesseract.image_to_string(image, config=config)
    match = re.search(r"\bID\s*(\d{10})\b", text, re.IGNORECASE)
    if match:
        return match.group(1)
    return "sin_numero"


def draw_roi(frame, color=(0, 0, 255)) -> tuple[int, int, int, int]:
    height, width = frame.shape[:2]
    roi_width = width // 3
    roi_height = min(height - 40, 2 * (height // 3))
    x1 = width - roi_width - 20
    y1 = (height - roi_height) // 2
    x2 = width - 20
    y2 = y1 + roi_height
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    return x1, y1, x2, y2


def crop_to_roi(frame, roi: tuple[int, int, int, int]):
    x1, y1, x2, y2 = roi
    return frame[y1:y2, x1:x2]


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

        roi = draw_roi(frame)
        cv2.imshow("Camara", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        if key == ord(" "):
            roi_frame = crop_to_roi(frame, roi)
            number_text = extract_number(roi_frame)
            output_path = build_filename(number_text)
            cv2.imwrite(str(output_path), frame)
            print(f"Imagen guardada en: {output_path}")
            continue

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
