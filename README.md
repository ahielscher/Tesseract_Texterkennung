# Tesseract_Texterkennung
Texterkennung mit Tesseract für RaspberryPi in Python

ZWECK / ZIEL

Grundanforderung: Texterkennung auf mit dem RaspberryPi gemachten Bildern (compl1.py). Gemacht in Anlehnung an Tutorial (Link unten).
Erweiterung 1: Live-Texterkennung (compl2.py). Gemacht in Anlehnung an Tutorial (Link unten).
Erweiterung 2: Eigene Vereinfachung von Code soweit es geht. Dabei wird nicht auf das Wörterbuch zugegriffen, wodurch keine Textboxen erstellt werden.



ANFORDERUNGEN

Hardware:
    - RaspberryPi mit MicroSD
    - RaspberryPi Camera

Software:
    - neue Pythonversion
    - OpenCV library
    - Tesseract OCR (UB-Mannheim)



ARBEITSPROZESS

    - da kein Vorwissen zum Thema vorhanden war, recherchierte ich erst ausgiebig. Dabei stiess ich auf Tesseract, welches von der UB Mannheim zur Texterkennung und 
      Digitalisierung verschiedener Texte gebraucht wird und für Windows verfügbar gemacht wurde. 
    - Ich stiess auf das Projekt "https://tutorials-raspberrypi.com/raspberry-pi-text-recognition-ocr/", welches mir sehr half, das Vorgehen mit Tesseract zu verstehen.
    - Die zwei Files "compl1.py" und "compl2.py" sind die Umsetzung des Projekts, versetz mit Kommentaren für Verständnis.
    - Mit diesem Wissen versuchte ich eine vereinfachte Version zu schreiben, "simple.py"
    - Tests wurden mit den ausführlicheren (complX.py) und der vereinfachten Version (simple.py) gemacht,
      jedoch eignen sich die complX.py-Dateien besser, da duch die Textbox eine schnellere Sichtbarkeit der Erkennung gewährleistet ist.



PROBLEME

    - erste Probleme bestanden darin, Tesseract herunterzuladen. Als ich es endlich geschafft hätte,
      wurde mir angezeigt, dass diese Aktion auf dem Schullaptop nicht möglich ist, da ich kein Admin bin.
    - der eigene Laptop konnte nnicht in der Schule mit dem Internet verbunden werden
    - Die Verbindung Zuhause von Laptop und RaspberryPi war nur mit Ethernetkabel möglich
    - Nach einem Systemupdate konnte nicht mehr auf OpenCV zugegriffen werden, obwohl dies korrekt innstalliert war etc. Bei Recherche des Problems stiess ich 
      auf weitere Lösungswege, welche alle nicht funktionierten. Schliesslich fand ich heraus, dass es mir nicht möglich sein wird, wieder mit cv2.___ von OpenCV zu arbeiten. 
      Weitere Tests konnten dadurch nicht durchgeführt werden :(
    - Teilweise traten Probleme mit der Kamera auf, die nach langem Pröbeln und Verändern des Codes an einem Wackelkontakt lagen.




TESTS UND ANPASSUNGEN:
Verschiedene Parameter bei Text verändert, da Tesseract eigentlich für gedruckten Text ist.:
                                                - Anordnung (auf einer Linie oder nicht)
                                                - Unregelmässigkeit von Schriftart
                                                - Handschriftlichkeit ("hässlicher" geschrieben)
                                                - Einheitlichkeit der Schriftgrösse
