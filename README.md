# CSC 196P - Final Project MVP - Cloud Solution: RFID Technology & Raspberry Pi as a Platform

Final project for CSC 196P, Cloud and Mobile Computing Pragmatics, where a
minimum viable product (mvp) using Radio Frequency Identification (RFID)
scanner + tags and Raspberry Pi. This project must leverage the cloud.

## Project Proposal

My project will use the Raspberry Pi as the platform and connects to Firebase.
The "service" will allow users to scan their RFID tags to indicate a "check-in"
and allow administrators to "enroll" users to their respective RFID tags via a
web/app portal customers (i.e. users and admin account holders) will use SSO to
log in. Restful APIs are used to interface with database to log "check-ins" and
"enroll" new users to RFID tags. SMS alerts will verify to users that their
RFID tag(s) has been assigned to them, has been used to "check-in", or notify
if it has been returned to lost-and-found.

## Python Dependencies

- **firebase_admin:** is the Firebase Admin SDK for Python. It enables access
  to Firebase services from privileged environments in Python. The SDK provides
  a way to interact with Firebase Cloud Firestore, Firebase Realtime Database,
  Firebase Authentication, Google Cloud Storage, and Firebase Cloud Messaging.
  - `pip install firebase_admin`
- **mfrc522:** is an implementation of the RFID RC522 interface, this library
  handles all the heavy lifting for talking with the RFID over the Pi’s SPI
  Interface and is used to read the RFID tags.
- **twilio:** is a Python module that allows you to interact with the Twilio
  API. With it, you can send SMS messages, make phone calls, and send emails.
- **python-escpos:** is a Python library that allows you to send data to
  thermal printers. It is a pure Python implementation that works with Python
  2.7 and Python 3.4+.
  - `python -m pip install python-escpos`
- **adafruit-circuitpython-thermal-printer:** is a CircuitPython library for
  thermal printers. It is designed to work with the Adafruit Mini Thermal
  Receipt Printer. It should work with any printer that uses ESC/POS commands
  like the Epson TM-T20 or the [Maikrt Micro Thermal Printer](https://a.co/d/7SnoBkb),
  but has only been tested with the Adafruit printer.
  - `pip install adafruit-circuitpython-thermal-printer`
  - [Mini Thermal Receipt Printers CircuitPython and Python](https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython)

## Resources

A list of resources that I used to help me with this project and to give credit

  - [Connect and Configure Printer - USB printers: `ls -l /dev/usb/lp0`](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer#:~:text=USB%20printers%20may%20present%20themselves%20to%20the%20system%20differently%20depending%20which%20USB%2Dto%2Dserial%20chip%20they%20use%20internally.)
- [Add the Firebase Admin SDK to your server](https://firebase.google.com/docs/admin/setup)
- [Automate the boring stuff - CH 18 - SENDING EMAIL AND TEXT MESSAGES](https://automatetheboringstuff.com/2e/chapter18/)
- [Django + Firebase](https://forum.djangoproject.com/t/django-firebase/16628/2)
- [Firebase - Documentation Admin SDK - Python](https://firebase.google.com/docs/admin/setup#python_1)
- [GitHub: Adafruit_Blinka](https://github.com/adafruit/Adafruit_Blinka)
- [Interfacing Thermal Printer with Raspberry Pi to Print Text, Images, Barcodes and QR Codes](https://circuitdigest.com/microcontroller-projects/thermal-printer-interfacing-with-raspberry-pi-zero-to-print-text-images-and-bar-codes)
- [Maikrt Compact Maikrt 58MM Thermal Receipt Printer Module|USB/TTL Serial Port ESCPOS Commands](https://www.ubuy.co.in/product/7LNB6RM8-maikrt-embedded-58mm-thermal-receipt-printer-mini-printing-module-support-usb-and-ttl-serial-port-es)
- [Mini Thermal Receipt Printers > Making Connections > Raspberry Pi](https://learn.adafruit.com/mini-thermal-receipt-printer/making-connections#to-raspberry-pi-3133486)
- [YouTube: Bytes Of Code - Python - Handle Data in Firestore Database](https://www.youtube.com/watch?v=-jWD-vIyirw&ab_channel=BytesOfCode)
- [YouTube: Bytes Of Code - Python - How To Create Firestore Database](https://www.youtube.com/watch?v=qsFYq_1BQdk&ab_channel=BytesOfCode)
- [YouTube: Fireship - 100 Firebase Tips, Tricks, and Screw-ups](https://youtu.be/iWEgpdVSZyg?si=XHr4D4m5K5Y9vM57&t=1090)
- [YouTube: Tech With Tim - Learn Django in 20 Minutes!!](https://www.youtube.com/watch?v=nGIg40xs9e4&ab_channel=TechWithTim)

## Raspberry Pi Setup & Configuration for Thermal Printer (Maikrt)

### Test via USB

`lsusb` - list USB devices: a utility for displaying information about USB
buses in the system and the devices connected to them. It uses udev's hardware
database to associate a full human-readable name to the vendor ID and the
product ID.

[USB printers may present themselves to the system differently depending which USB-to-serial chip they use internally. Try the following first:](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer#:~:text=USB%20printers%20may%20present%20themselves%20to%20the%20system%20differently%20depending%20which%20USB%2Dto%2Dserial%20chip%20they%20use%20internally.%20Try%20the%20following%20first%3A)

```bash
ls -l /dev/usb/lp0
```

Print a test page:

```bash
echo -e "This is a test.\\n\\n\\n" > /dev/usb/lp0
```

Print a test image:

```bash
lp -o fit-to-page /usr/share/raspberrypi-artwork/raspberry-pi-logo.png
```

### Test viaTransistor-Transistor Logic (TTL)

[For a TTL (not USB) printer, type the following (substitute the correct baud rate for your printer):](<https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer#:~:text=For%20a%20TTL%20(not%20USB)%20printer%2C%20type%20the%20following%20(substitute%20the%20correct%20baud%20rate%20for%20your%20printer)%3A>)

```bash
stty -F /dev/serial0 9600
echo -e "This is a test.\\n\\n\\n" > /dev/serial0
```

## Code Ideas and Inspirations

A list of code ideas and inspirations that I used to help me with this project

- [django-todo/todos/firebase_client.py](https://github.com/saadmk11/django-todo/blob/master/todos/firebase_client.py)
- [Python-Thermal-Printer/printertest.py](https://github.com/adafruit/Python-Thermal-Printer/blob/master/printertest.py)

## Table of Contents

- [CSC 196P - Final Project MVP - Cloud Solution: RFID Technology \& Raspberry Pi as a Platform](#csc-196p---final-project-mvp---cloud-solution-rfid-technology--raspberry-pi-as-a-platform)
  - [Project Proposal](#project-proposal)
  - [Python Dependencies](#python-dependencies)
  - [Resources](#resources)
  - [Raspberry Pi Setup \& Configuration for Thermal Printer (Maikrt)](#raspberry-pi-setup--configuration-for-thermal-printer-maikrt)
    - [Test via USB](#test-via-usb)
    - [Test viaTransistor-Transistor Logic (TTL)](#test-viatransistor-transistor-logic-ttl)
  - [Code Ideas and Inspirations](#code-ideas-and-inspirations)
  - [Table of Contents](#table-of-contents)
