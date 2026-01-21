REUTERS CONNECT FTP PUSH

# TECHNICAL IMPLEMENTATION GUIDE

# OVERVIEW

Reuters Connect Push distributes media content (text, pictures, graphics, videos, and packages) via a push mechanism, supporting the FTP, sFTP, FTP-S and AWS S3 protocols.

# CLIENT SETUP

# IP ADDRESSES

Set up your firewall to allow access for the following IPs from which content will be delivered.

- 34.238.216.121
- 54.175.251.97
- 52.193.144.45
- 52.193.230.215

We will notify you should we include additional IPs in the future.

# FTP PASSIVE MODE

Connect Push only supports Passive mode when sending over FTP. Please ensure that you have your firewall and FTP server configured appropriately.

# SECURE DELIVERY

Connect Push supports secure delivery using the FTP-S, sFTP, AWS S3 protocols.

# DETAILS REQUIRED FOR FTP AND FTP-S DELIVERY

Please inform your Account Manager or technical contact the following details to establish a successful connection:

| DETAILS REQUIRED          | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client Server IP/hostname | IP address or hostname of your server to which files are to be delivered.                                                                                                                                                                                                                                                                                                         |
| Username and Password     | Username and Password to access your server – each up to 40 alphanumeric characters.                                                                                                                                                                                                                                                                                              |
| Port                      | Port number to connect to (Port 21 by default)                                                                                                                                                                                                                                                                                                                                    |
| Destination Directory     | Optional. Specify here if you want the files to be pushed to a particular directory. In this case, (a) the specified directory MUST exist and (b) the destination directory path must be specified relative to user home directory. For example, if the destination directory is /home/reuters and the user home is /home, then you should specify the value here as just reuters |
| Media Delivery Format     | If your content subscription includes pictures or graphics, specify if you would like to receive (a) Images and NewsML-G2 metadata, or (b) Images only.                                                                                                                                                                                                                           |





# DETAILS REQUIRED FOR sFTP DELIVERY

Please inform your Account Manager or technical contact the following details to establish a successful connection:

| DETAILS REQUIRED          | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client Server IP/hostname | IP address or hostname of your server to which files are to be delivered.                                                                                                                                                                                                                                                                                                         |
| Username                  | Username to access your server –up to 40 alphanumeric characters.                                                                                                                                                                                                                                                                                                                 |
| Public key                | Ask to our technical team for our Public Key which should be added to your sFTP server                                                                                                                                                                                                                                                                                            |
| Password                  | If you would like to use the password approach instead of the public key, then provide us with the password.                                                                                                                                                                                                                                                                      |
| Port                      | Port number to connect to (Port 22 by default)                                                                                                                                                                                                                                                                                                                                    |
| Destination Directory     | Optional. Specify here if you want the files to be pushed to a particular directory. In this case, (a) the specified directory MUST exist and (b) the destination directory path must be specified relative to user home directory. For example, if the destination directory is /home/reuters and the user home is /home, then you should specify the value here as just reuters |
| Media Delivery Format     | If your content subscription includes pictures or graphics, specify if you would like to receive (a) Images and NewsML-G2 metadata, or (b) Images only.                                                                                                                                                                                                                           |

# DETAILS REQUIRED FOR AWS S3 DELIVERY

Please inform your Account Manager or technical contact the following details to establish a successful connection:

| DETAILS REQUIRED      | DESCRIPTION                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S3 Bucket Name        | Full S3 bucket name                                                                                                                                           |
| AWS Access Key ID     | AWS account Key ID                                                                                                                                            |
| AWS Secret Access Key | If apply (Reuters do not recommend use AWS Secret Access Key approach, the best way to grant permission is via S3 bucket policy)                              |
| Media Delivery Format | NINJS If your content subscription includes pictures or graphics, specify if you would like to receive (a) Images and NewsML-G2 metadata, or (b) Images only. |

# SUPPORT AND CONTACT INFORMATION

For technical support, create a case on the website http://liaison.reuters.com/contact-us

Or send an email to ReutersMediaSupport@thomsonreuters.com

© Thomson Reuters 2012. All rights reserved.

Thomson Reuters disclaims any and all liability arising from the use of this document and does not guarantee that any information contained herein is accurate or complete.

This document contains information proprietary to Thomson Reuters and may not be reproduced, transmitted, or distributed in whole or part without the express written permission of Thomson Reuters.

Document Version 1.2      THOMSON REUTERS

Date of issue: May 2022

