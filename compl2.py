# import von libraries
import cv2 # OpenCV
import pytesseract
from pytesseract import Output
 
 # Kamera initialisieren
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
 
 # While-Schlaufe für fortlaufende Kameraaktivität
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
 # Für jeden Frame wird mit Tesseract mit Funktion "pytesseract.image_to_data" Text und die Grösse der Textbox erkannt
    d = pytesseract.image_to_data(frame, output_type=Output.DICT)
    n_boxes = len(d['text'])
    
    # Loop: Jede Textbox durchlaufen um "confidence score = conf" zu überprüfen, ob über 60. Wenn über 60 wird Text, Position und Grösse extrahiert, dadurch Rechteck um Textbox und ausschrift des Textes durch Funktion "cv2.putText()"
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            
            if text and text.strip() != "":
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
 
    # Display von resultierendem Frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# Wenn alles fertig ist wird das Display-Fenster "destroyed" (cv2.destroyAllWindows() ) und Kamera freigestellt.
cap.release()
cv2.destroyAllWindows()
 