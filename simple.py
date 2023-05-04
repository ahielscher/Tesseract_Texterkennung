#Import von libraries
import cv2
import pytesseract

# Kamera anschalten und Foto machen
camera = cv2.VideoCapture(0)
_, image = camera.read()

# Foto in Grauskala wandeln, damit Tesseract besser erkennen kann (Kontrast)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# weitere "Vereinfachungen" für Tesseract
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#Tesseract OCR anwenden in der Sprache Deutsch
text = pytesseract.image_to_string(threshold_image, lang='ger')

# Ausgabe
print(text)