# Import von libraries
import cv2 # OpenCV
import pytesseract # Texterkennung
import numpy as np
from pytesseract import Output
 
 #Bild definieren
img_source = cv2.imread('images/camera.jpg')
 
 # zu Grautönen mit Hilfe von cv2.cvtColor()-Funktion für bessere Lesbarkeit für Tesseract
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
 # bessere Lesbarkeit für Tesseract durch einteilung in schwarze und weisse Pixel
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
 
 # das Grauton-Bild wird geöffnet und störende Elemente ("Noise") werden entfernt
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
 
 # "Randerkennung", für später: grüner Rand
def canny(image):
    return cv2.Canny(image, 100, 200)
 
 # Ablauf für jedes Bild:
gray = get_grayscale(img_source)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
 
 #Text erkennen mit Tesseract, "Output.DICT" ist Wörterbuch
for img in [img_source, gray, thresh, opening, canny]:
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
 
    # zurück zu farbig, Grautöne zu RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
 
 # Hinzufügen von Textboxen: "conf" ist confidence score, wenn grösser als 60 wird zu Textbox (mit Funktion "cv2.rectangle()")
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # don't show empty text
            if text and text.strip() != "":
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img = cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
 
 # Anzeigen von verarbeitetem Bild
    cv2.imshow('img', img)
    cv2.waitKey(0)