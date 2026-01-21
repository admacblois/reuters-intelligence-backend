# DL360 INSTALLATION MANUAL

# WNE Customer Technical Guide

Page 1 of 70




© Thomson Reuters 2024. All Rights Reserved.

Thomson Reuters, by publishing this document, does not guarantee that any information contained herein is and will remain accurate or that use of the information will ensure correct and faultless operation of the relevant service or equipment. Thomson Reuters, its agents, and employees, shall not be held liable to or through any user for any loss or damage whatsoever resulting from reliance on the information contained herein.

This document contains information proprietary to Thomson Reuters and may not be reproduced, disclosed, or used in whole or part without the express written permission of Thomson Reuters.

Any Software, including but not limited to, the code, screen, structure, sequence, and organization thereof, and Documentation are protected by national copyright laws and international treaty provisions. This manual is subject to U.S. and other national export regulations.

Nothing in this document is intended, nor does it, alter the legal obligations, responsibilities or relationship between yourself and Thomson Reuters as set out in the contract existing between us.

# WNE Customer Technical Guide

Page 2 of 70






# Contents

# 1     OVERVIEW

5

# 2     SERVER PREPARATIONS

6

# 2.1      Requirements Before Installation (Replacing WNE v6 Hardware)

6

# 2.2      What The WNE7 And RLS Does

7

# 2.3      How The WNE7 Interface Looks

7

# 2.4      How The WNE7 Server Works

7

# 2.5      WNE7 Data Flow

8

# 3     HARDWARE PROVIDED

9

# 4     REQUIRED CONNECTIVITY

10

# 4.1      Power Requirements

10

# 4.2      KVM Connections

10

# 4.3      Video Connections

10

# 4.4      Satellite Connection

10

# 4.5      Network Connections

11

# 4.6      Internet Connectivity

12

# 4.7      Security Recommendations

13

# 5     CONNECTIVITY DIAGRAMS

15

# 5.1      Ericsson RX8200 Receiver

15

# 5.2      HP DL-360 G10 Server

15

# 5.3      FULL Connectivity Diagram

15

# 6     NETWORK CHANGES

16

# 6.1      Using a Switch or Router

16

# 7     WNE SERVER CONFIGURATION

17

# 7.1      Access Team Viewer via KVM

17

# 7.2      No Internet Connectivity

18

# 7.3      Check The Server User Interface

18

# 7.4      Login To The Server Administrator User

18

# 7.5      Check The Server Software Version

19

# 7.6      Upload The Latest Server Software

19

# 7.7      Import The following Server Software Versions

20

# 7.8      Upload The Configuration

22

# 7.9      Import The Client Settings

22

# 7.10     Import The KenCast license

23

# 7.11     Import The File Distribution Settings

26

# 7.12     Check The Internet Backup Setting

27

# 7.13     Check The Playout Option

29

WNE Customer Technical Guide                                                   Page 3 of 70






# WNE Customer Technical Guide

# Contents

| 7.14       | Check Channel List                          | 30 |
| ---------- | ------------------------------------------- | -- |
| 8          | WNE User Interface                          | 31 |
| 8.1        | The Action Buttons And Icons                | 31 |
| 8.2        | Stories Page                                | 31 |
| 8.2.1      | Add Page to Distribution                    | 31 |
| 8.2.2      | Download Items To The Desktop               | 32 |
| 8.2.3      | My Videos                                   | 32 |
| 8.3        | User Management                             | 34 |
| 8.4        | File Distribution                           | 35 |
| 8.5        | Video Playout                               | 35 |
| 8.5.1      | Loop and Auto mode                          | 37 |
| 8.5.2      | Manual mode                                 | 38 |
| 8.5.3      | Live signals                                | 39 |
| 8.5.4      | Fixed channels                              | 41 |
| 8.5.5      | SDI Output ports panel                      | 42 |
| 8.6        | How to Link Different WNE7 Servers          | 42 |
| APPENDIX A | Changing Network Setting                    | 45 |
| APPENDIX B | System Checks                               | 51 |
| B.1        | Satellite Receiver Check                    | 51 |
| B.1.1      | Satellite Signal                            | 51 |
| B.1.2      | Service selection                           | 52 |
| B.1.1.3    | MPE selection                               | 52 |
| B.2        | WNE File Reception                          | 53 |
| B.3        | File Distribution Check                     | 53 |
| B.3.1      | File Distribution logs                      | 54 |
| B.4        | Video Playout                               | 55 |
| B.5        | Internet backup Check                       | 55 |
| APPENDIX C | WNE6 RETIREMENT INSTRUCTIONS                | 56 |
| APPENDIX D | CONFIGURATION OF MULTIPLE WNE UNITS         | 58 |
| APPENDIX E | WHAT’S NEW IN THE WNE7                      | 59 |
| I.1        | SENT FROM CONNECT FEATURE                   | 59 |
| I.2        | FOUR (4) SDI Video Outputs                  | 61 |
| APPENDIX F | HOW TO EXPORT OLD CONTENT FROM WNE6 TO WNE7 | 62 |
| APPENDIX G | FILE DISTRIBUTOR                            | 63 |
| APPENDIX H | TECHNICAL SUPPORT                           | 70 |

Page 4 of 70





# 1 OVERVIEW

Thomson Reuters as a leading company in the news agency field is working hard to provide the best for our clients; the Reuters video server known as World News Express (WNE) will be replaced with a new generation of servers known as WNE7.

World News Express (WNE) and Reuters Live Service (RLS) are Reuters’ media products delivering broadcast video news to many of the world’s leading news organisations.

To ensure a reliable and fault free reception it is important that the hardware and software provided by Reuters is maintained in a manner as set out in this guide.

If there are any technical issues, please contact our customer support centre via telephone, mobile application, or web form for prompt assistance. See Appendix J at the end of this document for contact details.

This document is based on version 7.0 (WNE7) of World News Express, released March 2021.

WNE Customer Technical Guide    Page 5 of 70



# SERVER PREPARATIONS

Before the server installation take place, there are several requirements that the client should fulfil.

# REQUIREMENTS BEFORE INSTALLATION (REPLACING WNE V6 HARDWARE)

There are different installation scenarios, therefore, the requirements before the server installation takes places are:

REQUIREMENTS
The WNE6 (existing hardware) Keep or Removal Letter has been signed
Scenario 1: Server swap
• External KVM {keyboard/mouse (USB)} and VGA video connector
• A Windows PC with access to the same WNE server subnet, Internet connectivity and a remote access application for Reuters Technical Support
• SDI cables (4x) – depends on the usage
• Internet connectivity
• Network settings of the WNE6
• File Distributor settings
• Log ZIP file of the WNE6
• Prepare 1 TB of storage space (cloud storage) to collect last 30-days of content
• Last 24-hours of content will be retrieved via Internet
Scenario 2: Running in parallel using WNE6 as CDN-only (Maximum 14-days)
• 1U Rack space
• Two (2) available power plugs socked
• UTP cable to connect the server to the network (new network settings)
• External KVM {keyboard/mouse (USB)} and VGA video connector
• A Windows PC with access to the same WNE server subnet, Internet connectivity and a remote access application for Reuters Technical Support
• SDI cables (4x) – depends on the usage
• Internet connectivity
• New server network settings
• File Distributor - new network settings (cloud storage) as well WNE6 File Distributor settings
• Log ZIP file of the WNE6
Scenario 3: Running in parallel via Satellite (Maximum 14-days)
• 1U Rack space
• Three (3) available power plugs socked
• UTP cable to connect the server to the network (new network settings)
• Network switch to split the Ericson receiver data/control connectivity
• 4 extra UTP cables to connect the server to the network switch
• External KVM {keyboard/mouse (USB)} and VGA video connector
• A Windows PC with access to the same WNE server subnet, Internet connectivity and a remote access application for Reuters Technical Support
• SDI cables (4x) – depends on the usage
• Internet connectivity
• New server network settings
• File Distributor - new network settings (cloud storage) as well WNE6 File Distributor settings
• Log ZIP file of the WNE6

WNE Customer Technical Guide    Page 6 of 70





# 2.2 WHAT THE WNE7 AND RLS DOES

WNE7 like the previous version WNE6 is a file-based delivery system designed for broadcast customers. The legacy delivery method is satellite broadcast using a number of satellites (see Section 4.4) to ensure global coverage, with Internet delivery or Satellite plus Internet now supported. Where satellite reception is required, an Ericsson IP/satellite receiver (see Section 5.1) processes the feed received from the customer managed antenna and outputs the RLS live video as an analogue and SDI video feed. The receiver also passes the encrypted file data (MPE data) to the provided WNE7 server for processing.

The WNE7 server receives this MPE data from the Ericsson receiver and stores the completed video and script files on the local hard drives. When Internet is provided it either replaces the real-time satellite reception or acts as a back-up for when content is missed over the satellite feed. A web page interface is provided for all user interaction and allows newsroom staff to preview video (with internet connection), control the playout of video via an SDI card (see Section 4.3) as well as selectively or automatically move videos to the customer’s own newsroom servers for ingest and processing.

# 2.3 HOW THE WNE7 INTERFACE LOOKS

The main interface for the WNE is a webpage. Typically, the provided server is networked to the customer editorial LAN allowing newsroom access from the desktop. A URL http://IP-address/ shows a list of recently received stories together with a search function, playout controls and action buttons to move or play a specific story.

REUTERS WORLD NEWS EXPRESS GMT Help Status Admin administrator

Stories Q Search Stories Search Advanced Search

Live All Stories Sent From Connect Advisories Playout Sent From Connect History My Videos

:: Show advisories Show early access scripts 6 Add Page To Distribution

# BOX 1: NOW PLAYING OUT

| Preview | HD            | Slug  | ID                    | Headline                                                                                  | Arrived          | Actions          |
| ------- | ------------- | ----- | --------------------- | ----------------------------------------------------------------------------------------- | ---------------- | ---------------- |
| 1       | SDI output 01 |       | Reuters               | 3163 Vaccine change will have negligible impact on rollout - England's deputy chief medic | 2021-04-08 08:32 | D + Via Internet |
| 2       | SDI output 02 | 02:57 | ASTRAZENECA-MHRA-MORE |                                                                                           |                  | (Rev. 5)         |
| 3       | SDI output 03 |       | Reuters               | Advisory - SPORTS DAILY OUTLOOK - THURSDAY APRIL 8, 2021                                  | 2021-04-08 08:31 | Advisory         |
| 4       | SDI output 04 |       | CCTV                  | 4602 CCTV promo video offers sneak peek into Chinese expressway development               | 2021-04-08 08:29 | + Via Internet   |

This screen shows the features when logged in as Administrator. The customer IT staff can create other logins with varying roles to enable or disable features such as playout control or ability to move files.

# 2.4 HOW THE WNE7 SERVER WORKS

The new WNE7 server provided uses an Ubuntu v18.04 host operating system where Dockers has been installed to allows running the required WNE7 server containers. Docker is a set of platforms as a service (Paas) product that use Operating System-level virtualization to deliver software in packages called containers.

The server contains server modules working as a group to support the server functionality as shown in the image below:






# 2.5 WNE7 DATA FLOW

As explained in Section 2.2, when satellite delivery is required, the Ericsson receiver passes encrypted file data to the WNE server for processing. This data stream is processed by the KenCast Fazzt software, which recombines the data into individual files moved to the WNE satellite input folder.

For Internet only or satellite units with Internet Backup, the CDN process routinely checks Reuters’ head-end servers for required files, downloaded either all new content or only those missed due to problems with satellite receptions. In the case of Internet back-up, when used only for backup purposes, downloaded content will be delayed by a period of 2-3 hours to prevent duplication of both satellite and Internet downloads.

The Reuters File Processor service determines which videos should be decrypted and presented to the customer and stores copies in a folder. Note that customers should not access this folder directly but should use the File Distribution process to make copies of files as needed.

Any received video, script or advisory that matches an automatic File Distribution process filter will be automatically transferred based on the distribution process settings to the customer’s server for instant processing.

The WNE Player allows to control the four SDI card outputs. Each port is fully configurable for Live events or File playout, including the option for dedicated “Sent from Connect” playout. The “Send from Connect” option will allow our clients to use points to access additional video stories and send directly from the Reuters Connect (www.reutersconnect.com) website to the Reuters video server (WNE7).






# 3 HARDWARE PROVIDED

To meet the needs of different customers we have two hardware options, one of which should have been provided to you:

# FOR ALL CUSTOMERS

An HP DL360 G10 is a 1U rack-mount server – this is the main provided unit and is designed to be installed in a standard 19-inch 800MM deep 42U machine rack using the provided mounts.

# OPTIONALLY

In addition to the server/workstation provided, customers needing satellite reception should have a 1U height Ericsson Rx8200 DVB receiver provided with rack mount panel holes. The Ericsson receiver is used to receive and forward satellite file-data to the server and receive and output the Reuters Live Service (RLS) where Internet reception is insufficient.

Unless space does not allow a space of 1U should always be allowed between the server and receiver as illustrated below.

|    | 1U                |     | 1U     |    |
| -- | ----------------- | --- | ------ | -- |
| 1U |                   | YOR | W'ADIT | 1U |
| 1U | SPACE FOR AIRFLOW | 1U  |        |    |
|    | 1U                |     | 1U     |    |
|    | 1U                |     | 1U     |    |

The WNE7 server specifications are:

- Model: Hewlett Packard (HP) ProLiant DL360 Gen10
- CPU: Xeon Silver 4114
- Processor base frequency: 2.20 GHz
- RAM: 16 GB (2 x 8GB)
- Disk drive: 4 TB SAS 7.2K rpm (x2) / 480 GB SATA MU (x2)
- Raid controller: HP Smart Array P408i-a SR G10
- Ethernet adapter 1GB 4-ports
- Deck Link 8k SDI card (4-ports)
- HPE 96W Smart Storage Battery
- HPE 800W power supply kit

WNE Customer Technical Guide    Page 9 of 70





# 4 REQUIRED CONNECTIVITY

# 4.1 POWER REQUIREMENTS

The (optional) Ericsson RX8200 requires a single IEC power cable. The HP DL360 G10 1U server has power redundancy and requires two IEC power cables. When powering up the units the Ericsson receiver should be switched on before the server.

# 4.2 KVM CONNECTIONS

The keyboard and mouse connecters on the servers are USB rather than PS/2 so any KVM device will need to support USB input.

# 4.3 VIDEO CONNECTIONS

The RX8200 receiver supports SD-SDI, HD-SDI, and analogue output of live video. Audio is provided as embedded in the SDI signal or as analogue audio – there is no separate digital audio output. The video playout from the provided server uses a Deck Link 8K PRO SDI only I/O card which can be configured as either SD-SDI or HD-SDI. The customer needs to provide a BNC cable to connect to a monitor, distribution playout system or recording device. Refer to the diagram below to confirm which ports to use for output as well as the Genlock (Ref In).

Deck Link 8k PRO SD/HD SDI Card – Installed in the WNE7 DL-360 G10.

| 12G-SDI In/Out | 4 o |          |
| -------------- | --- | -------- |
| 12G-SDI In/Out | —3ₒ | PCIZ     |
| 12G-SDI In/Out | —2ᵒ | EXPRESS⁸ |
| 12G-SDI In/Out | -01 | 0        |
| Ref In         | —   | o        |

# 4.4 SATELLITE CONNECTION

To receive the WNE and RLS service via satellite, the customer must provide a single RF coaxial connection to a satellite antenna positioned on the correct satellite for your region. In general, for the signal to be sufficient you must have a downlink that provides a C/N margin (signal quality above background noise) must be approximately 3dB or better. The RX8200 receiver will be pre-configured for the region by the engineer performing the installation, but you will need to confirm if the receiver needs to power your LNB and provide detail on the LNB local oscillator if you are in a region with Ku-band reception.

WNE Customer Technical Guide Page 10 of 70




WNE Customer Technical Guide

# The table below shows the satellites on which Reuters currently transmit the WNE and RLS services.

# Reuters Video: SES and AsiaSat-5 Satellite Scheduled for Decommissioning on August 22, 2025

| Region                 | North America         | South America         | Europe & North Africa  | Middle East & Africa   | Asia              |
| ---------------------- | --------------------- | --------------------- | ---------------------- | ---------------------- | ----------------- |
| Satellite              | SES-15                | SES-4                 | SES-4                  | SES-5                  | AsiaSat-5         |
| In Production till     | 22 August 2025        | 22 August 2025        | 22 August 2025         | 22 August 2025         | 22 August 2025    |
| Position               | 129° West             | 22° West              | 22° West               | 5 East                 | 100.5° East       |
| Down Link Frequency    | 12121.8 MHz (Ku-Band) | 12058.7 MHz (Ku-Band) | 11126.35 MHz (Ku-Band) | 12053.54 MHz (Ku-Band) | 3960 MHz (C-Band) |
| Symbol Rate            | 17 MS/s               | 15.5 MS/s             | 17.25 MS/s             | 30.0 MS/s              | 30.0 MS/s         |
| FEC                    | 3/5                   | 2/3                   | 3/5                    | 3/4                    | 5/6               |
| Modulation             | DVB-S2 8PSK           | DVB-S2 8PSK           | DVB-S2 QPSK            | 8PSK                   | DVB-S2 8PSK       |
| Down Link Polarisation | Horizontal            | Vertical              | Horizontal             | Vertical               | Horizontal        |
| Based on Antenna Size  | 1.8m or greater       | 1.8m or greater       | 1.8m or greater        |                        |                   |
| Coverage Map           | Link                  | Link                  | Link                   | Link                   | Link              |

# Reuters Video: Telstar Signal Enters Production Post June 23, 2025, with AsiaSat-5 Satellite Introducing a New Transponder Post July 16, 2025

| Region                 | North America           | South America           | Europe, Middle East & North Africa | Asia                 |
| ---------------------- | ----------------------- | ----------------------- | ---------------------------------- | -------------------- |
| Satellite              | T11N                    | T12V                    | T12V                               | AsiaSat-5            |
| In Production          | 16 June 2025            | 16 June 2025            | 16 June 2025                       | 16 July 2025         |
| Position               | 37.5° West              | 15.0° West              | 15.0° West                         | 100.5° East          |
| Down Link Frequency    | 11,723.64 MHz (Ku-Band) | 11,181.75 MHz (Ku-Band) | 11341.5 MHz (Ku-Band)              | 3,991.5 MHz (C-Band) |
| Symbol Rate            | 17.25 MS/s              | 17.25 MS/s              | 20.1667 MS/s                       | 15.833 MS/s          |
| FEC                    | 3/5                     | 3/5                     | 3/4                                | 2/3                  |
| Modulation             | DVB-S2 8PSK             | DVB-S2 8PSK             | DVB-S2 QPSK                        | DVB-S2 8PSK          |
| Down Link Polarisation | Vertical                | Vertical                | Vertical                           | Horizontal           |
| LNB Power              | 13V(VERT.)              | 13V(VERT.)              | 13V(VERT.)                         | 18V(HORIZ.)          |
| LNB 22khz              |                         |                         |                                    |                      |
| Based on Antenna Size  | 1.8m or greater         | 1.8m or greater         | 1.8m or greater                    | Existing Antenna     |
| Coverage Map           | Link                    | Link                    | Link                               | Link                 |
| Video resolution (fps) | HD60/SD525              | HD60/SD525              | HD50 & SD625                       | HD50 & SD625         |

# 4.5 NETWORK CONNECTIONS

There are two (2) Ethernet cables needed between the satellite receiver and the server. A control port is needed for configuration of the receiver and for decryption of the video’s files and a multicast data connection is required for the server to receive the MPE file data from the receiver. A managed Internet connection – firewall and/or proxy protected - should be connected via the Eno8 (UTP port 4) port on the WNE server. The internet connection is vital to the operation of the WNE service, supporting remote monitoring, alerts, and a back-up for retrieving any videos that are not successfully received over the satellite path, or a completely independent delivery path (Internet only units). Please refer to the diagrams in Section 5 for the correct network configuration as well as Appendix A which details the network set-up process. If you make use of network address translation you should use the real (physical) IP-

Page 11 of 70





# 4.6 INTERNET CONNECTIVITY

As listed above, a managed Internet connection via the Eno8 port is an important part of the delivery system. It is required for:

1. Back-up retrieval of content missed during to poor weather or local interference, or as a completely independent and reliable delivery path for customers not needing satellite delivery.
2. Remote monitoring of the server and receiver
3. Email alerting for specific problem conditions (e.g. Loss of satellite lock, hardware failure, etc)
4. Delivery of Internet delivered live video streams
5. Remote support, upgrades, and troubleshooting.

Unless DHCP on a Client Network assigns address credentials to WNE7, the following information will be required during installation:

- Fixed IP address on Client Network (including Subnet Mask, Gateway, and Broadcast address)
- DNS addresses
- Proxy address and password details for Internet access if required.
- NTP (Network Time Protocol) address of a machine on the client network if required.

The following domains and ports must be permitted on any firewall or proxy-server you use for WNE/RLS to function correctly. All are TCP ports and outbound access only is required and recommended:

| Domain Name                                    | Protocol & Port                  | Description                          |
| ---------------------------------------------- | -------------------------------- | ------------------------------------ |
| content.reuters.com                            | HTTP/HTTPS (TCP port 80 and 443) | Repository Server of Reuters         |
| secure.content.reuters.com                     | HTTPS (TCP port 443)             | Media Content                        |
| ums5rup13e.execute-api.eu-west-1.amazonaws.com | HTTP (TCP port 443)              | Preview Monitor Video                |
| videobroadcast.cdn.reuters.com                 | HTTPS (TCP port 80 and 443)      | Hosted Reuters Content               |
| videobroadcast.cdns.reuters.com                |                                  |                                      |
| rmb.reuters.com                                | HTTP/HTTPS (TCP port 80 and 443) | Reuters Content Web Service          |
| stats.wne.reuters.com                          | HTTPS (TCP port 443)             | Remote monitoring                    |
| commerce.reuters.com                           | HTTPS (TCP port 443)             | Reuters Connect Authorization Server |
| \*.teamviewer.com                              | HTTP (TCP port 80)               | Remote Support                       |
|                                                | HTTPS (TCP port 443)             |                                      |
|                                                | TCP port 5938                    |                                      |
| ssh access                                     | TCP port 22                      |                                      |
| rlsplus.wne.reuters.com                        | HTTP/HTTPS (TCP port 80 and 443) | RLS Plus video stream                |
| dat.wne.reuters.com                            | HTTP/HTTPS (TCP port 80 and 443) | Client Permissions                   |
| dat.wne.reutersconnect.com                     | HTTP/HTTPS (TCP port 80 and 443) |                                      |

WNE Customer Technical Guide

Page 12 of 70





WNE Customer Technical Guide

lives.reutersconnect.com              HTTP (TCP port 80)       Lives Preview

cdn1.agency.thomsonreuters.com        HTTPS (TCP port 443)

cdn2.agency.thomsonreuters.com        HTTPS (TCP port 443)

d3iwkuprshvnfk.cloudfront.net         HTTPS (TCP port 443)     Reuters Live

d1qvkrpvk32u24.cloudfront.net         HTTPS (TCP port 443)     Reuters Live (Broadcast)

ndg2bwusid.execute-api.us-east-       HTTPS (TCP port 443)     User Interface Preview

1.amazonaws.com

tr-wne-client.s3.amazonaws.com        HTTPS (TCP port 443)     Upgrades

stats.wne.reuters.com                 HTTPS (TCP port 443)     Monitoring

reutersconnect.com                    HTTPS (TCP port 443)     WebSocket

liaison.reuters.com                   HTTPS (TCP port 443)     Container update

usea1-thomsonreuters.sentinelone.net   HTTPS (TCP port 443)     Sentinelone Antivirus

dv-us-prod.sentinelone.net            HTTPS (TCP port 443)     Sentinelone Antivirus

ioc-gw-prod-us-1a.sentinelone.net     HTTPS (TCP port 443)     Sentinelone Antivirus

ioc-gw-prod-us-1b.sentinelone.net     HTTPS (TCP port 443)     Sentinelone Antivirus

mgmt-file-upload-us-east-1-prod.sentinelone.net  HTTPS (TCP port 443)     Sentinelone Antivirus

xdr.us1.sentinelone.net               HTTPS (TCP port 443)     Sentinelone Antivirus

cdn.sentinelone.net                   HTTPS (TCP port 443)     Sentinelone Antivirus

If you use a proxy server to allow external Internet connectivity it must be HTTP or SOCKS 4/5 compatible. The configuration requires an IP-address/domain name so a proxy.pac type configuration file cannot be used.

When a unit is Internet only a recommended Internet bandwidth of 30Mbps is recommended to support timely file reception alongside live video.

To support timely retrieval in a satellite back-up configuration we recommend an Internet bandwidth of 6.5mbps for timely SD retrieval and 13.5mbps for HD retrieval.  Less bandwidth will result in increased delays in retrieving any missed files.

Even if only a minimal bandwidth can be provided it is still extremely useful for remote support, alerting and monitoring.

It must be noted however that under no circumstances should an unprotected internet connection be attached to the WNE server given the obvious security risks this creates.

# 4.7  SECURITY RECOMMENDATIONS

Thomson Reuters strongly advises to configure the internet firewall outbound only for WNE!

The Customer DMZ should allow WNE to deliver content to the customer file distribution server outbound only.

The Customer's internal Firewall could allow HTTP access to the WNE to control the UI for configuration, status, manual SDI playout, and file distribution.

Page 13 of 70




# WNE Customer Technical Guide

# Page 14 of 70

For maintenance, a (remote) KVM is required and in some cases on request internet remote access via client equipment uses ssh.

# INTERNET

WNE documentation will explain minimum internet needs

| DMZ Network      | FIREWALL                       | Customer access to WNE UI           |
| ---------------- | ------------------------------ | ----------------------------------- |
| FIREWALL         | WNE Server (internet outbound) | Customer Distribution ingest server |
| Internal Network |                                |                                     |






# 5 CONNECTIVITY DIAGRAMS

Please refer to the images below for the various units to confirm the connections for your unit.

# 5.1 ERICSSON RX8200 RECEIVER

| RF          | Analogue          | Power         |
| ----------- | ----------------- | ------------- |
| Satellite   | Audio Output      | Input 1       |
| RLS         | DC VOLTAGE 13/18V | 6             |
| RX8200      | AS1               |               |
| WNE IP Data | SD-Analogue       | SD-SDI        |
| Management  | Port 2 Only       | Output        |
| RLS         | RLS               | Control Ports |

# 5.2 HP DL-360 G10 SERVER

| SDI ports                               | 4             | 3        | 2          | 1    | Ref. | + |
| --------------------------------------- | ------------- | -------- | ---------- | ---- | ---- | - |
| 3                                       |               |          |            | RE.A | L    |   |
| Ethernet ports                          | USB ports (2) | ILO port | VGA Port   |      |      |   |
| UTP port 1 → Eno5 - Engineering         |               |          | Dual Power |      |      |   |
| UTP port 2 → Eno6 - Control port RX8200 |               |          |            |      |      |   |
| UTP port 3 → Eno7 - Data port RX8200    |               |          |            |      |      |   |
| UTP port 4 → Eno8 - Client interface    |               |          |            |      |      |   |

# 5.3 FULL CONNECTIVITY DIAGRAM

| RF        | RLS Frame                      | ASI        |
| --------- | ------------------------------ | ---------- |
| Satellite | Analogue Audio                 | Sync Input |
| Input 1   | Output                         | Power      |
| IP OUT 2  | RLS                            |            |
| WNE Data  | Analogue Video                 |            |
| Output    | Plugin Module - RF & IP Output | or \[ASI]  |
|           | Default R8000 Rear Panel       | +          |
|           | +                              | 6660660    |
|           | -009000                        |            |

Eth0/Eno8 Control Engineering

Data Customer Network

REUTERS

WNE Customer Technical Guide

Page 15 of 70






# 6 NETWORK CHANGES

The default settings are given in the table below:

| Hardware                    | IP Address       | Purpose                         |
| --------------------------- | ---------------- | ------------------------------- |
| RX8200 IP OUT 2             | 172.16.2.2       | Used to carry WNE IP data only. |
| RX8200 CONTROL 2            | 172.16.2.20      | Management access to receiver.  |
| HP Server eno5 (UTP port 1) | Assigned by DHCP | Reuters Engineering             |
| HP Server eno6 (UTP port 2) | 172.16.2.125     | Default address for RX control. |
| HP Server eno7 (UTP port 3) | 172.16.2.25      | Default address for WNE IP Data |
| HP Server eno8 (UTP port 4) | \*.\*.\*.\*      | Customer Network address.       |

# 6.1  USING A SWITCH OR ROUTER

If multiple WNE servers share access of a common RX8200 receiver then it is necessary to place a switch or router between the receiver and servers as shown in Appendix D.

It is possible to use a switch or router with a single server if required, but the data connection from the receiver should not be routed over a common LAN since the traffic is multicast and may cause congestion on the LAN.

If a 100MBPS switch/router is used between the server and Eno8 connection, then it is essential the registry change to ensure network speed is not hampered, please contact Reuters Media Technical support, to perform this change.

WNE Customer Technical Guide    Page 16 of 70






# 7 WNE SERVER CONFIGURATION

After the server ports (network configuration) have been configured as shown on Appendix A, lets proceed and configure the server.

# 7.1 ACCESS TEAM VIEWER VIA KVM

To complete a new server configuration, it is necessary to access the Team Viewer application via KVM (Keyboard, Video and Mouse) and take note of the Team Viewer ID and access the password to share it with the Reuters Media Technical Team (MTS) to help with the server configuration.

- Go to the Application Launcher (left-bottom corner), click over “Applications”, go to the “Internet” section, and click over Remote Control and Meeting solution (Team Viewer application).
- Take note and provide to the Reuters Engineer the ID and password.

Please go in TeamViewer and click over the “Extras” tab and click “Options”, go to the “General” tab and check the “start TeamViewer with system” and click over OK.

The Team Viewer ID/password via KVM will change after each server reboot. After the container file installation, the Team Viewer ID/password via Internet access will remain.

WNE Customer Technical Guide Page 17 of 70







# 7.2 NO INTERNET CONNECTIVITY

In situations where there is no Internet connectivity, please test the server connectivity and connect to a client PC under the same server subnet environment and do a PING to eno8 (server IP) from the client PC as shown in the image below:

C:. Administrator: Command Prompt                                                                                  10X
Microsoft Windows [Uersion 6.1.7601]
Copyright (c) 2009 Microsoft Corporation. All rights reserved.
C:\Users\administrator.WNEC-WINDOWS>ping 10.127.0.29
Pinging 10.127.0.29 with 32 bytes of data:
Reply from 10.127.0.29: bytes=32 time&#x3C;1ms TTL=63
Reply from 10.127.0.29: bytes=32 time&#x3C;1ms TTL=63    Response from eno8
Reply from 10.127.0.29: bytes=32 time&#x3C;1ms TTL=63                                             Connectivity OK
Reply from 10.127.0.29: bytes=32 time&#x3C;1ms TTL=63
Ping statistics for 10.127.0.29:
Packets: Sent = 4, Received = 4, Lost = 0 &#x3C;0% loss>
Approximate round trip times in milli-seconds:
Minimum = Øms, Maximum = Øms, Average = 0ms

# 7.3 CHECK THE SERVER USER INTERFACE

After checking the server connectivity, access the server User Interface from the client PC using the server IP-address as shown in the image below: (the IP shown here is only an example)

Reuters |WNE Client  ×  +                                                                                           *
←       →  C                127.0.0.1/stories?advisories=false&#x26;earlyscripts=true#list                                                     90%    0 ↓ N

REUTERS       WORLD NEWS EXPRESS                                                                                                        GMT    Help  Logins
Stories               Q Search Stones                                                                                                            Search  Advanced Search
Live                   All Stories    Reuters  CCTV  Perform Inc.  Stats Perform  Sent From Connect
Advisories
Playout                Asia           CCTV News  Europe  Latin  Life!  Omnisport Uncut   Reuters Live Service  Reuters Live Service Plus  Sent From Connect  Showbiz  World
History

# 7.4 LOGIN TO THE SERVER ADMINISTRATOR USER

Go to the server IP-address using an Internet browser as shown in the image below, and click over Logins (in the upper-right corner) and then login to the Administrator page with the credentials shown in the image below;

Username: Administrator
password: admin

Reuters | WNE Client version 0.0.36 X  +    MV
←          C Not secure 10.127.0.29/auth/login?authredirect=%252Fstories%2523list#box-0    O Q
REUTERS | WORLD NEWS EXPRESS                                                               GMT V  Help Status  Logins
There are some problems with your WNE client on box BOX 1, click here for information    Log in to BOX 1
Stories    Search Stories                                                                                                                Search  Advanced Search
Live
Advisories
Playout                                         Log in to World News Express
History                                         on BOX 1 (box 1 of 1)

BOX 1: NOW PLAYING OUT                          Username
administrator
Password
admin
Keep me logged in
Log In

Forgotten your login details? Recover them






# 7.5 CHECK THE SERVER SOFTWARE VERSION

Go to “Status” tab and click over the “About” tab and check the version of the software.

- If the software version is 7.0.47.7 as shown in the following image, please go to section 7.6 and update the software version to the latest one.

| Software Version Info |          |
| --------------------- | -------- |
| Version:              | 7.0.47.7 |
| Installed Patches:    |          |

- If the software version is equal or higher than 7.2.90.1 as shown in the following image, please go straight to section 7.8

| Software Version Info |          |
| --------------------- | -------- |
| Version:              | 7.2.90.1 |
| Installed Patches:    |          |

# 7.6 UPLOAD THE LATEST SERVER SOFTWARE

To get the full server functionality it is essential to upload the latest software version to the WNE7 server. The four following files shown below should be provided by the Media Technical Support Engineer and stored on a client PC connected to the same network as the WNE7 server; the files should be installed in the order shown below and then all server services should be restarted.

1. It is mandatory to upgrade first to wnec-release_7.0.69.0_amd64.tgz as shown in Section 7.7
2. After the mandatory upgrade proceed with wnec-release_7.1.73.7_amd64.tgz
3. After above upgrades, install the latest available version wnec-release_7.2.xx.xx_amd64.tgz
4. settings.json
5. Example Kencast licence: PC181470-SerialMXQ945030F.kcl
6. distribution_processes.json
7. Restart all the server services

Connect to the WNE7 server via client PC (that should contain the configuration files)





# 7.7 IMPORT THE FOLLOWING SERVER SOFTWARE VERSIONS

To install the server software versions, go to “Status”, then click over “Software Upgrades” and click over “Upload File” to upload the first mandatory software version as shown in the image below:

Upload and install the first mandatory version wnec-release_7.0.69.0_amd64.tgz, and repeat the same steps with version wnec-release_7.1.73.7_amd64.tgz, and with the latest version wnec-release_7.2.xx.xx_amd64.tgz

|                  | Home              | Name                                |         | Size                              | Modified                |
| ---------------- | ----------------- | ----------------------------------- | ------- | --------------------------------- | ----------------------- |
| 1 manual         | Desktop           | wnec-release\_7.1.73.7\_amd64.tgz   | 2.7 GB  | 17 Jun                            |                         |
|                  | Documents         | PC181612-SerialMXQ94502Y2.kcl       | 22.1 kB | 5 Sep                             |                         |
| 2 Reuters Live 4 | Downloads         | MXQ94502Y2-settings-WNEFRFR241.json | 1.1 kB  | 5 Sep                             |                         |
| 3 Reuters Live 5 | Pictures          |                                     |         |                                   | 2022-06-20 12:10:43 GMT |
| 4 Reuters Live 6 | Videos            |                                     |         | 2022-06-17 14:56:03 GMT           |                         |
|                  | boot              |                                     |         |                                   |                         |
|                  | data              |                                     |         | 2022-06-17 14:31:08 GMT           |                         |
|                  | database          |                                     |         |                                   |                         |
|                  | debs              |                                     |         |                                   |                         |
|                  | docker            |                                     |         |                                   |                         |
|                  | efi               |                                     |         |                                   |                         |
|                  | Filesystem r...   |                                     |         |                                   |                         |
|                  |                   | upgrade                             |         |                                   |                         |
|                  | var               |                                     |         |                                   |                         |
|                  | wneclient         |                                     |         |                                   | 2022-06-17 13:55:32 GMT |
|                  | + Other Locations |                                     |         | All Files 2022-06-07 15:33:13 GMT |                         |

Upload the file to the server: This step will take approximately 5 minutes and the server will display the below message. Refresh the Internet browser (F5) before it will display the new release appear as shown in the image below.

| Version  | Status          | Release Note | Scheduled Start | Actions |
| -------- | --------------- | ------------ | --------------- | ------- |
| 7.0.69.0 | NEW             |              |                 |         |
| 7.0.47.7 | Current version |              |                 |         |
| 7.0.47.7 | INSTALLED       |              |                 |         |

Upgrade History

| Status Date | Old Status | UPLOAD PACKAGE | Message                                                                                                                                  |
| ----------- | ---------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
|             |            |                | Upgrade package has been uploaded successfully. The version will be available for upgrade as soon as the package processing is finished. |

Close



WNE Customer Technical Guide

Apply the file to the server: After the file has been registered by the server, click over the upload action (“Upgrade to latest version”) button as shown in the image below. Login again into the Administrator user if you have been signed out.

REUTERS | WORLD NEWS EXPRESS                                       GMT V  Help Status Admin    administrator

Stories          There are some problems with your WNE client on Box 1, click here for information.

Stories                                                                                                               Search  Advanced Search

Live                      About  Services  Software Upgrades  File Logs  Device Status  Host Info Advisories

Playout                                                                                                                   + Upload File

History

My Videos                 New Releases

| Version         | Status          | Release Note | Scheduled Start | Actions |
| --------------- | --------------- | ------------ | --------------- | ------- |
| 7.0.69.0        | NEW             |              |                 |         |
| 7.0.47.7        | Current version |              |                 |         |
| 1 SDI output 01 | 7.0.47.7        | INSTALLED    |                 |         |
| 2 SDI output 02 |                 |              |                 |         |
| 3 SDI output 03 |                 |              |                 |         |
| 4 SDI output 04 |                 |              |                 |         |

The server will ask you if you want to upgrade the system to the software version 7.0.69.0 as shown in the image below, click over “Upgrade” as shown in the image below:

REUTERS | WORLD NEWS EXPRESS                                                                                                                                        GMT  Help  Status  Admin    administrator

There are some problems with your WNE client on box Box 1, click here for information.

Stories                  Q                                                                                                                                                                      Souroh  Advanced Search

Live                     About        Services  Software Upgrades  File Logs  Device Status Advisories

Playout

History

My Videos            Version               Status                                     Release Note                                                             Scheduled Start                      Actions

7.0.69.0              NEW                                                                                                                                                      et +

BOX 1: NOW PLAYING OUT     7.0.47.7              Current version

1 SDI output 01         7.0.47.7              INSTALLED                                                                                                                                                or +

2 SDI output 02

3 SDI output 03        Upgrade History

4 SDI output 04             Status Date       Old Status                    New Status    Release Id                                                              Message

Are you sure you want to upgrade system to version 7.0.69.0?

Cancel                       Upgrade

The User Interface will not be accessible for 10 minutes approximately before showing that the software version has been installed as shown in the image below:

REUTERS | WORLD NEWS EXPRESS                                                                                                                                GMT V  Help Status  Admin           administrator

Stories                   Q Search Stories                                                                                                                                                 Search  Advanced Search

Live                          About        Services  Software Upgrades      File Logs    Device Status Advisories

Playout                                                                                                                                                                                          +Upload Software

History

My Videos               Version                      Status                                           Release Note                                                Cut off Time                 Scheduled Start Actions

7.0.69.0                     Current version

1 Live 1                  7.0.47.7                     INSTALLED                                                                                                                                                     $+

2 Playout                      Upgrade History

3 SDI output 03                Status Date            Old Status                        New Status     Version         Comment

4 SDI output 04                                                                                        No records found

Please, repeat above steps for each software version available!!

Page 21 of 70





# 7.8 UPLOAD THE CONFIGURATION

The three following files shown below should be provided by the Media Technical Support Engineer and stored on a client PC connected to the same network as the WNE7 server; the files should be installed in the order shown below and then all server services should be restarted.

1. settings.json
2. Example Kencast licence: PC181470-SerialMXQ945030F.kcl
3. distribution_processes.json
4. Restart all the server services

# 7.9 IMPORT THE CLIENT SETTINGS

After accessing with the Administrator credentials, go to the 3-bar menu in the top bar as shown in the image below, then click over “All Settings” and select “Import”. Look for the *.json file and click Open to import it.

| 90%               | U =                    |                  |
| ----------------- | ---------------------- | ---------------- |
| GMT L             | Help                   | administrator    |
| STATUS            | ADMIN                  | SETTINGS         |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     | Push Client            |                  |
| Host Info         | Linked Boxes           |                  |
|                   | Advanced               |                  |
| All Settings      |                        |                  |

WNE Customer Technical Guide Page 22 of 70






# 7.10 IMPORT THE KENCAST LICENSE

To import or upload the KenCast license into the server, go to the 3-bar menu and File Processor as shown in the image below:

STATUS ADMIN SETTINGS

- About
- Playout
- File Processor
- Services
- User Management
- Playout
- Software Upgrades
- File Distribution
- Internet Backup
- File Logs
- Kencast Administration
- Connection Tests
- Device Status
- Push Client
- Linked Boxes
- Advanced
- All Settings

Click over “Upload” and look for “Upload KenCast License key” and select the .KCL file as shown in the image below and click over “Open”.

WNE Customer Technical Guide Page 23 of 70





WNE Customer Technical Guide

# Search Stories

# File Processor

# Playout

# Internet Backup

# Connection Tests

# Push Client

# Linked Boxes

# Advanced

# All Settings

| **Name**                              | WNENLREU1         |
| ------------------------------------- | ----------------- |
| **IP Address of Satellite Receiver**  | 172.16.2.20       |
| **Frame Rate**                        | 25                |
| **Video Definition**                  | SDHD              |
| **MAC Address of Satellite Receiver** | 00-20-AA-58-69-08 |

Upload Kencast Licence Key Upload

# File Upload

Recent &#x3C;  wneclient Downloads  →  ed. Click "Update Settings" to save

| Name                          | Size    | Modified   |
| ----------------------------- | ------- | ---------- |
| PC181470-SerialMXQ94601L0.kcl | 22.1 kB | 7 May 2021 |

Home      Desktop      Documents      V Downloads      d Music      Pictures

All Files

Cancel Open

Then click over “Upload” again to upload the file.

After installation the license, check the Kencast License as shown in the image below; go to “Admin” and click over Kencast Administrator

# GMT

# Help

# administrator

| **STATUS**        | **ADMIN**              | **SETTINGS**     |
| ----------------- | ---------------------- | ---------------- |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     | Push Client            | Linked Boxes     |
| Advanced          | All Settings           |                  |

Page 24 of 70




# WNE Customer Technical Guide

It should show up the License ID as shown in the image below (ID is an example).

Not secure

10.127.0.29:4039/admin/index.fsp

KenCast Fazzt Administration (wneclient)

# Configuration

- License Info
- Channels
- Receive Settings
- To: Thomson Reuters (v10 E522322-222323 - S50PC)
- Storage Settings
- License ID: CA24C1A6-89A3-4F37-A14D-A7591C387F3E
- License: Faot Prnfegsiorel Client 10.0
- Logging
- Scripting
- Script Folders
- Backhaul
- Alarms
- Web Sites
- Tools
- Statistics
- Logs
- Documentation

IMPORTANT NOTE: If your new Fazzt license has different Site ID, please restart Fazzt after new license was updated successfully.

After checking the ID, go to the Logs tab and check the “Received files” as shown in the image below. The logs should show content. It may take up to 15 minutes to receive the wne.dat permission file for WNE, but other content should be received if the Satellite receiver has been connected and the satellite feed is working.

Not secure

10.127.0.29:4039/admin/index.fsp

KenCast Fazzt Administration (wneclient)

Wed Mar 31, 12:12:09

# Configuration

- Received File Transmissions
- Tools
- Statistics
- Search
- Clear Log Files: recv.csv
- View the last 20 lines
- Refresh
- Previous
- Next

# Logs

Ignore Heartbeat.txt

# Main Log

| Transmission ID | Transmission Status | Transmission Packet Count | Rx Stop Time | Server ID | Channel Handle | File Name                                |
| --------------- | ------------------- | ------------------------- | ------------ | --------- | -------------- | ---------------------------------------- |
| 2021-03-31      | Validated           | 3763066568                | 12:11:49     | 660119    | 3              | PLEASE-IGNORE-210331000809.MPG.enc       |
| 2021-03-31      | Validated           | 1684812237                | 12:11:46     | 660119    | 3              | USA-IMMIGRATION-CARAVAN-HONDURAS.MP4.enc |
| 2021-03-31      | Complete            | 577143165                 | 12:10:57     | 660119    | 3              | WNEHeartbeat.dat                         |
| 2021-03-31      | Validated           | 2793856130                | 12:10:57     | 660119    | 3              | BOLIVIA-COCA.XML                         |
| 2021-03-31      | Validated           | 3901525202                | 12:10:45     | 660119    | 3              | USA-IMMIGRATION-CARAVAN-HONDURAS.MPG.enc |

Page 25 of 70






# 7.11 IMPORT THE FILE DISTRIBUTION SETTINGS

Import the File Distribution settings if is applicable. To import the File Distributor, go to the 3-bar menu, and select over “File Distributor” as shown below:

GMT  Help  administrator

| STATUS            | ADMIN                  | SETTINGS         |
| ----------------- | ---------------------- | ---------------- |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     |                        | Push Client      |
| Host Info         |                        | Linked Boxes     |
| Advanced          |                        |                  |
| All Settings      |                        |                  |

Select “Import” as shown in the image below:

EWS EXPRESS                                                                                             GMTV          Help administrator

Q Search Stories                                                                                                      Search  Advanced Search

Playout        User Management   File Distribution  Kencast Administration                                                    Import JSON

+ Add New     Export All  Import

# AUTOMATION DISTRIBUTION PROCESSES (All Files That Arrive On WNE PC)

| Name   | File Upload | Type      | Actions  |
| ------ | ----------- | --------- | -------- |
| Recent | wneclient   | Downloads |          |
| Home   | Name        | Size      | Modified |

# MANUAL DISTRIBUTION PROCESSES

| Name                             | Type      | Actions     |
| -------------------------------- | --------- | ----------- |
| settings-esential-WNENLREU1.json | 1.1 kB    | 12 Oct 2021 |
| FTP Desktop Unkrgl5              | Downloads | FTP         |
| C WNEv7tolaptopSMB               | Pictures  | SMB v1      |

Important: after all the server files have been imported, please restart all server services as shown in the image below; Go to 3-bar menu, below “Status” column, go to “Services”:

WNE Customer Technical Guide    Page 26 of 70






GMT — Help administrator

# STATUS

# ADMIN

# SETTINGS

- About
- Playout
- File Processor
- Services
- User Management
- Playout
- Software Upgrades
- File Distribution
- Internet Backup
- File Logs
- Kencast Administration
- Connection Tests
- Device Status
- Push Client
- Host Info
- Linked Boxes
- Advanced
- All Settings

Then click over “Restart All”

# S EXPRESS

# GMT V Help administrator

# Search Stories

# Search

# Advanced Search

- About
- Services
- Software Upgrades
- File Logs
- Device Status
- Host Info

# Overall System Health: Bad

| Name            | Status  | Health | Version | Actions |
| --------------- | ------- | ------ | ------- | ------- |
| wne file purger | Running | Good   | 1.0.22  |         |

# 7.12 CHECK THE INTERNET BACKUP SETTING

The Internet backup servers help the video server to avoid loose content if there is a problem with the antenna/Ericsson receiver. The Internet backup service runs continuously comparing the content received on the Reuters’ servers. Any content missing from the machine is downloaded automatically and processed. If no Internet connection exists, then the Internet Backup should remain Disabled. To enable the Internet backup, go to the 3-bar icon bar at the top menu and select Internet Backup as shown in the below image.

WNE Customer Technical Guide Page 27 of 70





GMT  Help  administrator
# STATUS

# ADMIN

# SETTINGS

- About
- Playout
- File Processor
- Services
- User Management
- Playout
- Software Upgrades
- File Distribution
- Internet Backup
- File Logs
- Kencast Administration
- Connection Tests
- Device Status
- Push Client
- Host Info
- Linked Boxes
- Advanced
- All Settings

Click over the “Internet Backup” tab, select the “Enable” option, add a Proxy (if applicable), and click over “Update Settings”.

# Internet Backup

# Connection Tests

# Push Client

# Linked Boxes

# Advanced

# All Settings

Last Successful Access: 2022-11-24 12:01

Enabled

Username: WNENLREU1_CDN

Change Password

# PROXY SETTINGS

Proxy: XX.XX.XX.XX:YYYY or hostname:YYYY

Proxy Username

Change Proxy Password

Highlighted fields indicate values that have not been saved. Click "Update Settings" to save these values.

Current changing the settings on this page requires a restart of WNE Internet Backup service.

Reset
Update Settings
If the Internet backup has been set properly, go to the “Connection Tests” tab, as shown in the image below, and click over “Test CDN Connection” to check the Internet backup connectivity for and “Test DNS Connection” to check the outbound connectivity of the server.

# Search Stories

Search  Advanced Search

# File Processon

# Playout

# Internet Backup

# Connection Tests

# Push Client

# Linked Boxes

# Advanced

# All Settings

Test CDN Connection

Test DNS Connection

Backup Service must be re-started before testing connection.

Tests connection to all used DNSes.

WNE Customer Technical Guide    Page 28 of 70




Both options should show up a successful message as shown below, otherwise, please check your server connectivity based on the error message displayed.

| Test CDN Connection successful message | Test DNS Connection successful message |
| -------------------------------------- | -------------------------------------- |
| CONNECTION SUCCESSFUL!                 | CONNECTION SUCCESSFUL!                 |

Note: any future changes to settings must be saved and the World News Express backup service re-started. It is always recommended to test the connection after changing the settings.

Close

Close

# 7.13 CHECK THE PLAYOUT OPTION

To be able to use and playout the four output ports of the video card, go to the Playout option as shown below.

| STATUS            | ADMIN                  | SETTINGS         |
| ----------------- | ---------------------- | ---------------- |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     | Push Client            | Linked Boxes     |
| Advanced          | All Settings           |                  |

Check that the “Video Playout Mode” has been selected to HD-SDI as shown in the image below:

Q Search Stories

| File Processor | Playout | Internet Backup | Connection Tests | Push Client | Linked Boxes | Advanced | All Settings |
| -------------- | ------- | --------------- | ---------------- | ----------- | ------------ | -------- | ------------ |

Genlock

Genlock Offset

Show Waiting Video for Playout

RLSPLUS pre-roll

Show slug on video playout in Loop Mode

Video Playout Mode HD-SDI

ARC Playout to 4:3 (only available in SD HD-SDI SDI)

LIPSYNC OFFSET SETTINGS (mS)

| \*SD525 | 0 | 0 |
| ------- | - | - |
| \*SD625 | 0 | 3 |

And go to section 8.3 for detailed information about how the Playout works.

WNE Customer Technical Guide

Page 29 of 70







# 7.14 CHECK CHANNEL LIST

IMPORTANT: Verify that the server is getting all channel permissions as shown in the image below, please be aware that the servers should receive first the content, before to show up the channel as shown below, in addition, the channel permissions depend on the client's subscriptions.

| REUTERS    | WORLD NEWS EXPRESS |         |           |              | GMT           | Help              | administrator   |                      |                   |         |       |
| ---------- | ------------------ | ------- | --------- | ------------ | ------------- | ----------------- | --------------- | -------------------- | ----------------- | ------- | ----- |
| Stories    | Q Search Stories   | Search  |           |              |               | Advanced Search   |                 |                      |                   |         |       |
| Live       | All Stories        | Reuters | CCTV      | Perform Inc. | Stats Perform | Sent From Connect |                 |                      |                   |         |       |
| Advisories | Playout            | Asia    | CCTV News | Europe       | Latin         | Life!             | Omnisport Uncut | Reuters Live Service | Sent From Connect | Showbiz | World |
| History    | My Videos          |         |           |              |               |                   |                 |                      |                   |         |       |

If the server doesn’t show the channel list, Restart the complete server, going to the 3-bar menu bar, over the Status column, select Services and click over “Restart Hardware” as shown in the following image:

|                            | NEWS EXPRESS     |                   |           |               | GMT             | Help        | administrator    |
| -------------------------- | ---------------- | ----------------- | --------- | ------------- | --------------- | ----------- | ---------------- |
|                            | Q Search Stories | Search            |           |               | Advanced Search |             |                  |
| About                      | Services         | Software Upgrades | File Logs | Device Status | Host Info       |             |                  |
| Overall System Health: Bad |                  |                   |           |               | Restart All     | Suspend All | Restart Hardware |

WNE Customer Technical Guide Page 30 of 70






WNE USER INTERFACE

All software required for the receipt and processing of content is pre-installed and configured on installation by the engineer on behalf of the customer. The WNE web browser interface provides full access to the settings needed to handle the movement and control of received content.

# 8.1 THE ACTION BUTTONS AND ICONS

The WNE web page allows users who are logged in with a valid account to control playout and move videos. These action buttons are explained below.

These icons all appear in the ARRIVED column of the web page to show what has been received:

- D  Script has Arrived - Notify that the script of the item has arrived
- b  Video has Arrived - Notify that the video of the item has arrived

These icons all appear in the ACTIONS column of the web page:

- Add to My Videos - Add the selected video(s) to My Videos lists
- Add to Distribution - Adds the selected video/script to any matching distribution
- Playout Now - Adds the selected video to the main playlist for immediate playout and allows you to select the playout output where the video will be displayed
- Add to Playlist - Adds the selected video to a user playlist for later use

# 8.2 STORIES PAGE

The stories page (left menu) displays all the received items and provides some options, such as:

# 8.2.1 ADD PAGE TO DISTRIBUTION

The Stories page gives the option to add the current page to Distribution in one go, clicking over the option “Add Page to Distribution” as shown below:

REUTERS' I WORLD NEWS EXPRESS

GMT Help Administrator

BOX: BOX 1

Stories Q Search Stories

Live All Stories Sent From Connect

Advisories

Playout Sent From Connect

History

My Videos + Show early access scripts Show advisories Print Page Add Page To Distribution

| BOX 1: NOW PLAYING OUT | Preview       | Slug                          | ID    | Headline                                                                            | Arrived          | Actions |
| ---------------------- | ------------- | ----------------------------- | ----- | ----------------------------------------------------------------------------------- | ---------------- | ------- |
| 1                      | SDI output 01 | INDIA-AUSTRALIA/ARREST-UPDATE | 2229  | Indian court to decide on extradition of suspect in Australian murder case (Rev. 2) | 2022-11-25 13:20 | DO I +  |
| 2                      | SDI output 02 |                               | 01:09 | Reuters                                                                             |                  |         |
| 3                      | SDI output O3 | EL SALVADOR-VIOLENCE/         | 2105  | El Salvador's Bukele scales up anti-gang push with new deployments (Rev. 5)         | 2022-11-25 13:19 | EO      |
| 4                      | SDI output 04 |                               | 02:42 | Reuters                                                                             |                  | +       |

WNE Customer Technical Guide Page 31 of 70




# 8.2.2 DOWNLOAD ITEMS TO THE DESKTOP

The option to download to the user desktop the video scripts and xml file as shown below; it’s necessary to click over each item to download it.

| HD                                                                    | 2020                                  | Serbia-Kosovo deal is "common sense" - EU | 2022-11-24 |
| --------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------- | ---------- |
| A                                                                     | foreign policy chief Borrell (Rev. 2) | 15:59                                     | E +        |
| Via Internet                                                          |                                       |                                           |            |
| 01:19                                                                 | Reuters                               | REVISION 2                                |            |
| KOSOVO-SERBIA/EU-BORRELL UPDATE                                       |                                       |                                           |            |
| Serbia-Kosovo deal is "common sense" - EU foreign policy chief Borrel |                                       |                                           |            |

| Item ID                                                                               | Edit ID             | Service       | Video File                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------- | ------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2020WD                                                                                | 2020                | World         | 2022-11-24T135448Z\_1\_LWD202024112022RP1\_RTRWNEV\_C\_2020-KOSOVO-SERBIA-EU-BORRELL-UPDATE.MP4 (HD) 2022-11-24T135448Z\_1\_LWD20202412022RP1\_RTRWNEV\_B\_2020-KOSOVO-SERBIA-EU-BORRELL-UPDATE.MPG (SD) |
| Script File                                                                           | Arrived             | Sensitive     | Duration                                                                                                                                                                                                 |
| 2022-11-24T1354487 12 RW202024112022RP1 RTRMADC 0 KOSOVO-SERBIA-EU-BORRELL UPDATE.XML | 2022-11-24 15:59:57 |               | 01:19                                                                                                                                                                                                    |
| Audio                                                                                 | Location            | Script source | Video source                                                                                                                                                                                             |
| NATURAL WITH SPANISH SPEECH                                                           | BARCELONA, SPAIN    | Reuters       | Reuters                                                                                                                                                                                                  |
| Usage terms: Broadcast: None. Digital: None.. For Reuters customers only.             |                     |               |                                                                                                                                                                                                          |

VIDEO SHOWS: EUROPEAN FOREIGN POLICY CHIEF JOSEP BORRELL COMMENTING ON SERBIA-KOSOVO DEAL AT REGIONAL FORUM OF THE UNION FOR THE MEDITERRANEAN IN BARCELONA COMPLETE SCRIPT TO FOLLOW

# 8.2.3 MY VIDEOS

The story page allows to move videos to “My Videos” page clicking over the start symbol as shown below.

| REUTERS' | WORLD NEWS EXPRESS | GMT | Administrator | Box: BOX 1 |
| -------- | ------------------ | --- | ------------- | ---------- |

| Stories | Q                 | Search            | Advanced Search |
| ------- | ----------------- | ----------------- | --------------- |
| Live    | All Stories       | Sent From Connect | Advisories      |
| Playout | Sent From Connect | History           | My Videos       |

Show advisories Show early access scripts Print Page Add Page To Distribution

| Preview                | Slug            | ID    | Headline                                                                            | Arrived    | tions   |
| ---------------------- | --------------- | ----- | ----------------------------------------------------------------------------------- | ---------- | ------- |
| BOX 1: NOW PLAYING OUT | 1 SDI output 01 | 2229  | Indian court to decide on extradition of suspect in Australian murder case (Rev. 2) | 2022-11-25 | 13:20   |
|                        | 2 SDI output 02 | 01:09 | Reuters                                                                             |            |         |
|                        | 3 SDI output 03 | 2105  | El Salvador's Bukele scales up anti-gang push with new deployments (Rev. 5)         | 2022-11-25 | 13.19   |
|                        | 4 SDI output 04 |       |                                                                                     | 02:42      | Reuters |

On “My Videos” page, the videos will show up as below:

| REUTERS | WORLD NEWS EXPRESS | GMT | Help | Administrator | Box: BOX 1 |
| ------- | ------------------ | --- | ---- | ------------- | ---------- |

| Stories | Q          | Search Stories | Advanced Search |
| ------- | ---------- | -------------- | --------------- |
| Live    | Advisories | Playout        | Preview         |
| History | My Videos  | Slug           | ID              |

| Title                                                                                            | Duration                     | Arrived               |
| ------------------------------------------------------------------------------------------------ | ---------------------------- | --------------------- |
| CHRISTMAS-SEASON/GERMANY SCHOLZ                                                                  | 03:41                        | 2022-11-25            |
| German Chancellor Scholz kicks off Christmas as he receives traditional tree (Rev. 5)            | 13:21                        | +                     |
| BOX 1: NOW PLAYING OUT                                                                           | SOCCER-WORLDCUP-URY-KOR/FANS | 2045                  |
| We didn't play our best game, say Uruguayan fans after goalless draw in World Cup opener (Rev.5) | 02:00                        | 2022-11-25            |
|                                                                                                  | 1 SDI output 01              | 13:20                 |
|                                                                                                  | 2 SDI output 02              | Reuters               |
|                                                                                                  | 3 SDI output 03              | Total Duration: 05:41 |
|                                                                                                  | 4 SDI output 04              |                       |

WNE Customer Technical Guide Page 32 of 70




REUTERS           WORLD NEWS EXPRESS                                         GMT  Help                                                                                                     Administrator         BoX: BOX 1

# My Video Page Options

- Add to Playlist
- Print Page
- Add to Distribution
- Clear My Videos

# My Videos

| Slug                            | ID   | Title                                                                                              | Duration | Arrived    |
| ------------------------------- | ---- | -------------------------------------------------------------------------------------------------- | -------- | ---------- |
| CHRISTMAS-SEASON/GERMANY SCHOLZ | 1906 | German Chancellor Scholz kicks off Christmas as he receives traditional tree (Rev. 5)              | 03:41    | 2022-11-25 |
| SOCCER-WORLDCUP-URY-KOR/FANS    | 2045 | We didn't play our best game,' say Uruguayan fans after goalless draw in World Cup opener (Rev. 5) | 02:00    | 2022-11-25 |

Total Duration: 05:41

# Add to Playlist

The option, Add to Playlist, allows sending the videos on My Playlist page to a specific playlist port as shown below:

# Print Page

The option, Print Page, allows printing the list of videos within the My Videos page.

# Add to Distribution

The option, Add to Distribution, allows sending all the videos within the My Videos page to Distribution.

# Clear My Videos

The option, Clear My Videos, allows clearing My Videos page.

WNE Customer Technical Guide    Page 33 of 70




# 8.3 USER MANAGEMENT

To create new users and administrate each user privileges, go to the 3-bar top menu icon and select under Admin, option User Management as shown below.

GMT  Help  Administrator

| STATUS            | ADMIN                  | SETTINGS         |
| ----------------- | ---------------------- | ---------------- |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     |                        | Push Client      |
| Host Info         |                        | Linked Boxes     |
| Advanced          |                        |                  |
| All Settings      |                        |                  |

By default, the administrator user exists, to create new users, click over the Add User as shown below;

Q Search Stories    Search                                                                             Advanced Search

Playout     User Management  File Distribution  Kencast Administration

Y Filter Users                                                                                         + Add User

| Username      | Privileges |
| ------------- | ---------- |
| administrator | Admin      |

And the below options will appear; based on your user privileges, select the ones that applies. To add/remove the option to “Add Page To Distribution” as shown in section 8.2.1, select/unselect option “Distribute Page” as shown below:

# Add User

Username

Password

Password requirements:

- At least 8 characters
- A mixture of both uppercase and lowercase letters
- A mixture of letters and numbers
- Inclusion of at least one special character: @#$%^&#x26;+=!

Privileges

- Admin
- Add/Modify Playlist
- Playout Player Controls
- Playout Now
- Add to Distribution
- Channel 1
- Distribute Page
- Channel 2
- Delete History
- Channel 3
- My Videos
- Channel 4
- Saved Searches

Cancel
Save

WNE Customer Technical Guide    Page 34 of 70





# 8.4 FILE DISTRIBUTION

The File Distribution component can be configured through the WNE web page after login as Administrator. You can choose either to transfer files manually or automatically when have been received. The methods available to distribute the files are FTP, FTPS, SFTP and SMB as shown in the image below. The content can also be filtered by service, aspect ratio or to exclude sensitive content. Once created a distribution process can be stopped, paused, or restarted. The process definition can also be exported, imported, or deleted by the web control options. The complete guide of the File Distributor can be found at Appendix – G.

# 8.5 VIDEO PLAYOUT

The video playout is used by customers with a need to record or display the received videos via the Deck Link SDI (4-ports) video card. The playout output options need to be configured within the Admin > Playout menu as shown in the image below:

| GMT V             | Help                   | administrator    |
| ----------------- | ---------------------- | ---------------- |
| STATUS            | ADMIN                  | SETTINGS         |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     |                        | Push Client      |
| Host Info         |                        | Linked Boxes     |
|                   |                        | Advanced         |
|                   |                        | All Settings     |

There are five options such as Live, 6x Live Preview, RLS [Broadcast], File Playout, and Send from Connect.

- Live: allow you to playout any of the Live signals available
- 6x Live Preview: allow you to playout the six (6) live signals on one screen.
- RLS [Broadcast]: allow you to playout the Reuters main Live signal.
- File Playout: allow you to playout video files already received on the server
- Sent from Connect: allow you to playout video files sent from the Reuters Connect website.

WNE Customer Technical Guide Page 35 of 70





REUTERS IWORLD NEWS EXPRESS
# WNE Customer Technical Guide

# Playout

# BOX 1: NOW PLAYING OUT

| 1 | File play out manual | 3 | RLS               | 4 live 2 |
| - | -------------------- | - | ----------------- | -------- |
| 2 | RLS                  | 4 | Sent From Connect | 6        |
| 3 | Manual               |   |                   |          |

# Each of the 4-ports can be configured for different proposes or scenarios as shown below:

# BOX 1: NOW PLAYING OUT

| 1 | SDI output 01 | P | 3 | SDI output 03 |
| - | ------------- | - | - | ------------- |
| 2 | SDI output 02 |   | 4 | SDI output 04 |
| 3 | SDI output 03 |   |   |               |
| 4 | SDI output 04 |   |   |               |

# Depending on the playout option selected, each option could be configured in different modes as:

| PLAYOUT OPTION    | PLAYOUT MODE       |
| ----------------- | ------------------ |
| Live              | None               |
| 6x Live Preview   | None               |
| RLS \[Broadcast]  | None               |
| File Playout      | Loop, Auto, Manual |
| Sent from Connect | Loop, Auto, Manual |

Page 36 of 70



# 8.5.1 LOOP AND AUTO MODE

The playout modes “Loop” and “Auto” allow you to configure it as shown in the image below:

REUTERS

GMT Help administrator

Stories Q Search Stories Search Advanced Search

Live Playout User Management File Distribution Kencast Administration Advisories

Playout BOX 1 Fixed Channels

History File play out manual File Playout V Loop V Configure Loop :

My Videos

BOX 1: NOW PLAYING OUT G Manual File Playout Manual 6

1 File play out manual 3 V V

STATS-PERFORM 4559

00:27 06:51 4 live 2 Sent From Connect V Auto V Configure Auto 6

2 RLS

If you select the “Loop” mode and click over “Configure Loop”, the following menu will show up. Configure it as desire:

- Loop Count: allow you to select how many videos will be playout in a loop.
- Exclusions: allow you to exclude to playout video which contains nudity, profanity, or explicit graphic content
- Services: allow you to select from which services/feeds the videos are selected

# Configure Loop Settings

| Loop Count | 5 |
| ---------- | - |

Play script revisid 1

NOTE: This setting affects both Loop and Auto modes.

# EXCLUSIONS

| Graphic | Nudity | Profanity |
| ------- | ------ | --------- |

# SERVICES

| All                       | Af Daily             | Af Jour           |
| ------------------------- | -------------------- | ----------------- |
| Asia                      | Business Video       | CEEF              |
| Eyewitness                | Hollywood.TV         | Innovations       |
| Life!                     | Mid East             | R Rep             |
| Reuters Live Service      | Russian Video Report | Sent From Connect |
| Spanish Video Report      | Sports               | USVO              |
| Viral                     | Arabic Rep           | CCTV News         |
| Germany                   | Latin                | Next Media        |
| Reuters Live Service Plus | Showbiz              | Subcon            |
| World                     |                      |                   |

Cancel Save

The “Auto” mode allows configuring from which channels/feeds would like to pick up the latest videos (after the setting is configured) to be played out.

WNE Customer Technical Guide Page 37 of 70



Configure Auto Settings

# Play script revisions

NOTE: This setting impacts both Loop and Auto modes.

# EXCLUSIONS

- Graphic
- Nudity
- Profanity

# SERVICES

| All                       | Af Daily   | Af Jour              | Asia                 | Business Video    |
| ------------------------- | ---------- | -------------------- | -------------------- | ----------------- |
| CEEF                      | Eyewitness | Hollywood.TV         | Innovations          | Life!             |
| Mid East                  | R Rep      | Reuters Live Service | Russian Video Report | Sent From Connect |
| Spanish Video Report      | Sports     | USVO                 | Viral                |                   |
| Arabic Rep                | CCTV News  | Germany              | Latin                | Next Media        |
| Reuters Live Service Plus | Showbiz    | Subcon               | World                |                   |

Cancel
Save

# 8.5.2 MANUAL MODE

In the case, the “Manual” mode has been selected at any SDI output port, it is necessary to go to the “Stories” tab and selected from all items that arrived in the server which video would like to be played out as shown in the image below (e.g. SDI output 4 was set to File Playout > Manual).

# REUTERS° I WORLD NEWS EXPRESS

GMT Help administrator

# Stories

Q Search Stories

Search Advanced Search

# Live

All Stories Reuters CCTV Perform Inc. Stats Perform Sent From Connect Advisories

# Playout

Asia CCTV News Europe Latin Life! Omnisport Uncut Reuters Live Service Reuters Live Service Plus Sent From Connect Showbiz World

# History

My Videos Show advisories Print Page Add Page To Distribution Show early access scripts

# BOX 1: NOW PLAYING OUT

| Preview | Slug                 | ID            | Headline                                                                                                      | Arrived        | Actions        |
| ------- | -------------------- | ------------- | ------------------------------------------------------------------------------------------------------------- | -------------- | -------------- |
| 1       | File play out manual | G             | INDONESIA-QUAKE/MOMENT. MOMENT: Dramatic CCTV shows woman and child escaping as Indonesia quake hits (Rev. 1) | 2022-11-24     | O              |
|         | INDONESIA-QUAKE/AID  | 1636          | UGC                                                                                                           | 13:30          | Via Internet + |
| 2       | RLS                  |               | CLIMATE-CHANGE/GERMANY Climate activists disrupt Beethoven concert at Hamburg's Elbphilharmonie hall (Rev. 1) | 2022-11-24     | E              |
| 3       | Manual               |               | PROTEST-UGC                                                                                                   | 13:25          | Via Internet + |
| 4       | live 2               | O             | 00:12                                                                                                         | Reuters        |                |
|         | HD                   | STATS-PERFORM | 4559 241122\_UNCUT\_SPN\_EN\_WC\_MARCO\_ASENSIO\_SPAIN\_PLUS\_TRAINING (ev. 2)                                | 2022-11-24     | EO +           |
|         | INDONESIA-QUAKE/AID  | 1636          | Indonesia quake survivors struggle to rebuild lives, aid slow to arrive (Rev. 2)                              | 2022-11-24     | E +            |
|         |                      |               | 13:21                                                                                                         | Via Internet 7 |                |
|         | RLS Preview          |               | 04:07                                                                                                         | Reuters        |                |
|         |                      |               | SOCCER-WORLDCUP/DOHA-FOOD Doha's thriving food scene traces transformation before World Cup (Rev. 3)          | 2022-11-24     | E +            |
| I1      |                      | AIJ           | 05:52                                                                                                         | Reuters        |                |
|         |                      |               | MALAYSIA-ELECTION/ANWAR Malaysia's Anwar Ibrahim is sworn in as new prime minister (Rev. 4)                   | 2022-11-24     | EO +           |
|         |                      |               | SSWEARING-IN                                                                                                  | 13:20          | Via Internet   |

Prev Page of 55 Next Per Page90

RUSSIA-RIGHTS/LGBT-DUMA 1adults 2022-11-24

WNE Customer Technical Guide Page 38 of 70




# 8.5.3 LIVE SIGNALS

To playout the Live signals available, ensure to select the Live option over any of the outputs available as shown in the image below, go to 3-bar menu, then Admin > Playout.

| REUTERS | WORLD NEWS EXPRESS | GMTV | Help | administrator |
| ------- | ------------------ | ---- | ---- | ------------- |

| Stories | Q Search Stories | Search | Advanced Search |
| ------- | ---------------- | ------ | --------------- |

| Live | Playout | User Management | File Distribution | Kencast Administration |
| ---- | ------- | --------------- | ----------------- | ---------------------- |

| Advisories | Playout | BOX 1 | Fixed Channels |
| ---------- | ------- | ----- | -------------- |

| History   | File play out manual |   | File Playout | V | Loop   | V | Configure Loop | 6 |
| --------- | -------------------- | - | ------------ | - | ------ | - | -------------- | - |
| My Videos | 2 RLS                |   | File Playout | V | Manual | 6 |                |   |

# BOX 1: NOW PLAYING OUT

|                        |                      | Manual   | Live  | :                 |   |      |   |                |
| ---------------------- | -------------------- | -------- | ----- | ----------------- | - | ---- | - | -------------- |
| 1                      | File play out manual | P        | 3     |                   |   |      |   |                |
| UKRAINE-CRISIS/RUSSIA- | 1990                 | 01:22    | 01:25 | 4 live 2          |   |      |   |                |
|                        |                      |          |       | Sent From Connect | V | Auto | V | Configure Auto |
| 2 RLS                  | 3 Manual             | 4 live 2 | O     |                   |   |      |   |                |

After the desired SDI output port has been selected, go to the Live section in the left panel as shown in the image below, click over any of the available (in green) live signals and select the “Playout Now” option and select the SDI output port configured in the previous step.

| REUTERS | WORLD NEWS EXPRESS | GMT | Help | administrator |
| ------- | ------------------ | --- | ---- | ------------- |

| Stories | Q Search Stories | Search | Advanced Search |
| ------- | ---------------- | ------ | --------------- |

| Live | ALL | REUTERS LIVE | RLS |
| ---- | --- | ------------ | --- |

| Advisories | • Live Scheduled | Completed | Cancelled | Show completed/cancelled events |
| ---------- | ---------------- | --------- | --------- | ------------------------------- |

| Playout | History | < 24 November 2022 | "All start and end times are approximate |
| ------- | ------- | ------------------ | ---------------------------------------- |

| My Videos                 | Event                |                         | Start\*                 | End\*                     | Playout |       |
| ------------------------- | -------------------- | ----------------------- | ----------------------- | ------------------------- | ------- | ----- |
| BOX 1: NOW PLAYING OUT    |                      | MALAYSIA-ELECTION/ANWAR | 09:38                   | 12:00                     |         |       |
| 1                         | File play out manual | G                       | SOCCER-WORLDCUP/SKYLINE | 10:55                     | 14:00   |       |
| UN-Ukraine Crisis/Chinese | 4609                 | 01:25                   | 02:28                   | RUSSIA-PUTIN/-NEW SOURCE- | 11:37   | 12:00 |
| 2 RLS                     | 3 Manual             | 4 live 2                | O                       |                           |         |       |

# SCHEDULED

| Reuters Live Preview | RUSSIA-PUTIN/-TIME TBC-                   | 12:00 | 12:00 |                            |                                                                       |                     |                 |                    |
| -------------------- | ----------------------------------------- | ----- | ----- | -------------------------- | --------------------------------------------------------------------- | ------------------- | --------------- | ------------------ |
|                      | VIRGINIA-SHOOTING/WALMART-POSSIBLE ONLY-- | 13:00 | 14:00 |                            |                                                                       |                     |                 |                    |
|                      | EU-ENERGY/NEWS CONFERENCE                 | 14:30 | 15:45 | +                          | Live                                                                  | Playout Now         |                 |                    |
|                      | SOCCER-WORLDCUP/SKYLINE                   | 16:15 | 19:00 | +                          | Start: 24 Nov 2022 10:55 GMT                                          |                     |                 |                    |
|                      |                                           |       |       | End: 24 Nov 2022 14:00 GMT | DOHA, QATAR - Skyline view of Doha on day five of the Qatar World Cup |                     |                 |                    |
|                      |                                           |       |       | Restrictions:              | BROADCAST: Access all                                                 | DIGITAL: Access all | Source: REUTERS | Aspect Ratio: 16:9 |






# 8.5.3.1 Reuters Live Preview and RLS Preview

The Reuters Live Preview page and Reuters Live signal (RLS) page can be seen within the main Stories page as shown below, please use Google Chrome as an Internet browser for a better experience.

| REUTERS    | WORLD NEWS EXPRESS   |              |         |                |
| ---------- | -------------------- | ------------ | ------- | -------------- |
| Stories    | Search Stories       |              |         |                |
| Live       | All Stories          | Reuters      | Atlas   | CCT            |
| Advisories | Playout              | Af Daily     | Af Jour | Af Jour Online |
| History    | GNVO                 | Hollywood.TV | HTVO    | Lat            |
|            | Spanish Video Report |              |         |                |
|            |                      | Sports       |         |                |
|            |                      |              | Subco   |                |

BOX 1: NOW PLAYING OUT

| 1 | SDI output 01 | Preview | Slug          |
| - | ------------- | ------- | ------------- |
| 2 | SDI output 02 |         | O HD          |
| 3 | SDI output 03 |         |               |
| 4 | SDI output    | 01:51   | Reuters       |
|   |               | HD      | China-NEV Equ |

Reuters Live Preview

01:47

CCTV

ReutErs V LONDON

HD

please ignore

RLS Preview

00:08

2075422244

Reuters

LIVE

1430GMT

EU-ENERGY/NEWS-CONFERENCE

TV/WEB: ACCESS ALL

ASPECT RATIO: 16:9

REUTERS

G 023 8 94ak

HD

QATAR

VISA Cal

SOCCER-WOR

If you want to disable the Live Preview and/or RLS Preview on the main “Stories” page, go to the 3-bar menu icon, and go to “Advanced” as shown below:

|                   | GMT                    | Help             | Administrator | V |   |   |
| ----------------- | ---------------------- | ---------------- | ------------- | - | - | - |
| STATUS            | ADMIN                  | SETTINGS         |               |   |   |   |
| About             | Playout                | File Processor   |               |   |   |   |
| Services          | User Management        | Playout          |               |   |   |   |
| Software Upgrades | File Distribution      | Internet Backup  |               |   |   |   |
| File Logs         | Kencast Administration | Connection Tests |               |   |   |   |
| Device Status     |                        | Push Client      |               |   |   |   |
| Host Info         |                        | Linked Boxes     |               |   |   |   |
| Advanced          |                        |                  |               |   |   |   |
| All Settings      |                        |                  |               |   |   |   |

WNE Customer Technical Guide Page 40 of 70





Scroll down and look for the “Show Preview” option and select which one you want to display or not display, then select “Update Settings”

iLO Username

] Change iLo Password

Show Preview                                         Both        ^

None

RLS

Highlighted fields Indicate values that have no     Live Preview these values.

Warning!!! Changing any options on this page       Both WNE Client. Please contact your technical supp this section.

Factory Reset  Reset  Update Settings

# 8.5.4 FIXED CHANNELS

There is an option to fix each channel to any specific signal, enable the “Fixed Channels” option as shown below:

| REUTERS | WORLD NEWS EXPRESS | GMT             | Help              | Status                 | Admin      | Administrator |
| ------- | ------------------ | --------------- | ----------------- | ---------------------- | ---------- | ------------- |
| Stories | Q Search Stories   |                 | Search            | Advanced Search        |            |               |
| Live    | Playout            | User Management | File Distribution | Kencast Administration | Advisories |               |

Playout              BOX 1                                                                                           Fixed Channels

History                                 1 SDI output 01    Sent From Connect  V      Auto           V       Configure Auto  6

My Videos

| BOX 1: NOW PLAYING OUT |                 |   |   |                           |   |   |
| ---------------------- | --------------- | - | - | ------------------------- | - | - |
| 1 SDI output 01        | 3 SDI output 03 |   |   | File Playout V Manual V 6 |   |   |
| 2 SDI output 02        | 4 SDI output 04 |   |   | File Playout V Manual V 6 |   |   |
|                        | 3 SDI output 03 |   |   |                           |   |   |
|                        | 4 SDI output 04 |   |   |                           |   |   |





# 8.5.5 SDI OUTPUT PORTS PANEL

After a signal has been selected for playout, it will be displayed in the Playout panel option located in the left panel as shown below. Note: 6x Live Preview is available only for clients subscribed to our full Live signal’s product.

| REUTERS | WORLD NEWS EXPRESS      |                        |           |           | GMT              | Help administrator |
| ------- | ----------------------- | ---------------------- | --------- | --------- | ---------------- | ------------------ |
| Stories | Q Search Stories        | Search                 |           |           | Advanced SearchD |                    |
| Live    | Advisories              | BOX 1: NOW PLAYING OUT |           |           | 8                |                    |
| Playout | 1. File play out manual | 2. RLS                 | 3. Manual | 4. live 2 |                  |                    |
| History | My Videos               |                        |           |           |                  |                    |

# BOX 1: NOW PLAYING OUT

|                                 |                                                                 |                                                                             | No active playout | No active playout | No active playout |   |
| ------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------- | ----------------- | ----------------- | - |
| 1 File play out manual          | CHI                                                             | UN-Ukraine Crisis/Chinese Envoy                                             | 4609              |                   |                   |   |
| 01:15                           | 02:28                                                           | 01:15                                                                       | 02:28             |                   |                   |   |
| 2 RLS                           | NOW PLAYING:                                                    | UN-Ukraine Crisis/Chinese Envoy                                             | 4609              |                   |                   |   |
| 3 Manual                        | UPCOMING:                                                       | Total Duration: 06:26                                                       | UPCOMING:         |                   |                   |   |
| UKRAINE-CRISIS/BLACKOUT-SURGERY | Despite blackout heart surgery being performed in Kyiv hospital | Duration: 00:44                                                             |                   |                   |                   |   |
| 4 live 2                        | UKRAINE-CRISIS/EU-RUSSIA                                        | EU preparing new Russia sanctions package, von der Leven says               | Duration: 01:38   |                   |                   |   |
|                                 | STATS-PERFORM                                                   | TOP STORY: Football: 'Painful' for Cameroonians to see Embolo score against | his birth nation  |                   |                   |   |

# 8.6 HOW TO LINK DIFFERENT WNE7 SERVERS

If the customer has more than one WNE7 video server, the following option allows to connect several WNE7 servers.

1. The following option should be set up on the server that will not be used as “primary” server. In other words, in the “secondary” server.
2. Go to the 3-bar top icon, under “Setting” column, select “Linked Boxes”, as shown below:

| GMT               | Help                   | administrator    |
| ----------------- | ---------------------- | ---------------- |
| STATUS            | ADMIN                  | SETTINGS         |
| About             | Playout                | File Processor   |
| Services          | User Management        | Playout          |
| Software Upgrades | File Distribution      | Internet Backup  |
| File Logs         | Kencast Administration | Connection Tests |
| Device Status     | Push Client            |                  |
| Host Info         | Linked Boxes           | Advanced         |
| All Settings      |                        |                  |

WNE Customer Technical Guide Page 42 of 70



WNE Customer Technical Guide

# Allow Access from Other Boxes

Click over or select the option “Allow access from other boxes” as shown in the image below and change the server names to avoid servers ending with the same name.

For example, we assume that the user will configure the secondary server (named: BOX2)

- Name: enter the server’s name, in this case, BOX2
- From any box – select if you want the server to be accessed from any WNE7 box.
- From specified boxes – select if you want the server to be accessed from any specific box. Enter the server IP of the “primary” WNE7 server as http://serverIP or name using the server URL format as http(s)://example.com [Available in version 7.3.xx.xx]
- Deselect the option “Control other boxes from this UI” and click over “Update Settings”

# REUTERS | WORLD NEWS EXPRESS

GMT V Help Status Admin administrato

Stories α Search Stories

Live Playout Internet Backup Linked Boxes Advanced All Settings

File Processor Push Client Advisories

Playout ACCESS History My Videos Allow access from other boxes

| Name                   | Box 2                             |
| ---------------------- | --------------------------------- |
| Box 2: NOW PLAYING OUT | From any box                      |
| 1 manual               | From specified boxes              |
| 2 Reuters Live 4       | SPACE-EXPLORATION/SPACEWALK       |
| 01:39:34               | Approx. 07:33:34                  |
| 3 Reuters Live 5       | SOCCER-WORLDCUP-WAL-IRN/FANS-DOHA |
| 51:05                  | Approx. 15:05                     |
| 4 Reuters Live 6       |                                   |

Highlighted fields indicate values that have not been saved. Click "Update Settings" to save these values.

Reset Update Settings

# Primary Server Configuration

On the primary server, select the option “Allow access from other boxes” as shown in the image below – rename your primary server as desired, in our example BOX1 and select the option “Control other boxes from this UI” and enter the secondary server IP(s) as http://serverIP or server URL as http://example.com and click over “Update Settings”

File Processor Playout Internet Backup Connection Tests Push Client Linked Boxes Advanced All Settings

ACCESS

Allow access from other boxes

| Name         | Box One              |
| ------------ | -------------------- |
| From any box | From specified boxes |

LINKED BOXES

Control other boxes from this UI

http(s)://example.com

Highlighted fields indicate values that have not been saved. Click "Update Settings" to save these values.

Reset Update Settings

Page 43 of 70




REUTERS° | WORLD NEWS EXPRESS                                       GMT

# After configuring the linked servers, it should look as shown below:

# Stories

# QSearch Stories

- Live
- File Processor
- Playout
- Internet Backup
- Connection Tests
- Push Client
- Linked Boxes
- Advanced
- All Settings

# Advisories

# Playout

# ACCESS

# History

# My Videos

Allow access from other boxes

# BOX 1: NOW PLAYING OUT

| SDI output 01    | G                                                                                                          | Control other boxes from this UI |       |
| ---------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------- | ----- |
| VIRCINIA-        | 2051                                                                                                       | <http://10.127.0.29>             |       |
| SHOOTINGIWALMART | FILE-UGC                                                                                                   | 00.02                            | 00:10 |
| SDI output 02    | Highlighted fields indicate values that have not been saved. Click "Update Settings" to save these values. |                                  |       |
| 3 SDI output 03  | 4 SDI output 04                                                                                            |                                  | Reset |

# BOX 2: NOW PLAYING OUT

| 5 manual         |                             |               |                  |               |
| ---------------- | --------------------------- | ------------- | ---------------- | ------------- |
| 6 Reuters Live 4 | SPACE-EXPLORATION/SPACEWALK | 01:35.59      | Approx, 07.23.34 |               |
| 2 Reuters Live 5 | SOCCER-WORLDCUP-WAL         | IRN/FANS-DOHA | 47.30            | Approx, 15:05 |
| Reuters Live 6   |                             |               |                  |               |

WNE Customer Technical Guide    Page 44 of 70




APPENDIX A – CHANGING NETWORK SETTING

To set or change the server network information, please do the following steps:

1. Connect a keyboard, mouse, and monitor and power up the to the WNE7 server.
2. The server will start up and the home page as shown below will appear within a few minutes. Select the user:

wneclient
Password: reuters

12:25 PM
Tuesday, March 30, 2021

WNE Client Admini  wneclient
Password

Login

Suspend  Restart  Shutdown  Different User

After login, the desktop appears, and click over the icon wnec_netconfig.sh

netconfig
sh

WNE Customer Technical Guide    Page 45 of 70






# 4.

The network configuration script shortcut should automatically open a terminal emulator window as shown in the image below:

wnec_netconfig           wneclient:sudo Konsole
sh    File  Edit  View Bookmarks  Settings  Help

WNEC setting up serial number and pc model *

/usr/local/bin/wnec_netconfig.sh: line 1854: /usr/local/bin/wnec_get_serial_number: No such file or directory

# WNEc network related configuration

Do you want to configure the speed and duplex mode of eno5 interface? [yes/no]:

wneclient: sudo
# 5.

Now you are prompted to configure the speed and duplex of each of the network interfaces on the WNE server appliance. Unless a fixed speed and duplex is required for each interface, leave the settings as default by selecting No for each network interface. All interfaces will remain with an automatic network speed. If the server and receiver are wired via a switch, select yes/no based on your configuration.

wneclient:sudo-Konsole
File Edit View Bookmarks Settings Help

WNEc setting up serial number and pc model

/usr/local/bin/wnec_netconfig.sh: line 1854: /usr/local/bin/wnec_get_serial_number: No such file or directory

# WNEc network related configuration*

Do you want to configure the speed and duplex mode of eno5 interface? [yes/no]: n

Do you want to configure the speed and duplex mode of eno6 interface? [yes/no]: n

Do you want to configure the speed and duplex mode of eno7 interface? [yes/no]: n

Do you want to configure the speed and duplex mode of eno8 interface? [yes/no]: n

Device found:

- eno5 - added to network config.
- Device found: eno6 - added to network config.
- Device found: eno7 - added to network config.
- Device found: eno8 - added to network config.

Have you wired both the control and data interfaces into eno7 via a switch? [yes/no]: n

Do you want to configure eno5 interface (It could be used by Reuters Onsite Support)? [yes/no]: n

Do you want to configure eno6 interface? [yes/no]: y

wneclient: sudo






# 6.

After leaving all interfaces with an automatic network speed, lets configure the network interfaces. Eno5 (UTP port 1), should keep it as it is. Type: n

wneclient:sudo-Konsole
File Edit View Bookmarks Settings Help

WNEC setting up serial number and pc model

/usr/local/bin/wnec_netconfig.sh: line 1854: /usr/local/bin/wnec_get_serial_number: No such file or directory

WNEC network related configuration

Do you want to configure the speed and duplex mode of eno5 interface? [yes/no]: n
Do you want to configure the speed and duplex mode of eno6 interface? [yes/no]: n
Do you want to configure the speed and duplex mode of eno7 interface? [yes/no]: n
Do you want to configure the speed and duplex mode of eno8 interface? [yes/no]: n
Device found: eno5 - added to network config.
Device found: eno6 added to network config.
Device found: eno7  added to network config.
Device found: eno8 - added to network config.
Have you wired both the control and data interfaces into eno7 via a switch? [yes/no]: n
Do you want to configure eno5 interface (It could used by Reuters Onsite Support)? [yes/no]: n
Do you want to configure eno6 interface? [yes/no]: y
wneclient:sudo

# 7.

Now, let’s configure eno6 (UTP port 2). To the question, do you want to configure eno6 interface, type y

wneclient:sudo-Konsole
File Edit View Bookmarks Settings Help

WNEC setting up serial number and pc model

/usr/local/bin/wnec_netconfig.sh: line 1854: /usr/local/bin/wnec_get_serial number: No such file or directory

WNEC network related configuration

Do you want to configure the speed and duplex mode of eno5 interface? [yes/no]: n
Do you want to configure the speed and duplex mode of eno6 interface? [yes/no]: n
Do you want to configure the speed and duplex mode of eno7 interface? [yes/no]: n
Do you want to configure the speed and duplex mode of eno8 interface? [yes/no]: n
Device found: eno5 - added to network config.
Device found: eno6 - added to network config.
Device found: eno7 - added to network config.
Device found: eno8 - added to network config.
Have you wired both the control and data interfaces into eno7 via a switch? [yes/no]: n
Do you want to configure eno5 interface (It could used by Reuters Onsite Support)? [yes/no]: n
Do you want to configure eno6 interface? [yes/no]: y
wneclient: sudo






# 8. Now, let configure eno6 (UTP port 2).</h8>
The prompt window will show up the current port configuration. To the question, keep current setting for eno6 interface? Type n

wneclient: sudo —Konsale
File Edit View Bookmarks Settings Help
Do you want to configure the speed and duplex mode of eno7 interface? [yes/no]: n

Do you want to configure the speed and duplex mode of eno8 interface? [yes/no]: n

Device eno5 already listed in network config.

Device eno6 already listed in network config.

Device eno7 already listed in network config.

Device eno8 already listed in network config.

Have you wired both the control and data interfaces into eno7 via a switch? [yes/no]: n

Do you want to configure eno5 interface (It could used by Reuters Onsite Support)? [yes/no]: n

Do you want to configure eno6 interface? [yes/no]: y

Current network setting for eno6 interface as below:

eno6:                                 Current port configuration
dhcp4: false
optional: true
Keep current setting for eno6 interface? [yes/no]: n

Eno6 settings are:

IP: 172.16.2.125

Netmask: 255.255.255.0

After entering the new port information, to the question: Done with eno6 interface setting? Type y as shown in the image below:

Done with eno6 interface setting? [yes/no, hit enter for yes]:
Keep current setting for eno6 interface? [yes/no]:
What is the static ip for this interface? [default is 172.16.2.20, hit enter for default]: 172.16.2.125
what subnetmask? [default is n, hit enter for default]:
Here is the configuration information you provided:

address: 172.16.2.125
netmask: 255.255.255.0
Done with eno6 interface setting? [yes/no, hit enter for yes]: y
# 9. Now, let configure eno7 (UTP port 3).</h8>
The prompt window will ask you if you want to configure eno7 interface. Type y

The prompt will show up the current port configuration. To the question, keep current setting for eno7 interface? Type n

wneclient:sudo—Konsole
File  Edit View Bookmarks Settings Help
dhcp4: false
optional: true
Keep current setting for eno6 interface? [yes/no]: n

What is the static ip for this interface? [default is 172.16.2.125, hit enter for default]:

What is the subnet mask? (default is 255.255.255.0, hit enter for default]:

Here is the configuration information you provided:

address: 172.16.2.125
netmask: 255.255.255.0
Done with eno6 interface setting? [yes/no, hit enter for yes]: y
Do you want to configure eno7 interface? [yes/no]: y

Current network setting for eno7 interface as below:

eno7:                        Current port configuration
dhcp4: false
optional: true
Keep current setting for eno7 interface? [yes/no]: n

WNE Customer Technical Guide                                                                      Page 48 of 70




# WNE Customer Technical Guide

# Network Configuration

Eno7 settings are:

- IP: 172.16.2.25
- Netmask: 255.255.255.0

wneclient: sudo — Konsole
File Edit View  Bookmarks Settings Help
dhcp4: false
optional: true

Keep current setting for eno6 interface? [yes/no]: n

What is the static ip for this interface? [default is 172.16.2.125, hit enter for default]:

What is the subnet mask? (default is 255.255.255.0, hit enter for default]:

Here is the configuration information you provided:

- address: 172.16.2.125
- netmask: 255.255.255.0

Done with eno6 interface setting? [yes/no, hit enter for yes]: y

Do you want to configure eno7 interface? [yes/no]: y

Current network setting for eno7 interface as below:

- eno7:
- dhcp4: false
- optional: true

Keep current setting for eno7 interface? [yes/no]: n

What is the static ip for this interface? [default is 172.16.2.25, hit enter for default]:

What is the subnet mask? [default is 255.255.255.0, hit enter for default]:

Here is the configuration information you provided:

- address: 172.16.2.25
- netmask: 255.255.255.0

Done with eno7 interface setting? [yes/no, hit enter for yes]: y

3wneclient: sudo

After entering the new port information, to the question: Done with eno7 interface setting? Type y

Now, let’s configure eno8 (UTP port 4), which corresponds to the client network configuration.

To the question, do you want to configure eno8 interface? Type y

To the question, do you want to keep current setting for eno8 interface? Type n

To the question, do you want to assign a static ip to eno8 interface? Type y

Do you want to configure eno8 interface? [yes/no]: y

Current network setting for eno8 interface as below:

# This file describes the network interfaces available on your system
netplan(5).
eno8:
addresses: [10.127.0.29/24]
dhcp4: false                          current port configuration
gateway4: 10.127.0.1
nameservers:
addresses: [1.1.1.1, 1.0.0.1]
search: []

Keep current setting for eno8 interface? [yes/no]: n

Do you want to assign a static ip to eno8 interface? [yes/no]: y

wneclient : sudo

The windows prompt will ask for:

- Static IP
- Subnet mask
- IP of the Gateway
- IP of the DNS(s)

After entering the information, to the question, Done with eno8 interface setting? Type y

Page 49 of 70




WNE Customer Technical Guide

1. Keep current setting for eno8 interface? [yes/no]: n

Do you want to assign a static ip to eno8 interface? [yes/no]: y  hit enter for default

What is the static ip for this interface? [default is ]

What is the subnet mask? (default is 255.255.255.0, hit enter for default):

What is the ip of the gateway this interface should use? [default is 10.127.0.1, hit enter for default]:

What is the ip of the DNS nameserver(s)? (Use comma as delimiter for multiple servers i.e. 192.168.0.1, 192.168.0.2, default is 1.1.1.1, 1.0.0.1)

What is DNS domain name? :

Here is the configuration information you provided:
| address:         |                     |
| ---------------- | ------------------- |
| netmask:         | 255.255.255.0       |
| gateway:         |                     |
| dns-nameservers: | \[1.1.1.1, 1.0.0.1] |
| dns-search:      | \[]                 |

Done with eno8 interface setting? [yes/no, hit enter for yes]: y

wneclient: sudo
2. After configuring eno8 port, the windows prompt will ask you to press ENTER to save the new ports configuration. You have 120 seconds (2 minutes) to apply the changes as shown in the image below:

Done with eno8 interface setting? [yes/no, hit enter for yes]: y

ethernets:

No change to current eno5 setting

Configure eno6 setting

Configure eno7 setting

Configure eno8 setting

Applying configuration.

If system is unresponsive, networking will revert in 120 seconds.

or Hit <ctrl>+C to revert immediately

Do you want to keep these settings

Press ENTER before the timeout to accept the new configuration

Changes will revert in 116 seconds

wneclient: sudo
</ctrl>
3. After the windows prompt gives the confirmation that new settings have been applied, it will ask for the NTP servers as shown in the image below; type n to keep the current servers. If you want to set your own NTP servers, type y

Changes will revert in

Configuration accepted. 69 seconds

Networking service is now running with new setting.

Would you like to change the below list of NTP servers? [yes/no]:

| pool 0.ubuntu.pool.ntp.org | iburst |
| -------------------------- | ------ |
| pool 1.ubuntu.pool.ntp.org | iburst |
| pool 2.ubuntu.pool.ntp.org | iburst |
| pool 3.ubuntu.pool.ntp.org | iburst |

wneclient: sudo
4. Once the NTP address has been entered the network configuration is completed.

Page 50 of 70




APPENDIX B - SYSTEM CHECKS
To ensure that the WNE service is working properly, please perform the following simple checks:

# B.1. SATELLITE RECEIVER CHECK

The receiver home page (172.16.2.20) and the initial Status page should confirm uptime as well as the input/output status and any problems being reported.

| RX8200                             |             | About                                                           |
| ---------------------------------- | ----------- | --------------------------------------------------------------- |
| ERICSSON Advanced Modular Receiver |             |                                                                 |
| Status                             | Device Info | Alarms                                                          |
| Customization                      | CA Input    | Service plus Decode Output Download SNMP Presets Save/Load Help |
| 2 Refresh                          |             |                                                                 |

| Name           | Advanced Modular Receiver                                  |
| -------------- | ---------------------------------------------------------- |
| IP Address #1  | 192.168.001.001                                            |
| IP Address #2  | 192.169.002.021                                            |
| Current Status | OK                                                         |
| Current Time   | 2015-02-13 05:53:23                                        |
| Uptime         | 0227 06:28:39 DAYS H:M:S                                   |
| Input Status   | LOCKED 188 72.666 Mbits/s                                  |
| Video Status   | RUNNING 1920x1088 Interlaced 25Hz 4:2:0 16:9 1.995 Mbits/s |
| Audio 1 Status | RUNNING MUS                                                |
| Audio 2 Status | RUNNING MUS                                                |

The front panel LED light or the RX8200 page should show green in normal status. An orange or yellow LED colour may only reflect that a particular RX8200 parameter needs to be reselected and WNE Data and RLS video may well still be present. The home page will show more detail than the front-panel. If the RX8200 receiver is unresponsive via the front-panel or browser interface it should be power cycled (rebooted). If that does not resolve the issue, please contact the Thomson Reuters Support Team (see Appendix F).

From the RX8200 receiver web page the following basic checks can be performed.

# B.1.1 SATELLITE SIGNAL

Selecting Input then Sat Input will show the satellite reception details. The most important setting is C/N margin. At a minimum this must be 2-3dB, but a higher value as shown below is preferable. The screen to the left shows example reception in Europe (SES4) and to the right in Asia (Asiasat5).

| Status            | Device Info   | Alarms       |
| ----------------- | ------------- | ------------ |
| Customization     | CA Input      | Service plus |
| Input > SAT Input | Apply Changes | 2 Refresh    |

| Input 1 (L-band) | Input 2 (L-band) |
| ---------------- | ---------------- |
| Input 3 (L-band) | Input 4 (L-band) |

# Parameters

| RF Selection:          | Input 1 (L-band) |
| ---------------------- | ---------------- |
| Lock Status:           | LOCKED           |
| Signal Level Estimate: | -48 dBm          |
| Packet Error Ratio:    | <1.0E-8          |
| C/N:                   | 15.70 dB         |
| C/N Margin:            | +09.8 dB         |
| Modulation Mode:       | DVB S2           |
| Modulation Format:     | 8PSK             |

# The full parameters section

| RF Selection:          | Input 1 (L-band) |
| ---------------------- | ---------------- |
| Lock Status:           | LOCKED           |
| Signal Level Estimate: | >-30 dBm         |
| Packet Error Ratio:    | <1.0E-8          |
| C/N:                   | 16.40 dB         |
| C/N Margin:            | +06.9 dB         |
| Modulation Mode:       | DVB S2           |
| Modulation Format:     | 8PSK             |
| FEC Rate:              | 5/6              |
| Spectral Sense:        | INVERTED         |
| Pilot:                 | ON               |
| Frame Size:            | NORMAL           |
| Symbol Rate:           | 30.00 MSym/s     |
| Roll Off Status:       | 20%              |
| Detected Streams:      | SINGLE           |

WNE Customer Technical Guide Page 51 of 70





# B.1.2 SERVICE SELECTION

In Asia the Reuters signal is distributed alongside other broadcaster signals as part of a multiplex so it is vitally important that the receiver is always configured to receive the Reuters signal. The screens below show the selection in Europe SES-4 (top) and Asia Asiasat-5 (bottom).

# Status

Device Info    Alarms     Customization     CA Input Service plus   Decode Output     Download SNMP Presets Save/Load             Help

# Services

Apply Changes     x Drop All Selections            Refresh

# Service Control Table

| Encryption | Service Type   | Service ID | Service Name    | Decrypt | Decode | PID Info |
| ---------- | -------------- | ---------- | --------------- | ------- | ------ | -------- |
| Clear      | Digital TV     | 1          | Reuters TV News | V       | V      | Details  |
| Unknown    | Data Broadcast | 65534      | OAD Service HD  |         |        | 50       |

# For Europe

# Status

Device Info    Alarms     Customization     CA Input Service plus Decode   Output Download     SNMP Presets Save/Load Help

# Services

Apply Changes     Drop All Selections              Refresh

# Service Control Table

| Encryption | Service Type | Service ID | Service Name         | Decrypt | Decode | PID Info |
| ---------- | ------------ | ---------- | -------------------- | ------- | ------ | -------- |
| Unknown    | Digital TV   | 1          | Satlink OU           |         |        |          |
| Unknown    | Digital TV   | 3          | Colombo TV           |         |        |          |
| Unknown    | Digital TV   | 6          | AON Asia             |         |        |          |
| Unknown    | Other        | 8          |                      |         |        |          |
| Clear      | Digital TV   | 9          | Reuters TV News      | V       | √      | Details  |
| Unknown    | Digital TV   | 10         | EURONEWS-ASIA        |         |        |          |
| Unknown    | Other        | 15         | TRACE URBAN INTER HD |         |        |          |

# B.1.1.3 MPE SELECTION

It is important that the PID of the MPE data from the Ericsson receiver is selected. Go to Decode > MPE > PID: 3350

# RX8200

ERICSSON     RX8200 Madrid Bureau

# Status

Device Info Alarms Customization CA Input Service plus Decode Output Download SNMP Presets Save/Load Help

Decode > MPE

Apply Changes     Refresh

# MPE

Reset Stats

# MPE

|                  | PID         | IP Out Link 1          | IP Out Link 2 |
| ---------------- | ----------- | ---------------------- | ------------- |
| Filter MAC:      | 3550 - USER |                        |               |
| MPE Enable:      | V           | MPE Packets Out:       | 0             |
| MPE Packets Out: | 501702230   | Link Status:           | Down          |
| MPE Packets In:  | 501883985   | MPE Packets Processed: | 501702230     |





B.2 WNE FILE RECEPTION

# B.2 WNE FILE RECEPTION

The KenCast Fazzt software can be used to confirm that files are being received correctly from the RX8200. The Fazzt software could be used from the Web Browser link (http://localhost:4039/admin/index.fsp). Selecting received transmissions shows a list of the most recently received files and when refreshed new files should be displayed.

← → C Not secure | 10.127.0.29:4039/admin/index.fsp

KenCast Fazzt Administration (wneclient) Wed Mar 31, 12:12:09

# Configuration

# Received File Transmissions

Tools Statistics Search Clear Log Files: recvicsy View the last V 20 ines Refresh Previous Next

-Logs

Main Log Ignore: Heartbeat.txt

# Received Files

| Rx Stop Time        | Server ID | Channel Handle | Transmission ID | Transmission Status | File Name                                                                                       | Transmission Packet Count |
| ------------------- | --------- | -------------- | --------------- | ------------------- | ----------------------------------------------------------------------------------------------- | ------------------------- |
| 2021-03-31 12:11:49 | 660119    | 3              | 3763066568      | Validated           | 2012-12-06T172441Z\_49\_LWD000MVH9NXP\_RTRWNEV\_B\_T999-PLEASE-IGNORE-210331000809.MPG.enc      | 5080                      |
| 2021-03-31 12:11:46 | 660119    | 3              | 1684812237      | Validated           | 2021-03-31T114016Z\_1\_LWD0019QWRGMR\_RTRWNEV\_C\_3137-USA-IMMIGRATION-CARAVAN-HONDURAS.MP4.enC | 139776                    |
| 2021-03-31 12:10:57 | 660119    | 3              | 577143165       | Complete            | WNEHeartbeat.dat                                                                                | 1                         |
| 2021-03-31 12:10:57 | 660119    | 3              | 2793856130      | Validated           | 2021-03-31T120846Z\_1\_WDE6EYLTF\_RTRWNEC0\_3138-BOLIVIA-COCA.XML                               | 17                        |
| 2021-03-31 12:10:45 | 660119    | 3              | 3901525202      | Validated           | 2021-03-31T114016Z\_1\_LWD0019QWRGMR\_RTRWNEV\_B\_3137-USA-IMMIGRATION-CARAVAN-HONDURAS.MPG.enC | 83968                     |

# B.3 FILE DISTRIBUTION CHECK

Ensure that the file distribution tasks have been imported then check on the existence of any configured jobs open the File Distribution tab through the WNE browser page. If distribution jobs are present, then they will be visible as Automated and/or Manual Processes as shown in the following image:

REUTERS WORLD NEWS EXPRESS GMTV Help administrator

Stories Q Search Stories Search Advanced Search

Live Playout User Management File Distribution Kencast Administration Advisories

Playout + Add New Export All Import History

# AUTOMATION DISTRIBUTION PROCESSES (All Files That Arrive On WNE PC)

|                        | Name          |                           | Target                                                           |     | Type   | Actions |
| ---------------------- | ------------- | ------------------------- | ---------------------------------------------------------------- | --- | ------ | ------- |
| BOX 1: NOW PLAYING OUT | Reuters tests | Host: Directory: /reuters |                                                                  |     | FTP    |         |
| 1 File play out manual | STATS-PERFORM | 4561                      | MANUAL DISTRIBUTION PROCESSES (Files selected using the website) |     |        |         |
| 2 RLS                  | Name          |                           | Target                                                           |     | Type   | Actions |
| 3 Manual               |               | FTP Desktop Unkrgl5       | Host: Directory: /Reuters                                        | FTP |        |         |
| 4 live 2               |               | WNEv7tolaptopSMB          | Directory:                                                       |     | SMB v1 |         |

Reuters Live Preview

WNE Customer Technical Guide Page 53 of 70





# B.3.1 FILE DISTRIBUTION LOGS

The system messages screen will also display log information about the status of ftp jobs under File Distributor. To see these messages, select the STATUS tab then FILE LOG then File Distributor from the menu as shown below:

GMT V  Help  administrator

STATUS               ADMIN                 SETTINGS

About               Playout             File Processor

Services        User Management            Playout

Software Upgrades    File Distribution       Internet Backup

File Logs      Kencast Administration    Connection Tests

Device Status                                Push Client

Host Info                                  Linked Boxes

Advanced

All Settings

The File Distributor logs page have two options:

- a) Clear Completed: to clear all the items transferred and completed shown in the User Interface
- b) Clear Queue: to clear the current files waiting for file distribution transmission.

REUTERS I WORLD NEWS EXPRESS                                                                                                                                 GMT  Help    administrator

Stories                Q Search Stories                                                                                                                             Search  Advanced Search

Live                     About      Services        Software Upgrades        File Logs     Device Status  Host Info

Advisories

Playout                                                                                                                                                                       Download All

History

My Videos                      All Applications     File Distributor       File Processor  File Purger

# BOX 1: NOW PLAYING OUT

Q                    distributor history                                                                                                       Search

| 1                    | File play out manual  | G                                                                 | Clear Completed                                                   | Clear Queue                                 |             |             |       |
| -------------------- | --------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------- | ----------- | ----------- | ----- |
| SOCCER-              | WORLDCUP/NEYMAR-ALIKE | 02:59                                                             | 04:43                                                             |                                             |             |             |       |
| 2                    | RLS                   | File Distributor                                                  | File queue retrieved for "FTP Desktop Unkrgl5"                    | 2022-11-24                                  | information | 14:35       |       |
| 3                    | Manual                | File Distributor                                                  | "FTP Desktop Unkrgl5" file queue is empty. Nothing to distribute! | 2022-11-24                                  | information | 14:35       |       |
| 4                    | live 2                | O                                                                 | File Distributor                                                  | File queue retrieved for "WNEv7tolaptopSMB" | 2022-11-24  | information | 14:35 |
| Reuters Live Preview | File Distributor      | "WNEv7tolaptopSMB" file queue is empty. Nothing to distribute!    | 2022-11-24                                                        | information                                 | 14:35       |             |       |
|                      | File Distributor      | File queue retrieved for "FTP Desktop Unkrgl5"                    | 2022-11-24                                                        | information                                 | 14:34       |             |       |
| RLS Preview          | File Distributor      | "FTP Desktop Unkrgl5" file queue is empty. Nothing to distribute! | 2022-11-24                                                        | information                                 | 14:34       |             |       |
| LIVE                 | TSPWE ACCSALL         | File Distributor                                                  | File queue retrieved for "WNEv7tolaptopSMB"                       | 2022-11-24                                  | information | 14:34       |       |

Also check the File Distributor Health status, click over Status tab, then click over Services and check the health of the server, it should be “Good”.

WNE Customer Technical Guide    Page 54 of 70



REUTERS WORLD NEWS EXPRESS
# 1. File play out manual

| Name                 | Status  | Health | Version | Actions |
| -------------------- | ------- | ------ | ------- | ------- |
| wne file purger      | Running | Good   | 1.0.22  |         |
| wne kencast          | Running | Bad    | 1.2.4   |         |
| wne player-1         | Running | Good   | 1.2.55  |         |
| wne player-2         | Running | Good   | 1.2.55  |         |
| wne player-3         | Running | Good   | 1.2.55  |         |
| wne player-4         | Running | Good   | 1.2.55  |         |
| wne health reporter  | Running | Good   | 1.1.29  |         |
| wne file distributor | Running | Good   | 1.2.46  |         |

# B.4 VIDEO PLAYOUT

There are two checks for video playout. The first is the RLS (live) video playing out of the RX8200 as SDI or ANALOG video. Any system changes needed are conducted through the RX8200 webpage shown above via the Decode menu. The second is WNE files playing as SDI video through the Deck Link 8K PRO SDI video card (4-ports) to a monitor and verify if a Live signal or video file could be played on the four outputs. Click over Admin tab and then Playout.

# B.5 INTERNET BACKUP CHECK

If an Internet connection has been provided to the WNE7, the Internet Backup service should be online and Enabled as shown in the image below. Confirmation of activity and connection to the CDN can be tested via the Connection Test tab.

| Last Successful Access | Enabled | Username      |
| ---------------------- | ------- | ------------- |
| 2022-11-24 14:47       | Enabled | WNENLREU1 CDN |

WNE Customer Technical Guide Page 55 of 70



APPENDIX C – WNE6 RETIREMENT INSTRUCTIONS

To commit to the Thomson Reuters legal obligations in law, it is our obligation to remove the licensed software, clean out the user guests (Xen) and Windows data (E:\ drive) from the Reuters Video server version 6, known as WNE6.

# 6

# Reuters WNE6 server (DL180 G6 or DL360 G6)

In the case of Scenario 2 and Scenario 3 from section 2.1 on which the WNE6 server will be running in parallel with WNE7, there are two executables files that need to be stored on the WNE6 server. The two executables are:

- InstallRetireCron.exe
- TriggerWipe.exe

The file InstallRetireCron.exe will be uploaded via KenCast to the WNE6 or in case of a CDN-only WNE6 installation, it is required a manual upload to the WNE6 server. The job of the file is to look for a time extension if is requested. The file only works in conjunction with the file TriggerWipe.exe.

The file TriggerWipe.exe will be uploaded via KenCast to the WNE6 or in case of a CDN-only WNE6 installation, it is required a manual upload to the WNE6 server. The job of the file is to remove the licensed software, Xen guests and Windows data.

After executing the InstallRetireCron.exe file, check that the “About” tab of the WNE6 server; both files should be displayed as shown in the image below.

| Software Version:                                 | Version:6.3.117                      |
| ------------------------------------------------- | ------------------------------------ |
| Installed Patches:                                | Destroy-WNE-2021-04-29T14-18-00+0000 |
| Enlarged Body.Size                                | Linux wnec\_teamviewer\_idstore Fix  |
| reuters remote\_assistance\_controller\_v1        | Wipe\_Cron                           |
| wnecv2\_gold\_image\_1.0.0\_v6.3.117\_2020-11-117 |                                      |

The destroy day is displayed as shown in the below image, which means, it will run at the hour in this case will be:

2021-04-29T 15:00+0000

| BlackMagic.Output | None                     |
| ----------------- | ------------------------ |
| Destroy.Ddate     | 2021-04-29T14:18:00±0000 |

After executing the file InstallRetireCron.exe, then execute the file TriggerWipe.exe, whereby default, will show up the dateline to execute the destroy file, by default it is 14 days as shown in the image below. Press “Enter” to begin the 14-days countdown. The destroy file takes the date and time (until the hour).

WNE Customer Technical Guide

Page 56 of 70






KenCast Upgrades

For example, if you press 0 the destroy file will be executed until the clock hit the hour.

If you press 1 the destroy file will be executed the next day (24 hours after) when the clock hit the hour.

# KenCast Upgrades

# ComputerReuters (E:) KenCast Upgrades

# Search KenCast Upgrades

# Organize

Open New folder

# Favorites

|               | Name                          | Date modified    | Type        |
| ------------- | ----------------------------- | ---------------- | ----------- |
| Desktop       | InstallRetireCron.exe         | 15/04/2021 13:00 | Application |
| Downloads     | TriggerWipe.exe               | 14/04/2021 07:42 | Application |
| Recent Places | C:C:\Windows\system32\cmd.exe |                  |             |

# Libraries

- Documents
- Music
- Pictures
- Videos

# Computer

- System (C:)
- Apps (D:)
- Reuters (E:)

Note: During the installation day, the MTS technician should do a screenshot of the “About” tab or request a screenshot of the “About” tab (in case of no Internet connectivity) to ensure that both files are on the WNE6 server.

WNE Customer Technical Guide Page 57 of 70




APPENDIX D – CONFIGURATION OF MULTIPLE WNE UNITS

The diagram below depicts how more than one WNE machine could be connected to a single RX8200. For IP data and RX8200 Control, a single cable from eno7 should be connected from the server to the switch. Eno8 will still connect to the Customer Network as required.

Please note that Reuters do not supply switches for this type of connection. It is the client’s responsibility to provide a switch for this configuration.

Dual servers could be connected like below to save one receiver

| W             |                         | RX8200                  | Poo            |                |
| ------------- | ----------------------- | ----------------------- | -------------- | -------------- |
|               | DATA                    | CONTROL                 | eno7           | eno6           |
|               | 172.16.2.2              | 172.16.2.20             | SWITCH         |                |
|               | DATA & CONTROL          | DATA & CONTROL          | DATA & CONTROL | DATA & CONTROL |
| WNE7HP Server |                         | WNE7HB Server           |                |                |
|               | Customer Network (eno8) | Customer Network (eno8) |                |                |

As this example above shows, a total of 4 LAN connections into the switch are required. The RX8200 must still have its Control and Data ports connected to the switch, with unique IP addresses required for each connection. 2 unique addresses for each connection to the client LAN are also required.

|          | Control \[eno6] | Data \[eno7] | Client LAN \[eno8] example |
| -------- | --------------- | ------------ | -------------------------- |
| WNE HP 1 | N/A             | 172.16.2.25  | 192.168.0.101              |
| WNE HP 2 | N/A             | 172.16.2.26  | 192.168.0.102              |
| WNE HP n | N/A             | 172.16.2.n   | 192.168.0.n                |

The configuration for each of the servers’ network cards and covered in the network script. Below are lists of IP addresses that are assigned by Default to the WNE and RLS hardware.

| Hardware         | IP Address       | Purpose                         |
| ---------------- | ---------------- | ------------------------------- |
| RX8200 IP OUT 2  | 172.16.2.2       | Used to carry WNE IP data only. |
| RX8200 CONTROL 2 | 172.16.2.20      | Management access to receiver.  |
| HP Server eno8   | \*.\*.\*.\*      | Customer Network address.       |
| HP Server eno6   | 172.16.2.125     | Default address for RX control. |
| HP Server eno5   | Assigned by DHCP | Reuters Engineering             |
| HP Server eno7   | 172.16.2.25      | Default address for WNE IP Data |

WNE Customer Technical Guide    Page 58 of 70



APPENDIX E – WHAT’S NEW IN THE WNE7
The WNE7 software version includes a lot of improvements and bug fixes many of which are related to general stability and enhanced security.

The following technical notes related to specific changes in this version:

# I.1 SENT FROM CONNECT FEATURE

The “Send From Connect” option will allow our clients to use points to access additional video stories and send directly from the Reuters Connect (www.reutersconnect.com) website to the Reuters video server (WNE7).

| REUTERS | CONNECT                                                                           | REUTERS WORLD NEWS EXPRESS |
| ------------------------------------------------------------------------------------------- | -------------------------- |---|
| Planning                                                                                    | ¤                          | |
| Hong Kong Reuters set in e Javolins and arrows: Hix Chins urges U.S to recetfufils fourth.. | REVTERS                    | |

# PUSH TO WNE

The accessible content includes:

- Entire collection of the Video Archive dating back to 1896
- Content from our partners from the Marketplace as well as UGC providers
- Any content from other Reuters video products that you are not subscribed to already.

The Reuters Connect website will display the option as shown in the image below:

| ×    |                         |
| ---- | ----------------------- |
| B    | 9 2 iv = v              |
| 6PTS | DOWNLOAD HD 60FPS (MP4) |
| OLE  | 6PTS PUSH TO WNE        |

Source Format: HD

Audio: NATURAL WITH JAPANESE SPEECH/PART MUTE

Locations: YOKOHAMA JAPAN/UNIDENTIFIED LOCATIONS

Source: REUTERS VIA ZOOM/ARCHELIS HANDOUT

13/01/2021 17:47

Edit No: 3039 v2

Topics: Science, United States

Source News Feeds: Reuters Marketplace- Raw Video

USN: WDDV1D2SB

Exoskeleton leg device allows factory workers to 'sit' while technically standing

VIDEO SHOWS: PEOPLE WEARING ARCHELIS EXOSKELETON LEG DEVICE, INTERVIEW WITH ARCHELIS REPRESENTATIVE ABOUT DEVICE

WNE Customer Technical Guide Page 59 of 70



GREUTERS | WORLD NEWS EXPRESS
On the other hand, the WNE server, will display the videos received from the Reuters Connect website as shown in the image below:

# BOX 1: NOW PLAYING OUT

|   | Preview                      | ID                     | Slug                                                                      | Headline                                                                        | Arrived                           |      |                |                                                  |          |
| - | ---------------------------- | ---------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------- | ---- | -------------- | ------------------------------------------------ | -------- |
|   |                              |                        |                                                                           | 1                                                                               | SDI output 01 - sent from connect | 2267 | PEOPLE-        | Nikki Haley vows to campaign for Trump in 2020   | 13/11/19 |
| 2 | SDI output 02 - file playout | 3077                   | HEALTH-CORONAVIRUS/FRANCE-SHOPS                                           | Charlize Theron celebrates the resilience and beauty of her native South Africa | 13/11/10                          |      |                |                                                  |          |
|   |                              |                        |                                                                           | 3                                                                               | SDI output 03 - live              | 2268 | PEOPLE-SEXIEST | John Legend named magazine's 'sexiest man alive' | 13/11/19 |
|   |                              | 2248                   | TENNIS-                                                                   | Probably my best ever, says Thiem after Djokovic win                            | 13/11/19                          |      |                |                                                  |          |
|   | 2253                         | USA-TRUMP/IMPEACHMENT- | Ahead of public impeachment hearings, New York Republicans slam Democrats | 13/11/19                                                                        |                                   |      |                |                                                  |          |

And within the Reuters Connect account “history” of organization, it will show up the video file sent to the server:

# REUTERSCONNECT

Feed Planning Live Productivity Suite [Beta] 344 PTS 2- 45 Tania Vivero

Account Downloads

11021 items downloaded in the last 30 days

| DATE             | USERNAME             | HEADLINE                                                    | MEDIA TYPE    | SOURCE                      | POINTS USED | ACTION         | |
| ---------------- | -------------------- | ----------------------------------------------------------- | ------------- | --------------------------- | ----------- | -------------- |---|
| 27/05/2021 12:36 | Tania Vivero         | GLOBALink | Taiwan authorities should focus on fighting     | Video         | Xinhua News Agency          | 3           | Success        |
| 27/05/2021 12:26 | Tania Vivero         | Top African streaming platform focuses on local productions | Archive Video | Reuters                     | 0           | Success        | |
| 27/05/2021 12:11 | Yesim Dikmen         | Biden orders further review of COVID origins                | Video         | U.S. NETWORK POOL / REUTERS | 0           | Download Again | |
| 27/05/2021 11:30 | Foundation Editorial | FILE PHOTO: Extreme Heat in Death Valley                    | Picture       | REUTERS                     | 0           | Download Again | |

WNE Customer Technical Guide Page 60 of 70






# I.2 FOUR (4) SDI VIDEO OUTPUTS

The new WNE7 server has 4 SDI out ports per box. Each port is fully configurable for Live events or File playout, including the option for dedicated “Sent from Connect” playout.

| 12G-SDI In/Out | 4 | Blackmagic DeckLink PRO |
| -------------- | - | ----------------------- |
| 12G-SDI In/Out | 3 | PCI                     |
| 12G-SDI In/Out | 2 | EXPRESS                 |
| 12G-SDI In/Out | 1 |                         |

Ref In

4 SDI ports

WNE Customer Technical Guide    Page 61 of 70



APPENDIX F – HOW TO EXPORT OLD CONTENT FROM WNE6 TO WNE7
This section shows up how to export old content from the WNE6 to the WNE7 server in case there is a “server swap” during the installation day.

If there is no server swap then the WNE6 server will run in parallel for 14 days (by default) and the files could be moved from the WNE6 to the WNE7 manually.

1. The client should save all the files from the WNE6 file location E:\Reuters\Video to their own file server.

Important: the files allowed to be copied are: XML (non-legacy), MPEG, and MP4. The legacy XML file format could not be exported.
2. From the client file server, it is necessary to Map Network Drive as shown in the image below:

- System (C:)
- Apps (D:)
- RbReuters (E:)

Network

- Expand
- Open in new window
- Map network drive...
- Disconnect network drive...
- Delete
- Properties

Select the Z: drive and in the folder field, type the WNE7 server IP (\\wne7_server-IP\share) as shown in the image below:

Map Network Drive

What network folder would you like to map?

Specify the drive letter for the connection and the folder that you want to connect to:

| Drive:  | Z:                   |
| ------- | -------------------- |
| Folder: | \\\10.127.0.29\share |

Example: \\server\share

Reconnect at logon

Connect using different credentials

Connect to a Web site that you can use to store your documents and pictures

Finish  Cancel

Windows will ask for the WNE7 server user/password as shown below. User: wneclient password: reuters

Map Network Drive

Attempting to connect to \\10.127.0.29\share..

Drive: Z:

Folder: \\10.127.0.29\share

Example: \\server\share

Reconnect at logon

Connect using different credentials

Connect to a Web site that you can use to store your documents and pictures

Finish  Windows Security

Enter Network Password

Enter your password to connect to: 10.127.0.29

SDI OU

| Date                 | Status | Status | wneclient               |
| -------------------- | ------ | ------ | ----------------------- |
| Domain: WNEC-WINDOWS |        |        | Remember my credentials |
| Access is denied.    |        |        |                         |

OK  Cancel

Once the WNE7 server has been installed, all the files should be copied to the WNE7 location \\wnev7_server_ip\share and the WNE7 server will take the files.

WNE Customer Technical Guide Page 62 of 70



APPENDIX G – FILE DISTRIBUTOR

The File Distributor tool provides a more flexible way of distributing files from the WNEv7 server to external storage systems.

There are two types of distributions processes as follows:

- Automation Distribution Process – all the files that arrive on the WNE PC will be distributed. (it is also possible to filter which files are distributed by service)
- Manual Distribution Process – only the files selected manually using the ‘Add to Distribution’ button will be Distributed

The file distribution icon is shown under the “Actions” column as shown below:

| Preview | Slug    | ID   | Headline                                  | Arrived V        | Actions |
| ------- | ------- | ---- | ----------------------------------------- | ---------------- | ------- |
|         | Reuters | 3009 | Tornado strikes rural area of Philippines | 2021-06-02 08:51 | PO +    |

To add a new distribution process, follow the steps below:

1. Log in to WNE with your administrator account.
2. Click the Admin option
3. In the 3-bar menu icon, select the File Distribution option, click the +Add New button.

REUTERS WORLD NEWS EXPRESS GMT V Help administrator

Stories Q Search Stories Search Advanced Search 4 Live Playout User Management File Distribution Kencast Administration Advisories Playout + Add New Export All Import History

AUTOMATION DISTRIBUTION PROCESSES (All Files That Arrive On WNE PC)

| Name | Target | Type | Actions |
| ---- | ------ | ---- | ------- |
|      |        |      |         |

4. The main menu options appear, as first step, enter a name for the distribution process. You can configure up to 30 active processes.

FILE HANDLING Configure how the WNE PC will distribute the files that it ingests. You can configure up to 30 active processes (60 in total including paused or stopped processes). Each process can deliver files to a different location. Name *

5. As next step, please choose what files and the type of files and the method to distribute.

WNE Customer Technical Guide Page 63 of 70




WNE Customer Technical Guide

# What files would you like to distribute? *

Files selected manually using the website

All files that arrive on the WNE PC

# What types of files do you want to distribute? *

- SD Videos
- HD Videos
- Scripts

# a) What files would you like to distribute?

- Files selected manually using the website: These are files that are selected manually using the ‘Add to Distribution’ button located in the “Stories” tab. The resulting process will be placed under Manual Distribution Process section.
- All files that arrive on the WNE PC: These include all the files that arrive on the WNE PC. The resulting process will be placed under Automation Distribution Process sections.

# b) What types of files do you want to distribute?

- SD Videos – SD Videos will be distributed (.MPG)
- HD Videos - HD Videos will be distributed (.MP4)
- Scripts - Scripts will be distributed.
- Advisories – Advisories will be distributed.

Note: Advisories will be visible only when “All files that arrive on WNE PC” is selected in step (a)

# c) If the options “All files that arrive on WNE PC” and both a “Video” selection (SD or HD) and “Scripts” are chosen, additional choices appear as shown below:

- Distribute files in the order that they arrive – If scripts arrive earlier than videos, choosing this option will distribute them in the same order, as and when they arrive.
- Distribute videos and scripts together – Choosing this option will ensure both the script files and their corresponding video files have arrived before distributing them together.

# What files would you like to distribute? *

Files selected manually using the website

All files that arrive on the WNE PC

# What types of files do you want to distribute? *

- SD Videos
- HD Videos
- Scripts
- Advisories
- Distribute files in the order that they arrive
- Distribute videos and scripts together

Page 64 of 70




# 6. What method would you like to use to distribute these files?

What method would you like to use to distribute these files? *

- FTP
- FTPS
- SFTP
- SMB

These are the different methods of distribution available. Select the one of your preference.

# 7. Select this option to output legacy file types:

Select this option to output legacy file types

Legacy

The legacy file format was of the type: 202106015079WD-SOCCER-USA.xml

# 8. Depending on the method of distribution you choose in step 6, different options will appear.

a) If you had chosen FTP, the following options appear:

# FTP LOCATION DETAILS

Enter your FTP location details below. Optionally, enter a secondary location to be used if the primary location becomes unavailable.

| Host \*                              | Standby Host             |
| ------------------------------------ | ------------------------ |
| Target Directory                     | Standby Target Directory |
| Port Number \*                       | Standby Port Number      |
| 21                                   | 21                       |
| Username \*                          | Standby Username         |
| Password \*                          | Standby Password         |
| Active                               | Passive                  |
| Use proxy                            |                          |
| Use ".tmp" extension during transfer |                          |

WNE Customer Technical Guide Page 65 of 70




# Enter the following details:

- Host – hostname of the FTP server
- Target Directory – directory in the FTP Server where you want the files to be distributed
- Port Number – FTP Port number. The default value is 21.
- Username – username to access the FTP server
- Password – password to access the FTP server
- Active/Passive – Mode of FTP
- Use proxy (if applicable)

Active IP is an external IP address on the network card used on your box for this connection (i.e. active &#x3C;- connection -> host). If there is none it tries to guess basing on your local host settings.

Similarly, enter the standby location details if applicable. When the Primary configuration is not available, Standby will be used until the Primary is available again.

Use “.tmp” extension during transfer – specifies if the files should use a .tmp extension while being transferred. It is recommended to keep this checked to prevent processing of incompletely transferred files. It should be unchecked only if your FTP server does not allow renaming of files or if the FTP server already uses a .tmp extension.

If the ftp server is making use of User Isolation Settings for FTP, please make use of the ~ symbol to represent the home directory or use the full path. Example:

Solution 1 the full path: /thirdparties/Reuters

Solution 2 or the instruction: ~/Reuters

# b) If you had chosen FTPS, the following options appears:

# FTPS LOCATION DETAILS

Enter your FTPS location details below. Optionally, enter a secondary location to be used if the primary location becomes unavailable.

| Host \*                              | Standby Host             |            |         |
| ------------------------------------ | ------------------------ | ---------- | ------- |
| Target Directory\*                   | Standby Target Directory |            |         |
| Port Number \*                       | Standby Port Number      |            |         |
| 21                                   | 21                       |            |         |
| Username \*                          | Standby Username         |            |         |
| Password \*                          | Standby Password         |            |         |
| 0                                    | 0                        |            |         |
| Active                               | Passive                  | Active     | Passive |
| Advanced                             | Advanced                 |            |         |
| Trust Manager                        | Standby Trust Manager    |            |         |
| All                                  | V                        | All        | V       |
| Data Channel Protection              | Standby Data Channel     |            |         |
| Cleared                              | V                        | Protection |         |
| Implicit                             | oExplicit                | Cleared    |         |
| Use proxy                            | Implicit                 | oExplicit  |         |
| Use proxy                            |                          |            |         |
| Use ".tmp" extension during transfer |                          |            |         |

WNE Customer Technical Guide    Page 66 of 70





WNE Customer Technical Guide

# Enter the following details:

- Host – hostname of the FTPS server
- Target Directory – directory in the FTPS Server where you want the files to be distributed
- Port Number – FTPS Port number. The default value is 21.
- Username – username to access the FTPS server
- Password – password to access the FTPS server
- Active/Passive – Mode of FTP

# Select Advance (if applicable)

- Trust Manager: All or Valid
- Data Channel Protection: Cleared or Private

Use “.tmp” extension during transfer – specifies if the files should use a .tmp extension while being transferred. It is recommended to keep this checked in order to prevent processing of incompletely transferred files. It should be unchecked only if your FTP server does not allow renaming of files or if the FTP server already uses a .tmp extension.

# If you had chosen SFTP, the following options appears:

# SFTP LOCATION DETAILS

Enter your SFTP location details below. Optionally, enter a secondary location to be used if the primary location becomes unavailable.

| Host \*                              | Standby Host             |
| ------------------------------------ | ------------------------ |
| Target Directory \*                  | Standby Target Directory |
| Username                             | Standby Username         |
| Password/Private Key                 | Password Private Key     |
| Password \*                          | Standby Password         |
| Use proxy                            | Use proxy                |
| Use ".tmp" extension during transfer |                          |

# Enter the following details:

- Host – hostname of the SFTP server
- Target Directory – directory in the SFTP Server where you want the files to be distributed
- Username – username to access the SFTP server
- Password/Private Key – password or private key to access the SFTP server
- Use Proxy (if applicable)

Use “.tmp” extension during transfer – specifies if the files should use a .tmp extension while being transferred. It is recommended to keep this checked in order to prevent processing of incompletely transferred files. It should be unchecked only if your FTP server does not allow renaming of files or if the FTP server already uses a .tmp extension.

Page 67 of 70





# d) If you had chosen SMB, the following options appears.

# NETWORK LOCATION DETAILS

| Version 1                                                                                               | Version 2 |
| ------------------------------------------------------------------------------------------------------- | --------- |
| The target directory is a network directory where you wish the WNE files to be copied. Example /scripts |           |
| Target Directory Path \*                                                                                |           |
| Domain                                                                                                  |           |
| Username                                                                                                |           |
| Password                                                                                                |           |

Enter the following details:

- Choose from SMBv1 or SMBv2
- Target Directory – directory in the SMB File server where you want the files to be distributed
- Domain – SMB domain if applicable.
- Username – username to access the SMB
- Password – password to access the SMB

# 9. Which users are allowed to distribute?

If the option “Files selected manually using the website” is selected, then it is possible to set up file distribution processes such that can only be invoked by specific logins.

The logins can be created in the “User Management” tab under the “Admin” page.

# FILE HANDLING

Configure how the WNE PC will distribute the files that it ingests. Which users are allowed to distribute? *

You can configure up to 30 active processes (60 in total including paused or stopped processes).

Each process can deliver files to a different location.

Name *

# FTP LOCATION DETAILS

What files would you like to distribute? *

- Files selected manually using the website
- All files that arrive on the WNE PC

WNE Customer Technical Guide Page 68 of 70






# FILTERS

A filter allows you to specify that only files meeting a specific criteria be distributed. If you choose no filter, all files will be distributed. Consult the Help guide for more information about filters. If you are unsure, choose "No Filter".

# No Filter

| Service Filter | Sports |
| -------------- | ------ |
|                | Subcon |
|                | USVO   |
|                | Viral  |
|                | World  |

| Sensitivity Filter (exclusions) | Graphic   |
| ------------------------------- | --------- |
|                                 | Nudity    |
|                                 | Profanity |

- No Filter – All files will be distributed without any filtering
- Service Filter – Files will be filtered based on the channel(s) you chose. A drop-down menu of available channels will appear when you choose this option. You can select multiple channels by holding down the control (Ctrl) key and selecting the required values.
- Sensitivity Filter – Files will be filtered based on any graphic content, nudity and/or profanity.

To finish the file distributor process configuration, click SAVE.

The newly configured process will now be listed in the main page either under Automation or Manual Distribution, depending on how it was configured.

WNE Customer Technical Guide Page 69 of 70



# APPENDIX H – TECHNICAL SUPPORT

There are a variety of means by which you can contact Thomson Reuters for support. One of the easiest is to go to https://liaison.reuters.com/contact-us and complete the request form after which a customer representative should contact you within 15 minutes. No sign-in is required.