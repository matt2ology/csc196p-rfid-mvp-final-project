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


## Resources

- [Mini Thermal Receipt Printers > Making Connections > Raspberry Pi](https://learn.adafruit.com/mini-thermal-receipt-printer/making-connections#to-raspberry-pi-3133486)
  - [Connect and Configure Printer - USB printers: `ls -l /dev/usb/lp0`](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer#:~:text=USB%20printers%20may%20present%20themselves%20to%20the%20system%20differently%20depending%20which%20USB%2Dto%2Dserial%20chip%20they%20use%20internally.)
- [Interfacing Thermal Printer with Raspberry Pi to Print Text, Images, Barcodes and QR Codes](https://circuitdigest.com/microcontroller-projects/thermal-printer-interfacing-with-raspberry-pi-zero-to-print-text-images-and-bar-codes)

### Test via USB

`lsusb` - list USB devices: a  utility  for  displaying information about USB
buses in the system and the devices connected to them. It uses udev's hardware
database to associate a full human-readable name to the vendor ID and the
product ID.



```bash

```

### Test viaTransistor-Transistor Logic (TTL)
stty -F /dev/serial0 9600
echo -e "This is a test.\\n\\n\\n" > /dev/serial0
