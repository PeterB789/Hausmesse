
# Dokumentation für Hausmesse 2022/23

## Abstract

## Inhaltsangabe

## Ressourcen

Hardware:
	Raspberry Pi 3 b+
	RFID RC522 Read/Writer
	5v Relay und diverse Elektronik-Kleinteile
	
Software
	Maria DB Datenbank Server
	Python 3.10

## Projektplanung


### Zeitplanung
- Zeitplan 2,5 Schulblöcke bis zur Hausmesse
	Gantt Diagramm??
- Brainstorming - Authentifizierung mit Türöffnung
	Paar Sätze schreiben, was wir ursprünglich vorhatten und warum es das nicht geworden ist.
	--> RFID CHIP

### Anforderungen/Ziele
- Türöffnungsmechanismus wird über RFID-Chip geöffnet
- Authentifizierung des RFID-Chips über Datenbankabfrage
- Anlegen/Entfernen von neuen Nutzern mit zugehörigen Chips
- Logging Funktionalität der Zugangskontrolle mit Timestamps
- Visuelles Feedback des Authorisierungsstatus implementieren (LED)

- Umfang festlegen
	- Datenbank mit Usern
	- RFID Elektronik
	- Türöffner
	- Steuerung auf Raspberry PI
- Aufgabenteilung
	- Datenbank
	- Elektronik
	- Gesamtplanung/Umsetzung
- Meilensteine
	- Funktionalität aller Komponenten
	- Datenbankdesign
	- Zusammenspiel aller Komponenten
	- Finale Tests

### Theorie

## Durchführung

### Elektronik
- Schaltplan Design

### Datenbank
- Datenbankdesign/Anforderungen
	- --> ERM Diagramm
- Datenbank aufsetzen
	- --> sql Befehle für Datenbank

### Programmieren
- Code für RFID-Ansteuerung
- Code für Datenbankabfragen
- Code-Logik für Türöffner

## Ergebnis

- Beschreibung des fertigen Produktes
- Erkenntnisse/Offene Fragen/Security Aspekte

## Quellenangaben

(1) https://pimylifeup.com/raspberry-pi-rfid-attendance-system/
		Für grobes Konzept und Start-Katalysator
(2) 