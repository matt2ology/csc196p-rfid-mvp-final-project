# CSC 196P - Final Project - MVP RFID Technology & Raspberry Pi as a Platform

Final project for CSC 196P, Cloud and Mobile Computing Pragmatics, where a minimum viable product (mvp) using Radio Frequency Identification (RFID) scanner + tags and Raspberry Pi. This project must leverage the cloud.

## Project Proposal

My project will use the Raspberry Pi as the platform and connects to Firebase. The "service" will allow users to scan their RFID tags to indicate a "check-in" and allow administrators to "enroll" users to their respective RFID tags via a web/app portal customers (i.e. users and admin account holders) will use SSO to log in. Restful APIs are used to interface with database to log "check-ins" and "enroll" new users to RFID tags. SMS alerts will verify to users that their RFID tag(s) has been assigned to them, has been used to "check-in", or notify if it has been returned to lost-and-found.

## Resources

- [Mini Thermal Receipt Printers > Making Connections > Raspberry Pi](https://learn.adafruit.com/mini-thermal-receipt-printer/making-connections#to-raspberry-pi-3133486)
  - [Connect and Configure Printer - USB printers: `ls -l /dev/usb/lp0`](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer#:~:text=USB%20printers%20may%20present%20themselves%20to%20the%20system%20differently%20depending%20which%20USB%2Dto%2Dserial%20chip%20they%20use%20internally.)

## Micro Thermal Printer 5~9V Embedded Thermal Receipt Printer Serial Port Microcontroller Secondary Development MCU Printing Module TTL/RS232

Voltage: 5.44V

Temperature: 43

Printer Mode: Receipts

Command mode: EPSON(ESC/POS)

Interface: USB&TTL

Baudrate: 9600,N,8,1

USB Mode: Printer

Cutter: No

Chinese character mode: Yes

Drawer control: NO

character per line: 32-fontA/42-fontB

USB:PID:22337(0x5741)

VID:1157(0x0485)

Default Codepage: GB2312

[Hardware config]

Printer para:S:75,C:80,600, 150

Version: XP YC1.12.03.20221207

Modify: Dec 8 18:26:20

UID:CBA5A350-16030000-59433331  

QR Code: UID:CBA5A350-16030000-59433331
