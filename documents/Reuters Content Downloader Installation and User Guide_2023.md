# REUTERS CONTENT DOWNLOADER

# INSTALLATION AND USER GUIDE

Date of Issue: 2023

Document Version: 9.0




# Contents

# Chapter 1 Introduction

3

# 1.1 OVERVIEW OF REUTERS CONTENT DOWNLOADER

3

# 1.2 Help Document Organization

4

# Chapter 2 INSTALLATION AND STARTUP OPTIONS

5

# 2.1 SYSTEM REQUIREMENTS

5

# 2.2 Installing Content Downloader

6

# 2.2.1. Download Reuters Content Downloader for all platforms

6

# 2.2.2. Windows

8

# 2.2.3. Linux

15

# 2.2.4. Mac OS

24

# 2.3 Starting and Stopping the Application

29

# 2.3.1. Windows

29

# 2.3.2. Linux and Mac OS

30

# 2.4 Upgrading to latest releases

31

# 2.4.1. Upgrading using installer from Reuters Liaison

31

# 2.5 Uninstalling Content Downloader

31

# 2.5.1. Windows

31

# 2.5.2. Reinstalling Reuters Content Downloader

32

# 2.5.3. Linux

32

# 2.5.4. Mac OS

34

# Chapter 3 CONFIGURATION GUIDELINES

35

# 3.1 Quick start

35

# 3.2 Logging into Reuters CONNECT and validating Content Delivery

36

# Chapter 4 Configuration

# 4.1.1. Configuring Download Settings

37

# 4.1.2. Configuring News Feeds

40

# 4.1.3. Configuring Alerts

41

# 4.1.4. Configuring File Types to Download

42

# 4.1.5. Downloading Older Content

47

# 4.1.6. Downloading Top 10 Online Reports

50

# Chapter 5 Server Summary &#x26; Statistics

52

# 5.1 VIEWING LOCAL SERVER SUMMARY

52

# 5.2 How to customize the local server access

52

# 5.3 Viewing Hosted Server Statistics

53

# 5.4 Accessing Content Downloader Help

55

# 5.5 Accessing Account Details

55

# Chapter 6 TROUBLESHOOTING

57

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9 0






# Contents

# 6.1 LOG AND AUDIT FILES

.............................................................................................................. 57

# 6.2 Exceptions and Error Messages

.................................................................................................. 57

# Chapter 7 FAQs

......................................................................................................................................... 60

# Reuters Connect

..................................................................................................................................... 60

# Chapter 8 Customer Support

................................................................................................................... 61

# Chapter 9 Classification

........................................................................................................................... 63

© Thomson Reuters 2022. All Rights Reserved. Thomson Reuters, by publishing this document, does not guarantee that any information contained herein is and will remain accurate or that use of the information will ensure correct and faultless operation of the relevant service or equipment. Thomson Reuters, its agents, and employees, shall not be held liable to or through any user for any loss or damage whatsoever resulting from reliance on the information contained herein.

This document contains information proprietary to Thomson Reuters and may not be reproduced, disclosed, or used in whole or part without the express written permission of Thomson Reuters. Any Software, including but not limited to, the code, screen, structure, sequence, and organization thereof, and Documentation are protected by national copyright laws and international treaty provisions. This manual is subject to U.S. and other national export regulations.

Nothing in this document is intended, nor does it, alter the legal obligations, responsibilities or relationship between yourself and Thomson Reuters as set out in the contract existing between us.

Reuters Connect Content Downloader - Installation and User Guide 2

Document Version : 9.0




# Chapter 1 INTRODUCTION

# 1.1 OVERVIEW OF REUTERS CONTENT DOWNLOADER

The Content Downloader application downloads and stores Reuters media content for customer processing. The Content Downloader has been designed to:

- provide visibility of the delivered content on the client site, using a web server delivered as part of the Local Server installation
- offer remote access to the Hosted Server configuration, allowing remote support for the client and Thomson Reuters Customer Support
- designed as an easy-to-use frontend user interface which requests and downloads content using Reuters Connect Web Services as a backend data source.

Note: To ensure consistency across the document, the web server installed on the client site will be referred to as the Local Server (http://localhost:8080/summary.do) and the hosted Reuters Content Downloader Server (https://contentdownloader.reuters.com/cdt-server/) will be referred to as the Hosted Server.

For RCD v4.4.28 or higher, the Local Server will only be accessible by https (https://localhost:8080/summary.do)

| Hosted Server                           | Reuters Web Services      |
| --------------------------------------- | ------------------------- |
| <https://contentdownloader.reuters.com> | <https://rmb.reuters.com> |

Request for configuration

Request for content

Internet

Local Server (Installed on Client Site)

http://localhost:8080

For RCD v4.4.28 or above: https://localhost:8080

The Content Downloader application will be installed on the client site. The download options can be configured on the Hosted Server and based on this configuration; content will be downloaded from the Reuters Web Services onto the client machine. The downloaded files can then be parsed to process and publish the contents as per the customer's requirements.

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0





# 1.2 HELP DOCUMENT ORGANIZATION

The various sections that are covered in this help documentation are given below.

- INSTALLATION AND STARTUP OPTIONS - This section gives you an overview of system requirements and how to install the product. It also provides information on how to start and stop the application.
- CONFIGURATION GUIDELINES - This section is a quick reference guide if you want to start using the application right away.
- Summary &#x26; Statistics - This section gives you the summary of recently downloaded content and client statistics.
- Troubleshooting - This section helps you in troubleshooting some problems that you may encounter while using this application.
- FAQs – This section gives you details on how to access the list of frequently asked questions.
- Customer Support - This section provides you with details to contact Customer Support.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



# Chapter 2 INSTALLATION AND STARTUP OPTIONS

# 2.1 SYSTEM REQUIREMENTS

# Supported platforms

- Windows 7, Windows 8, Windows 10, Windows Server 2012 R2, Windows Server 2016, Windows Server 2019, Windows Server 2022
- Linux 4.14 (Red Hat 7.2.1), Linux 3.6 (Red Hat 4.7.2, UBUNTU v12.x)
- Macintosh OS X 10.13 or later version

# Supported Browsers

- Microsoft Edge version 100.0.1185.44 or later versions.
- Firefox 98.0.2 or later versions.
- Safari 10 or later versions.
- Google Chrome version 100.0.4896.127 or later versions.

# Domain Names and Ports used by the Local Server

PLEASE READ!! If your computer or server is protected by a firewall/proxy, please request your company IT department open the following ports or add DNS names to your proxy server to permit full functionality to the Reuters Content Downloader application:

| Domain Name                     | Protocol & Port      | Description                              |
| ------------------------------- | -------------------- | ---------------------------------------- |
| content.reuters.com             | HTTP (TCP port 80)   | Repository Server of Reuters Media       |
| secure.content.reuters.com      | HTTPS (TCP port 443) | Content                                  |
| Videobroadcast.cdn.reuters.com  | HTTP (TCP port 80)   | AWS CloudFront                           |
| Videobroadcast.cdns.reuters.com |                      |                                          |
| rmb.reuters.com                 | HTTP (TCP port 80)   | Reuters Web Services                     |
|                                 | HTTPS (TCP port 443) |                                          |
| commerce.reuters.com            | HTTP (TCP port 80)   | Reuters Authorization Server             |
|                                 | HTTPS (TCP port 443) |                                          |
| contentdownloader.reuters.com   | HTTP (TCP port 80)   |                                          |
| cdn1.agency.thomsonreuters.com  | HTTPS (TCP port 443) | Reuters Content Downloader Hosted Server |
| cdn2.agency.thomsonreuters.com  |                      |                                          |

The Content Downloader client site will initiate the contact for all the DNS.

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0



# 2.2 INSTALLING CONTENT DOWNLOADER

# 2.2.1 Download Reuters Content Downloader for all platforms

1. The first step consists of downloading the Content Downloader application from the Reuters Liaison website:
http://liaison.reuters.com/

REUTERS LIAISON

Home | Tools | Contact Support | Reuters News Agency

YOUR SERVICE HUB FOR REUTERS NEWS AGENCY &#x26; CONTENT SOLUTIONS

This site is an extension of our customer service application - Liaison - which is available on both iOS and Android platforms. Here you can open service requests, generate feedback to us, find other tool-kits to support content delivery, download guides, and learn about our products. The team at Reuters News Agency-Service and Support makes it our mission, and it's our pleasure, to ensure that your customer experience is second to none and the support of your Reuters content is to your satisfaction every single time.

Solutions &#x26; Delivery

Our content is delivered over a wide variety of mediums; either by internet or satellite. Our Reuters Media Delivery Platform offers solutions ranging from RSS to FTP Push. Even access our API to power content-driven applications. For details on Reuters Media Delivery.
2. Scroll down on the page and click on the dropdown menu and search for Content Downloader; then click on the Related Content tab and select your desired installer.

REUTERS LIAISON

Home | Tools | Contact Support | Reuters News Agency

Solutions &#x26; Delivery

Our content is delivered over a wide variety of mediums; either by internet or satellite. Our Reuters Media Delivery Platform offers solutions ranging from RSS to FTP Push. Even access our API to power content-driven applications. For details on Reuters Media Delivery please review our overview guide. Learn more >

You must be logged into your Media Express user to view available reference material. If you have not logged in, you will be prompted to do so when selecting a document. If you do not have one, please contact us by clicking on the Contact Support link in the top right. We'll get your request taken care of straight away.

Learn about your desired solution or delivery platform by selecting from the dropdown below.

Content Downloader

- Reuters Content Downloader for Windows
- Reuters Content Downloader for Mac OS X
- Reuters Content Downloader for Linux (32 bit)
- Reuters Content Downloader for Linux (64 bit)
- User Guide
- Communication Guide
- XML Quick Reference
- RCD Remote Administration

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0





# 3.

To download Content Downloader application, it’s necessary to login with your Reuters Connect username and password.

# REUTERS LIAISON

Login

Please login with any of your Reuters credentials below:

(Internal users please login using SAFE)

| Username | Enter Username |
| -------- | -------------- |
| Password | Enter Password |

Login

# 4.

After login, download Content Downloader installer based in your platform.

1. Select your platform: Windows, MAC OS, Linux 32 bit or Linux 64 bit
2. Download and save the application into your server/PC; after the application has been downloaded then unpack or uncompress the package into your desired location.
3. Open the unpack/uncompress folder and execute the file cdt-client-x.x.x-win.exe (for Windows); cdt-client.x.x.x-macos.dmg (for MacOS); cdt-client-x.x.x-linux.sh (for Linux 32 bit) and cdt-client-x.x.x-linux_x64.sh (for Linux 64bits) and follow the wizard to begin the installation.
4. For Windows, open the installer and run it as Administrator as shown below:

| cdt-client-4.4.28-win.exe | Open | Run as administrator |
| ------------------------- | ---- | -------------------- |

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0





# 2.2.2. Windows

1. The Welcome screen of the Content Downloader Setup Wizard appears. Click Next.

| Setup - Reuters Content Downloader 4.4.28                                                                                      | ×      |
| ------------------------------------------------------------------------------------------------------------------------------ | ------ |
| Welcome to the Reuters Content Downloader Setup Wizard                                                                         |        |
| This will install Reuters Content Downloader on your computer. The wizard will lead you step by step through the installation. |        |
| Click Next to continue, or Cancel to exit Setup.                                                                               |        |
| Next >                                                                                                                         | Cancel |
2. The License Agreement screen appears.

| Setup - Reuters Content Downloader 4.4.28                                                                                                                                                                                                                                                                                                                                                                                                                                    | ×      |        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------ |
| License Agreement                                                                                                                                                                                                                                                                                                                                                                                                                                                            |        |        |
| Please read the following important information before continuing.                                                                                                                                                                                                                                                                                                                                                                                                           |        |        |
| Please read the following License Agreement. You must accept the terms of this agreement before continuing with the installation.                                                                                                                                                                                                                                                                                                                                            |        |        |
| Copyright (c) 2012 John Resig, <http://jquery.com/>                                                                                                                                                                                                                                                                                                                                                                                                                          |        |        |
| Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:                             |        |        |
| The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.                                                                                                                                                                                                                                                                                                                                               |        |        |
| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. |        |        |
| \[ ] I accept the agreement                                                                                                                                                                                                                                                                                                                                                                                                                                                  |        |        |
| \[ ] I do not accept the agreement                                                                                                                                                                                                                                                                                                                                                                                                                                           |        |        |
| install4j                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |        |        |
| < Back                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Next > | Cancel |

Scroll down the page to read the entire agreement terms and choose 'I accept the agreement'. Then click Next.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0




# Reuters Connect Content Downloader - Installation and User Guide

# Document Version : 9.0

# 3. Select Destination Directory

In the Select Destination Directory screen, select a location to install the application and click Next. By default, it will be installed in C:\Program Files\Reuters\ContentDownloader4.

Select a location to install the application and click Next.

# Setup - Reuters Content Downloader 4.4.28

# Select Destination Directory

Where should Reuters Content Downloader be installed?

Select the folder where you would like Reuters Content Downloader to be installed, then click Next.

| `C:\Program Files\Reuters\ContentDownloader4` | Browse |
| --------------------------------------------- | ------ |
| Required disk space: 196 MB                   |        |

install4j

&#x3C; Back  Next >  Cancel

# 5. Local Web Server Configuration

Enter a port number to access the Local Content Downloader and click Next. You can use any free port number here. Default value is 8080. If you need to change the value later, it can be edited in &#x3C;installation directory>/conf/client.properties file.

# Setup - Reuters Content Downloader 4.4.28

During this installation a local web server will be installed to allow easy LAN access to configure and view Reuters Content Downloader files.

Please specify the port to run the web server on. The default Port Number is 8080.

| Local Web Server Port Number | r8080 |
| ---------------------------- | ----- |

install4j

&#x3C; Back  Next >  Cancel






# Reuters Connect Content Downloader - Installation and User Guide

# 6.

In the following screen, browse and choose the output directory for downloading the content and click Next.

Setup - Reuters Content Downloader 4.4.28

# Configure

Choose the root output directory for downloading media content

| Root output directory | C:\ReutersIN | Browse .. |
| --------------------- | ------------ | --------- |

install4j

&#x3C; Back  Next >  Cancel

# 7.

In the following screen, select a name for the Start menu folder name and click Next. By default, it will be Reuters Content Downloader.

Setup - Reuters Content Downloader 4.4.28

# Select Start Menu Folder

Where should Setup place the program's shortcuts?

Select the Start Menu folder in which you would like Setup to create the program's shortcuts, then click Next.

| Create a Start Menu folder              | Reuters Content Downloader |
| --------------------------------------- | -------------------------- |
| 7-Zip                                   |                            |
| Accessibility                           |                            |
| Accessories                             |                            |
| Administrative Tools                    |                            |
| AnyDesk                                 |                            |
| Cisco                                   |                            |
| Cisco Jabber                            |                            |
| Cisco Webex Network Recording Converter |                            |
| ConfiguradorFnmt                        |                            |
| Evernote                                |                            |
| FortiClient                             |                            |
| Garmin                                  |                            |
| Git                                     |                            |
| Healing Station Client                  |                            |
| HP                                      |                            |
| IIC                                     |                            |

Create shortcuts for all users

install4j

&#x3C; Back  Next >  Cancel

Document Version : 9.0






# Reuters Connect Content Downloader - Installation and User Guide

# 8.

Once the application has been installed, you will get the below screen, ensure that Start the Content Downloader service and Open browser and start configuring client are selected, then click on FINISH.

Setup - Reuters Content Downloader 4.4.28

Completing the Reuters Content Downloader Setup Wizard

Setup has finished installing Reuters Content Downloader on your computer. The application may be launched by selecting the installed icons.

Click Finish to exit Setup.

- Start the Reuters Content Downloader Service
- Open browser and start configuring the client

Finish

# 9.

After installation is complete Reuters Content Downloader service and Configuration page starts up automatically.

1. If Content Downloader service doesn’t start up automatically, please start up the service as follows: Start-->All Programs-->Reuters Content Downloader-->Start Reuters Content Downloader Service.
2. The Configuration page can be accessed at a later point of time by invoking Start-->All Programs-->Reuters Content Downloader-->Open Configuration Page.
3. Click Finish to complete the installation process.

# 10.

The following Installation Complete screen will be displayed if you had chosen to start the Content Downloader Service in the previous step.

Installation Complete

Please Sign In using the link above to complete your Reuters Connect Content Downloader Configuration.

CLOSE

# 11.

If Content Downloader has been installed correctly; you will be redirected to Local Server URL login page: http://localhost:8080/summary.do and for RCD 4.4.48 or above the local server is https://localhost:8080/summary.do and the following page appears:

Document Version : 9.0






Reuters Connect Content Downloader - Installation and User Guide

# Summary

Status: ACTIVE v4.4.28

# Summary

This page gives a real time view of content recently downloaded. Click the news feed name to get a full list of the last 30 files received.

And enter Reuters Content Downloader credentials:

https:/localhost:8080/login.action

# Sign In

To access the configuration features of the Reuters Content Downloader. Please enter your Reuters Connect credentials below:

| LOGIN:    |   |
| --------- | - |
| PASSWORD: |   |

SIGN IN

12. After login the application will ask for your Proxy information (if the application detected it), fill out with your Proxy information: URL, username and password and click on Test Connection. If you don’t use a Proxy, click on SIGN IN.

# REUTERS CONNECT CONTENT DOWNLOADER

# Summary

Sign In

We were unable to contact the Reuters Web Services to authenticate your entered credentials. Please check your connectivity to the Internet or enter proxy details below.

| Proxy URL:      |   |
| --------------- | - |
| Proxy Username: |   |
| Proxy Password: |   |

SIGN IN  TEST CONNECTION

13. IMPORTANT!! After Proxy connection has been tested; the Local Server will be redirected automatically to the Hosted Server to configure Connection Details. Please enter a description name.

Document Version : 9.0




REUTERS CONNECT CONTENT DOWNLOADER

# Content Downloader installation

and SAVE it. You can use Https for secure file transmissions.

# Summary

# Connection Details

This page allows you to configure a description to help identify your Content Downloader client as well as modify your web services credentials and proxy settings (if applicable). You can also test connectivity to our servers using the TEST CONNECTION button.

| Hostname:                                          | Win2012-Testserver                 |
| -------------------------------------------------- | ---------------------------------- |
| IP Address:                                        |                                    |
| Os Name:                                           | x86 Windows NT (unknown)           |
| Java Version:                                      | Sun Microsystems Inc. 1.6.0 18-b07 |
| \* Reuters Connect Content Downloader Description: |                                    |
| \*Login:                                           |                                    |
| \* Password:                                       | •                                  |
| Proxy URL:                                         |                                    |
| Proxy Username:                                    |                                    |
| Proxy Password:                                    |                                    |
| Use Https:                                         |                                    |

* are mandatory fields

SAVE TEST CONNECTION

# Test Connection

OPTIONAL: After the connection details information has been saved click on TEST CONNECTION button to verify that Content Downloader is able to connect to Reuters Content servers. The following information should show up:

This ensures the Reuters Connect Content Downloader is able to connect to the Internet to download your Reuters subscriptions. You will need to fix any reported issues before content will start to be downloaded.

- Reuters Connect Content Downloader was able to connect to Reuters Content Web Services.
- Web Services Login and Password were accepted.
- Reuters Connect Content Downloader was able to connect to contentdownloader.reuters.com.

CLOSE

Reuters Connect Content Downloader - Installation and User Guide
Document Version : 9.0



# 15.

If the Test Connection results into green check marks, then click on CLOSE and SAVE again. Your Connection Details and the following confirmation will show up:

# Connection Details

This ensures the Reuters Connect Content Downloader is able to connect to the Internet to download your Reuters subscriptions. You will need to fix any reported issues before content will start to be downloaded.

- Reuters Connect Content Downloader was able to connect to Reuters Content Web Services.
- Web Services Login and Password were accepted.
- Connection settings were updated.

CLOSE

# 16.

Your Content Downloader is now set and ready to be used.

# 17.

Go to Chapter 4 to continue configuring your Reuters Content Downloader installation.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0




# 2.2.3. Linux

Note:

- To install application from the Installation Wizard in a GUI-based Linux, refer to the section Installing Application from Installation Wizard.
- To install application in a non-GUI Linux, refer to the section Installing in a non-GUI Linux.

# Installing Application from Installation Wizard

1. Download the installer as explained in the section 2.2.1
2. To install the application from Installation Wizard:
1. Make the file executable using:
chmod u+x cdt-client-*.*.*-linux_x64.sh
or
chmod u+x cdt-client-*.*.*-linux_x32.sh
2. Execute the shell script:
sudo ./cdt-client-*.*.*-linux_x64.sh
or
sudo ./cdt-client-*.*.*-linux_x32.sh
3. On the Welcome screen that appears, click Next

Setup - Reuters Content Downloader 4.4.28

Welcome to the Reuters Content Downloader Setup Wizard

This will install Reuters Content Downloader on your computer. The wizard will lead you step by step through the installation.

Click Next to continue, or Cancel to exit Setup.

Next>  Cancel

Reuters Connect Content Downloader - Installation and User Guide    15

Document Version : 9.0






Setup - Reuters Content Downloader 4.4.28

# License Agreement

Please read the following important information before continuing.

Please read the following License Agreement. You must accept the terms of this agreement before continuing with the installation.

[Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"). to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

I accept the agreement

I do not accept the agreement

install4j

&#x3C; Back
Next >
Cancel

Scroll down the page to read the entire agreement terms and choose 'I accept the agreement'. Then click Next.

# 4. On the Select Destination Directory screen, select a location to install the application and click Next.

By default, it will be installed in /usr/local/Reuters/ContentDownloader4.

# Select Destination Directory

Where should Reuters Content Downloader be installed?

Select the folder where you would like Reuters Content Downloader to be installed, then click Next.

/usr/local/Reuters/ContentDownloader4 Browse ...

Required disk space: 419 MB

install4j

&#x3C; Back
Next >
Cancel

Reuters Connect Content Downloader - Installation and User Guide    16

Document Version : 9.0





Setup - Reuters Content Downloader 4.4.28

# 5.

Enter a port number to access the Local Content Downloader and click Next. You can use any free port number here. Default value is 8080. If you need to change the value later, it can be edited in <installation directory="">/conf/client.properties file.</installation>

# Local Web Server Configuration

During this installation a local web server will be installed to allow easy LAN access to configure and view Reuters Content Downloader files.

Please specify the port to run the web server on. The default Port Number is 8080.

Local Web Server Port Number 8080

install4j




# Reuters Connect Content Downloader - Installation and User Guide

# 7. Once the application has been installed, you will see the below screen. Click on Finish.

# Setup - Reuters Content Downloader 4.4.28

Completing the Reuters Content Downloader Setup Wizard

Setup has finished installing Reuters Content Downloader on your computer. The application may be launched by executing the installed start scripts. Click Finish to exit Setup.

# Start the Reuters Content Downloader Service

Open browser and start configuring the client

Finish

After completing the previous step, Reuters Content Downloader service will start automatically by default and Configuration Page will start up (jump to step 8 if configuration page starts up properly). If the Configuration Page won’t start up; then an alternative way to start up Content Downloader configuration page is running the command sh open_config.sh as shown in the following steps:

1. Open GUI-based Linux Terminal and go to the location where the Content Downloader has been installed and check if files exist:
File Edit View   Search Terminal   Help
Stopped Reuters ContentDownloader.
tania@tania-VirtualBox:/usr/local/Reuters/ContentDownloader3$ ls
AppCommand          OldCdt.sh         lib
AppCommand.sh       logs              wrapper-linux-390-32
cdt                 makeconfig.sh     wrapper-linux-390-64
cdt_bg_updater      open_config.sh    wrapper-linux-ppc-32
cdt-engine-4.1.0.jar removeservice.sh  wrapper-linux-ppc-64
cdt_updater         setupservice.sh    wrapper-linux-x86-32
conf                Uninstall         wrapper-linux-x86-64
jre                 Content Downloader Tool
jsp                 updater_console_start.sh
updater_start.sh

2. To start/stop/restart Reuters Content Downloader Service type:
- sh AppCommand.sh start (to start the service)
- sh AppCommand.sh stop (to stop the service)
- sh AppCommand.sh restart (to restart the service)
3. Once the service has been started open the configuration page and type:
- sh open_config.sh
4. After entering all details in the configuration page, click Finish to complete the installation process.
5. Execute the setupservice.sh located in the Content Downloader application folder as root to complete the installation and to ensure the application automatically starts after system reboot. Example: sudo ./setupservice.sh

Document Version : 9.0






# Reuters Connect Content Downloader - Installation and User Guide

If Content Downloader has been installed correctly; you will be redirected to Local Server URL login page: http://localhost:8080/summary.do and for RCD 4.4.48 or above the local server is https://localhost:8080/summary.do and the following page appears:

Click on Sign In as shown below:

| REUTERS CONTENT DOWNLOADER | Reuters Connect | Reuters Liaison | Help | Sign In |
| -------------------------- | --------------- | --------------- | ---- | ------- |

# Summary

Status: ACTIVE v4.4.28

# Summary

This page gives a real time view of content recently downloaded. Click the news feed name to get a full list of the last 30 files received.

And login with your Reuters Content Downloader credentials:

https:/localhost:8080/login.action

# REUTERS CONTENT DOWNLOADER

# Summary

# Sign In

To access the configuration features of the Reuters Content Downloader.

Please enter your Reuters Connect credentials below:

| LOGIN:    |   |
| --------- | - |
| PASSWORD: |   |

SIGN IN

Document Version : 9.0





# 9.

After login the application will ask for your Proxy information (if the application detected it), fill out with your Proxy information: URL, username and password and click on Test Connection. If you don’t use a Proxy, click on SIGN IN.

# REUTERS CONNECT CONTENT DOWNLOADER

# Summary

# Sign In

We were unable to contact the Reuters Web Services to authenticate your entered credentials. Please check your connectivity to the Internet or enter proxy details below.

| Proxy URL:      |   |
| --------------- | - |
| Proxy Username: |   |
| Proxy Password: |   |

SIGN IN TEST CONNECTION

# 10.

After Proxy connection has been tested; the Local Server will redirect you to Connection Details configuration page. Please enter a description name for your Content Downloader installation and SAVE it. You can use Https for secure file transmissions.

# REUTERS CONNECT CONTENT DOWNLOADER

RCCDv3.5_Win2012 Media Express Customer Zone My Account Help

# Summary

# Connection Details

This page allows you to configure a description to help identify your Content Downloader client as well as modify your web services credentials and proxy settings (if applicable). You can also test connectivity to our servers using the TEST CONNECTION button.

| Hostname:                                          | Win2012-Testserver                 |
| -------------------------------------------------- | ---------------------------------- |
| IP Address:                                        |                                    |
| Os Name:                                           | x86 Windows NT (unknown)           |
| Java Version:                                      | Sun Microsystems Inc. 1.6.0 18-b07 |
| \* Reuters Connect Content Downloader Description: |                                    |
| \*Login:                                           |                                    |
| \* Password:                                       | •                                  |
| Proxy URL:                                         |                                    |
| Proxy Username:                                    |                                    |
| Proxy Password:                                    |                                    |
| Use Https:                                         |                                    |

* are mandatory fields

SAVE TEST CONNECTION

# Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0





# 11. OPTIONAL!!

After the connection details information has been saved click on TEST CONNECTION button to verify that Content Downloader is able to connect with Reuters Content servers. The following information should show up:

# Test Connection

This ensures the Reuters Connect Content Downloader is able to connect to the Internet to download your Reuters subscriptions. You will need to fix any reported issues before content will start to be downloaded.

- Reuters Connect Content Downloader was able to connect to Reuters Content Web Services.
- Web Services Login and Password were accepted
- Reuters Connect Content Downloader was able to connect to contentdownloader.reuters.com

CLOSE

# 12.

If the Test Connection results display green check marks then click on CLOSE and SAVE again your Connection Details and the following confirmation will show up:

# Connection Details

This ensures the Reuters Connect Content Downloader is able to connect to the Internet to download your Reuters subscriptions. You will need to fix any reported issues before content will start to be downloaded.

- Reuters Connect Content Downloader was able to connect to Reuters Content Web Services.
- Web Services Login and Password were accepted.
- Connection settings were updated.

CLOSE

Your Content Downloader is now set and ready to be used.

# 13.

Go to chapter 4 to continue configuring your Content Downloader installation.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



Installing in a non-GUI Linux

Follow the steps below to install the application from command prompt in a non-GUI Linux.

1. Make the file executable using
chmod u+x cdt-client-x.x.x-linux_x64.sh
Or
chmod u+x cdt-client-x.x.x-linux_x32.sh
2. Execute the Linux shell script as root:
sudo ./cdt-client-x.x.x-linux_x64.sh -c
or
sudo ./cdt-client-x.x.x-linux_x32.sh -c
When prompted with the question for installing the application, click o or press Enter
[root@centos  chmod u+× cdt-client-4.1.0-linu×_×64.sh]
[root@centos  “]# sudo ./cdt-client-4.1.0-linu×_×64.sh -c
Unpacking JRE

Starting Installer

This will install Reuters Connect Content Downloader on your computer.

DK [o, Enter] Cancel
3. The License Agreement screen appears. Read it and click 1 to accept the agreement.
THE SOFTWARE . PROUIDED AS S JITHOUT WARRANTY UF ANY KIND EXPRESS OR THE CHANTAR r ILITY shaL. THI BE TE DAMAGES OR OTHER WHETHER AN ON IF ISE ARISING THER DEAL ING THE
4. Enter the location to install the application, for example, Home/opt/Reuters/ContentDownloader3
5. During installation, a local web server will be installed to allow easy access to configure and view the Local Server files. Enter an appropriate value for the port number to access the local server and press Enter.
- Local Web Server Port Number - You can use any port number here.
- Default value is 8080. If you need to change the value later, it can be edited in <installation directory="">/conf/client.properties file. For example, if the local server port number is 8082; then within the file client.properties, modified as local.jetty.port=8082</installation>
- Go to the <installation directory="">/open_config file and change it there too (considering that you want to change the local port number to 8082. start https://localhost:8082/summary.action</installation>
6. Choose an output directory for downloading the content and press Enter. Note that the directory specified here must exist.

Reuters Connect Content Downloader - Installation and User Guide 22

Document Version : 9.0




furnished to do so, subject to the following conditions

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software

THE SOFTWARE IS PROVIDED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

I accept the agreement

Yes[1], No [2]

1

# Where should Reuters Connect Content Downloader be installed?

[/opt/Reuters/ContentDownloader3]

During this installation a local web server will be installed to allow easy LAN access to configure and view Reuters Connect Content Downloader files

Please specify the port to run the web server on The default Port Number is 8080

# Local Web Server Port Number

[8080]

# 7. Choose y to start the service after installation.

Root output directory

temp

Extracting files

Setup has finished installing Reuters Connect Content Downloader on your compute

Start the Reuters Content Downloader Service

Yes [y, Enter], No [n]

# 8. To complete the installation and to ensure the application automatically starts after system reboot:

it's necessary to execute the following commands:

1. Locate where the Content Downloader has been installed and check if files exist:

File Edit View Search Terminal Help

Stopped Reuters Content Downloader.

tania@tania-VirtualBox:/usr/local/Reuters/ContentDownloader3$ ls

- AppCommand
- AppCommand.sh
- OldCdt.sh
- lib
- logs
- wrapper-linux-390-32
- cdt
- make config.sh
- wrapper-linux-390-64
- cdt_bg_updater
- open_config.sh
- wrapper-linux-ppc-32
- cdt-engine-4.1.0.jar
- removeservice.sh
- wrapper-linux-ppc-64
- cdt_updater
- setupservice.sh
- wrapper-linux-x86-32
- conf
- Uninstall
- wrapper-linux-x86-64
- jre
- Content Downloader Tool
- jsp
- updater_console_start.sh
- updater_start.sh

• sh setupservice.sh (to ensure the application starts after system reboot)

• sh make_config.sh (to finish the installation)

Reuters Connect Content Downloader - Installation and User Guide 23

Document Version : 9.0






b.  If Reuters Content Downloader service won’t start, execute below commands:

- sh AppCommand.sh start (to start the service)
- sh AppCommand.sh stop (to stop the service)
- sh AppCommand.sh restart (to restart the service)

This completes the Content Downloader Service installation.

# 2.2.4. Mac OS

1. Download the installation file as explained in section 2.2.1.

Note:

- You should have administrative privileges to perform this installation.
- If the system you are working on does not have Java application installed, please install the Legacy Java SE 6 runtime: http://download.info.apple.com/Mac_OS_X/031-03190.20140529.Pp3r4/JavaForOSX2014-001.dmg
- Once you install it, you can proceed with the following steps.

Open the installer as shown below:

Downloads

| Favorites    | Name                                     | Date Modified     | Size       | Kind       |
| ------------ | ---------------------------------------- | ----------------- | ---------- | ---------- |
| Recents      | cdt-client-4.4.28-macos                  | Open              | 90.2 MB    | Disk Image |
| iCloud Drive | Open With                                | 104.5 MB          | Disk Image |            |
| Applications | Move to Trash                            |                   |            |            |
| Desktop      | Get Info                                 |                   |            |            |
| Documents    | Rename                                   |                   |            |            |
| Downloads    | Compress "cdt-client-4.4.28-macos.dmg"   | Duplicate         |            |            |
| Devices      | Make Alias                               |                   |            |            |
| Remote Disk  | Quick Look "cdt-client-4.4.28-macos.dmg" | Share             |            |            |
| Tags         | Copy "cdt-client-4.4.28-macos.dmg"       | Show View Options |            |            |
| Red          | Tags...                                  |                   |            |            |
| Orange       |                                          |                   |            |            |
| Yellow       |                                          |                   |            |            |

And double click over the Reuters Content Downloader installer as shown below:

https://trten.sharepoint.com/sites/TaniaViveroExternalSh

| Favorites    | Name                                 |
| ------------ | ------------------------------------ |
| Recents      | cdt-client-4.4.28-macos.dmg          |
| iCloud Drive | Reuters Content Downloader Installer |
| Applications |                                      |
| Desktop      |                                      |
| Documents    |                                      |
| Downloads    |                                      |
| Devices      |                                      |
| Remote Disk  |                                      |
| Tags         |                                      |
| Red          |                                      |
| Orange       |                                      |
| Yellow       |                                      |

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0






Setup - Reuters Content Downloader 4.4.28

# 4. The Welcome screen appears. Click Next.

Welcome to the Reuters Content Downloader Setup Wizard

This will install Reuters Content Downloader on your computer. The wizard will lead you step by step through the installation.

Click Next to continue, or Cancel to exit Setup.

Next > Cancel

# 5. The License Agreement screen appears.

License Agreement

Please read the following important information before continuing.

Please read the following License Agreement. You must accept the terms of this agreement before continuing with the installation.

of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

I accept the agreement

I do not accept the agreement

install4j

Next > Cancel

Scroll down the page to read the entire agreement terms and choose 'I accept the agreement'. Then click Next.

Reuters Connect Content Downloader - Installation and User Guide    25

Document Version : 9.0




# 6. Select Destination Directory

On the Select Destination Directory screen, select a location to install the application and click Next.

By default, it will be installed in /Reuters/ContentDownloader4.

# Setup - Reuters Content Downloader 4.4.28

# Select Destination Directory

Where should Reuters Content Downloader be installed?

Select the folder where you would like Reuters Content Downloader to be installed, then click Next.

/Applications/Reuters/ContentDownloader4 Browse ...

Required disk space: 237 MB

install4j

&#x3C; Back Next > Cancel

# 7. Local Web Server Configuration

A local web server will be installed to allow easy access to configure the Local Content Downloader and also to prevent unauthorized access to change the local configuration.

# Setup - Reuters Content Downloader 4.4.28

# Local Web Server Configuration

During this installation a local web server will be installed to allow easy LAN access to configure and view Reuters Content Downloader files.

Please specify the port to run the web server on. The default Port Number is 8080.

Local Web Server Port Number

install4j

&#x3C; Back Next > Cancel

Enter a port number to access the Local Content Downloader and click Next. You can use any port number here. Default value is 8080. If you need to change the value later, it can be edited in &#x3C;installation directory>/conf/client.properties file.

Reuters Connect Content Downloader - Installation and User Guide 26

Document Version : 9.0



# 8.

On the following screen, browse and choose the output directory for downloading the content and click Next.

# Setup - Reuters Content Downloader 4.4.28

Configure

Choose the root output directory for downloading media content

| Root output directory | Browse ... |
| --------------------- | ---------- |

install4j

&#x3C; Back  Next >  Cancel

# 9.

Once the application has been installed, you will get the below screen, make your selections, and click FINISH.

# Setup - Reuters Content Downloader 4.4.28

Completing the Reuters Content Downloader Setup Wizard

Setup has finished installing Reuters Content Downloader on your computer. The application may be launched by selecting the installed icons.

Click Finish to exit Setup.

Start the Reuters Content Downloader Service   >

Open browser and start configuring the client  √

Finish

Reuters Connect Content Downloader - Installation and User Guide    27

Document Version : 9.0




# 10.

Check 'Start the Reuters Content Downloader Service' if you would like the service to be started right after installation. The service can be started at a later point of time by invoking serviceAgent from the installation directory. Alternatively, you can also invoke the Content Downloader icon on the tool bar and then click Launch configuration page.

Finder            File Edit View          Go Window Help                                                       Mon 10:17  Q in
&#x3C;        I                                            Start Reuters Content Downloader           Downloader
Stop Reuters Content Downloader
Con     Open Reuters Content Downloader config page
II 101     88R                  Exit
Favorites                   Calendar                  ContentDownloader4           AppCommand_OldCdt.sh
Recents              Chess                                                  AppCommand.sh
Contacts                                               cdt
iCloud Drive         Dashboard                                              cdt_bg_updater
Applications         Dictionary                                             cdt_updater
Desktop              DVD Player                                             cdt-engine-4.4.28.jar
FaceTime                                               cdt.java.status
Documents            Font Book                                              cdt.pid
Downloads            Google Chrome                                          cdt.status
iBooks                                                 cont
Devices                     Image Capture                                          img
Remote Disc          iTunes                                                 jetty-temporary
Launchpad                                              lib
Install ma..         Mail                                                   logs
ReutersC..           Maps                                                   macsudowrapp.sh
Messages                                               outstore.pkcs12
Tags                         Mission Control                                       Reuters Co. rUninstalle
Red                  Notes                                                 service agent mac.sh
Photo Booth                                            struts.xmi
Orange               Photos                                                 updater_start_mac.sh
Yellow               Preview                                                webapp
QuickTime Player                                       wrapper-m...universal-32
Green                Reminders                                              wrapper-m...universal-64
Blue                 Reuters
Purple               Safari
Siri
Gray                 Stickies
All Tags...          System Preferences
TextEdit
Time Machine              11                    11                                 II

# 11.

Check 'Open browser and start configuring the client' if you would like to access the Local Content Downloader configuration page, right after installation. The Configuration page can be accessed at a later point of time by invoking the Content Downloader icon on the tool bar and then clicking Launch configuration page.

# 12.

Click Finish to complete the installation process.

# 13.

If you selected both the options in the previous screen, you will be directed to the Content Downloader home page to sign in and start the configuration process.

localhost           C                      d
REUTERS CONTENT DOWNLOADER                                                                       Reuters Connect  Routers Liaison  Help  Sign In
Summary                                                                                                                            Status: ACTIVE

Sign In
To access the configuration features of the Reuters Content Downloader.
Please enter your Reuters Connect credentials below:

LOGIN:
PASSWORD:

SIGN IN

# 14.

Go to Chapter 4 to continue configuring your Reuters Content Downloader installation.

Reuters Connect Content Downloader - Installation and User Guide    28

Document Version : 9.0





# 2.3 STARTING AND STOPPING THE APPLICATION

Once the application is installed, you can start, stop, check its status, and open the configuration page using the following options.

# 2.3.1 Windows

- To start / stop the service
Content Downloader will be started as a Windows service. Hence it will start when Windows starts. You can stop / restart the service by any of the following methods.

- From Windows Start menu
- To stop the service, invoke Start-->All Programs-->Reuters Content Downloader-->Stop Reuters Content Downloader Service.
- To start the services, invoke Start-->All Programs-->Reuters Content Downloader-->Start Reuters Content Downloader Service.
- From Services
- Go to Start-->Control Panel-->Administrative Tools-->Services
- Select Reuters Content Downloader and choose the links 'Stop the service' or 'Restart the service' to do the desired action.
- From Taskbar
- Right-click the Content Downloader icon on the Windows taskbar.
- Click Start Content Downloader / Stop Content Downloader / Launch Configuration Page to do the desired action.
- From Run Window
- Start > Run
- Type – services.msc
- Enter

Note: The default settings of User Access Control (UAC) in Windows 7 prevents making system-level changes without administrator privileges. Hence to stop the service in Windows 7, log in as an administrator.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0




# Reuters Connect Content Downloader - Installation and User Guide

# 2.3.2. Linux and Mac OS

Open a terminal and execute the script files with appropriate parameters as shown below to do the desired action. The script files can be found in the installation directory. The default installation directory will be /usr/local/Reuters/ContentDownloader4.

- To start the service: sh AppCommand.sh start
- To stop the Service: sh AppCommand.sh stop
- To restart the service: sh AppCommand.sh restart
- To view the status of the service: sh AppCommand.sh status
- To open the local configuration page: sh open_config.sh
- To complete the installation and to ensure the application automatically starts after system reboot: sh setupservice.sh and sh make_config.sh

Document Version: 9.0







# 2.4 UPGRADING TO LATEST RELEASES

# 2.4.1 Upgrading using installer from Reuters Liaison

The latest Reuters Content Downloader installer could be found on http://liaison.reuters.com/ or send an email to ReutersMediaSupport@thomsonreuters.com. Follow section steps provided in section 2.2.1 to download Reuters Content Downloader latest version.

Note: It is not necessary to uninstall an outdated Reuters Content Downloader version; you can simply update to the latest version. Existing settings will be adopted.

# 2.5 UNINSTALLING CONTENT DOWNLOADER

Follow the steps below for uninstalling the Content Downloader.

Note:

1. This will uninstall only the Content Downloader application. The configuration and any content already downloaded will not be removed. You can manually delete the content after uninstalling.
2. Before uninstalling Content Downloader remember to disable all Alert Messages that have been set previously, see section Configuring Alerts.

# 2.5.1 Windows

1. Launch the uninstaller in one of the following ways:
- Invoke Start-->All Programs-->Reuters Content Downloader and select Reuters Content Downloader Uninstaller
- Go to Control Panel-->Add or Remove Programs. Select Reuters Content Downloader and click Change/Remove button.
2. In the Uninstaller screen that appears, click Next.

Reuters Content Downloader 4.4.28 Uninstall

Are you sure you want to completely remove Reuters Content Downloader and all of its components? Click Next to continue, or Cancel to exit Setup.

Next Cancel

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0







# 3.

In the following screen that appears, click Finish to complete the uninstallation process.

Reuters Content Downloader 4.4.28 Uninstall

Reuters Content Downloader Uninstall

Reuters Content Downloader was successfully removed from your computer.

Finish

IMPORTANT!! After performing previous steps, Content Downloader application has been removed from your PC, but all media content (text/pictures/graphics/video) will remain; if you want to ELIMINATE all files delete folder C:\Program Files\Reuters; and all files and Content Downloader configuration/details will be removed from your PC.

# 2.5.2. Reinstalling Reuters Content Downloader

If you need to reinstall Reuters Content Downloader and Reuters folder still exists under C:\Program Files or installation folder; the new version will keep your latest connection details and configuration.

# 2.5.3. Linux

Note

- To uninstall application from the Installation Wizard in a GUI-based Linux, see section Uninstalling Application from Uninstall Wizard below.
- To uninstall application in a non-GUI Linux, see section Uninstalling in a non-GUI Linux.

# Uninstalling Application from Uninstall Wizard

1. From the directory where Content Downloader is installed, locate Uninstall Content Downloader Tool, and run it.
2. The Content Downloader uninstaller will be displayed. Click Next to uninstall.

Reuters Connect Content Downloader - Installation and User Guide 32

Document Version : 9.0





Reuters Content Downloader 4.4.28 Uninstall

# Uninstall

Are you sure you want to completely remove Reuters Content Downloader and all of its components?

Click Next to continue, or Cancel to exit Setup.

| Next > | Cancel |
| ------ | ------ |

# 3.

On the following screen, click Finish to exit the setup.

# Reuters Content Downloader 4.4.28 Uninstall

# Uninstall

Reuters Content Downloader was successfully removed from your computer.

Finish

# Uninstalling in a non-GUI Linux

Follow the steps below to uninstall the application from command prompt in a non-GUI Linux.

1. Run ‘Uninstall Content Downloader Tool -c’ from the installation folder as shown in the image below:
2. sudo ./Uninstall\ Reuters\ Content\ Downloader\ Tool -c
Enter y when prompted with the question ‘Are you sure you want to completely remove Reuters Content Downloader and all components?’ type y and hit ENTER to proceed.

[ubuntu@ubuntu:/usr/local/Reuters/ContentDownloader4$ sudo ./Uninstall\ Reuters\ Content\ Downloader\ Tool -C
Are you sure you want to completely remove Reuters Content Downloader and all of its components?
Yes[y, Enter], No [n]
Uninstalling Reuters Content Downloader 4.4.28
Reuters Content Downloader was successfully removed from your computer.
Finishing uninstallation
ubuntu@ubuntu:/usr/local/Reuters/ContentDownloader4$

Reuters Connect Content Downloader - Installation and User Guide 33
Document Version : 9.0



# 3.

Once uninstalled, you will get the message 'Reuters Content Downloader was successfully removed from your computer'.

# 2.5.4. Mac OS

1. From the directory where Content Downloader is installed, locate Reuters Content Downloader Uninstaller, and run it.
2. The Content Downloader uninstaller will be displayed. Click Next to uninstall.

Reuters Content Downloader 4.4.28 Uninstall

Reuters Content Downloader

Uninstall

Are you sure you want to completely remove Reuters Content Downloader and all of its components?

Click Next to continue, or Cancel to exit Setup.

Next > Cancel

On the following screen, click Finish to complete the uninstall process.

Reuters Content Downloader 4.4.28 Uninstall

Reuters Content Downloader

Uninstall

Reuters Content Downloader was successfully removed from your computer.

Finish

Reuters Connect Content Downloader - Installation and User Guide 34

Document Version : 9.0



# Chapter 3 CONFIGURATION GUIDELINES

# 3.1 QUICK START

This section summarizes the set-up and configuration steps for Content Downloader. More details can be found in the following chapters.

1. Start the Content Downloader service:
- Windows: Invoke Start-->All Programs-->Reuters Content Downloader-->Start Reuters Content Downloader Service
- Linux: Execute sh AppCommand.sh start
- Mac OS: Invoke ‘Start Content Downloader’ from the tool bar.
2. Open the Local web server configuration page:
- Windows: Invoke Start-->All Programs-->Reuters Content Downloader-->Open Configuration Page
- Linux: Execute sh open_config.sh
- Mac OS: Invoke ‘Launch configuration page’ from the MAC menu bar.
- Click Sign In at the top right corner of the page. Enter the Content Downloader credentials and click SIGN IN.
- Enter the following information in Connection Details:
- Reuters Content Downloader Description
- Proxy details (optional)
- Proxy Server details, if any, should follow the convention 'http://&#x3C;proxy server>:&#x3C;proxy port>'
- Use HTTPS if required.
- Click SAVE. If any issues are reported in the status message, correct them and click CLOSE.
3. Open the Storage tab.
- Configure the following as per your requirements.
- POLLING SETTINGS
- STORAGE PREFERENCES
- MODIFY DEFAULT OUTPUT FOLDERS
- Click SAVE.
- Note: Downloading of content begins in a few minutes after you selected the storage directory and click SAVE.
4. Open News Feeds tab
- Select the news feeds that should be downloaded by the client and click SAVE.
5. Go to Alerts tab
- Configure Alerts Message details here if you want to be notified about connection status, and click SAVE.
6. Go to Content Options tab

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0



Configuration

Select the file types that should be downloaded for each of the news feeds selected in step 4 and click SAVE.

Note: Any changes made in the Text, Pictures, Graphics and Online Video sections will also impact the delivery of Online Reports and Multimedia, when permissioned.

# 3.2 LOGGING INTO REUTERS CONNECT AND VALIDATING CONTENT DELIVERY

In order to validate you are receiving all of your subscribed content, accessing Reuters Connect to compare downloaded content against our Reuters Connect platform database can be useful. Once logged into Reuters Connect, all the content you subscribe to is displayed. In order to validate content against Content Downloader, select a Source News Feed you would like to compare by:

1. Selecting the link within a story.

For example, select a story and look into Source News Feeds line which contains the name of the feeds that your account is permissioned for:

| Date:               | 18/04/2022 16:15                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Dimensions:         | 8192 x 5464                                                                                                                                                        |
| Size:               | 9.9MB                                                                                                                                                              |
| Category:           | S                                                                                                                                                                  |
| Topic Codes:        | SPO US                                                                                                                                                             |
| Fixture Identifier: | MT1USATODAY18109837                                                                                                                                                |
| Byline:             | Paul Rutherford                                                                                                                                                    |
| City:               | Boston                                                                                                                                                             |
| Country Name:       | United States                                                                                                                                                      |
| Country Code:       | USA                                                                                                                                                                |
| OTR:                | IMAGN-486580                                                                                                                                                       |
| Credit:             | USA TODAY Sports                                                                                                                                                   |
| Source:             | USA TODAY Sports                                                                                                                                                   |
| Source News Feeds:  | Reuters Marketplace - USA Today Pictures, Reuters News Picture Service - RNPS, Reuters Online Global Pictures, Reuters Sports Picture Service - RSPS, US Presswire |
| USN:                | MT1USATODAY18109837                                                                                                                                                |

Then click over your username in Reuters Connect web site, then click over Settings, scroll down, and look for Feed Settings. Note: Reuters Connect will show up the list of all the news received in selected channel for the last 30 days.

# Feed Settings

| MARKETPLACE     | ARCHIVE 360 | ARCHIVE PICTURE | ARCHIVE VIDEO | GRAPHICS | LIVE VIDEO | MULTIMEDIA |
| --------------- | ----------- | --------------- | ------------- | -------- | ---------- | ---------- |
| All Marketplace |             |                 |               |          |            |            |

Filter your channels selecting which News Feeds you want to validate and deselect all others. This will give you a selection of desired channels.

Reuters Connect Content Downloader - Installation and User Guide 36

Document Version : 9.0



Configuration
# Chapter 4 CONFIGURATION

# 4.1.1.Configuring Download Settings

Once you are logged in to Reuters Content Downloader configuration page, click the Storage tab to configure the download options.

# REUTERS CONTENT DOWNLOADER

- Summary
- Connection Details
- Storage
- News Feeds
- Alerts
- Content Options
- Manual Download

# Storage

This page allows you to make changes to the folder where the Reuters Content Downloader will save files on your local or network filesystem. Please ensure the Reuters Content Downloader has valid permissions to write to this location.

# POLLING SETTINGS

Period to wait after checking: 15 Seconds

Period window to search back: 8 Hours

# STORAGE PREFERENCES

Root Output Directory: C:\ReutersIN

WARNING - Ensure the directory exists on the target machine.

Sub Directories:

- O Use News Feed Name
- O None

# MODIFY DEFAULT OUTPUT FOLDERS

This section allows you to overwrite the default download locations for each news feed. The first option in each category allows you to choose a single output folder to download all the news feeds listed below.

Filter by: Text, Pictures, Graphics, Online Video, Online Reports

| All Text News Feeds                   | C:/ReutersIN/                                      |
| ------------------------------------- | -------------------------------------------------- |
| Reuters World Service                 | C:/ReutersIN/Reuters World Service                 |
| Spanish Domestic News Service         | C:/ReutersIN/Spanish Domestic News Service         |
| Spanish Language General News Service | C:/ReutersIN/Spanish Language General News Service |
| Spanish Soccer Channel                | C:/ReutersIN/Spanish Soccer Channel                |

To edit the default location tick the relevant checkbox

SAVE
# POLLING SETTINGS

The Hosted Server will be polled periodically to check for new content. The following two parameters can be configured to customize the polling process.

PERIOD TO WAIT AFTER CHECKING: This denotes the sleeping period between every polling cycle. By default, it is set to 15 seconds. So once a polling cycle is done, the scheduler will wait for 15 seconds before resuming polling again. You can choose a different value from the drop-down menu.

Possible values are: 15 seconds, 30 seconds, 1 minute and 5 minutes.

Reuters Connect Content Downloader - Installation and User Guide 37

Document Version : 9.0





Configuration

# PERIOD WINDOW TO SEARCH BACK

This denotes the window of time to consider for searching new content. By default, it is set to 8 hours. This means that the last 8 hours of data will be polled for updates. If the Content Downloader has not been running for some time and the outage period is greater than your search back period, increase this window by using the drop-down menu or use the Manual Download option to download the missed content. Possible values are: 2 Hours, 3 Hours, 4 Hours, 8 Hours, 16 Hours and 1 day. Default value is 8 hours.

# STORAGE PREFERENCES

Root Output Directory - This specifies the directory where the contents should be downloaded. By default, this will take the value given during installation. You can however edit this value and update it. Note that the absolute path of the directory should be given. For example, “C:/ReutersIN”.

Note: The directory you specify here must exist.

Sub Directories - You can choose to categorize and organize the content from different channels by downloading them into different sub-directories.

- Use News Feed Name - Choose this if you want to create a sub directory with the same name as the news feed. All the content will then be downloaded to this location. Example: For Reuters World Service, the related content will be downloaded under C:/ReutersIN/Reuters World Service
- None - Choose this if don’t wish to create a subdirectory. All the content will be downloaded directly into the top-level directory. Example, C:/ReutersIN.

Note: If the same file is present in two different channels (for example, a picture file in 'UK Picture Service' and 'Sports Picture Service'), it will be downloaded only once if both the channels are configured to be stored in the same directory. If the configuration is set to download them in different directories (default configuration), the content will be downloaded and stored in both the directories.

If you need to store data on a network drive; map the network path as follow: \\servername\sharefolder

# MODIFY DEFAULT OUTPUT FOLDERS

If you want to change the root output directory or sub-directories for any of the news feeds set in the previous step, you can do so here. For example, for PICTURES, if you want the content belonging to “Reuters News Picture Service” to be stored in C:/ReutersIN/RNPS instead of the default C:/ReutersIN/Reuters News Picture Service - RNPS, you can configure it by following the steps below.

Reuters Connect Content Downloader - Installation and User Guide    38

Document Version : 9.0



Configuration

# MODIFY DEFAULT OUTPUT FOLDERS

This section allows you to overwrite the default download locations for each news feed. The first option in each category allows you to choose a single output folder to download all the news feeds listed below.

# Filter by:

- Text
- Pictures
- Graphics
- Online Video
- Online Reports

# All Pictures News Feeds

| France Soccer Pictures              | C:/ReutersIN/France Soccer Pictures     |
| ----------------------------------- | --------------------------------------- |
| Germany Soccer Pictures             | C:/ReutersIN/Germany Soccer Pictures    |
| Italy Soccer Pictures               | C:/ReutersIN/Italy Soccer Pictures      |
| ROVR and ACIOVR Overs feed          | C:/ReutersIN/ROVR and ACIOVR Overs feed |
| Reuters News Picture Service - RNPS | C:/ReutersIN/RNPS                       |

To edit the default location tick the relevant checkbox.

# SAVE

- Select the channel category. E.g. Pictures.
- Select the news feed for which you want to change the output directory. This allows editing the text box.
- Rename the storage path, e.g. C:/ReutersIN/RNPS. If this folder name does not exist, it will be created.
- Click SAVE button on the bottom of the screen to save the changes. You will get an ‘Update success’ message if your configuration was successful.

All the pictures from the “Reuters News Picture Service – RNPS” feed will now be stored in C:/ReutersIN/RNPS.

Note: Downloading of content begins in a few minutes after you choose a folder for storage and click the SAVE button.

Reuters Connect Content Downloader - Installation and User Guide    39
Document Version : 9.0



# Configuration

# 4.1.2. Configuring News Feeds

You can choose the news feeds to be downloaded.

# REUTERS CONTENT DOWNLOADER

Summary  Connection Details  Storage  News Feeds  Alerts  Content Options  Manual Download

# News Feeds

This page allows you to select which news feeds or category should be downloaded by the client. Only news feeds with a tick will be downloaded by the client - this is useful if you want to stop receiving a specific news feed.

Filter by: ALL  Text  Pictures  Graphics  Online Video  Online Reports

# All feeds

# All Text feeds

| NEWS FEED                             | NEWS FEED                     |
| ------------------------------------- | ----------------------------- |
| Reuters World Service                 | Spanish Domestic News Service |
| Spanish Language General News Service | Spanish Soccer Channel        |

• Select a channel category.

• Check the news feeds that you would like to download.

• Click SAVE.

This will download the news feeds from the channels that you have selected. Choosing 'All Feeds' option will download all news feeds across all channels. You will get an ‘Update success’ message if your configuration was successful.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



Configuration

# 4.1.3. Configuring Alerts

You can enable an email alert to be sent to you if the local web server has not contacted the hosted server for a period of 30 minutes.

# REUTERS CONTENT DOWNLOADER

| Summary | Connection Details | Storage | News Feeds | Alerts | Content Options | Manual Download |
| ------- | ------------------ | ------- | ---------- | ------ | --------------- | --------------- |

# Alert Message

This page allows you to enable an email alert to be sent if we do not receive a request from your Reuters Content Downloader client within 30 minutes.

Send Connection Alert: OOn Ooff

Administrator's Email Address:

Email Subject: Reuters Content Downloader Connection Failure for test-user

Email Body Text: The Reuters Content Downloader Client test-user has not contacted our servers recently. Please check that your Reuters Content Downloader client is functioning correctly. This message has been generated as your server has not checked in to Reuters for 10 minutes. This message will repeat every 15 minutes for up to 2 hours. Your server specific client details, username, and IP address can be found below:

SAVE
TEST EMAIL ALERT

# Go to Alerts tab and configure the Alert details as follows:

| Field                         | Description                                                                                                                                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Send Connection Alert         | On - Choose On if you need to be notified in case of a connection failure. Off - Choose Off if you do not wish to be notified.                                                                                                                     |
| Administrator’s Email Address | A valid email address where the notification should be sent.                                                                                                                                                                                       |
| Email Subject                 | The default value will be 'Reuters Content Downloader Connection Failure for \<Content Downloader Username>'. You can edit this field to give a different subject to the mail.                                                                     |
| Email Body Text               | The default value will be "The Reuters Content Downloader Client \<Content Downloader Username> has not contacted our servers recently. Please check that your client is functioning correctly". You can edit this value to give a custom message. |

Click TEST EMAIL ALERT button to check the validity of the email address entered.

Click SAVE to save the values to the hosted server.

Reuters Connect Content Downloader - Installation and User Guide    41
Document Version : 9.0



Configuration

Note:

- If you are getting Alert Notification emails for inactive Content Downloader clients, you can disable them as follows:
- - Log in to the hosted server: https://contentdownloader.reuters.com/cdt-server/ and from the top right corner drop-down list, choose the account that should be turned off for notifications.
- Go to Alerts page and choose 'Off' for Send Connection Alert. Click SAVE.

If you are getting Alert Notification emails for clients whose installations have been deleted, contact the Help Desk for support.

# 4.1.4. Configuring File Types to Download

If you want to download only certain types of files within a channel category, you can do so by configuring the Content Options.

# 4.1.4.1. For text

The only option available for text files is XML:

# REUTERS CONNECT CONTENT DOWNLOADER

Tania_v4.1.0

# Summary

Connection Details

Storage

News Feeds

Alerts

Content Options

Manual Download

# Content Options

Please choose file types you would like to receive in Text | Pictures | Graphics | Online Video filter.

Filter by: Text  Pictures

Grphics Onlne Vio

IOnlne Report

Please choose file types you would like to receive:

- xML

Any changes made in this section will also impact the delivery of Online Reports or Multimedia, when permissioned.

SAVE

Reuters Connect Content Downloader - Installation and User Guide    42

Document Version : 9.0



Configuration

# 4.1.4.2. For Pictures

For Pictures, you can choose different types of resolutions; check desired formats and click on SAVE.

# Resolutions:

- Small JPEG: 150 pixels (Pictures &#x26; Online Reports)
- Medium JPEG: 640 pixels (Pictures) and 450 pixels (Online Reports)
- Limited JPEG: 3500 pixels* (Pictures Only) * Only available in Content Downloader v4.2.40 and above
- Base JPEG: Highest quality resolution (Pictures) 800 pixels (Online Reports)
- Filed JPEG: Highest quality resolution (Online Reports only)*
- XML

# REUTERS CONNECT CONTENT DOWNLOADER

# Summary

# Connection Details

# Storage

# News Feeds

# Alerts

# Content Options

# Manual Download

# Content Options

Please choose the required file size(s) and type you would like to receive in Text | Pictures | Graphics | Online Video filter.

Filter by: Text | Pictures | Online Video | Online Reports

Please choose file types you would like to receive:

- Small JPEG: 150 pixels (Pictures &#x26; Online Reports)
- Medium JPEG: 640 pixels (Pictures) 450 pixels (Online Reports)
- Limited JPEG: 3500 pixels (Pictures only)* Only available in Content Downloader v4.2.40 and above
- Base JPEG: Highest quality resolution (Pictures) 800 pixels (Online Reports)
- Filed JPEG: Highest quality resolution (Online Reports only)*
- XML

Any changes made in this section will also impact the delivery of Online Reports or Multimedia, when permissioned.

NOTE: JPEG pixel size measured on the longest edge

* If selected file size is unavailable, Base JPEG will be downloaded by default

NOTE: * If selected file size is unavailable, Base JPEG will be downloaded by default.

Above statement refers in the cases in which some of our third-party images providers don’t provide content resized to the Limited rendition. Additionally, Online Reports do not always offer the highest quality resolution too, therefore, in those cases the default picture - Base JPEG – will be downloaded.

Reuters Connect Content Downloader - Installation and User Guide    43
Document Version : 9.0




# Configuration

# 4.1.4.3. For Graphics

For Graphics, you can choose:

- Thumbnail resolution JPEG Image
- View resolution JPEG Image
- EPS File
- ZIP File
- XML

# REUTERS CONNECT CONTENT DOWNLOADER

# Summary

# Connection Details

# Storage

# News Feeds

# Alerts

# Content Options

Content Options

Please choose file types you would like to receive in Text | Pictures | Graphics | Online Video filter.

Filter by: Text I Pictures I Graphics I Online Video | Online Reports

Please choose file types you would like to receive:

- √ Thumbnail resolution JPEG Image
- View resolution JPEG Image
- √ EPS File
- ZIP File
- XML

Any changes made in this section will also impact the delivery of Online Reports or Multimedia, when permissioned.

# 4.1.4.4. For Online Video

For Online video, choose the file types you would like to receive and then click on SAVE

- MPEG 4 HD 1080 - 1920x1080 (Split Audio)
- MPEG 4 HD 1080 - 1920x1080 (Mixed Audio)
- MPEG 4 HD 720 - 1280x720
- MPEG 4 300 - 384x216 frame size
- MPEG 4 700 - 576x324 frame size
- MPEG-4 2000 - 768x432 frame size
- MPEG2 Broadcast Quality - 720x576 frame size
- Flash 300 - 384x216 frame size
- Flash 512 - 512x288 frame size
- Flash 700 - 576x324 frame size
- 3GPP2 80 KDDI - 176x144 frame size
- 3GPP 80 Docomo - 176x144 frame size
- Thumbnail - 160x90 Image
- View Image - 512x288 Image
- Base Image - 960x540 Image
- MP3 - Audio Only
- XML
- Advisories

Reuters Connect Content Downloader - Installation and User Guide 44

Document Version : 9.0





Configuration
# REUTERS CONNECT CONTENT DOWNLOADER

# Content Options

Please choose the required file size(s) and type you would like to receive in Text | Pictures | Graphics | Online Video filter.

Filter by: Text  Pictures  Graphics I Online Video

Please choose file types you would like to receive:

| MPEG 4 HD 1080 - 1920x1080 (Split Audio)     | JMPEG 4 HD 1080 - 1920x1080 (Mixed Audio) |
| -------------------------------------------- | ----------------------------------------- |
| MPEG 4 HD 720 - 1280x720                     | MPEG 4 300 - 384x216 frame size           |
| MPEG 4 700 - 576x324 frame size              | MPEG-4 2000 - 768x432 frame size          |
| MPEG2 Broadcast Quality - 720x576 frame size | Flash 300 - 384x216 frame size            |
| Flash 512 - 512x288 frame size               | Flash 700 - 576x324 frame size            |
| 3GPP2 80 KDDI - 176x144 frame size           | 3GPP 80 Docomo - 176x144 frame size       |
| Thumbnail - 160x90 Image                     | View Image - 512x288 Image                |
| Base Image - 960x540 Image                   | ) MP3 - Audio Only                        |
| XML                                          | Advisories                                |

Any changes made in this section will also impact the delivery of Online Reports or Multimedia, when permissioned.

# For Online Reports

For Online Reports, choose the report type you want to receive and then click on SAVE.

# REUTERS CONNECT CONTENT DOWNLOADER

# Content Options

Please choose file types you would like to receive in Text | Pictures | Graphics | Online Video filter.

Filter by: Text  Pictures I Graphicsᴵ Online Video|Online Reports

Please choose report types you would like to receive:

- Download Everything (linklist, packages, items)
- Download Packages (packages, items)
- Download Items Only
- Download Summaries

The rendition options for Pictures, Graphics and Online Video within Online Reports can be modified via the appropriate tab.

SAVE
Reuters Connect Content Downloader - Installation and User Guide    45
Document Version : 9.0



# Configuration

Note:

- Any changes made to the Pictures, Graphics and Online Video sections will also impact the content delivered in Online Reports.
- For example, if the user wants to get only XMLs in their Online Reports packages, it should be selected in the “Pictures” tab.
- It is not possible to uncheck the XML option for Text and Online Video.
- Changes made to the content options after a Manual Download is started will take effect after 5-10 minutes of delay.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



Configuration

# 4.1.5. Downloading Older Content

If the Content Downloader has not been running for some time and the outage period is greater than your search back period (which is by default, 8 hours), you can use the Manual Download option to download the missed content. You can also use this feature to download archived content following your first login.

# REUTERS CONTENT DOWNLOADER

| Summary | Connection Details | Storage | News Feeds | Alerts | Content Options | Manual Download |
| ------- | ------------------ | ------- | ---------- | ------ | --------------- | --------------- |

# Manual Download

This page allows you to download archived Reuters content from a specific time period. Please choose the required news feeds below then define the time period to retrieve content.

Filter by: ALL Text itre phics Online Video

All feeds

All Text feeds

| NEWS FEED                             | NEWS FEED                     |
| ------------------------------------- | ----------------------------- |
| Reuters World Service                 | Spanish Domestic News Service |
| Spanish Language General News Service | − Spanish Soccer Channel      |

Start Date (UTC): 15 Apr 2022 12:00

End Date (UTC): 18 Apr 2022 12:00

Maximum number of items: 1000

NEXT >

You can download content as old as four days back by following the steps below:

1. Choose a specific channel category or ALL
2. Choose the Channel(s) you want to download
3. Choose Start Date (UTC) and End Date (UTC) with timings from the drop-down menu. You can choose up to 4 days back.
4. Choose a value for Maximum number of items from the drop-down menu and click NEXT. An item is a story and all its associated files. The value here denotes the maximum number of items per channel that will be downloaded. The maximum number of items allowed per channel is 1000.
5. The Confirm Manual Download page will appear. This will give you a summary of the options you chose in the previous step.

Reuters Connect Content Downloader - Installation and User Guide 47

Document Version: 9.0




Configuration

# REUTERS CONTENT DOWNLOADER

# Summary

# Connection Details

# Storage

# News Feeds

# Alerts

# Content Options

# Manual Download

# Confirm Manual Download

Following news feeds will be sent to manual download queue once you click Download button:

It will take normally 10-15 minutes for the queue to start.

Selected News Feeds: Reuters World Service

Date Range (UTC): 18 Apr 03:00:00 - 18 Apr 12:00:00

Maximum item numbers: 1000 Items

Send an email to the following comma separated email address(es) when the download has completed:

&#x3C;BACK QUEUE DOWNLOAD

1. If you want to get notified when the download has completed,
2. 1. Check 'Send an email to the following comma separated email address(es) when the download has been completed:'
2. If you checked the above step, enter valid email addresses as comma separated values.

Click QUEUE DOWNLOAD
3. A 'Success' message will be displayed in the local server under Summary tab indicating successful scheduling of the manual download.
4. Important!! The Manual Download might take some minutes to register and download desired content.
5. After the manual download begins, you will get another message to notify you of the request for the manual download with details as shown below. This will take a few minutes to appear.

# REUTERS CONTENT DOWNLOADER

# Summary

# Connection Details

# Storage

# News Feeds

# Alerts

# Content Options

# Manual Download

# Summary

This page gives a real time view of content recently downloaded. Click the news feed name to get a full list of the last 30 files received.

Success: Your manual download has been scheduled successfully.

# MANUAL DOWNLOAD

A Manual Download Request was received at 12:55 +00:00 18.04.2022

Selected Channels: Reuters World Service Not started

Date Range: 03:00 18.04.2022 - 12:00 18.04.2022

Maximum number of items: 1000 items per channel

# STOP MANUAL DOWNLOAD

This message contains a STOP MANUAL DOWNLOAD button. You can click this if you want to abort the manual downloading process.

Reuters Connect Content Downloader - Installation and User Guide 48

Document Version : 9.0





# Configuration

11. If email notification was selected in step 6a, you will get an email from ContentDownloader@thomsonreuters.com with the subject 'The manual download for the Reuters Content Downloader Client - <content downloader="" description="" name=""> has completed.' once the manual download is completed.</content>

12. You can view the downloaded content in the same location as the rest of the files. (See Storage Preferences for more details.)

Identify content items that are older than the current day by the date in their name rather than the received date.

| 2022-04-18T090729Z | 2046820405 | L2N2WG0BO        | RTRMADT | 0 | SOUTHKOREA-USA-NORTHKO..         | 4/18/2022 11:55 | XML Doc |
| ------------------ | ---------- | ---------------- | ------- | - | -------------------------------- | --------------- | ------- |
| 2022-04-18T090833Z | 681866918  | R4N2W201N        | RTRMADT | 0 | UKRAINE-CRISIS-RUSSIA-NABIU..    | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T091052Z | 413771004  | S6N2TX005        | RTRMADT | 0 | SOUTHKOREA-USA-NORTHKORE..       | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T092517Z | 1403672563 | L2N2WG0C7        | RTRMADT | 0 | HEALTH-CORONAVIRUS-INDI..        | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T 2528Z  | 989005995  | L5N2WG0ON        | RTRMADT | 0 | UKRAINE-CRISIS-SUMY-DEFEN.       | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T093013Z | 557423888  | L2N2WG0CK        | RTRMADT | 0 | SOCCER-ITALY.XML                 | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T094000Z | 1809578682 | MT1ALTR4N2W201R3 | RTRMADT | 0 | KREMLIN-SAYS-UKRA..              | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T094001Z | 724716657  | MT1ALTR4N2W201S2 | RTRMADT | 0 | KREMLIN-SAYS-THERE-..            | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T094002Z | 930249549  | MT1ALTR4N2W201R4 | RTRMADT | 0 | KREMLIN-SAYS-TREND...            | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T094615Z | 8          | MTZXEI4HHQXV5D   | RTRFIPT | 0 | SOCCER-BRAZIL-SUMMARIES-UPD...   | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T094631Z | 349932698  | L2N2WG0BO        | RTRMADT | 0 | SOUTHKOREA-USA-NORTHKOR..        | 4/18/2022 11:55 | XML Doc |
| 2022-04-18T094916Z | 3          | MTZXEI4HHE7KR7   | RTRFIPT | 0 | SOCCER-JAPAN-RESULTS-UPDATE-3... | 4/18/2022 11:55 | XML Doc |

13. Depending on the subscriptions, different types of content are available, the file name has identifiers for each type of content as shown below:

For text files the identifier is T; for pictures is P, for graphics is G, for Audio files is A, for video is V, for Linked list is C.

| 2022-04-18T093013Z | 557423888  | L2N2WG0CK        | RTRMADT | 0 | SOCCER-ITALY.XML               | 4/18/2022 11:55 |
| ------------------ | ---------- | ---------------- | ------- | - | ------------------------------ | --------------- |
| 2022-04-18T094000Z | 1809578682 | MT1ALTR4N2W201R  | RTRMADT | 0 | KREMLIN-SAYS-UKRA...           | 4/18/2022 11:55 |
| 2022-04-18T094001Z | 724716657  | MT1ALTR4N2W201S2 | RTRMADT | 0 | KREMLIN-SAYS-THERE-…           | 4/18/2022 11:55 |
| 2022-04-18T094002Z | 930249549  | MT1ALTR4N2W201R4 | RTRMADT | 0 | KREMLIN-SAYS-TREND...          | 4/18/2022 11:55 |
| 2022-04-18T094615Z | 8          | MTZXEI4HHQXV5D   | RTRFIPT | 0 | SOCCER-BRAZIL-SUMMARIES-UPD... | 4/18/2022 11:55 |

Category Identification

| RTRMADT | Text                    |
| ------- | ----------------------- |
| RTRMADP | Picture                 |
| RTRMADG | Graphics                |
| RTRMADA | Audio                   |
| RTRMADV | Online Video            |
| RTRMADC | Composite - Linked List |

Note: In case of manual downloading, it is assumed that the user wants all the content they requested. Hence an already available content could be downloaded a second time in the same directory.

If you try to schedule another manual download when the current one is still in progress, you will get the message 'Manual Download in Progress' as shown below.

Reuters Connect Content Downloader - Installation and User Guide 49

Document Version : 9.0




# Configuration

# Manual Download in Progress

There is already a manual download in progress. Please wait until the download is complete before requesting for a new manual download.

It is possible to cancel or view the progress of a manual download by navigating to the local webserver where the Connect Content Downloader is installed. After logging into the website using the "Login" link on the top right navigation bar. The current progress will be shown as well as a 'Stop Manual Download' button on the summary page.

# 4.1.6. Downloading Top 10 Online Reports

You can download the top 10 Online Reports using the Manual Download option by following the steps below:

1. Click the Top 10 Online Reports Only link on the bottom of the Manual Download screen.

REUTERS CONTENT DOWNLOADER

Summary  Connection Details  Storage  News Feeds  Alerts  Content Options  Manual Download

# Manual Download

This page allows you to download archived Reuters content from a specific time period. Please choose the required news feeds below then define the time period to retrieve content.

Filter by: ALL | Text I Pictures | Graphics Online Video  Online Reports

All feeds

All Text feeds

| NEWS FEED                             | NEWS FEED                      |
| ------------------------------------- | ------------------------------ |
| Reuters World Service                 | CSpanish Domestic News Service |
| Spanish Language General News Service | Spanish Soccer Channel         |

Start Date (UTC): 15 Apr 2022 12:00

End Date (UTC): 18 Apr 2022 12:00

Maximum number of items: 1000

NEXT >

Choose the Online Report News Feeds you want to download and click NEXT.

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0






Configuration

# Summary

# Connection Details

# Storage

# News Feeds

# Alerts

# Content Options

# Manual Download

# Top 10 Online Reports

This page allows you to download the latest Top Ten Packages from the selected Online Report News Feeds

# All feeds

# NEWS FEED

- Brazil Online Report World News
- Canada Online Report Domestic News
- Canada Online Report Sports News
- Canada Online Report Top News
- UK Online Report Top News

# NEWS FEED

- Canada Online Report Business News
- Canada Online Report Entertainment News
- Canada Online Report Technology News
- Latam Online Report Domestic News
- UK Online Report World News

NEXT BACK TO MANUAL DOWNLOAD

# 3. The Confirm Manual Download – Top 10 Online Reports page will appear.

This will give you a summary of the options you choose in the previous step.

# Confirm Manual Download - Top 10 Online Reports

Following news feeds will be sent to manual download queue once you click Download button:

It will take normally 10-15 minutes for the queue to start.

Selected News Feeds: UK Online Report World News

Send an email to the following comma separated email address(es) when the download has completed:

BACK QUEUE DOWNLOAD

# 4. If you want to get notified when the download has completed,

1. Check 'Send an email to the following comma separated email address(es) when the download has been completed'.
2. If you checked the above step, enter valid email addresses as comma separated values.

# 5. Click QUEUE DOWNLOAD

# 6. A 'Success' message will be displayed in the local server under Summary tab indicating successful scheduling of the manual download.

# 7. After the manual download begins, you will get another message to notify you of the request for the manual download with a summary of the requested channels.

This message contains a STOP MANUAL DOWNLOAD button, which you can use if you want to abort the scheduled manual download process.

# 8. If email notification was selected in step 4,

you will get an email from ContentDownloader@thomsonreuters.com with the subject 'The manual download for the Reuters Content Downloader Client - <content downloader="" description="" name=""> has completed.' once the manual download is completed.</content>

# 9. You can view the downloaded content in the same location as the rest of the files.

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



Server Summary &#x26; Statistics

# Chapter 5 SERVER SUMMARY &#x26; STATISTICS

# 5.1 VIEWING LOCAL SERVER SUMMARY

For RCC v4.4.28 or above, to access the Local Server is only accessible by HTTPS as https://localhost:8080. After accessing on the Local server web page, click the Summary tab in the Local Server to view the summary of the recently downloaded content for your client. Clicking on the news feed name under News Feed selector will display the list of last thirty files received from that news feed.

REUTERS CONTENT DOWNLOADER RCD 4.4.28 Tania My Account Sign Out

Status: ACTIVE v4.4.28

# Summary

Export Logs

# News Feed selector

| News feed name        | Date/Time UTC    | Filename                                                          |
| --------------------- | ---------------- | ----------------------------------------------------------------- |
| All News Feeds        | 12:58 18.04.2022 | Last API connection                                               |
| Reuters World Service | 12:58 18.04.2022 | 2022-04-18T1258222\_1271055944\_L2N2WG0L4\_RTRMADT\_0\_BC-ODD.XML |

Note: If this is the first login after installation, you may not see any details here.

# Exporting Log files

If you are reporting a problem to Customer Support, click the Export Logs button (available on the top and bottom of the screen) to get the entire set of log files and audit files in a zip format to send them.

# 5.2 HOW TO CUSTOMIZE THE LOCAL SERVER ACCESS

It is possible to customize the access to the local server, in other words, if the local server needs to be changed to something different from localhost.

To change it, it is necessary to manually update the file “client.properties” located on C:\Program Files\Reuters\ContentDownloader4\conf after the installation is completed.

The following line should be added to the “client.properties” file, for example:

ip.patterns=127.0.0.1,10.127.0.121
Where 127.0.0.1 is the default localhost, in other words, the IP address where the RCD has been installed. Where 10.127.0.121 is the IP address of the remote PC where you would like to access the RCD User Interface.

After adding this line, restart the RCD application as shown in section 2.3, then the local website will be accessible by:

- https://127.0.0.1
- https://10.127.0.121/

Also, is possible to assign a range of IPs to the ip.patterns as follow.

ip.patterns=192.168.178.0/8
ip.patterns=10.127.0.25-10.127.0.210
ip.patterns will not allow server naming; it only allows IPs address.

Reuters Connect Content Downloader - Installation and User Guide    52 Document Version: 9.0



Summary and Help

# 5.3 VIEWING HOSTED SERVER STATISTICS

The Statistics page of the Hosted Server gives the account statistics of all the clients associated with your Content Downloader credentials.

Note: You need to access the Hosted Server directly via Hosted Server to view this page the following page.

Select your desired RCD installation name, look at the drop down list as shown in the red rectangle in the following image:

REUTERS CONTENT DOWNLOADER

Please click here to choose your account:

- Reuters Connect
- Reuters Liaison
- My Account
- Help
- Sign Out

# Account Statistics

This page shows the Reuters Content Downloader clients associated with your account. You can click a client below to access their configuration details. Inactive clients can also be hidden from this page.

| CLIENT ID | VERSION | STATUS   | IP ADDRESS   | HOSTNAME                   | DESCRIPTION                 | LAST ACCESS (UTC) |
| --------- | ------- | -------- | ------------ | -------------------------- | --------------------------- | ----------------- |
| 38436649  | 3.9.1   | INACTIVE | 10.0.2.15    | 10.0.2.15                  | Centos 5.7 Kemel 2.6.1&-274 | 08:43 26.06.2014  |
| 943671750 | 3.9.1   | INACTIVE | 10.0.2:15    | 10.0.2.15                  | Centos5.8Tania              | 14:53 24.06.2014  |
| 890172880 | 44.14   | INACTIVE | 10.0.2.15    | 10.0.2.15                  | Linux Tania 4 4 1 4         | 13:48 25.02.2022  |
| 451733006 | 4.4.1.4 | INACTIVE | 10.0.2.15    | 10.0.2.15                  | Mac4414 Tania               | 08:48 23.03.2022  |
| 156911003 | 4.4.28  | ACTIVE   | 192.168.0.17 | TR-BFMSYY2.technicolor.net | RCD 4.4.28 Tania            | 13:02 18.04.2022  |

# Accessing other Content Downloader Clients

If you manage multiple installs, you can navigate to and configure them directly from any browser. Once signed into your Hosted Server, a list of different installations/instances/clients will be displayed in a drop-down list in the top right corner identified by their given description entered upon install, as shown in the above screen. These are separate Content Downloader installations connected to the same Content Downloader user. To view or configure a particular installation/instance/client, click on its description from the drop-down box. This will take you to that particular installation/instance/client.

# Account Statistics

The following details will be displayed for all the accounts.

| Key       | Description                                                         |
| --------- | ------------------------------------------------------------------- |
| CLIENT ID | Unique ID indicating the particular Content Downloader installation |
| VERSION   | Version of the Content Downloader application.                      |

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0



# Summary and Help

| Key    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| STATUS | Status of the account, which can be one of the following:- ACTIVE - The local server is able to access the Reuters Connect web services and its configuration from the hosted server.

- INACTIVE - There is a problem with the Content Downloader connectivity. In this case, check if you can connect to the web services and the hosted server. For inactive clients, you have the option to hide it from the hosted website by clicking the 'X' button at the end of its row, as shown belowHOSTNAME	DESCRIPTION	LAST ACCESS (UTC)&#xA;Centos 5.7 Kernel 2.6.18-274		08:43 26.06.201 |

Note: This will hide its corresponding Alert history as well.

INVALID PASSWORD - The Reuters web services has rejected the login and password entered on the Connection Details tab. In this case, validate and check if the credentials are correct.
INVALID CONFIGURATION – Your server configuration is invalid. Please update the same.
WARNING - The local server has not contacted the hosted server recently. This could be due to a system restart or temporary loss of connectivity between the local and hosted server.

IP ADDRESS
IP address of the client machine where the Content Downloader is running.

HOSTNAME
Hostname of the client machine where the Content Downloader is running.

DESCRIPTION
Text describing the Content Downloader installation. Clicking this hyperlink will take you to the Summary Downloads page of the selected account.

LAST ACCESS
The time the Hosted Server was last contacted by the Local Server.

# History of Alert Messages

Here, you can view the history of Alert messages sent to the Local Server in case of a connection failure. For more details on Alert Messages, see Configuring Alerts section. The following details are listed in the Alert History.

| Key                | Description                                                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TIME CREATED (UTC) | The time the Alert was generated and sent to the Local Server.                                                                                              |
| CLIENTID           | Unique ID indicating the Content Downloader installation.                                                                                                   |
| DESCRIPTION        | Text describing the particular Content Downloader installation. This will be the value set in Connection Details tab while connecting to the Hosted Server. |

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



Summary and Help

# Key

| ALERT | Alert messages sent to the Local Server. This contains a link, which when clicked, pops up a message box with additional alert details as follows: |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- |

# Alert Details

Time (UTC): 11:45 16.12.2011

Receivers:

System Log: A Reuters Connect Content Downloader client has not contacted our servers recently

CLOSE

# Recent Download Information

The list of recently downloaded content by different clients (pertaining to different Content Downloader installations) can be viewed on the Recent Downloads tab. The details displayed include the news feeds, the file names and the time the request to download was received by the Hosted Server. You have the option to filter the view based on the channel category. You can switch to different accounts by choosing the appropriate account on the top right corner.

# REUTERS CONTENT DOWNLOADER

Statistics  Recent Downloads  Storage  News Feeds  Alerts  Content Options  Manual Download

# Recent Downloads

This page shows the latest files received by the Reuters Content Downloader. These statistics are not real-time and may be delayed up to 5 minutes. Real time downloads are always available on the local client.

Filter by: ALL | Text | Pictures | Graphics | Online Video | Online Reports

| NEWS FEED NAME        | LAST FILE RECEIVED                                                  | TIME RECEIVED (UTC) |
| --------------------- | ------------------------------------------------------------------- | ------------------- |
| Reuters World Service | 2022-04-18T130226Z 1167946933 MT1ALTE1N2U402A6 RTRMADT 0 MEXICO-... | 13:02 18.04.2022    |

# 5.4 ACCESSING CONTENT DOWNLOADER HELP

Clicking Help at the top right corner of the web page will open the help documentation file.

Reuters Connect  Reuters Liaison  My Account  Help  Sign Out

# 5.5 ACCESSING ACCOUNT DETAILS

To access and update your account details, click the My Accounts tab as shown below. You can edit the name, email id and phone number and click the SAVE button. Note that your login information cannot be changed here.

Reuters Connect Content Downloader - Installation and User Guide

Document Version: 9.0




# Summary and Help

# REUTERS CONNECT CONTENT DOWNLOADER

Media Express  Customer Zone  My Account Help Sign Out

# Statistics

- Recent Downloads
- Storage
- News Feeds
- Alerts
- Content Options
- Manual Download

# Account Information

Login:

* First Name:

* Last Name:

* Email Address:

Phone Number:

* - required field

SAVE

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0




TROUBLESHOOTING

# Chapter 6 TROUBLESHOOTING

# 6.1 LOG AND AUDIT FILES

You can access all the log files and audit files from the 'logs' folder in the installation directory (Windows - C:\Program Files\Reuters\ContentDownloader3, by default). Audit files (audit.csv) will be generated in CSV format and contain information on date/time, file name and directory details of all the files downloaded.

# Exporting Log and Audit Files from the local server

If you are reporting a problem to Customer Support, go to Summary tab in the local server and click the ‘Export Logs’ button on the bottom of the screen. This will give you the entire set of log files and audit files in a zip format, which you can send to the helpdesk.

# 6.2 EXCEPTIONS AND ERROR MESSAGES

1. # REUTERS CONNECT CONTENT DOWNLOADER

Statistics  Recent Downloads  Storage  News Feeds  Alerts  Content Opti

Important Notice: At Reuters, we continually work to improve our customers' experience on the installation, documentation, support or functionality of Reuters Connect Content.

# Validation errors:

Please select at least 1 Content Type for Pictures

Please select at least 1 Content Type for Graphics

# Content Options

This page allows you to choose which renditions should be downloaded on your filesystem from:

Filter by: Text  Pictures   Graphics   Online Video   Online Reports

Reason: While setting up the Hosted Server configuration, if you do not select at least one file type for each Channel category in Content Options to download, you will get the above error message.

Solution: For each of the channel categories displayed in the error message (Pictures, Graphics and Online Video), select at least one file type (XML, Thumbnail etc.) to be downloaded.

Reuters Connect Content Downloader - Installation and User Guide    57

Document Version: 9.0






Troubleshooting

# 2. REUTERS CONNECT CONTENT DOWNLOADER

# Statistics

- Recent Downloads
- Storage
- News Feeds
- Alerts
- Content

# Validation errors:

Please, select at least one news feed

# Manual Download

This page allows you to download archived Reuters content from a specific time period. Please choose the required news feeds below then define the time period to retrieve content.

Filter by: ALL Text Pictures Graphics Online Video Online

Reason: If you try to schedule a manual download without selecting any news feeds, you will get the above error message.

Solution: Select at least one news feed to schedule a manual download.

# 3. Sign In

Validation error. Sorry! The LOGIN or PASSWORD entered does not match our records. Please try again.

LOGIN:  *

PASSWORD:

SIGN IN

Reason: If the username or password is entered incorrectly or includes a space, you will get the above error message.

Solution: Enter the correct username and password. Note that passwords are case sensitive.

Reuters Connect Content Downloader - Installation and User Guide 58

Document Version : 9.0





# Troubleshooting

# 4. Sign In

Validation error: Reuters Connect Content Downloader is configured for use with another Web Services Account - RogerCD01

LOGIN:

PASSWORD:

SIGN IN

Reason: If you enter different Reuters Content Downloader credentials to a live and working installation, you will get the above error message.

Solution: Enter your Content Downloader credentials. To find the Login that is in use, search for the configuration.xml file (C:\Program Files\Reuters\ContentDownloader3\conf) on your machine and review &#x3C;wsUsername>XXXXXXXX&#x3C;/wsUsername>. If you forgot the password, contact Customer Support to resend the associated password for wsUsername.

Reuters Connect Content Downloader - Installation and User Guide 59

Document Version : 9.0



# Chapter 7 FAQS

# REUTERS CONNECT

Log into Reuters Liaison web site to access the list of frequently asked questions.

- Scroll down in the page and click over the dropdown menu and search for Content Downloader; then click over Related Content tab and select Content Downloader FAQs

REUTERS LIAISON

Home

Tools

Contact Support

Reuters News Agency

Our content is delivered over a wide variety of mediums; either by internet or Satellite. Our Reuters Field Delivery Platform offers solutions ranging from RSS to FTP Push. Even access our API to power content driven applications. For details on Reuters Media Delivery please review our overview guide. Learn more >

You must be logged into your Media Express user to view available reference material. If you have not logged in, you will be prompted to do so when selecting a document. If you do not have one, please contact us by clicking on Contact Support link in the top right. We'll get your request taken care of straight away.

Learn about your desired solution or delivery platform by selecting from the dropdown below.

# Content Downloader

# About

# Related Content

- Reuters Content Downloader for Windows
- Reuters Content Downloader for Mac OS X
- Reuters Content Downloader for Linux (32 bit)
- Reuters Content Downloader for Linux (64 bit)

# User Guide

- Communication Guide
- XML Quick Reference
- RCD Remote Administration

Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



# Chapter 8 CUSTOMER SUPPORT

To access customer support details,

- Go to Reuters Liaison web site
- There are two options to contact us: via Email or Phone call
- Or send an email to ReutersMediaSupport@thomsonreuters.com

REUTERS LIAISON

Home Tools Contact Support Reuters News Agency

# Contact Support

Submit a request to Reuters Customer Service here. Selecting Support in the Query Type will send a service inquiry to our Helpdesk and you will receive a response within 15 minutes. If Feedback or Billing is selected, your request will be brought to an appropriate team and you will receive a response within 1 business day.

Email Us
Call Us

# Personal Details

English 5

| Name    | Enter Name            |
| ------- | --------------------- |
| Company | Enter Company Name    |
| Phone   | Enter Phone Number    |
| Email   | Enter Corporate Email |
| Country | United States         |

Next

If you select Email Us option, fill out the form and you will receive a response within 15 minutes.

Note: Please send the entire set of log files when mailing for support. See Log and Audit files for more details.

Reuters Connect Content Downloader - Installation and User Guide 61
Document Version : 9.0



# Reuters Connect Content Downloader - Installation and User Guide

Document Version : 9.0



# Chapter 9

# CLASSIFICATION

US ECCN : 5D992

EU ECCN : None

Thomson Reuters Export Code : NL (MM)

Export Note: This export code applies to third party software and Thomson Reuters software where the product does not need a license to be exported as it has already been self approved as a Mass market product. Mass Market means that the product meets the requirements of the Cryptography Note under the US and EU regulations. The product can be exported without restriction to all countries except embargoed destinations (Cuba, Iran, Sudan, Syria and North Korea) (Crimea) and France, where the key length of any symmetric algorithms exceeds 40bits. Dependent upon the length of the encryption algorithm, a declaration or authorization may be needed for import into, use in, supply in or export from France. The product must be reviewed by Trade control staff to determine export legibility.

Reuters Connect Content Downloader - Installation and User Guide 63

Document Version : 9.0