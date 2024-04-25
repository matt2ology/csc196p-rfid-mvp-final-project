# CSC 196P - Final Project - MVP RFID Technology & Raspberry Pi as a Platform

Final project for CSC 196P, Cloud and Mobile Computing Pragmatics, where a minimum viable product (mvp) using Radio Frequency Identification (RFID) scanner + tags and Raspberry Pi. This project must leverage the cloud.

## Project Proposal

My project will use the Raspberry Pi as the platform and connects to Firebase. The "service" will allow users to scan their RFID tags to indicate a "check-in" and allow administrators to "enroll" users to their respective RFID tags via a web/app portal customers (i.e. users and admin account holders) will use SSO to log in. Restful APIs are used to interface with database to log "check-ins" and "enroll" new users to RFID tags. SMS alerts will verify to users that their RFID tag(s) has been assigned to them, has been used to "check-in", or notify if it has been returned to lost-and-found.
