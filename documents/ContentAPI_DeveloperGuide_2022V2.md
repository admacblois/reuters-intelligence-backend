# REUTERS CONNECT API

# DEVELOPER GUIDE

Page 1 of 27




© Thomson Reuters 2022. All Rights Reserved.

Thomson Reuters, by publishing this document, does not guarantee that any information contained herein is and will remain accurate or that use of the information will ensure correct and faultless operation of the relevant service or equipment. Thomson Reuters, its agents, and employees, shall not be held liable to or through any user for any loss or damage whatsoever resulting from reliance on the information contained herein.

This document contains information proprietary to Thomson Reuters and may not be reproduced, disclosed, or used in whole or part without the express written permission of Thomson Reuters.

Any Software, including but not limited to, the code, screen, structure, sequence, and organization thereof, and Documentation are protected by national copyright laws and international treaty provisions. This manual is subject to U.S. and other national export regulations.

Nothing in this document is intended, nor does it, alter the legal obligations, responsibilities or relationship between yourself and Thomson Reuters as set out in the contract existing between us.

Page 2 of 27






# Contents

# 1     OVERVIEW

4

# 2     HOW GRAPHQL WORKS

5

# 3     WHAT IS NEW IN THE REUTERS CONNECT API

6

# 4     QUICK REFERENCE USER GUIDE FOR THE REUTERS CONNECT API

7

# 4.1        Authentication and Authorization

7

# 4.2        How to access the API

7

# 4.2.1     Get Access Token

7

# 4.2.2     Sent GraphQL Query

8

# 4.2.3     Get Access Token Via Postman

8

# 4.2.4     How to do GraphQL queries in Postman

10

# 4.2.5     How to do GraphQL queries

11

# 4.2.5.1         How to get all subscribed feeds/channels name/channel alias

11

# 4.2.5.2         How to get all subscribed content or map all available items

11

# 4.2.5.3         How to retrieve content from a specific channel.

11

# 4.2.5.4         How to perform a query of a specific item and all its associations

12

# 4.2.5.5         How to perform a mutation/download (fetch items)

12

# 4.2.5.6         How to do a search using two parameters:

13

# 4.2.5.7         How to search for two words within the Headline parameter

13

# 4.2.5.8         How to search using one parameter and filtering by media type:

13

# 4.2.5.9         How to get the items qcodes

14

# 4.2.6     Samples of GraphQL queries using Postman

14

# 5     SEARCH API

19

# 6     QUERY PARAMETER

21

# 7     APPENDIX 1 – LANGUAGE CODES

23

# 8     APPENDIX 2 – ESCAPING METHOD PARAMETERS

24

# 9     CONTENT FORMATS

25

# 10    TECHNICAL SUPPORT

27

Page 3 of 27






# 1 OVERVIEW

The new Reuters Connect API provides a set of functions and procedures which are a consistent way to programmatically access your subscribed content, and it is based on GraphiQL, which is an open-source data query language commonly used for APIs and allows to execute of queries using a type system the user defines for their data.

This document is designed to be used by the client developer, who will write and implement the code that interfaces with the Reuters Connect Web Services to which your organization is subscribed. This document provides:

1. A list of data of the data elements you must obtain from Reuters (including your login credentials) to gain access to Reuters Connect Web Services and retrieve the content you want.
2. Examples of the most used query. For each sample query, the user could use it to obtain a response from the Reuters Connect API.
3. A list of the renditions available for each media type.





# HOW GRAPHQL WORKS

GraphQL works based on typed schemas. The GraphQL schema is the syntax for writing queries and mutations, which are composed to get back the required information from the server. Since the structure of the data returned from the single GraphQL endpoint is entirely flexible, the query must be particular in what it requires.

A GraphQL operation can either be a read or a write operation. A GraphQL query is used to read or fetch values, while a GraphQL mutation is used to write or post values. In either case, the operation is a simple string that a GraphQL server can parse and respond to with data in a specific format. The response format that is usually used for web applications is JSON.



# 3 WHAT IS NEW IN THE REUTERS CONNECT API

The new Reuters Connect API allows you to access all our assets such as text, pictures, graphics, video, archive video, and pictures; in addition, it supports a flexible, points-based spending model that provides clients the freedom to access and utilize different content topics and asset classes – allowing for greater control of budgets as the Reuters Connect website does.

The essential news points content gives you unparalleled access to a wealth of high-quality multimedia content from both Reuters and other world-class media organizations - enabling you to tell deeper, richer stories that engage your audience and enhance your credibility.

The new API platform has been designed to improve editorial efficiency and streamline your workflow, making research and content discovery quicker and easier.

In addition, to the flexible spending of your points, our usage-based spending model optimizes your budget and the return on your investment, but it also affords you a way to explore new content categories and discover alternative ways to grow your audience.




# QUICK REFERENCE USER GUIDE FOR THE REUTERS CONNECT API

# 4.1 AUTHENTICATION AND AUTHORIZATION

The Reuters Content API uses the OAuth2 security protocol to protect system and user security. We support two types of OAuth 2 flows.

1. Client credentials flow

Machine-to-machine (M2M) applications, such as CLIs, daemons, or services running on the back-end, the system authenticates and authorizes the app rather than a user.
2. Authentication Code flow

For Server-side regular web applications or single-page applications, which require exchange of an authorization code for an access token. For single-page applications, we need additional security with a Proof Key for Code Exchange (PKCE).

Once successfully authenticated, we provide the client id credential in the form of an access token that will be issued. The Reuters Content API will verify the token and grant access to the API and all user functionalities.

# 4.2 HOW TO ACCESS THE API

1. To obtain the API credentials (client_id, client_secret, and audience).

The API credentials will be provided by Reuters Technical team.
2. How to obtain the Authentication Token.

After obtaining the client credentials, the access token is requested from the authorization server by the client. The protocol used is OAuth 2.0.
3. How to perform an HTTP Get request.

The GraphiQL query should be specified in the “query” string. For example, if we wanted to execute the following GraphiQL query:

The request could be sent via a POST like:

https://api.reutersconnect.com/content/graphql

# 4.2.1 GET ACCESS TOKEN

Besides the standard OAuth2 request parameters for a different flow, we also need to provide the below audience and get a valid token.

POST https://auth.thomsonreuters.com/oauth/token
{
"client_id": "XXX",
"client_secret": "XXX",
"grant_type": "client_credentials",
"audience": "7a14b6a2-73b8-4ab2-a610-80fb9f40f769",
"scope": "https://api.thomsonreuters.com/auth/reutersconnect.contentapi.read https://api.thomsonreuters.com/auth/reutersconnect.contentapi.write"
}

Page 7 of 27






# 4.2.2 SENT GRAPHQL QUERY

Only the post method was supported by Graphql Server, OAuth2 access token must be present in the request header.

curl --request POST 'https://api.reutersconnect.com/content/graphql’ \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1VTXpPRU14TWpFeU0wWXhSa00yTWpWQ1JrTkd \
--header 'Content-Type: application/json' \
--data-raw '{"query":"query MyQuery {\n currentUser {\n  email\n }\n search {\n  totalHits\n  items {\n  uri\n  type\n  usn\n  versionCreated\n  language\n  slug\n  }\n }\n}","variables":{}}'

# 4.2.3 GET ACCESS TOKEN VIA POSTMAN

Postman is a free application used for API testing. In addition, it is an interactive and automatic tool for verifying the APIs and presents you with a friendly GUI for constructing requests and reading API responses. Postman platform will help users know which code is needed to use depending on their implementation language.

After downloading the application, create a “New Collection” and give it your desired name. Inside the New Collection, right-click and select “Add Request,” as shown in the following image:

My Workspace                                  New Import b
U                                  +                                             00o
Collections                             >Graphql
0                                  > New Collection
APIS                                New Collection
Environments                            Tania GraphQ                Add Request
POST New R       Add Folder
POST https:/     Monitor Collection
Mock Servers                                       GET New R        Mock Collection
A                                                              Create a fork
Monitors                                                          Rename            Ctrl+E
D$                                                             Duplicate         Ctrl+D
Flows                                                            Export
D                                                              Manage Roles
History                                                            Delete            Del

After creating a “request,” please do a POST and fill out the fields shown in the following image to get the Token. Do the POST to https://auth.thomsonreuters.com/oauth/token. Select the “Body” tab and “x-www-form-urlencoded,” and under the “Key” column, write down the following fields as shown in the next image:

POST    (  hputomu/n
Params  Authorization  Headers (9)  Body Pre-request Script Tests   Settings
none    form-data x-www-form-urlencoded raw binaryGraphQL
0
KEY                                                                 VALUE                     DESCR
client_id
client_secret
audience
grant_type
scope
Key                                                                Value                     Descri

Important: when entering the information (copy/paste) under the “Value” column, do not hit the ENTER key






# API Authentication

| Key            | Value                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| client\_id     | XXXXXXXXXXXXXXXXXX                                                                                                                       |
| client\_secret | XXXXXXXXXXXXXXXXXX                                                                                                                       |
| audience       | 7a14b6a2-73b8-4ab2-a610-80fb9f40f769                                                                                                     |
| grant\_type    | client\_credentials                                                                                                                      |
| scope          | https\://api.thomsonreuters.com/auth/reutersconnect.contentapi.read https\://api.thomsonreuters.com/auth/reutersconnect.contentapi.write |

After entering the above information, click over SEND as shown below, and the application should return your account TOKEN.

Note: “client_id” and “client_secret” are not shown to protect the credentials.

After the token is generated, you can begin to do the GraphQL queries.

# POST

https://auth.thomsonreuters.com/oauth/token

Params  Authorization  Headers (9)  Body Pre-request Script Tests Settings Cookies

•none • form-data x-www-form-urlencoded • raw • binary • GraphQL

| KEY            | VALUE                                                               | DESCRIPTION |
| -------------- | ------------------------------------------------------------------- | ----------- |
| client\_id     |                                                                     |             |
| client\_secret |                                                                     |             |
| audience       | 7a14b6a2-73b8-4ab2-a610-80fb9f40f769                                |             |
| grant\_type    | client\_credentials                                                 |             |
| scope          | https\://api.thomsonreuters.com/auth/reutersconnect.contentapi.read |             |

# Response

Status: 200 OK

Time: 993 ms

Size: 1.82 KB

Response Body:

{
"access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6I1JERTBPVEF3UVVVMk16Z3hPRUpGTkVSRk5qUkRNakkzUVVFek1qZEZOVEJCUkRVM1JrTTRSZyJ9.",
"scope": "https://api.thomsonreuters.com/auth/reutersconnect.contentapi.write https://api.thomsonreuters.com/auth/reutersconnect.contentapi.read",
"expires_in": 86400,
"token_type": "Bearer"
}





# 4.2.4 HOW TO DO GRAPHQL QUERIES IN POSTMAN

After the token is generated, create a new “request” and make a POST request to our URL https://api.reutersconnect.com/content/graphql as shown in the image below, click over the “Authorization” tab and select “Bearer Token” and copy/paste your token on the Token field as shown below:

| POST   | <https://api.reutersconnect.com/content/graphql> | Send        |      |                    |       |          |         |
| ------ | ------------------------------------------------ | ----------- | ---- | ------------------ | ----- | -------- | ------- |
| Params | Authorization                                    | Headers (9) | Body | Pre-request Script | Tests | Settings | Cookies |

Type Bearer Token

Heads up! These parameters hold sensitive data. To keep this data secure while working in a collaborative environment, we recommend using variables.

The authorization header will be automatically generated when you send the request. Learn more about authorization.

Token

eyJhbGciOiJSUzI1NilsInR5cCI6IkpXVCIslmtp ZCI6IIJERTBPVEF3UVVVMk16Z3hPRUpGTkV SRk5aUJkRNakk7UVVFek1a7F7OVF.ICUkRVM

# Response

After entering the TOKEN, verify that your account is working fine. Go to “Body” and select “GraphQL,” write down a simple query to get your account details, and click “Send.” The application should show you your account details.

query MyQuery {
currentUser {
email
firstName
lastName
loginName
userCountry
}
}

| POST   | <https://api.reutersconnect.com/content/graphql> |                       |      |                    | Send    |           |         |
| ------ | ------------------------------------------------ | --------------------- | ---- | ------------------ | ------- | --------- | ------- |
| Params | Authorization                                    | Headers (9)           | Body | Pre-request Script | Tests   | Settings  | Cookies |
| none   | form-data                                        | x-www-form-urlencoded | raw  | binary             | GraphQL | No schema |         |

# GRAPHQL VARIABLES

QUERY
query MyQuery
currentUser
email
firstName
lastName
loginName
userCountry
1

# Response

{
"data": {
"currentUser": {
"email": "tania.vivero@tr.com",
"firstName": "Tania",
"lastName": "Vivero",
"loginName": "newapi_tests",
"userCountry": []
}
}
}

Status: 200 OK

Time: 586 ms

Size: 772 B

Save Response




# 4.2.5 HOW TO DO GRAPHQL QUERIES

All the API GraphiQL parameters information is found under the Reuters GraphQL portal. The Reuters GraphiQL Portal (https://api.reutersconnect.com/graphql/portal/) is new and will allow developers to learn more about the Content API and GraphiQL. It is designed to enable developers to have an easier way to debug queries and study the schema.

# 4.2.5.1 How to get all subscribed feeds/channels name/channel alias

query MyQuery {
currentUser {
subscriptions {
alias
category
name
}
}
}

# 4.2.5.2 How to get all subscribed content or map all available items

query MyQuery {
search {
totalHits
items {
headLine
versionedGuid
uri
language
type
profile
slug
version
credit
firstCreated
sortTimestamp
contentTimestamp
productLabel
urgency
}
}
}

# 4.2.5.3 How to retrieve content from a specific channel.

Select any channel alias from the ones shown on point (a) and execute the following query to get the content from a specific channel, for example, channel “Reuters World News,” channel alias: “STK567” – if you know your channel alias ask our Technical Support Team.

query MyQuery {
search(filter: {channel: "channel_alias"}) {
items
}
}

REUTERS | CONNECT 1.0.58

Explorer × GraphiQL Prettify History Explorer

query MyQuery {
currentUser
downloadHistory
item
pointBalance
search
cursor:
filter:
channel: "STK56."
channelCategoris:
dateRange:
languages:
maxAge:
mediaTypes:
}





# 4.2.5.4 How to perform a query of a specific item and all its associations

query MyQuery {
currentUser {
firstName
lastName
loginName
email
lastChangedTimestamp
}
item(id: "item_ID") {
byLine
copyrightNotice
versionCreated
fragment
headLine
versionedGuid
uri
language
type
profile
slug
usageTerms
usageTermsRole
version
credit
firstCreated
productLabel
pubStatus
urgency
usn
position
intro
}
}

# 4.2.5.5 How to retrieve a video item with all renditions

If, instead of a video item, you would like to get audio, image, and text renditions, replace VideoRendition for ImageRendition or AudioRendition, GeneralRendition, respectively.

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
mimeType
remotePath
type
uri
version
... on VideoRendition {
mimeType
fileName
rendition
}
}
}
}
}

# 4.2.5.6 How to perform a mutation/download (fetch items)

mutation MyMutation {
download(
itemId: "item_ID"
type: NEWSML
renditionId: "item_ID"
) {
type
... on GenericItem {
url
}
}
}






# 4.2.5.7 How to do a search using two parameters:

query MyQuery {
currentUser {
email
firstName
lastChangedTimestamp
lastName
loginName
userCountry
}
search(query: "topic:SPO||+headline:nadal") {
items {
channels
intro
language
slug
type
firstCreated
headLine
destination
fragment
urgency
}
totalHits
}
}

# 4.2.5.8 How to search for two words within the Headline parameter

query MyQuery {
search(query: "headline:(cycling OR france)") {
items
}
}

# 4.2.5.9 How to search using one parameter and filtering by media type:

query MyQuery {
currentUser {
email
firstName
lastChangedTimestamp
lastName
loginName
userCountry
}
search(query: "headline:Spain", filter: {mediaTypes: TEXT}) {
items {
headLine
language
position
renditions {
... on ImageRendition {
mimeType
fileName
}
}
}
}
}







# 4.2.5.10 How to get the items qcodes

query MyQuery {
item(id: "item_ID") {
subject {
code
name
rel
}
}
}

# 4.2.6  SAMPLES OF GRAPHQL QUERIES USING POSTMAN

a) How to get all RAW video clips distributed by the “Core-World” feed on 1/Dec/2021

The Core News feed channel alias is Wbz248. All the content related to “World” comes with the topic code: WNSFR:WORLD. The dataRange parameter should have the format YYYY.MM.DD.HH.MM (Year, month, day, hour, minutes).

query MyQuery {
search(
filter: {channel: "Wbz248", topicCodes: "WNSFR:WORLD", dateRange: "2021.12.01.23.59"}
) {
totalHits
items {
byLine
copyrightNotice
versionCreated
fragment
headLine
versionedGuid
uri
language
type
profile
slug
usageTerms
usageTermsRole
version
credit
firstCreated
productLabel
pubStatus
urgency
usn
position
intro
}
}
}

After checking that your query is working correctly in our portal, copy and paste the above question in Postman and click over send and the query should provide you the same results as in our portal.






# POST

# https://api.reutersconnect.com/content/graphql

# Send

# Params

| Authorization | Headers (9) | Body                  | Pre-request Script | Tests  | Settings | Cookies   |
| ------------- | ----------- | --------------------- | ------------------ | ------ | -------- | --------- |
| none          | form-data   | x-www-form-urlencoded | ©raw               | binary | GraphQL  | No schema |

# QUERY

# GRAPHQL VARIABLES

| 1  | query MyQuery                                         |
| -- | ----------------------------------------------------- |
| 2  | search(                                               |
| 3  | filter: {channel: "wbz248", topicCodes; "wNsFR:woRLD" |
| 4  | )t dateRange: \*2021.12.01.23.59"}                    |
| 5  | totalHits                                             |
| 6  | items {                                               |
| 7  | byLine                                                |
| 8  | copyrightNotice                                       |
| 9  | versionCreated                                        |
| 10 | fragment                                              |
| 11 | headline                                              |
| 12 | versionedGuid                                         |
| 13 | uri                                                   |

# Cookies

# Headers (18)

# Test Results

| Status: 200 OK | Time: 1017.ms | Size: 48.05 KB | Save Response |
| -------------- | ------------- | -------------- | ------------- |

# Pretty

# Raw

# Preview

# Visualize

# JSON

| 1  | "data": {                                                                                                                                                            |
| -- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2  | "search": {                                                                                                                                                          |
| 3  | "totalHits": 978,                                                                                                                                                    |
| 4  | "items": \[                                                                                                                                                          |
| 5  | {                                                                                                                                                                    |
| 6  | "byLine": "Reuters, DEC 12",                                                                                                                                         |
| 7  | "copyrightNotice": "(c) 2021 Thomson Reuters, unless otherwise identified. Full statement available at https\://www\.thomsonreuters.com/en/policies/copyright.html", |
| 8  | "versionCreated": "2021-12-12T20:28:08Z",                                                                                                                            |
| 9  | "fragment": null,                                                                                                                                                    |
| 10 | "headLine": "Israeli PM Bennett arrives in Abu Dhabi to meet de facto ruler"                                                                                         |
| 11 | "versionedGuid": "tag:reuters.com,2021:ninjs\_wDF7QG213:3",                                                                                                          |
| 12 | "uri": "tag:reuters.com,2021:ninjs\_WDF7QG213",                                                                                                                      |
| 13 | "language": "en",                                                                                                                                                    |
| 14 | "type": "video",                                                                                                                                                     |
| 15 | "profile": "NEP-External\_MNP",                                                                                                                                      |

# NodeJs - Request

# NodeJs - Unirest

# Objective-C - NSURLSession

# OCaml - Cohttp

# PHP - cURL

# PHP - HTTP_Request2

# PHP - pecl_http

# PowerShell - RestMethod

# Python - http.client

# Python - Requests

# Ruby - Net:HTTP

# Bootcamp 0Runder Trash T

# For example, if you want to do your implementation using Python, use the code shown below.






# POST

# https://api.reutersconnect.com/content/graphql

# Send

# Python - Requests

# Params

- Authorization

# Headers (9)

# Body

# Pre-request Script

# Tests

# Settings

# Cookies

import requests
import json

url = "https://api.reutersconnect.com/content/graphql"
payload="{\"query\":\"query MyQuery {\\r\\n search(\\r\\n  filter: {channel: \\\"Wbz248\\\", topicCodes: \\\"wNsFR:woRLD\\\", dateRange: \\\"2021.12.01.23.59\\\"}\\r\\n){\\r\\n  totalHits\\r\\n  items {\\r\\n      byLine\\r\\n  copyrightNotice\\r\\n  versionCreated\\r\\n      fragment\\r\\n  headLine\\r\\n  versionedGuid\\r\\n     uri\\r\\n  language\\r\\n  type\\r\\n      profile\\r\\n      slug\\r\\n        usageTerms\\r\\n  usageTermsRole\\r\\n      version\\r\\n   credit\\r\\n  firstCreated\\r\\n      productLabel\\r\\n     pubStatus\\r\\n  urgency\\r\\n      usn\\r\\n     position\\r\\n     intro\\r\\n      \\r\\n}\\r\\n}\",\"variables\":{}}"
headers = {
'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTBPVEF3UVVVMk16Z3hPRUpGTkVSRk5qUkRNakkzUVVFek1qZEZOVEJCUkRVM1JrTTRSZyJ9.',
'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
# Response

"data": {
"search": {
"totalHits": 1005,
"items": [
{
"byLine": "Reuters, DEC 13",
"copyrightNotice": "(c) 2021 Thomson Reuters, unless otherwise identified. Full statement available at https://www.thomsonreuters.com/en/policies/copyright.html",
"versionCreated": "2021-12-13T08:49:23Z"
}
]
}
}
# How to get all RAW clips which Slug is “Reuters-Next.”

Go to the Reuters GraphQL portal: https://api.reutersconnect.com/portal/graphql and test your query first.

query MyQuery {
search(query: "slug:reuters\\-next") {
items {
byLine
copyrightNotice
versionCreated
fragment
headLine
versionedGuid
uri
language
type
profile
slug
usageTerms
usageTermsRole
version
credit
firstCreated
productLabel
pubStatus
urgency
usn
position
intro
}
}
}
Test your query in our portal; if you get results, move to Postman, copy/paste the code, click over Send, and the results should show as in the image. Click over the code symbol and select your desired language for further implementation.






# API Documentation

# GraphQL API

POST https://api.reutersconnect.com/content/graphql

# Request

POST /content/graphql HTTP/1.1
Host: api.reutersconnect.com
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsIntpZCI6I1JERTBPVEF3UVVV
Mk16Z3hPRUoGTkVSRk5oUkRNakkzUVVEek1oZEZOVEJCUkRVM1JxTTRSZy19
eyJpc3MiOiJodHRwczovL2F1dGgudGhvbXNvbnJldXRlcnMuY29tLyIsInN1
YiI6In1WNUV2WTkwdzBRO29tcGdKbnJnWXNPOWRoZ1hhZFdxOGNsaHVudHMi
LCJhdWQiOiI3YTE0YjZhMi03M2I4LTRhYjItYTYxMC04MGZiOWY0MGY3Njki
LCJpYXOiOiE2MzkwNzAzNiYsImV4cCI6MTYzOTE1Nic2NiwiYXpwIioieVY1
RXZZOTB3MFFDb21wZ0pucmdZc09BZGlnWGFkV2siLCJzY29wZSI6Inh0dHBz
018yYXBnLnRob21zb25yZXVoZXJzLmNybS9hdXRoL3JldXRlcnNib25uZWN0
LmNvbnR1bnRhcGkud3JodGUsaHRBcHM6Ly9hcGkudGhvbXNydW5ldXR1cnMu
Y29tL2F1dGgvcmV1dGVyc2Nvbm51Y3QuY29udGVudGFwaS5yZWFkIiwiZ3R5
Ijoic2VydmVyIn0.
Content-Type: application/json
Content-Length: 529

# Query

{"query":"query MyQuery {\n search(query: \"slug:reuters\\-next\") {\n items {\n byLine\n copyrightNotice\n versionCreated\n fragment\n headLine\n versionedGuid\n uri\n language\n type\n profile\n slug\n usageTerms\n usageTermsRole\n version\n credit\n firstCreated\n productLabel\n pubStatus\n urgency\n usn\n position\n intro\n }\n }\n}","variables":{}}

# Response

{
"data": {
"search": {
"items": [
{
"byLine": "Dado Ruvic",
"copyrightNotice": "(c) Copyright Thomson Reuters 2021. Click For Restrictions - https://agency.reuters.com/en/copyright.html",
"versionCreated": "2021-12-09T13:06:48Z",
"fragment": null,
"headLine": "Câmara aprova projeto que prevè regras para negociação de moedas digitais"
}
]
}
}
}

# cURL Example

curl --location --request POST 'https://api.reutersconnect.com/content/graphql' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTBPVEF3UVVV
Mk16Z3hPRUpGTkVSRk5aUkRNakkzUVVFek1aZEZOVEJCUkRVM1JrTTRSZyJ9' \
--header 'Content-Type: application/json' \
--data-raw '{"query":"query MyQuery {\n search(query: \"slug:reuters\\-next\") {\n items {\n byLine\n copyrightNotice\n versionCreated\n fragment\n headLine\n versionedGuid\n uri\n language\n type\n profile\n slug\n usageTerms\n usageTermsRole\n version\n credit\n firstCreated\n productLabel\n pubStatus\n urgency\n usn\n position\n intro\n }\n }\n}","variables":{}}'

Page 17 of 27





# Page 18 of 27




# SEARCH API

The search method is used to obtain a list of news items that match the search criteria desired. This method provides more advanced filtering options.

The search method accepts the following parameters:

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channel         | This parameter is used to specify the channel alias for which you wish to retrieve the news items. To obtain the alias for a given channel, see section 4.2.5 (a). If multiple channel aliases are specified, each should be specified as a separate query string parameter (Example: channel=ABC\&channel=DEF). Default Value: If no channel alias is supplied, results will be returned for all the channels you have subscribed to.                                                                                                                                                                          |
| channelCategory | This parameter is used to specify the channel categories to be used when retrieving news items. A channel category is a group of channels containing similar content (Example: Text, Online Reports, Pictures, or Online Video). When both channel and channelCategory are supplied, all channels matching ‘channel’ as well as ‘channelCategory’ will be returned i.e., the result will be a union of the criteria passed. Default Value: If no value is supplied, all channel categories will be included for searching.                                                                                      |
| dateRange       | This parameter is used to specify the date range for the news items to be retrieved. The date range should be specified as \<start\_date>-\<end\_date> (For example, 2022.05.01-2022.05.04 for news items from 00:00 on May 1 to 00:00 on May 4th). If a start date is specified without an end date, the current time will be considered as the end date. Default Value: If no date range filter is supplied, the news items returned will be limited to the past 24 hours.                                                                                                                                    |
| languages       | This parameter is used to specify the primary language associated with the news items to be retrieved. You must use a 2-letter code to specify the language. If multiple languages are specified, each must be separated by the OR operator. Example: language=en OR fr Refer to Chapter 7 (Appendix 1) for a list of valid 2-letter language codes. Default Value: All available languages will be considered.                                                                                                                                                                                                 |
| maxAge          | This parameter is used to provide a date limit relative to the current date and time. This filter will be translated into a date range using the current time as the starting point. This parameter should be specified in the format maxAge=\<Positive Number>\<Unit> \<Unit> can be one of the following: s – for seconds m – for minutes h – for hours D – for days Examples: maxAge=2D will retrieve results limited to the past 2 days, maxAge=6h will retrieve results from the last 6 hours. Default Value: 24h Note: When both maxAge and dateRange are specified in a request, maxAge will be ignored. |
| mediaTypes      | This parameter is used to specify the media type for the news items to be retrieved. Valid media types are T (text), P (pictures), V (video), G (graphics) and C (composite i.e. a package of content containing references to other items). If multiple media types are specified, each should be specified in a separate query string parameter. Example: mediaType=T\&mediaType=P Default Value: All available media types will be considered.                                                                                                                                                               |






# Parameters

minAge This parameter is used to provide a date limit relative to the current date and time.

topicCodes Used to specify the topic codes (i.e., NewsML News2000 subject codes) associated with the news items to be retrieved.

All the topic codes are available at https://liaison.reuters.com/tools/topic-codes






# QUERY PARAMETER

This parameter is a string used to specify the attributes by which the news items returned should be filtered. The query parameter filters are specified in the following manner:

[filter1_name]:[filter1_value]||[filter2_name]:[filter2_value]

Note: If multiple filters are used, each must be separated by the || (double pipe) delimit. The values of the query parameter and its filters have additional character escaping requirements. The full list of character which must be escaped for this parameter, are listed in Appendix 2.

The query parameter can be used with the following filters.

- headline - Used to specify the required/optional keywords that must/may be contained within the headline of the news items that are retrieved.
- slug - used to specify the required/optional keywords that must/may be contained within the slug of the news items that are retrieved.
- body - used to specify the required/optional keywords that must/may be contained within the body of the news items that are retrieved.
- caption - used to specify the keywords contained within the caption of the news items that are retrieved. Caption is only valid for Picture and Graphic content.
- id - used to specify one of the following news item identifiers by which to retrieve news items. Valid news item identifiers are id, guid, USN, OTR, IID, SID, and editNumber.
- topic - used to specify the topic codes (i.e., NewsML News2000 subject codes) associated with the news items to be retrieved.
- signal - used to specify the signal codes (i.e., NewsML signal codes) associated with the news items to be retrieved.
- fulltext - used to specify the keywords that may be contained within one or more of the following fields of the news items that are retrieved: body, headline, caption.
- main - used to specify the keywords that may be contained within one or more of the following fields of the news items that are retrieved: body, headline, caption, id, topic, signal and slug.

# Filter options

Note: All the above filters and pre-defined groups except id support the use of all the filter options described below. Id supports only wildcards and inclusion/exclusion modifiers (+,-)

- Phrase searches - Reuters supports searching on a collection of one or more terms by surrounding those terms with double quotes (“state of the union”). By placing a series of terms in double-quotes, you are requesting that only news items with these exact terms in the precise order you entered be returned. The terms that you enter within the double quotes do not need to be escaped.
- Wildcards - Reuters supports the use of the * and ? wildcards within search terms. The asterisk character (*) is used to substitute for zero or more characters. The question mark is used to substitute for any single character. Reuters does not support the use of wildcard characters at the beginning of a single search term or within an explicit phrase (Example: “board of health”).
- Boolean operators - Reuters supports the use of AND, OR and NOT to refine the way terms with a search are applied.
- Grouping (nesting) – Reuters allows you to use the parenthesis symbols ( ) to group/nest terms and/or phrases within a search. For example, if your search contained, “bird flu” AND (China OR europe) AND immunizations





it would mean that you wanted all news items containing the phrase bird flu and the term immunizations and either the term China or Europe.

# Inclusion / Exclusion modifiers (+, -)

Reuters supports the use of modifiers to explicitly require that data specified by a particular filter be included in or excluded from the news items returned.

- The plus symbol (+) indicates that the data specified after the “+” symbol must be present somewhere in the news items returned.
- Example: To search for documents that must contain “cricket” and may contain “England”, use the query: +cricket England

The minus symbol (-) indicates that the data specified by the filter must NOT be present in the news items returned.

Note: The absence of either a plus or minus symbol indicates that the data specified by the filter is optional (although the presence of this data in a news item will increase its score)



# 7 APPENDIX 1 – LANGUAGE CODES

| ar | – Arabic                     |
| -- | ---------------------------- |
| ko | – Korean                     |
| cs | – Czech                      |
| nl | – Dutch                      |
| da | – Danish                     |
| no | – Norwegian                  |
| de | – German                     |
| pl | – Polish                     |
| el | – Greek                      |
| pt | – Portuguese                 |
| en | – English                    |
| ru | – Russian                    |
| es | – Spanish                    |
| sv | – Swedish                    |
| fr | – French                     |
| th | – Thai                       |
| it | – Italian                    |
| tr | – Turkish                    |
| ja | – Japanese                   |
| zh | – Chinese Simple/Traditional |

Page 23 of 27



# 8 APPENDIX 2 – ESCAPING METHOD PARAMETERS

The following characters must be escaped with a backslash character (\) when designated as the value of a method parameter (unless otherwise noted):

- ,
- !
- *
- {}
- \

Note: The query parameter (used within the search method) requires an additional list of characters to be escaped.

- [ ]
- -
- +
- /
- ( )
- ~
- ^
- !
- |
- :
- ,
- &#x26;
- '
- "
- {}
- \

This list is in addition to the characters that must be escaped for other method parameters. Only the actual values of the query filters (not the filter names themselves) must be escaped. When using double quotes to search for one or more terms (i.e., an exact phrase), you do not need to escape the terms within the double-quotes.




# 9 CONTENT FORMATS

The Reuters API GraphiQL subscribers can access a wide range of standardized text, pictures, graphics, videos, and audio formats.

# For text:

FORMAT
XML
JSON

# For pictures:

| FORMAT       | RENDITIONS                          |
| ------------ | ----------------------------------- |
| viewImage    | Width: 640 pixels                   |
| Thumbnail    | Width: 150 pixels                   |
| baseImage    | Width: highest resolution available |
| limitedImage | Width: 3500 pixels                  |

# For graphics:

| FORMAT | RENDITIONS                         |
| ------ | ---------------------------------- |
| PDF    | Highest resolution available       |
| EPS    | Highest resolution available       |
| JPEG   | viewImage: width of 450 pixels     |
|        | thumbnail: width of 150 pixels     |
|        | limitedImage: width of 1200 pixels |

# For packaged videos:

| FORMAT          | RENDITIONS                                 |
| --------------- | ------------------------------------------ |
| 3GPP2 80        | stream:80:11x9:3g2 176x144 frame size      |
| 3GPP 80         | stream:80:11x9:3gp 176x144 frame size      |
| Flash Video 512 | stream:512:16x9:flv 512x288 frame size     |
| Flash Video 300 | stream:300:16x9:flv 384x216 frame size     |
| H264/mpeg 300   | stream:300:16x9:mp4 384x216 frame size     |
| H264/mpeg 720   | stream:5128:16x9:mp4 1280x720 frame size   |
| H264/mpeg 2000  | stream:2000:16x9:mp4 768x432 frame size    |
| H264/mpeg 700   | stream:700:16x9:mp4 640x360 frame size     |
| Flash Video 700 | stream:700:16x9:flv 576x324 frame size     |
| H264/mpeg 2000  | stream:8256m:16x9:mp4 1920x1080 frame size |
| Mpeg 6756       | stream:6756:16x9:mpg 720x576 frame size    |
| H264/mpeg 8256  | stream:8256:16x9:mp4 1920x1080 frame size  |
| H264/mpeg 1756  |                                            |





# 1280x720 frame size

# For raw video:

| FORMAT               | RENDITIONS                      |
| -------------------- | ------------------------------- |
| video/mpeg SD 525    | stream:6756:16x9:sd525i30:mpg   |
| video/mpeg SD 625    | stream:6756:16x9:sd625i25:mpg   |
| video/mp4 HD 1080i50 | stream:13756:16x9:hd1080i50:mp4 |
| video/mp4 HD 1080i60 | stream:13756:16x9:hd1080i60:mp4 |
| video/mp4 HD 486     | stream:2128:16x9:mp4            |
| video/mp4 HD 720     | stream:1756:16x9:mp4            |

# For Archive video:

| FORMAT               | RENDITIONS                      |
| -------------------- | ------------------------------- |
| video/mpeg SD 525    | stream:6756:16x9:sd525i30:mpg   |
| video/mpeg SD 625    | stream:6756:16x9:sd625i25:mpg   |
| video/mp4 HD 1080i50 | stream:13756:16x9:hd1080i50:mp4 |
| video/mp4 HD 1080i60 | stream:13756:16x9:hd1080i60:mp4 |
| video/mp4 HD 486     | stream:2128:16x9:mp4            |
| video/mp4 HD 720     | stream:1756:16x9:mp4            |

# For audio:

| FORMAT     | RENDITIONS        |
| ---------- | ----------------- |
| audio/mpeg | stream:22.050:mp3 |
| audio/mpeg | stream:48000:mp3  |
| audio/aa   | stream:48000:m4a  |
| audio/wav  | stream:48000:wav  |
| audio/wav  | stream:48000m:wav |
| audio/mpeg | preview:48000:mp3 |

Page 26 of 27




# 10 TECHNICAL SUPPORT

There are a variety of means by which you can contact Thomson Reuters for support. One of the easiest is to go to https://liaison.reuters.com/contact-us and complete the request form after which a customer representative should contact you within 15 minutes. No sign-in is required.

