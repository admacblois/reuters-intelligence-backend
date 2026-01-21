# Reuters

# Reuters API

# Developer Guide

# Version 15 | 2025

© 2024 Reuters



Reuters API
# CONTENTS

- INTRODUCTION 6
- REVISION HISTORY 7
- OVERVIEW 9
- HOW GRAPHQL WORKS 9
- WHAT IS NEW IN THE API 10
- AUTHENTICATION 11
- - CLIENT CREDENTIALS FLOW 11
- AUTHENTICATION CODE FLOW 11

REUTERS API PORTAL 12
- HOW TO ACCESS THE API 12
- - HOW TO OBTAIN THE AUTHENTICATION TOKEN 12
- GET ACCESS TO YOUR TOKEN. 12
- TOKEN BEST PRACTICES 13
- TOKEN ERROR ACCESS 13
- THROTTLING ERROR 13
- HOW TO PERFORM A QUERY 13
- HOW TO ACCESS THE REUTERS API PORTAL 14

ENDPOINTS 14
- METHODS SUMMARY TABLE 15
- API QUICK REFERENCE GUIDE 16
- 19
- CURRENTUSER METHOD 20
- EXAMPLES 22
- DOWNLOADHISTORY METHOD 23
- EXAMPLES 24
- - 1. How to retrieve the download history of the API users. 24

FILTEROPTIONS METHOD 25
- EXAMPLES 28
- - 1. How to query to see the categories list: 28
- 2. How to query to see the sub-categories of the categories: 28
- 3. How to search for items under the category: Climate Change 29
- 4. How to search for items under the sub-category: News > Politics 29
- 5. How to search for items under the media type sub-category: Video > Raw 30
- 6. How to search for two or more options. Category: Business and Source: Reuters 30
- 7. How to query to see the sub-category of a sub-category. 30
- 8. How to see the available Marketplace feeds categories. 31
- 9. How to see the sources list and its code, names and uri. 31

ITEM METHOD 32
- EXAMPLES 35

© 2024 Reuters




3
Reuters API

# 4. How to retrieve a video item with all renditions

# 5. How to retrieve a video item with all renditions information/parameters

# 6. How to get the items qcodes (Topic Codes)

# 7. How to see the points value of an item rendition, for example a picture

# 8. How to see the points value of an item rendition, for example a video

# 9. How to see the direct download URL of an image preview or thumbnail

# 10. How to retrieve a video transcript (shotlist.JSON)

# 11. How to retrieve a video closed captions (VTT and SRT)

# ITEMREVISIONS METHOD

# EXAMPLES

# 1. How to see an item previous versions

# POINTSBALANCE METHOD

# EXAMPLES

# 2. How to see the Points available and points information

# SEARCH METHOD

# EXAMPLES

# 1. How to get all subscribed content or map all available items.

# 2. How to retrieve content from a specific channel.

# 3. How to do a search using an interval of time (dateRange)

# 4. How to get the total number of items distributed by the topicCodes: CMPNY and DIP

# 5. How to get the direct URL of the /previewURL or /thumbnailUrl or /thumbnailUrlLarge

# 6. How to filter for Marketplace content (free and paid/points)

# 7. How to get filter using the source feed code.

# 8. How to use the cursor parameter for pagination

# 9. How to use the page parameter for pagination

# 10. How to search for items under the category: Business &#x26; Finance

# 11. How to search for items under the sub-category: Sports > Cycling

# 12. How to search for items under the media type sub-category: Video > Raw

# 13. How to search for two or more options. Category: Business and Source: Reuters

# 14. How to search for a sub-category of a sub-category, for example, Europe > South Europe > Spain

# 15. How to do a query search using variables

# 17. How to search by first_created parameter

# 18. How to search by first_created parameter and sort by version_created parameter

# 19. How to use the cursorMode:POLL to periodically poll for new content, excluding items that have already been polled.

# QUERY PARAMETER

# FILTER OPTIONS

# Boolean operators

# Grouping (nesting)

# WILDCARDS

# EXAMPLES

# 1. How to do a search/query using two parameters

# 2. How to search for two words within the Headline parameter

# 3. How to search using one parameter and filtering by media type

# 4. How to search two or more media types:

# 5. How to search two or more channel alias:

# 6. How to get the total number of RAW clips with the slug: “Reuters-Next”

# 7. How to query using the item USN supplied by Reuters

REUTERS
© 2024 Reuters





4
Reuters API

# 8. How to query using the item signal.

# 9. How to query using the item ID

# 10. How to query using the priority/urgency parameter.

# 11. How to query using wildcards.

# 12. How to exclude content

# MUTATION METHOD

# EXAMPLES

# 1. How to perform a mutation/download – Text Item (fetch items)

# 2. How to perform a mutation/download – Package (fetch items)

# 3. How to perform a mutation/download of an image renditions

# 4. How to perform a mutation/download of a video renditions

# 5. How to perform a mutation/download of an image

# LIVE API

# LIVE VIDEO SIGNALS QUICK REFERENCE QUIDE

# 1. How to retrieve the start/end date and event status of the live events

# 2. How to retrieve an event rendition

# 3. How to subscribe to an event and get back an HLS URL

# 4. How to subscribe to an event and get back an RTMP stream

# 5. How to unsubscribe from an event

# LIVEEVENTS METHOD

# EXAMPLES

# 1. How to retrieve the start/end date and event status of the live events

# 2. How to retrieve live events using the dateRange

# 3. How to retrieve an event rendition

# 4. How to filter content based on event uri, id or usn

# LIVEEVENTSUBSCRIPTIONS METHOD

# EXAMPLES

# 1) How to get the current live events the API user is subscribed to:

# MUTATION METHOD FOR LIVES

# EXAMPLES

# 1) How to get the HLS live stream URL

# 2) How to push a live stream via RTMP:

# 4) How to unsubscribe to a live event

# API POINTS USAGE

# HOW TO ASSIGN POINTS TO AN API USER VIA THE REUTERS CONNECT WEBSITE

# Scenario 1; API user isn’t a Marketplace subscriber.

# Scenario 2; API user is a Marketplace subscriber. Don’t need to control the API points usage.

# Scenario 3; API user is a Marketplace subscriber. Wants to control the API points usage.

# UPDATES, CORRECTIONS AND DELETIONS FOR PICTURES

# POSTMAN

# HOW TO DO GRAPHQL QUERIES IN POSTMAN

# SAMPLES OF QUERIES USING POSTMAN

# 1. How to get all RAW video clips

# 2. HOW TO GET ALL ITEMS USING A SLUG

# APPENDIX 1 - CONTENT FORMATS

# APPENDIX 2 – LANGUAGE CODES

# APPENDIX 3 - PICTURES RESTRICTIONS CODES

# APPENDIX 4 - VIDEO – MACHINE READABLE RESTRICTION TYPES

# APPENDIX 5 – LIVE EVENT RENDITIONS

REUTERS
© 2024 Reuters





5
Reuters API

# TECHNICAL SUPPORT

................................................................................................................................ 112

REUTERS

© 2024 Reuters




6
Reuters API

# INTRODUCTION

The Reuters API provides access to a comprehensive range of multimedia content, including live feeds, videos, pictures, graphics, audio, and ready-to-publish articles from Reuters and our Connect marketplace partners. This also includes access to our extensive video and picture archive dating back to 1896.

This document is designed to be used by the client developer, who will write and implement the code that interfaces with the Reuters API to which your organization is subscribed.

REUTERS/Pedro Nunes

REUTERS

© 2024 Reuters





Reuters API

# REVISION HISTORY

# Reuters API MVP Documentation

- Use cases added
- Query examples added
- Postman examples included
- Method descriptions included

# 1)

A new parameter was added called: derivedFrom: to know if an item is derived from another one.

# 2)

An extra pagination option was added called: page (all info in the doc).

# 1)

A new parameter called: derivedFrom to know if an item is derived from another (works for Online Reports). All the Online Reports derived from a text feed. DerivedFrom provides the item id.

# 2)

An extra pagination option was added, called: page. Allows to make pagination based on the number of items introduced in the limit parameter. An example was added.

# 3)

A new endpoint was added, called: filterOptions. An example was added.

- Feeds > marketplace: allows to see the current marketplace feeds categories [Free | Paid].
- Sources: Allows to see the source codes of the partners.
- Code: code of the partners
- Literal: literal name of the partners

# 4)

A new parameter called source. Allows to filter based on the source (for example, Red Bull, Anadolu, etc.). An example was added.

# 5)

A new parameter called feeds. Allows to filter Marketplace free and paid content. An example was added.

# 6)

It’s clarified that for TRIALs client is only allowed to access the API portal. If is a trial client and still want to access the API, needs to agree on a paid trial.

# 1)

A chapter that explains how to assign points to an API user via a Reuters Connect Admin page.

# 2)

How to use wildcards

# 3)

New examples about how to search several topic codes.

There are new filters in the Reuters API. Now are available the same filters as the Reuters Connect website, as shown below;

# Filters for

- MediaType (and its categories)
- Category (and its categories/sub-categories)
- Region (and its categories/sub-categories)

The date and source filters already exist.

# 1.

The rendition of the video_preview (stream:2128:16x9:mp4) has been removed from the documentation. This rendition will not be provided via the API. There are other renditions that the clients can use for the same purpose. Also, we provide the video screener.

# 2.

It has been included in the documentation that the infoSource > code: shows up the pictures.

# 3.

It has been clarified that when you use the search endpoint without a date range, it will retrieve the last 30 days of content by default.

# 4.

Document dates were updated to reflect the current year, 2024.

# 1.

A Quick Reference Guide chapter has been added. This chapter gives a basic overview of the API queries.

# 2.

The category parameter is deprecated but a subscriptions endpoint parameter has been added. channelCategory > code and name.

# 3.

contentCreated parameter explanation has been included.

REUTERS © 2024 Reuters



Reuters API

# 4. Picture restrictions codes - Appendix 3 added.

# 5. Video – Machine Readable Restriction Types – Appendix 4 added.

# 5. New parameters were added to allow data filtering depending on different date parameters.

Under the option parameter, it is possible to use the parameter: dateFilterField. This parameter allows you to filter based on:

- SORT_TIMESTAMP
- VERSION_CREATED
- FIRST_CREATED
- CONTENT_TIMESTAMP

# 6. New options have been added under the sort parameter.

Now, it will be possible to sort based on different date parameters, such as:

- VERSION_CREATED
- FIRST_CREATED
- CONTENT_TIMESTAMP

# 7. itemRevision endpoint added.

This endpoint helps to review the previous version of a specific item. Example included.

# 8. New examples added: search Method chapter).

- a) How to do a query search using variables
- b) How to get the top 10 items within an Online Report/Reuters Ready feed.
- c) How to do a query to search for items based on the FIRST_CREATED timestamp.
- d) How to do a query to search for items based on the FIRST_CREATED timestamp and sort by VERSION_CREATED.

1. Items method was deprecated and replaced by itemRevisions
2. A query example about how to exclude content.
3. A query example about how to retrieve video transcript (shotlist).
4. A query example about how to retrieve video closed captions (VTT and SRT)
5. Live video streams (Live API)

- Thumbnails with large dimension (640x640) Parameter /thumbnailUrlLarge
- Pull the latest content without content duplication. New parameter: cursorMode:POLL

© 2024 Reuters




9
Reuters API

# OVERVIEW

The Reuters API provides a set of functions and procedures which are a consistent way to programmatically access your subscribed content. It is based on GraphQL, an open-source data query language commonly used for APIs that allows the execution of queries using a type system.

This document provides the following:

1. You must obtain a list of data elements from Reuters (including your login credentials) to gain access to Reuters Web Services and retrieve the content you want.
2. Examples of the most used queries. For each sample query, the user could use it to obtain a response from the Reuters API.
3. A list of the renditions available for each media type.

# HOW GRAPHQL WORKS

GraphQL works based on typed schemas. The GraphQL schema is the syntax for writing queries and mutations, composed to get back the required information from the server. Since the structure of the data returned from the single GraphQL endpoint is flexible, the query must be particular in what it requires.

A GraphQL operation can either be a read or a write operation. A GraphQL query is used to read or fetch values, while a GraphQL mutation is used to write or post values. In either case, the operation is a simple string that a GraphQL server can parse and respond to with data in a specific format. The response format that is usually used for web applications is JSON.

REUTERS © 2024 Reuters





# 10

# Reuters API

# WHAT IS NEW IN THE API

The Reuters API allows you to access all our assets, such as text, pictures, graphics, video, live video and audio; in addition, it supports a flexible, points-based spending model that provides clients the freedom to access and utilize different content topics and asset classes – allowing for greater control of budgets as the Reuters Connect website does.

The essential news points content gives you unparalleled access to high-quality multimedia content from Reuters and other world-class media organizations - enabling you to tell deeper, richer stories that engage your audience and enhance your credibility.

The new API platform has been designed to improve editorial efficiency and streamline workflow, making research and content discovery quicker and easier.

In addition, to the flexible spending of your points, our usage-based spending model optimizes your budget and the return on your investment, but it also affords you a way to explore new content categories and discover alternative ways to grow your audience.

REUTERS

© 2024 Reuters






# 11

# Reuters API

# AUTHENTICATION

The Reuters Content API uses the OAuth2 security protocol to protect system and user security. We support two types of OAuth 2 flows.

# Client credentials flow

Machine-to-machine (M2M) applications, such as CLIs, daemons, or services running on the back end, the system authenticates and authorizes the app rather than the user.

# Authentication Code flow

Server-side regular web applications or single-page applications require exchanging of an authorization code for an access token. For single-page applications, we need additional security with a Proof Key for Code Exchange (PKCE).

Once successfully authenticated, we provide the client id credential in the form of an access token that will be issued. The Reuters Content API will verify the token and grant access to the API and all user functionalities.

REUTERS

© 2024 Reuters




12
Reuters API

# Reuters API Portal

The Reuters API Portal site https://api.reutersconnect.com/graphql/portal/ allows you to configure/test your queries and enjoy the experience of our API. Access to the API Portal is free for TRIAL clients.

Request access to the Media Technical Support by sending an email to: ReutersMediaSupport@thomsonreuters.com

# HOW TO ACCESS THE API

To obtain the API credentials (client_id, client_secret, and audience); it’s required:

- Contract signed with the Sales Team.

The Reuters Technical team will provide the API credentials; only if the above conditions are in place.

# How to obtain the Authentication Token.

After obtaining the client credentials, the access token is requested from the authorization server by the client. The protocol used is OAuth 2.0

# Get access to your TOKEN.

Besides the standard OAuth2 request parameters, it is necessary to provide the below audience and get a valid token.

The authentication token is used to identify you to the API Authentication servers and is valid for 24 hours.

POST https://auth.thomsonreuters.com/oauth/token

{
"client_id": "XXX",
"client_secret": "XXX",
"grant_type": "client_credentials",
"audience": "7a14b6a2-73b8-4ab2-a610-80fb9f40f769",
"scope":"https://api.thomsonreuters.com/auth/reutersconnect.contentapi.read
https://api.thomsonreuters.com/auth/reutersconnect.contentapi.write"
}

REUTERS

© 2024 Reuters




13
Reuters API

# TOKEN Best Practices

The correct and best practice for client applications/DAMs is to cache the access token returned until it expires. The access token has an "exp" timestamp as one of the claims, and you can use that to determine how long to cache the token. Alternatively, the /token response includes an "expires in" (expires_in": 86400); 86400 seconds = 24 hours. This claim that can be used to anticipate when the access token will expire. The clients should not get a new access token every time the client makes an API call to a resource server.

# TOKEN Error Access

The error scenario is a 401 Unauthorized access message.

# Throttling Error

To ensure a high level of service for all customers, requests to the Reuters API GraphQL are limited. Method requests are limited to 500 requests per minute. Requests to downloaded binary assets are counted separately and limited to 500 requests per minute.

# How to perform a Query

GraphQL Server supports only the post method, OAuth2 access token must be present in the request header. The request should be sent to https://api.reutersconnect.com/content/graphql

curl --request POST 'https://api.reutersconnect.com/content/graphql’ \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1VTXpPRU14TWpFeU0wWXhSa00yTWpWQ1JrTkd' \
--header 'Content-Type: application/json' \
--data-raw '{"query":"query MyQuery {\n currentUser {\n  email\n }\n search {\n  totalHits\n  items {\n  uri\n  type\n usn\n  versionCreated\n  language\n        slug\n  }\n }\n}","variables":{}}'

REUTERS
© 2024 Reuters





# 14

# Reuters API

How to access the Reuters API Portal

The Reuters API Portal site https://api.reutersconnect.com/graphql/portal/ allows you to configure/test your queries. Request access to the Media Technical Support by sending an email to: ReutersMediaSupport@thomsonreuters.com

# Endpoints

- To get token https://auth.thomsonreuters.com/oauth/token
- For query/mutation: https://api.reutersconnect.com/content/graphql

REUTERS

© 2024 Reuters




15
Reuters API

# METHODS SUMMARY TABLE

This section describes the content methods associated with the Reuters API.

| Provides all the account information of the API user, such as contacts, account id, last time logged in, and the list of the channels to which the API user is subscribed. | Populate a list of the API user channels list and account information.                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Provides the download history of the API user                                                                                                                              | Pull the list of all downloaded items and the points value.                                                                                                                                    |
| Retrieves all the options available to filter our content                                                                                                                  | Pull details for the code necessary to use to filter content.                                                                                                                                  |
| Retrieves item information as a JSON formatted                                                                                                                             | Pull details for an item returned in the items or search method.                                                                                                                               |
| Retrieves all the previous item versions of a specific item.                                                                                                               | Pull the previous version of a specific item                                                                                                                                                   |
| Provides the points balance of the API user if is a points content subscribed                                                                                              | Pull the API available points, overage points, and Trial points when the points expire.                                                                                                        |
| Obtains a list of items that match the search criteria provided by the API user                                                                                            | Retrieves the metadata for a specific search, such as all videos containing the word “cycling” in the title and published within the last three days and containing the topic code for France. |
| Provides all the live event information, such as status, headline, usage terms, event details (duration, start date, end date), and more.                                  | To populate a list of detailed information about a live event.                                                                                                                                 |
| Request to pull or push video of an event stream by providing the event id and rendition code, view existing subscriptions                                                 | Consume the content from a live event using the stream URL or pushing to a destination                                                                                                         |
| Retrieves the binary file requested.                                                                                                                                       | Download the rendition of a specific item and Subscribe and unsubscribe to a live event.                                                                                                       |

REUTERS

© 2024 Reuters






# Reuters API

# API QUICK REFERENCE GUIDE

This section shows up the most important queries to use the Reuters API after getting authentication token.

# 1.

Use the following query to obtain a list of the channels to which you have access/subscribed.

query MyQuery {
currentUser {
subscriptions {
alias
name
channelCategory {
code
name
}
}
}
}

# 2.

Use the following query to retrieve content for a specific channel (for example, Reuters World Service, channel alias: STK567 – text channel).

query MyQuery {
search(filter: {channel: "STK567"}) {
items {
headLine
versionedGuid
usn
uri
contentTimestamp
}
}
}

REUTERS

© 2024 Reuters



17
# Reuters API

1. Use the following query to retrieve the latest 20 stories during the last 24 hours.

query MyQuery {
search(filter: {maxAge: "24h"}) {
items {
headLine
type
contentTimestamp
versionedGuid
uri
usn
}
}
}

Use the following query to retrieve the latest 100 stories during the last 7 days.

query MyQuery {
search(filter: {maxAge: "7D"}, limit: 100) {
items {
headLine
type
contentTimestamp
versionedGuid
uri
usn
}
}
}

REUTERS

© 2024 Reuters






18
Reuters API

# 5.

Use the following query to retrieve the latest 20 package (composite) items from an Online Report/Reuters Ready channel (for example, US Online Report Top News, channel alias: FES376).

query MyQuery {
search(filter: {channel: "FES376", mediaTypes: COMPOSITE}) {
items {
headLine
type
contentTimestamp
versionedGuid
uri
usn
}
}
}

# 6.

Use the following query to retrieve the latest 20 pictures of your subscribed feeds and its renditions.

query MyQuery {
search(filter: {mediaTypes: PICTURE}) {
items {
caption
headLine
uri
renditions {
mimeType
uri
type
version
code
points
}
}
}

REUTERS
© 2024 Reuters




# Reuters API

1. Use the following mutation to download the NewsML (XML) from a text item. For example, itemID: tag:reuters.com,2024:newsml_KCN3640WS
mutation MyMutation {
download(
itemId: "tag:reuters.com,2024:newsml_KCN3640WS"
renditionId: "tag:reuters.com,2024:newsml_KCN3640WS"
) {
... on GenericItem {
url
}
}
}

2. Use the following mutation to download the Base image (JPEG) rendition from an image. For example,
itemId: tag:reuters.com,2024:newsml_RC2OX6AY5A8Q
renditionId: tag:reuters.com,2024:binary_RC2OX6AY5A8Q-BASEIMAGE
mutation MyMutation {
download(
itemId: "tag:reuters.com,2024:newsml_RC2OX6AY5A8Q"
renditionId: "tag:reuters.com,2024:binary_RC2OX6AY5A8Q-BASEIMAGE"
) {
... on GenericItem {
url
}
}
}

REUTERS

© 2024 Reuters





20
# Reuters API

# currentUser Method

The currentUser method is used to obtain the API account details, such as Reuters Account Manager, Reuters Account Manager name &#x26; email, and client contact information (business &#x26; technical contact), including the API feed subscriptions.

The currentUser method accepts the following parameters:

| PARAMETERS              | DEFINITION                                      |
| ----------------------- | ----------------------------------------------- |
| currentUser             |                                                 |
| account                 | Account name                                    |
| allowEmbeddedUrl        | Account with access to HLS/HDS stream links     |
| allowPublishMediaStream | Account with access to the RTMP service         |
| contacts                |                                                 |
| businessContact         | Account business contact                        |
| email                   | email of the business contact                   |
| name                    | full name of the business contact               |
| phone                   | phone number of the business contact            |
| reutersAccountManager   | Reuters Account Manager assigned to the account |
| Email                   | Reuters Account Manager email address           |
| name                    | Reuters Account manager Name                    |
| phone                   | Reuters Account Manager phone number            |
| technicalContact        | Technical contact assigned to the account       |
| Email                   | Technical contact email address                 |
| Name                    | Technical contact full name                     |
| phone                   | Technical contact phone number                  |

REUTERS © 2024 Reuters




21
Reuters API

# country

| alpha2Code | Two-letter country codes defined in ISO 3166-1   |
| ---------- | ------------------------------------------------ |
| Alpha3Code | Three-letter country codes defined in ISO 3166-1 |
| name       | Country name                                     |

# currency

| id   | Account id   |
| ---- | ------------ |
| name | Account name |

# pointsManagementAdmin

| email     | Email of the Points Management Admin      |
| --------- | ----------------------------------------- |
| Firstname | First name of the Points Management Admin |
| lastname  | Last name of the Points Management Admin  |

# pricePerPoint

| pricePerPoint     | Price of the points   |
| ----------------- | --------------------- |
| pricePerPointAsOf | Price per point as of |

# region

| region | Region of the Account |
| ------ | --------------------- |

# type

| type | Type of Account |
| ---- | --------------- |

# createdTimestamp

| createdTimestamp | Date when the API user was created (deprecated) |
| ---------------- | ----------------------------------------------- |

# createdAt

| email                     | Email of the API user                                              |
| ------------------------- | ------------------------------------------------------------------ |
| firstname                 | First name of the API user                                         |
| Id                        | API user ID number (used by Reuters – internal database id number) |
| isTrial                   | True if the account is trial; False if not.                        |
| lastChangedTimestamp      | Last time a change made to the API user (deprecated)               |
| lastChangedAt             |                                                                    |
| lastLoggedIn (deprecated) | Last time the API user was used.                                   |
| lastLoggedInAt            |                                                                    |
| lastName                  | Last name of the API user                                          |
| loginName                 | login name of the API user                                         |

REUTERS
© 2024 Reuters




22
# Reuters API

scriptFormat

Script format used in the account

subscriptions

List all the channel subscriptions.

alias

Channel alias of each channel

category (deprecated)

Channel category (text, picture, graphic, online reports, packaged video, broadcast video (raw video), archive video, archive pictures, audio)

name

channel name

channelCategory

| code | Channel code depending on its category. TXT: Text, PIC: Pictures, OLR: Online Reports; AUD: Audio, PICA: Archive Pictures; OLV: Online Video, GRA: Graphics, RVA: Archive Video, BRV: Broadcast Video |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name | Category name.                                                                                                                                                                                        |

channelId

Channel ID

# Examples

1) How to get the API user feeds/channel name/channel alias.

query MyQuery {
currentUser {
subscriptions {
alias
channelCategory {
code
name
}
channelId
name
}
}
}
REUTERS © 2024 Reuters




23
Reuters API

# downloadHistory Method

The downloadHistory method is used to obtain the API download history, select from a date range, limit the number of results, sort by order, and specify the start position next to the page and the list of items, including essential information.

| PARAMETERS      | DEFINITION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| downloadHistory |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| cursor          | token - first 60 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| from            | date format like "1996-12-19" specify the history start from, by default only recent 30 days history data return.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| limit           | limit the number of results – by default 20 (min: 1, max: 50)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| sort            | Sort by ascending or descending date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| to              | date format like "1996-12-19" specify the history end by.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| count           | Total number of items on the download history                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| cursor          | Shows up the cursor token of the downloadHistory. Specify the start position of the next page. The cursor parameter is used to specify the start position of the next page based on the query and sort criteria. Each search page returns a limited number of matching documents, and the "pageInfo" field tracks the pagination result across the search results based on current search queries and sort criteria. Repeat the same query and sort with the "endCursor" value on the last page until "hasNextPage" returns false to the page through a more extensive set of results. |
| items           | number of items downloaded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| downloadDate    | download date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| headline        | headline of the item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| points          | points cost of the item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| renditionId     | rendition id of the item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| slug            | slug of the item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| source          | source of the type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| type            | content type of the item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| versionedGuid   | versionedGuid of the item, last version id number of an item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

REUTERS
© 2024 Reuters




# Reuters API

# Examples

1. How to retrieve the download history of the API users.

© 2024 Reuters



25
# Reuters API

# filterOptions Method

The filterOptions method is used to obtain the API filter categories available in the Reuters Connect website (www.reutersconnect.com) displayed in the left side under the filter tab as shown in the following image:

| For Media Type         | For Category            | For Region      |
| ---------------------- | ----------------------- | --------------- |
| MEDIA TYPE             | CATEGORY                | REGION          |
| Select all             | Select all              | Select all      |
| Graphics               | Business & Finance      | Africa          |
| Flat                   | Sports                  | Central Africa  |
| Interactive            | American Football       | East Africa     |
| Packages               | Athletics               | North Africa    |
| Pictures               | Baseball                | Algeria         |
| Landscape              | Basketball              | Libya           |
| Portrait               | Boxing                  | Morocco         |
| Text                   | Cricket                 | Sudan           |
| Alerts                 | Cycling                 | Tunisia         |
| Top Stories of the Day | Esports                 | Western Sahara  |
| Exclusives             | Golf                    | Southern Africa |
| In-depth reporting     | Ice Hockey              | West Africa     |
| Explainers and context | Motor Sports            | Asia            |
| Human interest stories | Olympics                | Europe          |
| Other headlines        | Rugby                   | Latin America   |
| Schedules              | Soccer                  | Middle East     |
| In case you missed it  | Tennis                  | North America   |
| Video                  | Water Sports            | Oceania         |
| Captioned Video        | News                    | Other           |
| Raw                    | Environment             |                 |
| Ready To Publish       | Health                  |                 |
| Audio                  | Politics                |                 |
|                        | Science                 |                 |
|                        | Technology              |                 |
|                        | Entertainment & Leisure |                 |
|                        | The British Royals      |                 |
|                        | Collection              |                 |
|                        | Fashion                 |                 |
|                        | Lifestyle               |                 |
|                        | User Generated Content  |                 |
|                        | Creative Use            |                 |
|                        | Climate Change          |                 |
|                        | Human Interest Stories  |                 |

REUTERS

© 2024 Reuters






26
Reuters API

For Language

For Source (go to www.reutersconnect.com to see the complete list of Sources.)

# LANGUAGE

Select all  FILTER

- Arabic
- English
- French
- German
- Italian
- Japanese
- Portuguese
- Russian
- Spanish

# SOURCE

Select all

- Reuters
- Reuters Events
- Thomson Reuters Foundation
- A Starting Point
- Abaca Press
- AccuWeather
- AFLO
- AGIF
- Anadolu Agency
- AOP.Press
- ARK.Media
- Asian News International (ANI)
- Australian Associated Press (AAP)
- Australian Broadcasting Corporation (ABC)
- BANG Showbiz
- BBC
- Belgaimage
- BERNAMA
- Bildbyran
- Brazil Photo Press
- Caters News Agency
- CCTV Business
- CCTV+
- China News Service
- CNBC
- CNBC Africa
- CoinDesk
- Contrasto
- Cover Media
- Covering Climate Now

REUTERS © 2024 Reuters



27 Reuters API

# PARAMETERS

| categories      | The filter categories available are Business & Finance, Sports (and it’s sub-categories), News (sub-categories), Entertainment & Leisure (and it’s sub-categories), User Generated Content, Creative Use, Climate Change and Human Interest Stories. |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code            | Provides the code of the category                                                                                                                                                                                                                    |
| literal         | Provides the name of the category                                                                                                                                                                                                                    |
| uri             | Provides the identifier of the category needed for the API calls                                                                                                                                                                                     |
| NamedGroupQuery |                                                                                                                                                                                                                                                      |
| children        | Identify to request the children of the category                                                                                                                                                                                                     |
| code            | Provides the code of the sub-category                                                                                                                                                                                                                |
| literal         | Provides the name of the sub-category                                                                                                                                                                                                                |
| uri             | Provides the identifier of the sub-category needed for the API calls                                                                                                                                                                                 |

# feeds

| marketplace | Provides the Marketplace categories. |
| ----------- | ------------------------------------ |
|             | FREE: free content                   |
|             | PAID: points content                 |

# language

| code    | Provides the code of the category                                |
| ------- | ---------------------------------------------------------------- |
| literal | Provides the name of the category                                |
| uri     | Provides the identifier of the category needed for the API calls |

# mediaType

| The filter categories available are Graphics (sub-categories: Flat and Interactive), Packages, Pictures (sub-categories: Landscape and Portrait), Text (sub-categories: Alerts, Top Stories of the Day, Exclusives, In-depth reporting, Explainers and content, Human interest stories, Other headlines, Schedules and In case you missed it), Video (sub-categories: Captioned Video, Raw and Ready to Publish), and Audio (sub-categories: Natural Sound and Voice Package). |                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| code                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Provides the code of the category                                    |
| literal                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Provides the name of the category                                    |
| uri                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Provides the identifier of the category needed for the API calls     |
| NamedGroupQuery                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Endpoints to display the sub-categories                              |
| children                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Identify to request the children of the category                     |
| code                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Provides the code of the sub-category                                |
| literal                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Provides the name of the sub-category                                |
| uri                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Provides the identifier of the sub-category needed for the API calls |

# regions

| The filter allows to filter based on regions. Go to the www\.reutersconnect.com website to review all the region and sub-categories available. The full list is not listed here. |                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| code                                                                                                                                                                             | Provides the code of the category                                |
| literal                                                                                                                                                                          | Provides the name of the category                                |
| uri                                                                                                                                                                              | Provides the identifier of the category needed for the API calls |

REUTERS © 2024 Reuters



28
# Reuters API

# NamedGroupQuery

Endpoints to display the sub-categories

- children - Identify to request the children of the category
- code - Provides the code of the sub-category
- literal - Provides the name of the sub-category
- uri - Provides the identifier of the sub-category needed for the API calls

# sources

Provides the list of all the sources name of our contributors.

- code - Provide the code of a contributor.
- literal - Provides the literal name of a contributor

# Examples

1. How to query to see the categories list:

query MyQuery {
filterOptions {
categories {
code
literal
uri
}
}
}
2. How to query to see the sub-categories of the categories:

query MyQuery {
filterOptions {
categories {
code
literal
uri
... on NamedGroupQuery {
children {
code
literal
uri
}
}
}
}
}

REUTERS © 2024 Reuters




Reuters API

# 3. How to search for items under the category: Climate Change

Execute the query to search for the categories uri

query MyQuery {
filterOptions {
categories {
code
literal
uri
}
}
}

Then, it’s found that the uri is cat://climate. Use the search method and nameQueries and filter parameters to use the category uri as shown below:

query MyQuery2 {
search(filter: {namedQueries: {filters: "cat://climate"}}) {
totalHits
items {
headLine
usn
uri
}
}
}

# 4. How to search for items under the sub-category: News > Politics

Execute the query to look for the sub-categories, shown in the example 2. The uri of the sub-category – Politics is cat://news/pol

query MyQuery {
query MyQuery2 {
filterOptions {
search(filter: {namedQueries: {filters: "cat://news/pol"}}) {
feeds {
totalHits
marketplace
items {
} }  headLine
}         usn
uri
}
}
}
}

© 2024 Reuters





30
Reuters API

# 5. How to search for items under the media type sub-category: Video > Raw

Execute the query to look for the sub-categories, shown in the example 2. The uri of the sub-category – Raw is med://vid/raw

query MyQuery {
query MyQuery2 {
filterOptions {
search(filter: {namedQueries: {filters: "med://vid/raw"}}) {
feeds {
totalHits
marketplace
items {
}
headLine
}
usn
uri
}
}
}
}

# 6. How to search for two or more options. Category: Business and Source: Reuters

query MyQuery3 {
search(filter: {namedQueries: {filters: ["cat://bus", "src://rtrs"]}}) {
totalHits
items {
headLine
uri
usn
}
}
}

# 7. How to query to see the sub-category of a sub-category.

query MyQuery {
filterOptions {
regions {
code
literal
uri
... on NamedGroupQuery {
children {
code
literal
uri
... on NamedGroupQuery {
uri
children {
code
literal
uri
}
}
}
}
}
}
}

REUTERS
© 2024 Reuters





# 8. How to see the available Marketplace feeds categories.

query MyQuery {
filterOptions {
feeds {
marketplace
}
}
}

# 9. How to see the sources list and its code, names and uri.

query MyQuery {
filterOptions {
sources {
code
literal
uri
}
}
}

REUTERS

© 2024 Reuters





32
# Reuters API

# Item Method

The item method is used to retrieve a particular news item JSON formatted. To invoke this method, you must know the item ID of the news item you wish to retrieve. You may use the items or search method to obtain the desired item ID.

# PARAMETERS

| Id             |                                                                                                                           | retrieve latest version of the item with full details, only accept versionGuid or Uri.                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | versionedGuid: last version item id                                                                                       |                                                                                                                                                             |
|                | uri: first version item id                                                                                                |                                                                                                                                                             |
| option         | completeSentences                                                                                                         | option to retrieve fragments as complete sentences and is defaulted to a false value.                                                                       |
|                | dateFilterField                                                                                                           | Allow content filtering depending on different date parameters. This parameter allows you to filter based on:                                               |
|                | CONTENT\_TIMESTAMP                                                                                                        | Timestamp referred to as the "Date Taken" or "Original Date Time," is a piece of data that indicates the exact date and time when the photograph was taken. |
|                | FIRST\_CREATED                                                                                                            | timestamp when the first version was created                                                                                                                |
|                | SORT\_TIMESTAMP                                                                                                           | Timestamp filed for sorting content, that corresponds to the contentTimeStamp.                                                                              |
|                | VERSION\_CREATED                                                                                                          | timestamp when this version item was created                                                                                                                |
| fragmentLength | define the length of the fragment to be retrieved. The default value when not specified is 200, and the max value is 400. |                                                                                                                                                             |
| previewMode    | Direct                                                                                                                    | it provides the direct URL of our CDN server of the /thumbnailURL or /previewURL parameters. URL TTL (Time To Live) is 5 minutes.                           |
|                | Redirect                                                                                                                  | it provides the non-direct URL of the /thumbnailURL or /previewURL parameters                                                                               |
| altID          | Alternative identities id of a news object                                                                                |                                                                                                                                                             |
|                | eaid                                                                                                                      | eaid                                                                                                                                                        |
|                | editNumber                                                                                                                | Video id number                                                                                                                                             |
|                | iid                                                                                                                       | iid                                                                                                                                                         |
|                | otr                                                                                                                       | otr                                                                                                                                                         |
|                | rpid                                                                                                                      | Reuters Picture website picture id                                                                                                                          |
|                | sid                                                                                                                       | sid                                                                                                                                                         |
|                | tpcid                                                                                                                     | tpcid                                                                                                                                                       |
|                | tpguid                                                                                                                    | tpguid                                                                                                                                                      |

REUTERS © 2024 Reuters




33
Reuters API

usn unique story number. this is the same identifier as the guid

vid vid

associations items associations if apply

audio Audio information of the item

bodyXhtml html of the body of the item

bodyXhtmlRich xhtml of the body of the item

byLine The name(s) of the creator(s) of the content

caption Picture description, restriction, and Editorial notes

channels Where the item has been published

contentCreated Timestamp when the item was created.

contentMetaExtProperty Content metadata external property

qcode topic code associated

rel rel of the qcode

contentTimestamp Timestamp referred to as the "Date Taken" or "Original Date Time," is a piece of data that indicates the exact date and time when the photograph was taken.

contributor Any necessary copyright notice for claiming the intellectual property for the content

code code associated to the contributor

literal literal code

role role associated to the contributor

copyrightNotice Any necessary copyright notice for claiming the intellectual property for the content

copyrightHolder Copyright holder of the item

copyrightHolderIds Copyright holder id if the copyright holder has one

credit Content owner

dateLine Date mentioned on the article

derivedFrom Provides the item id and information if an item belongs from another item.

destination The point(s) of destination of this item

evolvedFrom Shows when an item evolved from another item

uri Uri of the item from where it evolved from

versionedGuid versionedGuid of the item from where it evolved from

exclAudience Exclusions codes applied to an item

firstCreated timestamp when the first version was created

fragment For text and video, by default it represents up to the first 200 characters of the body of the news item. For pictures/graphics, by default it represents up to the first 200 characters of the caption of the news item

genre Genre codes indicate the nature of the news object, not specifically its content. For example, if a news item is a Press Release, the item would contain the ‘N2:NEWR’ genre code.

© 2024 Reuters





Reuters API

# 34

| code    | code of the genre |
| ------- | ----------------- |
| literal | literal code      |
| name    | name of the genre |

# headline

A brief and snappy introduction to the content, designed to catch the reader's attention

# infosource

The sources of the news object.

| code    | code of the source | Xcode for the pictures |
| ------- | ------------------------------------------- |---|
| literal | literal name of the source                  | |
| role    | role code of the source                     | |

# intro

| itemMetaExtProperty | item metadata external property            |
| ------------------- | ------------------------------------------ |
| rel                 | internal code                              |
| value               | channel alias where the item was published |
| valueDataType       | valueDataType                              |

# keyword

Terms relate to the content

# language

language of the item

# position

# previewUrl

Preview ULR of the item. To use this URL, it is necessary to append the bearer token. Make use the redirection URL within your CMS system to display the image. URL TTL (Time To Live) is 5 minutes.

# productLabel

A description of the product type, for example slideshow, story-package, top-story-list

# profile

An identifier for the kind of content of this news object

# pubStatus

The publishing status of the news object, its value is usable by default

# relatedItems

Related items associated to the item

# renditions

Wrapper for different renditions of non-textual content of the news object

| mimeType | Multipurpose Internet Mail Extensions |
| -------- | ------------------------------------- |
| uri      | Rendition id of the rendition.        |
| type     | Type of item                          |
| version  | Version of the rendition              |
| code     | Rendition code name                   |
| points   | Points value of the rendition         |

# signal

Edit status of an item

- "edStat:N", New
- "edStat:U", Update
- "edStat:C", Correction
- "edStat:D", Deletion

# slug

The slug of this item, or short name used to identify it

© 2024 Reuters





Reuters API

# 35

# sortTimeStamp

Timestamp filed for sorting content, it's typically the same as the content timestamp.

# source

| code    | Code of the source of the item |
| ------- | ------------------------------ |
| literal | Name of the source of the item |

# subject

| code | qcode                  |
| ---- | ---------------------- |
| name | name of the topic code |
| rel  | rel of the qcode       |

# subjectLocation

| city               | city name related where the item was created |
| ------------------ | -------------------------------------------- |
| countryCode        | country code                                 |
| countryName        | country name                                 |
| CountrySubdivision | country subdivision if applied               |

# thumbnailUrl

Thumbnail URL of the item. Dimensions 300x300. To use this URL, it is necessary to append the bearer token. Make use the redirection URL within your CMS system to display the image. URL TTL (Time To Live) is 5 minutes.

# thumbnailUrlLarge

Thumbnail URL of the item. Dimensions 640x640. To use this URL, it is necessary to append the bearer token. Make use the redirection URL within your CMS system to display the image. URL TTL (Time To Live) is 5 minutes.

# type

type of item, it could be text, picture, online reports, broadcast video, archive

# urgency

The editorial urgency of the content from 1 to 9. 1 represents the highest urgency, 9 the lowest. The urgency parameter is equivalent to the “priority” parameter in the NewsML-g2 schema.

- <urgency>1</urgency> Alert
- <urgency>2</urgency> Urgent news
- <urgency>3</urgency> High priority news
- <urgency>4</urgency> Normal news

To search based on the urgency/priority; use the priority parameter.

# uri

The identifier for this rendition

# usageTerms

usage terms of the item

# usageTermsRole

usage terms of the item

# usn

unique story number. this is the same identifier as the guid

# version

The version of the news object which is identified by the uri property

# versionCreated

timestamp when this version item was created

# versionProcessed

timestamp when this version was processed in our internal systems

# versionedGuid

The globally unique identifier of the target item (guid) which also includes the version identifier

# Examples

1. How to perform a query of a specific item and all its associations

© 2024 Reuters




36
# Reuters API

The following query allows to retrieve an item complete information. The item_ID is equivalent to the uri parameter.

query MyQuery {
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

# 2. How to retrieve a picture item with all renditions.

The following query allows to retrieve picture, graphics, and audio renditions. It is necessary to use only the renditions parameter to retrieve all the renditions.

query MyQuery {
item(id: "item_ID") {
renditions {
mimeType
remotePath
type
uri
version
... on ImageRendition {
mimeType
fileName
format
rendition
version
width
}
}
}
}

REUTERS © 2024 Reuters



37
# 3. How to retrieve an Online Reports/Reuters Ready/Pictures Packages/Video Packages

The Online Reports/Reuters Ready consist of a package that contains a text and multimedia content such as picture(s), and/or video(s). Also, this applies to pictures and video packages.

The query to get all the package renditions is:

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
mimeType
uri
type
version
code
points
}
associations {
renditions {
mimeType
uri
type
version
code
points
}
}
}
}
}

If you want only to get the picture renditions; the query to get all the picture renditions is:

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
mimeType
uri
type
version
code
points
}
}
}
}

REUTERS

© 2024 Reuters





38
# Reuters API

If the item includes a video; the query to get the video renditions is:

- to download the video rendition from a package, you must use the video uri and video rendition uri.

query MyQuery {
item(id:"item_ID") {
associations {
renditions {
mimeType
uri
type
version
code
points
}
associations {
renditions {
mimeType
uri
type
version
code
points
}
}
}
}
}

NOTE: To download/mutation the picture or the video item, make sure to use the picture uri or video uri, and not the text uri.

# 4. How to retrieve a video item with all renditions

The following query allows to retrieve video item and packaged video renditions, it is necessary to use the associations and renditions parameter to retrieve all the renditions.

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
mimeType
remotePath
type
uri
version
}
}
}
}

REUTERS

© 2024 Reuters





Reuters API

# 5. How to retrieve a video item with all renditions information/parameters

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
code
mimeType
type
uri
version
... on VideoRendition {
mimeType
fileName
audioBitRate
audioSampleRate
colourIndicator
duration
code
format
height
sizeInBytes
type
uri
version
videoAspectRatio
videoAvgBitrate
width
}
}
}
}
}

# 6. How to get the items qcodes (Topic Codes)

The following query allows to get the items Topic Codes.

query MyQuery {
item(id: "item_ID") {
subject {
code
name
rel
}
}
}

REUTERS © 2024 Reuters




40
Reuters API

# 7. How to see the points value of an item rendition, for example a picture

query MyQuery {
item(id: "item_ID") {
renditions {
points
}
}
}

# 8. How to see the points value of an item rendition, for example a video

query MyQuery {
items(id: "item_ID") {
associations {
renditions {
... on VideoRendition {
points
}
}
}
}
}

# 9. How to see the direct download URL of an image preview or thumbnail

query MyQuery {
item(
id: "item_ID"
option: {previewMode: DIRECT}
) {
previewUrl
thumbnailUrl
}
}

REUTERS
© 2024 Reuters




41
# Reuters API

# 10. How to retrieve a video transcript (shotlist.JSON)

The shotlist is the video transcript, Avista-based transcripts. The shotlist file is referred as machine generated metadata that is time coded. Fully automated contains:

- Transcription
- Translation to English &#x26; Spanish
- Scene lists
- Person appearing recognition
- Speaker recognition

The first step is to retrieve a video transcript (shotlist) is to make a query using the video id to get listed all the renditions as shown below:

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
mimeType
remotePath
type
uri
version
}
}
}
}
Then, make use of the shot_list rendition (uri) to make use of the mutation.

mutation MyMutation {
download(
itemId: "tag:reuters.com,2024:newsml_xxxxxxxxxxxxx"
renditionId: "tag:reuters.com,2024:binary_xxxxxxxxxxxxx-STREAM:SHOTLIST:JSON"
) {
... on GenericItem {
url
}
}
}
REUTERS

© 2024 Reuters






42
Reuters API

# 11. How to retrieve a video closed captions (VTT and SRT)

The video transcripts of English package video also available as standard SRT and VTT subtitle files. The first step is to retrieve a video closed captions is to make a query using the video id to get listed all the renditions as shown below:

query MyQuery {
item(id: "item_ID") {
associations {
renditions {
mimeType
remotePath
type
uri
version
}
}
}
}

Then, make use of the VTT or SRT rendition (uri) to make use of the mutation.

mutation MyMutation {
download(
itemId: "tag:reuters.com,2024:newsml_xxxxxxxxxxxxx"
renditionId: "tag:reuters.com,2024:binary_xxxxxxxxxxxxx-STREAM:CLOSEDCAPTION:SRT"
) {
... on GenericItem {
url
}
}
}

REUTERS

© 2024 Reuters





43
# Reuters API

# itemRevisions Method

The itemRevisions method is used to obtain the previous version of a selected item.

The itemRevisions method accepts the following parameters:

| PARAMETERS         | DEFINITION                                                                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                 | retrieve latest version of the item with full details, only accept versionGuid or Uri. versionedGuid: last version item id uri: first version item id |
| includeAllVersions | true: If this is true, it includes the item's previous versions. false: If it is false, it will not include the item's previous versions              |

# Item parameters

This endpoint will provide all the parameters of the item method.

# Examples

# 1. How to see an item previous versions

Use the following query to see the previous versions. If you want to download/mutation any of the previous version of an item id, make use of the versionedGuid id.

query MyQuery {
itemRevisions(
id: "item_id"
includeAllVersions: true
) {
byLine
headLine
caption
versionedGuid
uri
language
type
profile
slug
}
}
REUTERS

© 2024 Reuters





Reuters API

# pointsBalance Method

The pointsBalance method is used to obtain the API points balance.

| PARAMETERS      | DEFINITION                 |
| --------------- | -------------------------- |
| asOf            | points available asOf date |
| availablePoints | points available           |
| grantEnd        | points ending date         |
| grantStart      | points starting date       |
| grantedPoints   | granted points provided    |
| isTrial         | trial points               |
| overagePoints   | overage points             |

# Examples

# 2. How to see the Points available and points information

The following query allows to retrieve the points information of the customer account.

query MyQuery {
pointBalance {
asOf
availablePoints
grantStart
grantEnd
grantedPoints
isTrial
overagePoints
}
}

REUTERS © 2024 Reuters



Reuters API

# Search Method

The search method is used to obtain a list of news items matching your search criteria. This method provides more advanced filtering options than those offered with the items method and full-text search capabilities.

| PARAMETER                                                                                                                                                                                                                                                                                                                                          | DEFINITION                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |   |   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | - |
| cursor                                                                                                                                                                                                                                                                                                                                             | The cursor parameter is used to specify the start position of the next page based on the query and sort criteria. Each search page returns a limited number of matching documents, and the "pageInfo" field tracks the pagination result across the search results based on current search queries and sort criteria. Repeat the same query and sort with the "endCursor" value on the last page until "hasNextPage" returns false to the page through a more extensive set of results. |   |   |
| filter                                                                                                                                                                                                                                                                                                                                             | Filter parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |   |   |
| channel                                                                                                                                                                                                                                                                                                                                            | specify the channel alias to be used when retrieving news items and use comma to separate multiple values. By default, if no channel alias is supplied, all channels to which you subscribe will be returned. To see the subscribed channels list, go to currentUser > subscriptions > alias.                                                                                                                                                                                           |   |   |
| channelCategories specify the channel categories to be used when retrieving news items. A channel category is a group of channels containing similar content (e.g. Online Reports, Pictures, or Online Video). If both channel and channelCategory parameters are supplied, both fields will be used to calculate the full set of channels to use. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   |   |

| name            | code |
| --------------- | ---- |
| Text            | TXT  |
| Pictures        | PIC  |
| Graphics        | GRA  |
| Online Video    | OLV  |
| Online Reports  | OLR  |
| Broadcast Video | BRV  |
| Live Broadcast  | LBRV |
| Live Online     | LOLV |
| Archive Picture | PICA |
| Interactive     | ITRA |
| Archive Video   | RVA  |
| Live Video      | LVID |
| Audio           | AUD  |

dateRange This parameter makes use of the contentTimestamp of the item. Specify the date range for the news items to be retrieved. By default, if no date range filter is supplied, the news items returned will be limited to the last month. The date range should be specified as &#x3C;start_date>-&#x3C;end_date> (e.g 2023.06.01-2023.06.04 for news items from 00:00 on June 1 to 00:00 on June 4th). If a start date is

REUTERS © 2024 Reuters



Reuters API

specified without an end date, the assumed end date will be the current time. For information on specifying date formats, refer to the Date format used when specifying input.

If you want to filter based on different date parameters, please make use of the parameter option dateFilterField

# feeds

This option allows you to filter the Marketplace free and paid (points) content.

# geography

Filter by geography. It is based on the Geography codes ISO-3166 https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes (it could be used the Alpha-2 and/or Alpha-3 codes)

# languages

filter by language. This parameter is used to specify the primary language associated with the news items to be retrieved.

You must use a 2-letter code to specify the language. If multiple languages are specified, each must be separated by a comma. Example: language=ES, languages: ES

Refer to Appendix 2 for a list of valid 2-letter language codes.

Default Value: All available languages will be considered.

# maxAge

This parameter is used to provide a date limit relative to the current date and time. This filter will be translated into a date range using the current time as the starting point. This parameter should be specified in the format maxAge=&#x3C;Positive Number>&#x3C;Unit>

<unit> can be one of the following:</unit>

- s – for seconds
- m – for minutes
- h – for hours
- D – for days

Examples: maxAge=2D will retrieve results limited to the past 2 days, maxAge=6h will retrieve results from the last 6 hours.

Default Value: 24h

Note: When both maxAge and dateRange are specified in a request, maxAge will be ignored

# mediaTypes

Filter by mediaTypes.

This parameter is used to specify the media type for the news items to be retrieved.

Valid media types are T (text), P (pictures), V (video), G (graphics) and C (composite i.e. a package of content containing references to other items) and Audio.

If multiple media types are specified, each should be specified in a separate query string parameter. Example:

mediaTypes: TEXT, mediaTypes: PICTURE

Default Value: All available media types will be considered.

# namedQueries

This option allows to search using all the options mentioned on the “filterOption” method chapter. It’s necessary to specify the named query uri to be used to retrieved news items.

# filters

used to insert the query uri of the namedQueries.

# source

Filter by source. Specify filter feed sources by feed code. All supported feed codes can be retrieved through the “feedSource” endpoint.

# topicCodes

Used to specify the topic codes (i.e., NewsML News2000 subject codes) associated with the news items to be retrieved.

All the topic codes are available at https://liaison.reuters.com/tools/topic-codes

# limit

This parameter is used to designate the maximum number of news items to be retrieved. The current limit is 100, but Reuters reserves the right to change this value at any time. If no limit is specified, the default number of news items returned will be 20.

REUTERS © 2024 Reuters



Reuters API

# 47

# page

This parameter is used to designate a specific page of search results to retrieve. The first page is 1 and if no value is specified for the page parameter, the default is 1. The maximum number of news items returned per page is constrained by the limit parameter. The maximum number of page is constrained by the combination of page and limit, page * limit must be less than 2500. If the cursor parameter is specified, the page parameter will be ignored.

# option

- completeSentences - option to retrieve fragments as complete sentences and is defaulted to a false value.
- cursorMode
- - POLL - The parameter cursorMode:POLL enables periodic polling for all new content available, excluding items that have already been polled.
- It is important to specify both the sort direction (sort:{direction: ASC}) and the field (field:DATE) in the cursorMode configuration to get the correct behavior.
- SEARCH - The parameter cursorMode:SEARCH will work as the regular “cursor” mode by default.
- The cursor parameter is used to specify the start position of the next page based on the query and sort criteria. Each search page returns a limited number of matching documents, and the "pageInfo" field tracks the pagination result across the search results based on current search queries and sort criteria. Repeat the same query and sort with the "endCursor" value on the last page until "hasNextPage" returns false to the page through a more extensive set of results.

dateFilterField - Allow content filtering depending on different date parameters. This parameter allows you to select which date parameter the filter “dateRange” is based on:
- - CONTENT_TIMESTAMP - Timestamp referred to as the "Date Taken" or "Original Date Time," is a piece of data that indicates the exact date and time when the photograph was taken.
- FIRST_CREATED - timestamp when the first version was created
- SORT_TIMESTAMP - Timestamp filed for sorting content, that corresponds to the contentTimeStamp.
- VERSION_CREATED - timestamp when this version item was created

fragmentLength - define the length of the fragment to be retrieved. The default value when not specified is 200, and the max value is 400.
- previewMode

# query

See the Query Parameter chapter

# sort

This parameter is used to designate the sort order. The supported values are “DATE”, “SCORE”, “VERSION_CREATED”, “FIRST_CREATED”, “CONTENT_TIMESTAMP”. Score is the relevance score.

- direction - Ascendent or Descendent
- field

© 2024 Reuters




Reuters API

# VERSION_CREATED

timestamp when this version item was created

# FIRST_CREATED

timestamp when the first version was created

# CONTENT_TIMESTAMP

Timestamp referred to as the "Date Taken" or "Original Date Time," is a piece of data that indicates the exact date and time when the photograph was taken.

# SCORE

Numeric value representing the ranking of this news item within the set of total results in relation to the search criteria used. Score can be seen using the relevance score parameter.

# items

Please refer to the ItemMethod chapter

# mediaType

# Breakdown

| count | Provides the numeric number of items available                                                                                |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| name  | P refers to Pictures, T refers to Text, C refers to Composite, V refers to Video, A refers to Audio and G refers to Graphics. |

# pageInfo

| endCursor   | endCursor token information                       |
| ----------- | ------------------------------------------------- |
| hasNextPage | if the search has next page or not: true or false |

# totalHits

Total number of findings

REUTERS

© 2024 Reuters




49
# Reuters API

# Examples

# 1. How to get all subscribed content or map all available items.

The following query allows to provide the list of all items within all channels:

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

# 2. How to retrieve content from a specific channel.

Select any channel alias from the ones shown on currentUser Method section (Example 1) and execute the following query to get the content from a specific channel, for example, channel “Reuters World News,” channel alias: “STK567” – if you know your channel alias ask our Technical Support Team.

query MyQuery {
search(filter: {channel: "channel_alias"}) {
items
}
}

# 3. How to do a search using an interval of time (dateRange)

To get assets using an interval date, it is necessary to use the dateRange parameter.

The dateRange parameter is used to specify the date range for the news items to be retrieved. The date range should be specified as &#x3C;start_date>-&#x3C;end_date> (For example, 2023.03.01-2022.03.05 for news items from 00:00 on April 1 to 00:00 on April 5th). If a start date is specified without an end date, the assumed end date will be the current time.

This query will give you all the picture information of each item.

REUTERS © 2024 Reuters



50 Reuters API

query MyQuery {

search(filter: {mediaTypes: PICTURE, dateRange: "2023.03.01-2023.03.05"}) {

items {

byLine

caption

contentTimestamp

copyrightNotice

credit

firstCreated

headLine

keyword

language

}

}

}

# 4. How to get the total number of items distributed by the topicCodes: CMPNY and DIP

The Reuters World Service channel alias is STK567. All the content related to “Company News” and “Diplomacy” comes with the topic code: N2:CMPNY and N2:DIP.

query MyQuery {

search(

filter: {channel: "STK567", topicCodes: ["CMPNY", " DIP"]}

) {

totalHits

}

}

# 5. How to get the direct URL of the /previewURL or /thumbnailUrl or /thumbnailUrlLarge

- Direct URL: it provides the direct link from our CDN servers to download the thumbnail or the preview image (with watermark). URL TTL (Time To Live) is 5 minutes.
- Redirect URL: it provides the redirect URL of our CDN servers to download the thumbnail or the preview image. From here, it is necessary to check the redirection URL to see the Direct URL. URL TTL (Time To Live) is 5 minutes.

REUTERS © 2024 Reuters



Reuters API

# 6. How to filter for Marketplace content (free and paid/points)

This option allows you to filter the free content of our Marketplace content.

query MyQuery {
search(filter: {feeds: {marketplace: FREE}}) {
totalHits
}
}

Also, you can filter to see all the Marketplace content (free and points)

query MyQuery {
search(filter: {feeds: {marketplace: [FREE,PAID]}}) {
totalHits
}
}

# 7. How to get filter using the source feed code.

It’s necessary to specify the source feed code. All supported feed codes can be retrieved through the “filterOption” endpoint. For example, filtering using the code of our contributor: Anadolu Agency.

Use the filterOptions to search for the source code as:

query MyQuery {
filterOptions {
sources {
code
literal
}
}
}

Filter by source code of Anadolu Agency. The code is: ANADL. Filter as:

REUTERS © 2024 Reuters



52
# Reuters API

query MyQuery {
search(filter: {sources: "ANADL"}) {
totalHits
}
}

# 8. How to use the cursor parameter for pagination

The cursor parameter is used to specify the start position of the next page based on the query. Each search page returns a limited number of matching documents, and the "pageInfo" field tracks the pagination result across the search results based on current search queries and sort criteria. Use this query to get the start position of the next page using the endCursor parameter.

query MyQuery {
search {
totalHits
pageInfo {
endCursor
hasNextPage
}
}
}

On your next query, use the “endCursor” token in the “cursor” parameter, and use again the “endCursor” to get the start position of the next page.

query MyQuery {
search(cursor:
"WzE2ODg3NTM2NDgzNzAsInRhZzpyZXV0ZXJzLmNvbSwyMDIzOm5ld3NtbF9NVDFQQU5QMj
cyMTA2MDI4NiJd") {
totalHits
pageInfo {
endCursor
hasNextPage
}
}
}

Repeat the same query and sort with the "endCursor" value on the last page until "hasNextPage" returns false to the page through a more extensive set of results.

# 9. How to use the page parameter for pagination

This parameter is used to designate a specific page of search results to retrieve. The first page is 1 and if no value is specified for the page parameter, the default is 1. The maximum number of news items returned per page is constrained by the limit parameter. The maximum number of pages is constrained by the combination of page and limit, page * limit must be less than 2500. If the cursor parameter is specified, the page parameter will be ignored.

REUTERS © 2024 Reuters



53
# Reuters API

query MyQuery {
search(page: 1, limit: 10) {
totalHits
items {
uri
}
pageInfo {
hasNextPage
}
}
}

# 10. How to search for items under the category: Business &#x26; Finance

Execute the query to search for the categories uri

query MyQuery {
filterOptions {
categories {
code
literal
uri
}
}
}

Then, it’s found that the uri is cat://bus. Use the search method with the name Quieres and filter parameters to use the category uri as shown below:

query MyQuery2 {
search(filter: {namedQueries: {filters: "cat://bus"}}) {
totalHits
items {
headLine
usn
uri
}
}
}

# 11. How to search for items under the sub-category: Sports > Cycling

Execute the query to look for the sub-categories.

REUTERS © 2024 Reuters



54
# Reuters API

query MyQuery {
filterOptions {
categories {
code
literal
uri
... on NamedGroupQuery {
children {
code
literal
uri
}
}
}
}
}

The uri of the sub-category – Politics is cat://spo/cycling

Use the search method, including the name Quieres and filter parameters to use the category uri as shown below:

query MyQuery2 {
search(filter: {namedQueries: {filters: "cat://spo/cycling"}}) {
totalHits
items {
headLine
usn
uri
}
}
}

# 12. How to search for items under the media type sub-category: Video > Raw

Execute the query to look for the sub-categories, shown in the example 11.

The uri of the sub-category – Raw is med://vid/raw

query MyQuery {
query MyQuery {
filterOptions {
search(filter: {namedQueries: {filters: "med://vid/raw"}}) {
feeds {
totalHits
marketplace
items {
} }  headLine
}         usn
uri
}
}
}

REUTERS

© 2024 Reuters






55
Reuters API

# 13. How to search for two or more options.

Category: Business and Source: Reuters

query MyQuery {
search(filter: {namedQueries: {filters: ["cat://bus", "src://rtrs"]}}) {
totalHits
items {
headLine
uri
usn
}
}
}

REUTERS

© 2024 Reuters






56
Reuters API

# 14. How to search for a sub-category of a sub-category, for example, Europe > South Europe > Spain

Execute the query to search for the uri of sub-categories of a sub-category.

query MyQuery {
filterOptions {
regions {
code
literal
uri
... on NamedGroupQuery {
children {
code
literal
uri
... on NamedGroupQuery {
uri
children {
code
literal
uri
}
}
}
}
}
}
}

Then, it’s found that the uri is reg://europ/seu/es. Use the search method with the nameQuieres and filter parameters to use the category uri as shown below:

query MyQuery2 {
search(filter: {namedQueries: {filters: "reg://europ/seu/es"}})
{
totalHits
items {
headLine
usn
uri
}
}
}

REUTERS
© 2024 Reuters




57
# Reuters API

# 15. How to do a query search using variables

The below query allows you to use variables. In this case, the variables are the “page” parameter and the “limit” parameter. The query allows you to search for picture items under a dateRange using specific topic codes.

query MyQuery ($pageAmount: Int, $limitAmount: Int) {
search(option: {previewMode: DIRECT}, page: $pageAmount, limit: $limitAmount, query: "main: pope",
filter: {mediaTypes: PICTURE, dateRange: "1800.01.01-2023.09.07", topicCodes: ["SPO", "SCI", "REL",
"POL", "ODD", "DIS", "CRIM", "CLJ", "CWP", "ENT"]}, ) {
items {
slug
byLine
credit
firstCreated
keyword
uri
type
headLine
caption
usageTerms
thumbnailUrl
previewUrl
copyrightHolder
copyrightNotice
usn
}
totalHits,
}
}

# Variables

{
"pageAmount": 2,
"limitAmount": 5
}

REUTERS © 2024 Reuters




# Reuters API

# 16. How to get the top 10 items from an Online Reports/Reuters Ready channels

Make a search to the channel alias and get the id of the Link List item. The headline should show as: “OXXX Link List”

Execute the query to search for the uri and headline under a specific channel.

query MyQuery {
search(filter: {channel: "channel_alias", mediaTypes: COMPOSITE} {
items {
uri
versionedGuid
type
headLine
}
}
}

The Link List item headline shows as: "headLine": "OXXXX Link List"

Then, make a query using the Link List uri and call their associations.

query MyQuery {
item(id: "link_list_uri") {
associations {
byLine
copyrightNotice
versionCreated
fragment
headLine
caption
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
usn
position
intro
}
}
}

REUTERS

© 2024 Reuters





Reuters API

# 17. How to search by first_created parameter

Execute the query to search for items based on the first_created parameter

query MyQuery {
search(
filter: {dateRange: "2000.01.01-2000.01.10"}
option: {dateFilterField: FIRST_CREATED}
) {
items {
uri
contentCreated
contentTimestamp
sortTimestamp
firstCreated
relevanceScore
}
}
}

# 18. How to search by first_created parameter and sort by version_created parameter

Execute the query to search for items based on the first_created and sort by version_created.

query MyQuery {
search(
filter: {dateRange: "2000.01.01-2000.01.10"}
option: {dateFilterField: FIRST_CREATED}
sort: {direction: ASC, field: VERSION_CREATED}
) {
items {
uri
contentCreated
contentTimestamp
sortTimestamp
firstCreated
relevanceScore
}
}
}

© 2024 Reuters



60
# Reuters API

# 19. How to use the cursorMode:POLL to periodically poll for new content, excluding items that have already been polled.

The parameter cursorMode:POLL enables periodic polling for all new content available, excluding items that have already been polled.

- It is important to specify both the sort direction (sort:{direction: ASC}) and the field (field:DATE) in the cursorMode configuration to get the correct behavior.
- The cursor changes with every page, especially when reaching the last page.
- When there are no new items, the last page can have zero items.
- The "hasNextPage" flag will be false if there are no more items, but new items can still appear on the current page if the limit parameter is not reached.
- Values show up on the same page if the limit parameter is greater than the number of results on the last page. In other words, the new results will appear at the end of this page, and hasNextPage=false.
- Values show up on a new page with hasNextPage=true if the limit parameter value is lower than the number of results on the last page.

For example, if the current date is June 26, 2025 and you wish to poll for the last 30 minutes, your first request to get the endCursor would be as follows:

query pullToken {
search(
option: {cursorMode: POLL}
filter: {channel: "STK567", dateRange: "2025.06.26.10.00-2025.06.26.10.30"}
sort: {direction: ASC, field: DATE}
query: "slug:\"IRAN-NUCLEAR\""
) {
totalHits
pageInfo {
hasNextPage
endCursor
}
items {
contentTimestamp
slug
}
}
}
REUTERS © 2024 Reuters



61
# Reuters API

You will get an endCursor value in the query response. If the hasNextPage=true, it means that there are more results on the following pages. If the hasNextPage=false, the current page contains all the results.

Assuming you get hasNextPage=true, the following query should contain the “cursor” parameter with the endCursor value of the previous query as:

query pullToken2 {
search(
option: {cursorMode: POLL}
filter: {channel: "STK567", dateRange: "2025.06.26.10.00-2025.06.10.30"}
sort: {direction: ASC, field: DATE}

cursor:"WzE3NDkxNTYzMTA1OTAsInRhZzpyZXV0ZXJzLmNvbSwyMDI1Om5ld3NtbF9
GV04zUzgwS1kiXQ=="
query: "slug:\"IRAN-NUCLEAR\""
) {
totalHits
pageInfo {
hasNextPage
endCursor
}
items {
contentTimestamp
slug
}
}
}

Repeat the above query until the hastNextPage=false, which means no more new items are available). It is suggested that you repeat all the steps in this procedure at a regular interval (for example, every 60 seconds) to ensure that you continually obtain new content.

REUTERS © 2024 Reuters




# 62

# Reuters API

Query Parameter

This parameter is a string used to specify the attributes by which the news items returned should be filtered.

The query parameter filters are specified in the following manner:

Note: If multiple filters are used, each must be separated by the || (double pipe) delimit.

For the query filter parameter, escaped quotation marks for matching text are required.

For example; slug:\"reuters-next\"

For example; main: \"joe biden\"

The query parameter can be used with the following filters.

REUTERS

© 2024 Reuters




# Reuters API

# Filter Options

Boolean operators - Reuters supports the use of AND, OR and AND NOT to refine the way terms with a search are applied.

Grouping (nesting) – Reuters allows you to use the parenthesis symbols ( ) to group/nest terms and/or phrases within a search. For example, if your search contained, “bird flu” AND (China OR europe) AND immunizations it would mean that you wanted all news items containing the phrase bird flu and the term immunizations and either the term China or Europe.

Inclusion / Exclusion modifiers (+, -) - Reuters supports the use of modifiers to explicitly require that data specified by a particular filter be included in or excluded from the news items returned.

- The plus symbol (+) indicates that the data specified after the “+” symbol must be present somewhere in the news items returned.
- Example: To search for documents that must contain “cricket” and may contain “England”, use the query: +cricket England

The minus symbol (-) indicates that the data specified by the filter must NOT be present in the news items returned.

Note: The absence of either a plus or minus symbol indicates that the data specified by the filter is optional (although the presence of this data in a news item will increase its score).

# Wildcards

The Reuters API supports the use of the * (asterisk) and ? (question mark) wildcards within search terms.

- The asterisk character (*) is used to substitute for zero or more characters.
- The ? (question mark) is used to substitute for any single character.

headline, slug, body and caption will search for “containing” keywords while the signal will look for exact matches.

Reuters does not support the use of wildcard characters at the beginning of a single search term or within an explicit phrase (Example: “board of health”).

REUTERS © 2024 Reuters







# 64

# Reuters API

# Examples

# 1. How to do a search/query using two parameters

The following query allows to search using the topic code for Sports, which is SPO, and for a word in the headline, in this case: nadal.

query MyQuery {
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

# 2. How to search for two words within the Headline parameter

The following query allows to search for two words within the Headline parameter using a Boolean operator.

query MyQuery {
search(query: "headline:(cycling OR france)") {
items
}
}

# 3. How to search using one parameter and filtering by media type

The following query allows to search using one parameter and filter by MediaType.

query MyQuery {
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

REUTERS

© 2024 Reuters





65
# Reuters API

# 4. How to search two or more media types:

The following query allows searching two different media types, such as text or picture, for example.

query MyQuery {
search(filter: {mediaTypes: [TEXT, PICTURE]}) {
items {
byLine
}
}
}
# 5. How to search two or more channel alias:

query MyQuery {
search(filter: {channel: ["fal605", "gzy495"]}) {
items {
versionedGuid
}
}
}
# 6. How to get the total number of RAW clips with the slug: “Reuters-Next”

query MyQuery {
search(query: "slug:\"reuters-next\"") {
totalHits
}
}
# 7. How to query using the item USN supplied by Reuters

For example, Picture USN: RC2Y5X9RVD61. Use the parameter “signal” to retrieve the edit status (edStat).

query MyQuery {
search(query:
"id:RC2Y5X9RVD61") {
items {
uri
signal
}
}}
REUTERS

© 2024 Reuters





66
# Reuters API</h8>
# 8. How to query using the item signal.</h9>
To search for the complete list of pictures with the edStat:D, including the picture id (usn), signal and URI information, the query should be:

query MyQuery {
search(query: "signal:\"edStat:D\"") {
items {
Uri
signal
usn
}
}
}

# 9. How to query using the item ID</h9>
This query allows you to search using the item_id; itemID:

tag:reuters.com,2022:newsml_RC22XX9RKI89:468160593
query MyQuery {
search(query: "id:\" tag:reuters.com,2022:newsml_RC22XX9RKI89:468160593\"") {
items {
Uri
signal
usn
}
}
}

REUTERS

© 2024 Reuters






67
Reuters API

# 10. How to query using the priority/urgency parameter.

The item priority, restricted to the values 1-9 (inclusive), where 1 is the highest priority and 9 is the lowest. Priority would be used by a transmission system to determine the order in which a message is transmitted, relative to others in a queue. Urgency is an editorial judgement expressing the relative news value of an item.

query MyQuery {
search(query: "priority:1") {
totalHits
}
}

# 11. How to query using wildcards.

The use of the * (asterisk) can be used within search terms as wildcards. The asterisk character (*) is used to substitute for zero or more characters. For example, if you want to search for items similar to the id: L4N3A62FI; it’s possible to add the * (asterisk) at the beginning and end.

query MyQuery {
search(query: "id:*4N3A62F*") {
items {
versionedGuid
}
}
}

The question mark (?) is used to substitute for any single character. For example, looking for the item id UP1EJ8P0ZF1I5. Make use of the same length of characters.

query MyQuery {
search(query: "id:UP1EJ8P0Z????") {
items {
versionedGuid
}
}
}

REUTERS
© 2024 Reuters




68
# Reuters API

Also, could be used for headline, slug, body, and caption. The API will search for “containing” keywords.

query MyQuery {
search(query: "headline:soc??r") {
items {
headLine
}
}
}

An example, using the caption parameter and the ? (question mark).

query MyQuery {
search(query: "caption:ge?m?ny") {
items {
headLine
caption
}
}
}

# 12. How to exclude content

If you want to exclude content out of the search results, as for example, exclude content that contains the words “Link List” within the headline, please make a query as follow.

query excludeContent {
search(
filter: {channel: "channel_alias", mediaTypes: COMPOSITE}
query: "-headline:\"Link List\""
limit: 100
) {
items {
uri
versionedGuid
type
headLine
contentTimestamp
}
}
}

REUTERS
© 2024 Reuters



69
# Reuters API

# Mutation Method

The mutation parameter is an operation of GraphQL used in our case to download content.

| download          | To any item rendition                                                        |
| ----------------- | ---------------------------------------------------------------------------- |
| isWatermarked     | To retrieve an image with the watermark (not applied to videos)              |
| true              | If true is selected, it will generate a Watermark rendition of the item      |
| false             | If false is selected, it will not generate a Watermark rendition of the item |
| itemID            | Corresponds to the item versionedGuid                                        |
| rendtionID        | Corresponds to the rendition uri of the item                                 |
| Type              | Text, picture, video, audio, etc.                                            |
| Type              | Display the type of item                                                     |
| GenericItem       |                                                                              |
| url               | Download URL                                                                 |
| type              | Type of item requested                                                       |
| Interactive       |                                                                              |
| embededCode       | Embedded code for Interactive content                                        |
| type              | Type of item requested                                                       |
| downloadPackage   | Download the package of an item                                              |
| itemID            | VersionedGuide of the package                                                |
| Ulr               | Download URL                                                                 |
| Status            | Status of the package request                                                |
| downloadStoryText | Download the item full text.                                                 |
| itemId            | Corresponds to the item versionedGuid                                        |
| Type              | Display the type of item                                                     |
| GenericItem       |                                                                              |
| type              | Display the type of item                                                     |
| url               | Download URL                                                                 |

REUTERS © 2024 Reuters



70
# Reuters API

# Examples

# 1. How to perform a mutation/download – Text Item (fetch items)

The following query allows to download a text item (XML) file

mutation MyMutation {
download(
itemId: "item_ID"
renditionId: "item_ID"
) {
... on GenericItem {
url
type
}
}
}

# 2. How to perform a mutation/download – Package (fetch items)

The following query allows to download an item package

mutation MyMutation {
downloadPackage(itemId: "ITEM_ID") {
url
}
}

# 3. How to perform a mutation/download of an image renditions

The following query allows to download a picture rendition. There are four pictures’ renditions (viewImage, thumbnail, baseImage and limitedImage – see Appendix 1).

To download the rendition “limitedImage”, for example, the mutation query is as follow; within the itemID use the versionedGuid of the picture and within the renditionID use the uri of the LIMITED rendition.

For example, itemID of the picture: tag:reuters.com,2021:newsml_RC2ZJN92Q51R:1904928654

uri of the LIMITED rendition: tag:reuters.com,2021:binary_RC2ZJN92Q51R-LIMITEDIMAGE

mutation MyMutation {
download(
itemId: "tag:reuters.com,2021:newsml_RC2ZJN92Q51R:1904928654"
renditionId: "tag:reuters.com,2021:binary_RC2ZJN92Q51R-LIMITEDIMAGE"
) {
... on GenericItem {
url
}
}
}

REUTERS © 2024 Reuters




# 4. How to perform a mutation/download of a video renditions

There are plenty of video renditions, see our Appendix 1. To download the rendition “hd1080i50”, for example, the mutation query is as follow; within the itemID use the ID of the video and within the renditionID use the uri of the video rendition.

For example, itemID of the video: tag:reuters.com,2022:newsml_WD601320062022RP1:4

uri of the video rendition: tag:reuters.com,2022:binary_LWD601320062022RP1-STREAM:13756:16X9:HD1080I50:MP4

mutation MyMutation {
download(itemId: "tag:reuters.com,2022:newsml_WD601320062022RP1:4",
renditionId: " tag:reuters.com,2022:binary_LWD601320062022RP1-
STREAM:13756:16X9:HD1080I50:MP4") {
... on GenericItem {
url
type
}
}
}

# 5. How to perform a mutation/download of an image

mutation MyMutation {
download(
isWatermarked: true
itemId: "item_ID"
renditionId: "uri_renditionID"
) {
type
... on GenericItem {
url
}
}
}

REUTERS

© 2024 Reuters






# Reuters API

This section is designed to be used by developers, who will write and implement the code that interfaces with the Reuters Live video streams. The Reuters API includes a reference implementation of the Live Production Exchange (LPX) recommendation for live video.

Reuters Live streams are currently available for HLS, and RTMP.

Reuters Live streams are also available under the Live tab on the www.reutersconnect.com website as shown below:

| REUTERS CONNECT | Feed                                                                        | Planning | Live  | Stock                                                                         | 3428P | 115 | My Account |
| --------------- | --------------------------------------------------------------------------- | -------- | ----- | ----------------------------------------------------------------------------- | ----- | --- | ---------- |
| TODAY           | Friday, September 20th                                                      |          |       | 24 hrsNow                                                                     |       |     |            |
| STATUS          | SLUG                                                                        | START    | end   | PlayL                                                                         |       |     |            |
| live            | ISRAEL-PALESTINIANS/LEBANON-                                                | 02:34    | TBD   | ①                                                                             |       |     |            |
| live            | ISRAEL-PALESTINIANS/LEBANON                                                 | 03:43    | TBD   | 0                                                                             |       |     |            |
| T live          | ISRAEL-PALESTINIANS/NORTHERN BORDER-EAST                                    | 03:51    | TBD   | ②                                                                             |       |     |            |
| live            | UKRAINE-CRISIS/RUSSIA FOREIGNMINISTRY-ENGLISH TRANSLATION-UPDATED LOCATION- | 08:09    | TBD   |                                                                               |       |     |            |
| live            | BRITAIN-HARRODS/AL UPDATED SPEAKER DETAILS                                  | 10:48    | 12:00 |                                                                               |       |     |            |
| scheduled       | ISRAEL-PALESTINIANS/LEBANON-HEALTH MINISTER                                 | 14:30    | 13:20 |                                                                               |       |     |            |
| scheduled       | RELIGION-BRITAIN                                                            | 14:30    | TBD   |                                                                               |       |     |            |
| scheduled       | FARAGE -UPDATED START TIME AND SPEAKERS                                     | 16:15    | TBD   |                                                                               |       |     |            |
| scheduled       | BOXING-HEAVYWEIGHT DUBOIS-JOSHUA/WEIGH IN                                   | 20:00    | 18:45 |                                                                               |       |     |            |
| scheduled       | UN-SUMMIT/GUTERRES                                                          | 19:45    | TBD   | LIVE                                                                          |       |     |            |
| scheduled       | CLIMATE-CHANGE/USA PROTEST-POSSIBLE                                         | 19:45    | TBD   | Overview Clip & Download                                                      |       |     |            |
| scheduled       | ISRAEL-PALESTINIANS/HEZBOLLAH-UN                                            | 20:45    | TBD   | A view of the western side of Israel's border with Lebanon                    |       |     |            |
| scheduled       | UKRAINE-CRISIS/EU-TAPE REPLAY                                               | TBD      | TBD   |                                                                               |       |     |            |
| cancelled       | APPLE-CHINA/                                                                | 02:45    | 05:00 | NORTHERN ISRAEL - A view of the western side of Israel's border with Lebanon. |       |     |            |

REUTERS © 2024 Reuters



73
# Reuters API

# LIVE VIDEO SIGNALS QUICK REFERENCE GUIDE

This section shows up the most important queries to retrieve the video live signals information via the Reuters API after getting authentication token.

# 1. How to retrieve the start/end date and event status of the live events

query MyQuery {
liveEvents {
events {
id
headline
eventStatus
eventDetails {
dates {
startDate
endDate
}
}
}
}
}

# 2. How to retrieve an event rendition

query MyQuery {
liveEvents {
events {
renditions {
code
name
frameRate
scanType
aspectRatio
frameSize
minBitrate
maxBitrate
bitrate
}
}
}
}

REUTERS
© 2024 Reuters





# 3. How to subscribe to an event and get back an HLS URL

To subscribe to an event, it’s required to have the “eventId" and the rendition “code”.

For example,

eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"

code: "hls:29.97"

mutation MyMutation {
liveEventSubscribe(
eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"
renditionCode: "hls:29.97"
) {
subscriptionId
url
}
}

# 4. How to subscribe to an event and get back an RTMP stream

To subscribe to an event, it’s required to have the “eventId" and the rendition “code”.

For example,

eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"

code: " rtmp:29.97:4096"

And it’s required to provide the RTMP destination URL and RTMP stream key.

The “rtmpDestinationUrl” should be structured as: RTMP destination URL + RTMP stream key, such as:

rtmps://your.server.com:port/your.app/your.stream.key

REUTERS

© 2024 Reuters





75
# Reuters API

For example, the following mutation is to push a stream to Facebook, where the:

- RTMP server URL: rtmps://live-api-s.facebook.com:443/rtmp/
- Stream key: FB-1561648428024292-0-AbzMquS2JFKB6k1L

mutation MyMutation {
liveEventSubscribe(
eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"
renditionCode: "rtmp:29.97:4096"
rtmpDestinationUrl: "rtmps://live-api-s.facebook.com:443/rtmp/ FB-1561648428024292-
0-AbzMquS2JFKB6k1L"
) {
subscriptionId
url
}
}

# 5. How to unsubscribe from an event

To unsubscribe to an event, it’s required to use the “subscriptionId” provided on the mutation response of “liveEventSubscribe”. See the preview query.

mutation MyMutation {
liveEventUnsubscribe(subscriptionId: "d3793a9172a4") {
message
}
}

REUTERS © 2024 Reuters



76
# Reuters API

# liveEvents Method

The liveEvents method obtains all the live event information via the API, such as status, headline, usage terms, event details (duration, start date, end date), and more.

| PARAMETERS       | TYPE   | DEFINITION                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | JSON REPRESENTATION                                             |
| ---------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| channels         | String | Filter based on the customer-subscribed channels.                                                                                                                                                                                                                                                                                                                                                                                                                                       | "jbh288"                                                        |
| cursor           | String | The cursor parameter is used to specify the start position of the next page based on the query and sort criteria. Each search page returns a limited number of matching documents, and the "pageInfo" field tracks the pagination result across the search results based on current search queries and sort criteria. Repeat the same query and sort with the "endCursor" value on the last page until "hasNextPage" returns false to the page through a more extensive set of results. | "WzE3MTgxMDA1NDAxXJzL mNvbSwyMDI0Om5ld3NtbF9L QkU5OVQwM1kiXQ==" |
| dateRange        | String | To filter using dates. The date range should be specified as \<start\_date>-\<end\_date>. Date format: YYYY-MM-DD.                                                                                                                                                                                                                                                                                                                                                                      | "2024.01.01-2024.02.02"                                         |
| eventIdentifiers | Scalar | To filter using a live event by id, uri or usn.                                                                                                                                                                                                                                                                                                                                                                                                                                         | "uri": "9767edef-d472-4109-aaa5-1260424bd0d3"                   |
| limit            | Int    | This parameter is used to designate the maximum number of news items to be retrieved. The current limit is 100, but Reuters reserves the right to change this value at any time. If no limit is specified, the default number of news items returned will be 20.                                                                                                                                                                                                                        | "10"                                                            |
| page             | Int    | This parameter is used to designate a specific page of search results to retrieve. The first                                                                                                                                                                                                                                                                                                                                                                                            |                                                                 |

REUTERS © 2024 Reuters




77
Reuters API

page is 1 and if no value is specified for the page parameter, the default is 1. The maximum number of news items returned per page is constrained by the limit parameter. The maximum number of page is constrained by the combination of page and limit, page * limit must be less than 2500. If the cursor parameter is specified, the page parameter will be ignored.

# events

Object Live event results

events:{}

# contentCreated

Scalar The date and time when this live event was created

"contentCreated": "2024-02-05T17:07:25.599Z"

# copyrightHolder

String Corporation for the time being in possession of the copyright of the live event.

"copyrightHolder": "Thomson Reuters"

# copyrightNotice

String Any necessary copyright notice for claiming the intellectual property for the live event.

"copyrightNotice": “(c) 2024 Thomson Reuters, unless otherwise identified.
Full statement available at https://www.thomsonreuters.com/en/policies/copyright.html

# eventDetails

Object Property containing details of the event.

# dates

Scalar Dates and times for this event.

"dates": {}

# startDate

Scalar The start date of live event.

"startDate": "2024-02-07T12:07:02.000Z"

# endDate

Scalar The end date of the live event

"endDate": "2024-02-12T17:55:06.000Z"

# expected Duration

String Duration of the live event

"duration": "5 Days 5 Hours 48 Minutes"

# eventStatus

Enum Status of the event, categories are: Cancelled, Scheduled, Live, and Completed.

"eventStatus": "canceled"

# genre

Object Genre codes indicate the nature of the live event, not specifically its content.

# name

String Genre name

"Sport news"

# code

String Genre topic or category code

N2: SPO

REUTERS © 2024 Reuters





Reuters API

# 78

# literal

| String      | Genre literal name                                                                                                               |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| headline    | A brief and snappy introduction to                                                                                               |
|             | “headline” : “Nikki Haley bus tour in Bamberg, South Carolina                                                                    |
| id          | String                                                                                                                           |
|             | Live event stream unique identifier                                                                                              |
|             | "id": "9767edef-d472-4109-aaa5-1260424bd0d3"                                                                                     |
| language    | String                                                                                                                           |
|             | language of the live item                                                                                                        |
|             | "language": "en"                                                                                                                 |
| located     | String                                                                                                                           |
|             | The location where the live event happens.                                                                                       |
|             | “location” : “BAMBERG, SOUTH CAROLINA                                                                                            |
| renditions  | Object                                                                                                                           |
|             | An array of objects, each of which is a rendition of the event.                                                                  |
|             | The Appendix 5 contains all the rendition list.                                                                                  |
| aspectRatio | String                                                                                                                           |
|             | Live event aspect ratio. We only offer a 16:9 aspect ratio.                                                                      |
|             | "16:9"                                                                                                                           |
| bitrate     | String                                                                                                                           |
|             | Signal bitrate. There are different options.                                                                                     |
|             | "8000Kbps"                                                                                                                       |
| code        | String                                                                                                                           |
|             | Live video profile code. There are different options. Unique identifier                                                          |
|             | "hls:29.97"                                                                                                                      |
| frameRate   | String                                                                                                                           |
|             | Live event frame rate. There are different options.                                                                              |
|             | "29.97"                                                                                                                          |
| frameSize   | String                                                                                                                           |
|             | Live event frame Size                                                                                                            |
|             | "1920x1080"                                                                                                                      |
| minBitrate  | String                                                                                                                           |
|             | Minimum bitrate provided                                                                                                         |
|             | "200Kbps"                                                                                                                        |
| maxBitrate  | String                                                                                                                           |
|             | Maximum bitrate provided                                                                                                         |
|             | "4Mbps"                                                                                                                          |
| name        | String                                                                                                                           |
|             | Live video profile name.                                                                                                         |
|             | "200Kbps-4Mbps Video: 1080p29.97 h.264"                                                                                          |
| scanType    | String                                                                                                                           |
|             | Live event scan type. We only offer progressive scan type.                                                                       |
|             | "progressive"                                                                                                                    |
| slugline    | String                                                                                                                           |
|             | Item slug or short name used to identify an event. Slugs are a Reuters editorial mechanism used to standardize content by event. |
|             | They are combinations of 2 or 3 words describing a news event – a string of keywords. For example, GLOBAL-CLIMATECHANGE/         |
| topic       | String                                                                                                                           |
|             | Indicates subject of the event                                                                                                   |
|             | “Topic” : “Politics / International Affairs”                                                                                     |
| uri         | String                                                                                                                           |
|             | Live event story unique number                                                                                                   |
|             | "uri": "tag:reuters.com,2024: Newsml\_ADKQ4TP20"                                                                                 |

REUTERS © 2024 Reuters




79

# Reuters API

| usageTerms     | String  | Usage terms of the live event, it will display the live event restrictions. | "usageTerms": "Broadcast: No use UK, Digital: No use UK"        |
| -------------- | ------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| usn            | String  | Live event story unique number. Same identifier as the uri                  | "usn": "ADKQ4TP20"                                              |
| version        | String  | Version of the live event                                                   | "version": "681326751"                                          |
| versionCreated | Scalar  | Date when the current version was created                                   | "versionCreated": "2024-02-14T17:55:06.000Z"                    |
| pageInfo       | Object  | Search results page information                                             |                                                                 |
| endCursor      | String  | endCursor token information                                                 | "WzE3MTgxMDA1NDAxXJzL mNvbSwyMDI0Om5ld3NtbF9L QkU5OVQwM1kiXQ==" |
| hasNextPage    | Boolean | if the search has next page or not: true or false                           | "true"                                                          |
| totalHits      | Scalar  | Total number of findings                                                    | "8"                                                             |

# Examples

# 1. How to retrieve the start/end date and event status of the live events

query MyQuery {
liveEvents {
events {
id
headline
eventStatus
eventDetails {
dates {
startDate
endDate
}
}
}
}
}

REUTERS © 2024 Reuters





Reuters API

# 2. How to retrieve live events using the dateRange

The dateRange criteria should be specified as <start_date>-<end_date>. Date format: YYYY-MM-DD.</end_date></start_date>

query MyQuery {
liveEvents(dateRange: "2024.09.01-2024.09.05") {
totalHits
events {
eventDetails {
dates {
endDate
}
}
}
}
}

# 3. How to retrieve an event rendition

The complete list of stream renditions is on the Appendix 5.

query MyQuery {
liveEvents {
events {
renditions {
code
name
frameRate
scanType
aspectRatio
frameSize
minBitrate
maxBitrate
bitrate
}
}
}
}

© 2024 Reuters




81
Reuters API

# 4. How to filter content based on event uri, id or usn

The following query allows you to filter content based on event uri, id or usn.

The three identifiers may look like:

"id": "f0191d53-8be7-4674-b593-17b5d162e842",
"uri": "tag:reuters.com,2024:newsml_ADKQ9DK9K",
"usn": "ADKQ9DK9K"

The following query is using the uri.

query MyQuery {
liveEvents(eventIdentifiers: "\"tag:reuters.com,2024:newsml_ADKQ9DK9\"") {
events {
headline
language
located
}
}
}

The following query is using the usn.

query MyQuery {
liveEvents(eventIdentifiers: "ADKQ9DK9") {
events {
headline
language
located
}
}
}

REUTERS
© 2024 Reuters





82
# Reuters API

# liveEventSubscriptions Method

The liveEventSubscriptions method is used to provide information about existing live event subscriptions of an API user.

| PARAMETERS     | TYPE   | DEFINITION                                                                                                         | JSON REPRESENTATION                    |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| dateRange      | String | To filter using dates. The date range should be specified as \<start\_date>-\<end\_date>. Date format. YYYY-MM-DD. |                                        |
| eventIds       | Scalar | To filter using live event ids (unique identifiers per event)                                                      | "2554f23f-05a1-435c-ab5b-adf614025d20" |
| types          | Enum   | To filter based on the type of subscription (HLS, HDS, RTMP)                                                       |                                        |
| eventId        | String | The unique identifier of the event                                                                                 |                                        |
| subscriptions  | Object | Property containing details of subscriptions                                                                       |                                        |
| renditionCode  | String | Identifier of a particular rendition of an event                                                                   | "hls:29.97"                            |
| rtmpUserName   | String | Username parameter for the RTMP destination in a push subscription request                                         |                                        |
| subscriptionId | String | Unique identifier of the event                                                                                     | "3c9802025ee68bdb120f"                 |
| url            | String | Location to the content rendition for a pull rendition (e.g HLS)                                                   |                                        |

# Examples

1) How to get the current live events the API user is subscribed to:

query MyQuery {
liveEventSubscriptions {
eventId
subscriptions {
subscriptionId
renditionCode
url
rtmpUserName
}
}
}

REUTERS © 2024 Reuters



83
# Reuters API

# Mutation Method for Lives

The mutation method used for lives allows you to subscribe and unsubscribe to a live event.

# PARAMETERS

| Type   | Definition           | JSON REPRESENTATION                                                                                                                                                          |
| ------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object | liveEventSubscribe   |                                                                                                                                                                              |
| Scalar | eventId              | "1140e03a-05e1-4d80-b4a0-89698434b028"                                                                                                                                       |
| String | renditionCode        | "hls:29.97"                                                                                                                                                                  |
| String | rtmpDestinationUrl   |                                                                                                                                                                              |
| String | rtmpPassword         |                                                                                                                                                                              |
| String | rtmpUserName         |                                                                                                                                                                              |
| String | srtDestinationUrl    | srt://your.server.com:portnumber/your.stream.key                                                                                                                             |
| String | srtKeyLength         | Your encryption key length with algorithm, e.g. AES\_128, AES\_192, AES\_196, need to match your receivers setting                                                           |
| String | srtPassPhrase        | Your encryption passphrase                                                                                                                                                   |
| String | subscriptionId       | "c6d2af76b714bcb6490a"                                                                                                                                                       |
| String | url                  | "https\://d3cgfqae8o6oiw\.cloudfront.net/RL/smil:EU-1140e03a-05e1-4d80-b4a0-89698434b028.smil/3856324909234557211370536214628957630wsauy2xfxsfli8y9viamv8579l/playlist.m3u8" |
| Object | liveEventUnsubscribe |                                                                                                                                                                              |
| String | subscriptionId       | "1140e03a-05e1-4d80-b4a0-89698434b028"                                                                                                                                       |
| String | message              | "Subscription c6d2af76b714bcb6490a is removed"                                                                                                                               |

REUTERS © 2024 Reuters




84
# Reuters API

# Examples

# 1) How to get the HLS live stream URL

The first step is to subscribe to an event.

To subscribe to an event, it’s required to have the “eventId" and the rendition “code”.

For example,

To get the “eventId" and the rendition “code”, use the following query:

query MyQuery {
liveEvents {
events {
headline
id
renditions {
code
}
}
}
}
From the response get the following parameters

- eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"
- code: "hls:29.97"

To generate the live video stream URL, use the following query:

mutation MyMutation {
liveEventSubscribe(
eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"
renditionCode: "hls:29.97"
) {
subscriptionId
url
}
}
# 2) How to push a live stream via RTMP:

Use the following mutation to subscribe to an event and push a live stream via RTMP.

REUTERS © 2024 Reuters



85
# Reuters API

To subscribe to an event, it’s required to have the “eventId" and the rendition “code” using the liveEvents method as shown below.

To get the “eventId" and the rendition “code”, use the following query:

query MyQuery {
liveEvents {
events {
headline
id
renditions {
code
}
}
}
}

From the response get the following parameters, for example,

eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"
code: " rtmp:29.97:4096"

And it’s required to provide the RTMP destination URL and RTMP stream key.

The “rtmpDestinationUrl” should be structured as: RTMP destination URL + RTMP stream key, such as:

rtmps://your.server.com:port/your.app/your.stream.key

For example, the following mutation is to push a stream to Facebook, where the:

RTMP server URL: rtmps://live-api-s.facebook.com:443/rtmp/
Stream key: FB-1561648428024292-0-AbzMquS2JFKB6k1L

mutation MyMutation {
liveEventSubscribe(
eventId: "1c104b45-6b07-41ee-8e78-d3793a9172a4"
renditionCode: "rtmp:29.97:4096"
rtmpDestinationUrl: "rtmps://live-api-s.facebook.com:443/rtmp/ FB-1561648428024292-
0-AbzMquS2JFKB6k1L"
) {
subscriptionId
url
}
}

REUTERS © 2024 Reuters




86
Reuters API

# 4) How to unsubscribe to a live event

To unsubscribe to an event, it’s required to use the “subscriptionId” provided on the mutation response of “liveEventSubscribe”. See the preview query.

mutation MyMutation2 {
liveEventUnsubscribe(subscriptionId: "3c9802025ee68bdb120f") {
message
}
}

REUTERS

© 2024 Reuters






Reuters API

# API Points Usage

How to assign points to an API user via the Reuters Connect website.

This section explains the possible subscription scenarios for the Reuters Marketplace content (points). The Marketplace content consists of the content provided by our 3rd party Contributors. There are three possible scenarios for the API users.

# Scenario 1; API user isn’t a Marketplace subscriber.

Your organization isn’t a Marketplace points content subscriber. It means that your API user can search within the Marketplace content but can’t download points content but can filter for the FREE content. To filter for FREE content, look at chapter Search Method, example: 6.

If your organization is a Marketplace (points) content subscriber, and you would like to download the Marketplace content via the API, there are two possible scenarios 2 and 3.

# Scenario 2; API user is a Marketplace subscriber. Don’t need to control the API points usage.

Your organization doesn’t have a Reuters Connect points Administrator but is a Marketplace points content subscriber, which means all the points available are accessible to the API user and all the Reuters Connect account users. If you want to assign a Reuters Connect user as a points Administrator, please get in touch with our Support Team at ReutersMediaSupport@thomsonreuters.com.

Once there is a points Administrator user, please follow Scenario 3 steps.

# Scenario 3; API user is a Marketplace subscriber. Wants to control the API points usage.

Your organization does have a Reuters Connect points Administrator, which means that it is necessary to assign points to your API user if you want to download Marketplace content via the API.

To assign points to your API user, follow these steps:

1. The Reuters Connect User points Administrator should access the “My Organization” page https://www.reutersconnect.com/my-organization as shown below:

REUTERS © 2024 Reuters





Reuters API

PTS    My Account

7509   166

0 Poln     My Settings

My Organization

Download History

Privacy Policy

ed 10    Copyright Notice

Website Terms

# 2.

Verify that you can see your API user on the Reuters Connect website “My Organization” page. Click over Users, and select only API users as shown below:

REUTERS CONNECT             Feed            Planning                Live    Stock

# My Organization

July 01, 2023 - September 30, 2023 (GMT)

Account Manager

Tania Vivero tania.vivero@thomsonreuters.com

MORE POINTS

Groups (1)      Users (1/3779)

Search for a user...                        Search for a group..            •  Standard  Admins      API Users

| NAME                     | GROUP                 | TYPE | CREATED    | LA                   |
| ------------------------ | --------------------- | ---- | ---------- | -------------------- |
| Tania Vivero (RC-API-QA) | Default Account Group | API  | 27/07/2023 | tania.vivero\@tr.com |

# 3.

Create a new group for the API user. Click over “Create Group”;

- Assign a Group Name as shown below, for example, API user.
- Assign points to the user in the “Points Allocation” field. In this case, one (1) point was assigned.
- Look for your API user and select it; and click CONFIRM.

REUTERS

© 2024 Reuters





89
Reuters API

# Used 98

# Create Group

| Group Name                       | Users                 |
| -------------------------------- | --------------------- |
| API User Reuters                 | tania                 |
| Points group                     | USERA                 |
| Media Types                      |                       |
| Graphic                          | Picture               |
| Video                            | Live Video            |
| Standard                         | Default Account Group |
| tania.vivero\@thomsonreuters.com | Admin                 |
| tania.vivero\@tr.com             | API                   |

Points Allocation (2 Unallocated)

CANCEL
CONFIRM

# 4.

Your API user will be listed under the “Group” tab as shown below, now your API user is allowed to download the Marketplace (points) content.

# My Organization

July 01, 2023 - September 30, 2023 (GMT)

# Account Manager

Tania Vivero tania.vivero@thomsonreuters.com

+ MORE POINTS

# Groups (2)     Users (3779)

Search for a group...

| GROUP NAME              | USERS | ALLOCATED POINTS |
| ----------------------- | ----- | ---------------- |
| Default Account Group A | 3778  | 99               |
| API User Reuters        | 1     | 1                |

REUTERS
© 2024 Reuters





90
Reuters API

# Updates, Corrections and Deletions for Pictures

Reuters use IPTC Edit Status to help customers manage changes to the status of a picture. This notification process is used by clients, partners, and within Reuters products. The Edit Status metadata appears in the JPEG, the NewsML-G2 XML files, and the JSON files; please see below and linked examples.

# ASSET LIFECYCLE (VIDEO/PICTURE)

The feed supports the entire document lifecycle: New, Updated, Corrected, and Deleted items. In each case, the item can be identified by the ID and the incrementing version number:

1. New - The ‘new publish’ message contains the signal ‘edStat:N’. The new item marks the delivery of a new image. The original picture is present.
2. Update - The ‘update’ message contains the signal ‘edStat:U’. The complete item will be resent in case of an update or if the item provides extra new information.
3. Correction – The ‘correction’ message contains the signal ‘edStat:C’. The correction item will be resent in case of a correction. Identifies an error discovered post-publication. NOTE: a minor CORRECTION, such as a grammatical or punctuation error, is known as a REFILE. The term REFILE appears in the caption, but NO correction template is published, just the JPEG and XML.
4. Delete - The ‘deletion’ message contains the signal ‘edStat:D’, and the downstream system should delete all item versions when “received” this parameter. It may require immediate attention. The image needs to be deleted or, if published online, taken down for a website as soon as possible.

| "edStat:N" | New        |
| ---------- | ---------- |
| "edStat:U" | Update     |
| "edStat:C" | Correction |
| "edStat:D" | Deletion   |

The best approach to finding an impacted image is to search for:

1. The unique ID (usn) supplied by Reuters. For example, Picture USN: RC2Y5X9RVD61. Use the parameter “signal” to retrieve the edit status (edStat).

query MyQuery {
search(query:
"id:RC2Y5X9RVD61") {
items {
uri
signal
}
}
}

REUTERS
© 2024 Reuters




91
Reuters API

# b)

To search for the complete list of pictures with the edStat:D, including the picture id (usn), signal and URI information, the query should be:

query MyQuery {
search(query: "signal:\"edStat:D\"") {
items {
Uri
signal
usn
}
}
}

# c)

To search for the complete list of pictures with the edStat:D, make use of the Deletion channel alias cez863 (Picture bin all)

query MyQuery {
search(filter: {channel: “cez863”}) {
items
}
}

REUTERS
© 2024 Reuters






92
# Reuters API

# POSTMAN

Postman is a free application used for API testing. In addition, it is an interactive and automatic tool for verifying the APIs and presents you with a friendly GUI for constructing requests and reading API responses. Postman platform will help users know which code is needed to use depending on their implementation language.

After downloading the application, create a “New Collection” and give it your desired name. Inside the New Collection, right-click and select “Add Request,” as shown in the following image:

My Workspace

New Import b

Collections

Graphql

New Collection

APIS

Environments

Tania GraphQ

Add Request

POST New R

Add Folder

Monitor Collection

Mock Servers

GET New R

Mock Collection

Create a fork

Rename

Ctrl+E

Duplicate

Ctrl+D

Export

Manage Roles

Delete

Del

History

After creating a “request,” please do a POST and fill out the fields shown in the following image to get the Token.

Do the POST to https://auth.thomsonreuters.com/oauth/token. Select the “Body” tab and “x-www-form-urlencoded,” and under the “Key” column, write down the following fields as shown in the next image:

POST

Params

Authorization

Headers (9)

Body

Pre-request Script

Tests

Settings

none

form-data

x-www-form-urlencoded

raw

binary

GraphQL

| KEY            | VALUE | DESCR |
| -------------- | ----- | ----- |
| client\_id     |       |       |
| client\_secret |       |       |
| audience       |       |       |
| grant\_type    |       |       |
| scope          |       |       |

Important: when entering the information (copy/paste) under the “Value” column, do not hit the ENTER key

REUTERS

© 2024 Reuters





# Reuters API

Key

|                | Value                                                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| client\_id     | XXXXXXXXXXXXXXXXXX                                                                                                                           |
| client\_secret | XXXXXXXXXXXXXXXXXX                                                                                                                           |
| audience       | 7a14b6a2-73b8-4ab2-a610-80fb9f40f769                                                                                                         |
| grant\_type    | client\_credentials                                                                                                                          |
| Scope          | * https\://api.thomsonreuters.com/auth/reutersconnect.contentapi.read
* https\://api.thomsonreuters.com/auth/reutersconnect.contentapi.write |

After entering the above information, click over SEND as shown below, and the application should return your account TOKEN.

Note: “client_id” and “client_secret” are not shown to protect the credentials.

After the token is generated, you can begin to do the GraphQL queries.

POST https://auth.thomsonreuters.com/oauth/token

Params Authorization Headers (9) Body Pre-request Script Tests Settings Cookies

•none • form-data x-www-form-urlencoded • raw • binary • GraphQL

| KEY            | VALUE                                                               | DESCRIPTION |
| -------------- | ------------------------------------------------------------------- | ----------- |
| client\_id     |                                                                     |             |
| client\_secret |                                                                     |             |
| audience       | 7a14b6a2-73b8-4ab2-a610-80fb9f40f769                                |             |
| grant\_type    | client\_credentials                                                 |             |
| scope          | https\://api.thomsonreuters.com/auth/reutersconnect.contentapi.read |             |

Body Cookies (2) Headers (20) Test Results Status: 200 OK Time: 993 ms Size: 1.82 KB Save Response

Pretty Raw Preview Visualize JSON

1 E

2 "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6I1JERTBPVEF3UVVVMk16Z3hPRUpGTkVSRk5qUkRNakkzUVVFek1qZEZOVEJCUkRVM1JrTTRSZyJ9. GiLCJp vbnRl HXqEf

3 "scope": "https://api.thomsonreuters.com/auth/reutersconnect.contentapi.write https://api.thomsonreuters.com/auth/reutersconnect.contentapi.read",

4 "expires_in": 86400,

5 "token_type": "Bearer"

# How to do GraphQL queries in Postman

After the token is generated, create a new “request” and make a POST request to our URL https://api.reutersconnect.com/content/graphql as shown in the image below, click over the “Authorization” tab and select “Bearer Token” and copy/paste your token on the Token field as shown below:

REUTERS © 2024 Reuters






94
Reuters API

# POST

https://api.reutersconnect.com/content/graphql

Send

# Params

Authorization Headers (9) Body Pre-request Script Tests Settings Cookies

Type Bearer Token

Heads up! These parameters hold sensitive data. To keep this data secure while working in a collaborative environment, we recommend using variables.

Learn more about variables

The authorization header will be automatically generated when you send the request. Learn more about authorization

Token

eyJhbGciOiJSUzI1NilsInR5cCI6IkpXVCIslmtp ZCI6IIJERTBPVEF3UVVVMk16Z3hPRUpGTkV SRk5aUJkRNakk7UVVFek1a7F7OVF.ICUkRVM

# Response

After entering the TOKEN, verify that your account is working fine. Go to “Body” and select “GraphQL,” write down a simple query to get your account details and click “Send.” The application should show you your account details.

query MyQuery {
currentUser {
email
firstName
lastName
loginName
}
}

# POST

√ https://api.reutersconnect.com/content/graphql

Send

# Params

Authorization● Headers (9) Body Pre-request Script Tests Settings Cookies

•none Oform-data • x-www-form-urlencoded •raw •binary GraphQL Auto-fetchC Schema Fetched

# QUERY

query MyQuery {
currentUser {
email
firstName
lastName
loginName
}
}

# Bod

CookiesHeaders (18) Test Results

Status: 200 OK Time: 197 ms Size: 772 B Save as Example 000

letty Raw Preview Visualize JSON

"data": {
"currentUser": {
"email": "tania.i@tr.com",
"firstName": "Tania_Archive_test",
"lastName": "I (RC-API)",
"loginName": "archivetest_newapi"
}
}

REUTERS © 2024 Reuters



95
# Reuters API

# Samples of Queries using Postman

# 1. How to get all RAW video clips

How to get all RAW video clips distributed by the “Core-World” feed on 1/Feb/2023

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

REUTERS © 2024 Reuters




# Reuters API

POST https://api.reutersconnect.com/content/graphql Send

Params Authorization • Headers (9) Body Pre-request Script Tests Settings Cookies

none form-data x-www-form-urlencoded raw binary GraphQL No schema

# QUERY

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
}
}
}

# GRAPHQL VARIABLES

{
"query": "query MyQuery {\\r\\n search(filter: {channel:\\\"Wbz248\\\", topicCodes: \\\"WNSFR:WORLD\\\", dateRange: \\\"2021.12.01.23.59\\\"}) {\\r\\n totalHits\\r\\n items {\\r\\n byLine\\r\\n copyrightNotice\\r\\n versionCreated\\r\\n fragment\\r\\n headLine\\r\\n versionedGuid\\r\\n uri\\r\\n language\\r\\n }\\r\\n}}"
}

# Response

Status: 200 OK Time: 1017 ms Size: 48.05 KB

# Data

"data": {
"search": {
"totalHits": 978,
"items": [
{
"byLine": "Reuters, DEC 12",
"copyrightNotice": "(c) 2021 Thomson Reuters, unless otherwise identified. Full statement available at https://www.thomsonreuters.com/en/policies/copyright.html",
"versionCreated": "2021-12-12T20:28:08Z",
"fragment": null,
"headLine": "Israeli PM Bennett arrives in Abu Dhabi to meet de facto ruler",
"versionedGuid": "tag:reuters.com,2021:ninjs_wDF7QG213:3",
"uri": "tag:reuters.com,2021:ninjs_wDF7QG213",
"language": "en",
"type": "video",
"profile": "NEP-External_MNP"
}
]
}
}

# Code Examples

After checking a response from the query, move forward and click over the code symbol

- Python - http.client
- C# - RestSharp
- cURL
- Dart - http
- Go - Native
- Java - OkHttp
- Java - Unirest
- JavaScript - Fetch
- JavaScript - jQuery
- NodeJs - Axios
- PHP - cURL
- PowerShell - RestMethod

REUTERS © 2024 Reuters






97
Reuters API

For example, if you want to do your implementation using Python, use the code shown below.

POST https://api.reutersconnect.com/content/graphql

Send

Python - Requests

import requests
import json

Params

Authorization • Headers (9) Body Pre-request Script Tests Settings Cookies

none • form-data • x-www-form-urlencoded • raw • binary

QUERY

query MyQuery {
search(
filter: {channel: "Wbz248", topicCodes: "WNSFR:WORLD", dateRange: "2021.12.01.23.59"}
){
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
}
}
}

url = "https://api.reutersconnect.com/content/graphql"
payload="{\"query\":\"query MyQuery {\\r\\n search(\\r\\n  filter:
{channel: \\\"Wbz248\\\", topicCodes: \\\"wNsFR:woRLD\\\", dateRange:
\\\"2021.12.01.23.59\\\"}\\r\\n){\\r\\n  totalHits\\r\\n  items
{\\r\\n         byLine\\r\\n  copyrightNotice\\r\\n
versionCreated\\r\\n          fragment\\r\\n  headLine\\r\\n
versionedGuid\\r\\n     uri\\r\\n  language\\r\\n
type\\r\\n      profile\\r\\n      slug\\r\\n        usageTerms\\r\\n
usageTermsRole\\r\\n         version\\r\\n   credit\\r\\n
firstCreated\\r\\n      productLabel\\r\\n     pubStatus\\r\\n
urgency\\r\\n      usn\\r\\n     position\\r\\n     intro\\r\\n      \\r\\n}\\r\\n}\",\"variables\":{}}
headers = {
'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTBPVEF3UVVVMk16Z3hPRUpGT
kVSRk5qUkRNakkzUVVFek1qZEZOVEJCUkRVM1JrTTRSZyJ9.
eyJpc3MiOiJodHRwczovL2F1dGgudGhvbXNvbnJldXRlcnMuY29tLyIsInN1YiI6InlWNUV2W
TkwdzBRO29tcGdKbnJnWXNPOWRpZ1hhZFdrOGNsaWVudHMiLCJhdWOi0iI3YTE0YjZhMi03M2
I4LTRhYjItYTYxMC04MGZiOWY0MGY3NjkiLCJpYXQiOjE2MzkzNDA5MTMsImV4cCI6MTYzOTQ
Imh@dHBzOi8vYXBpLnRob21zb25yZXV0ZXJzLmNvbS9hdXRoL3J1dXRlcnNjb25uZWN0LmNvb
nR1bnRhcGkud3JpdGUgaHR0cHM6Ly9hcGkudGhvbXNvbnJ1dXR1cnMuY29tL2F1dGgvcmV1dG
Vyc2Nvbm51Y3OuY29udGVudGFwaS5yZWFkIiwiZ3R5IjoiY2xpZW50LWNyZWR1bnRpYWxzIn©
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

# 2. How to get all items using a Slug

query MyQuery {
search(query: "slug:\"reuters-next\"") {
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

REUTERS
© 2024 Reuters




98
Reuters API

Test your query in our portal; if you get results, move to Postman, copy/paste the code, click over Send, and the results should show as in the image. Click over the code symbol and select your desired language for further implementation.

# HIIP Tania GraphQL / Tania Main Requests

HSave  0  Code snippet

| POST | √ | https\://api.reutersconnect.com/content/graphql | Send | □ | HTTP | √ |
| ---- | - | ----------------------------------------------- | ---- | - | ---- | - |

# Params

# Headers (9)

# Body

# Settings

# Cookies

&#x3C;1> 1 POST /content/graphq1 HTTP/1.1

Authorization•

Pre-request Script

Tests

2 Host: api.reutersconnect.com

| none | form-data | x-www-form-urlencoded | •raw•binary |
| ---- | --------- | --------------------- | ----------- |

# QUERY

1      query MyQuery {
2       search(query: "slug:\"reuters-next\"") {
3       items {
4           byLine
5           copyrightNotice
6           versionCreated
7           fragment
8           headLine
9           versionedGuid
10          uri
11          language
12          type
13          profile
14          slug
}

# Body

# Cookies

# Headers (18)

# Test Results

Pretty    Raw         Preview    Visualize  JSON√     =

1           "data": {
2            "search": {
3                   "items": [
4                         {
5
Auto-fetchC Schema Fetched
3 Content-Type: application/json
4 Authorization: Bearer
eyJhbGciOiJSUzI1NiIsInR5cCIE
GRAPHQL VARIABLES
1
eyJpc3MiOiJodHRwczovL2F1dGgL
NUV2WTkwdzBR029tcGdKbnJnWXNF
YjZhMi03M2I4LTRhYjItYTYxMC04
ImV4cCI6MTY5MjEwMTAz0CwiYXpv
WGFkV2siLCJzY29wZSI6Imh0dHBz
L3J1dXR1cnNib25uZWN0LmNybnR]
bnJ1dXRlcnMuY29tL2F1dGgvcmV1
Z3R5IjoiY2xpZW50LWNyZWR1bnRp
VQfK2DEbiWPnfyQiTYubJgGXZuLG
NhmOtE30AIP6Xw9wKFV2J0Ibi0h1
GmJprsWWE1ZGfWju3T5W dXvyPCE
6PWiMZwJGx26qgVLoYu5J2aZ0rg1
Y4gpuFT0cNLX clRVcIjKwBp0ts9
Bw
Ea 200 OK 1094 ms 1.48 KB  Save as Example
5 Content-Length: 537
6
7 5"query":"query MyOuery 5\r\n s
"slug:\||"reuters-next\|\"1
byLine\r\n          copyrightNot
fragment\r\n          headLine\r
uri\r\n        language\r\n
slug\r\n         usageTerms\r\n
version\r\n          credit\r\n
productLabel\r\n         pubSta

If the client IT team wants to program using cURL, for example, the code is shown in Postman.

# HTTF  Tania GraphQL / Tania Main Requests

Save V                                                                Code snippet

| POST | √ | https\://api.reutersconnect.com/content/graphql | Send | □ | cURL |
| ---- | - | ----------------------------------------------- | ---- | - | ---- |

# Params

# Authorization •

# Headers (9)

# Body

# Pre-request Script

# Tests

# Settings

# Cookies

1 curl --location 'https://api.reutersconnect.com/contt
2 --header 'Content-Type: application/json' |
3 --header 'Authorization: Bearer
•none •form-data          •x-www-form-urlencoded  •raw •binary         GraphQL Auto-fetch V c Schema Fetched
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJER
RUpGTkVSRk5qUkRNakkzUVVFek1qZEZOVEJCUkRVM1JrTTRSZ
query
1      query MyQuery {
2      search(query: "slug:\"reuters-next\"") {
3      items {
4           byLine
5           copyrightNotice
6             versionCreated
7           fragment
8           headLine
9           versionedGuid
10          uri
11          language
12          type
13          profile
14          slug
}

# Body

# Cookies

# Headers (18)

# Test Results

Pretty   Raw          Preview    Visualize     JSON (

1                                                                                                                               byLine\r\n    copyrightNotice\r\n            versionC
fragment\r\n  headLine\r\n              versionedGuid
uri\r\n       language\r\n     type\r\n    prof
slug\r\n      usageTerms\r\n   usageTermsRole
version\r\n   credit\r\n       firstCreated\r\n

REUTERS
© 2024 Reuters



99
# Reuters API

# Appendix 1 - Content Formats

The Reuters API GraphiQL subscribers can access a wide range of standardized text, pictures, graphics, videos, and audio formats.

# For text:

FORMAT
XML
JSON

# For pictures:

| FORMAT       | RENDITIONS                          |
| ------------ | ----------------------------------- |
| Thumbnail    | Width:150 pixels                    |
| viewImage    | Width: 640 pixels                   |
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
| Flash Video 512 | stream:512:16x9:flv 512x288 frame size     |
| Flash Video 300 | stream:300:16x9:flv 384x216 frame size     |
| H264/mpeg 300   | stream:300:16x9:mp4 384x216 frame size     |
| H264/mpeg 720   | stream:5128:16x9:mp4 1280x720 frame size   |
| H264/mpeg 2000  | stream:2000:16x9:mp4 768x432 frame size    |
| H264/mpeg 700   | stream:700:16x9:mp4 640x360 frame size     |
| Flash Video 700 | stream:700:16x9:flv 576x324 frame size     |
| H264/mpeg 2000  | stream:8256m:16x9:mp4 1920x1080 frame size |
| Mpeg 6756       | stream:6756:16x9:mpg 720x576 frame size    |
| H264/mpeg 8256  | stream:8256:16x9:mp4                       |

REUTERS

© 2024 Reuters





Reuters API

# Video Formats and Streams

# Frame Sizes

| Format               | Stream                                               |
| -------------------- | ---------------------------------------------------- |
| 1920x1080 frame size | H264/mpeg 1756 (SCREENER) stream:1756:16x9:mp4       |
| 1280x720 frame size  | video/mpeg SD 525 stream:6756:16x9:sd525i30:mpg      |
|                      | video/mpeg SD 625 stream:6756:16x9:sd625i25:mpg      |
|                      | video/mp4 HD 1080i50 stream:13756:16x9:hd1080i50:mp4 |
|                      | video/mp4 HD 1080i60 stream:13756:16x9:hd1080i60:mp4 |
|                      | video/mp4 HD 720 (Screener) stream:1756:16x9:mp4     |

# For RAW video:

| Format                      | Renditions                      |
| --------------------------- | ------------------------------- |
| video/mpeg SD 525           | stream:6756:16x9:sd525i30:mpg   |
| video/mpeg SD 625           | stream:6756:16x9:sd625i25:mpg   |
| video/mp4 HD 1080i50        | stream:13756:16x9:hd1080i50:mp4 |
| video/mp4 HD 1080i60        | stream:13756:16x9:hd1080i60:mp4 |
| video/mp4 HD 720 (Screener) | stream:1756:16x9:mp4            |
| Flash Video 512             | stream:512:16x9:flv             |
|                             | 512x288 frame size              |
| Flash Video 300             | stream:300:16x9:flv             |
|                             | 384x216 frame size              |
| H264/mpeg 300               | stream:300:16x9:mp4             |
|                             | 384x216 frame size              |
| H264/mpeg 720               | stream:5128:16x9:mp4            |
|                             | 1280x720 frame size             |
| H264/mpeg 2000              | stream:2000:16x9:mp4            |
|                             | 768x432 frame size              |
| H264/mpeg 700               | stream:700:16x9:mp4             |
|                             | 640x360 frame size              |
| Flash Video 700             | stream:700:16x9:flv             |
|                             | 576x324 frame size              |
| H264/mpeg 2000              | stream:8256m:16x9:mp4           |
|                             | 1920x1080 frame size            |
| Mpeg 6756                   | stream:6756:16x9:mpg            |
|                             | 720x576 frame size              |
| H264/mpeg 8256              | stream:8256:16x9:mp4            |
|                             | 1920x1080 frame size            |
| H264/mpeg 1756 (SCREENER)   | stream:1756:16x9:mp4            |
|                             | 1280x720 frame size             |

# Additional Information

- Video Shot List: STREAM:SHOTLIST:JSON
- Video Closed Caption (SRT format): CLOSEDCAPTION:SRT
- Video Closed Caption (VTT format): CLOSEDCAPTION:VTT
- VIEW_IMAGE: viewImage:768x432
- GRID_THUMBNAIL: thumbnailgrid
- VIEW_IMAGE: viewImage:512x288

© 2024 Reuters




101
Reuters API

THUMBNAIL thumbnail:160x90

BASE_IMAGE baseImage:960x540

# For Archive video:

| FORMAT               | RENDITIONS                      |
| -------------------- | ------------------------------- |
| video/mpeg SD 525    | stream:6756:16x9:sd525i30:mpg   |
| video/mpeg SD 625    | stream:6756:16x9:sd625i25:mpg   |
| video/mp4 HD 1080i50 | stream:13756:16x9:hd1080i50:mp4 |
| video/mp4 HD 1080i60 | stream:13756:16x9:hd1080i60:mp4 |
| video/mp4 HD 720     | stream:1756:16x9:mp4            |

# For audio:

| FORMAT                     | RENDITIONS        |
| -------------------------- | ----------------- |
| audio/mpeg                 | stream:22.050:mp3 |
| audio/mpeg                 | stream:48000:mp3  |
| audio/aa                   | stream:48000:m4a  |
| audio/wav                  | stream:48000:wav  |
| audio/wav                  | stream:48000m:wav |
| audio/mpeg (Audio Preview) | preview:48000:mp3 |

REUTERS

© 2024 Reuters





# Appendix 2 – Language codes

REUTERS

© 2024 Reuters




103
Reuters API

# Appendix 3 - Pictures restrictions codes

This section contains the picture restrictions codes applied depending on the picture use case. We apply the below restrictions and instructions codes to a subset of our pictures in the JPG metadata IPTC “Special Instructions” field and in the NewsML-G2 “usageTerms” field, and also into a new “XMP Plus” field. We append the accompanying human readable text in the caption parameter.

| Category                                                                      | Sample codes  | Proposed XMP field | Sample value in the XMP field                                         |
| ----------------------------------------------------------------------------- | ------------- | ------------------ | --------------------------------------------------------------------- |
| Concatenating the human readable text of all the codes applied to the picture | MNDTY         | Plus: Custom1      | MANDATORY CREDIT. NO RESALES.                                         |
|                                                                               | NARCH/NARCH30 |                    | NO ARCHIVES. THIS IMAGE HAS BEEN SUPPLIED BY A THIRD PARTY.           |
|                                                                               | 3TP USAOUT    |                    | UNITED STATES OUT. NO COMMERCIAL OR EDITORIAL SALES IN UNITED STATES. |

The codes are:

| Code          | Human Readable Text                                                                                                       | Action Required                                         | IPTC Field | XMP Field                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------- | ---------------------------------------------------------- |
| NARCH/NARCH30 | NO RESALES. NO ARCHIVE                                                                                                    | Do not publish after 30 days from the publication date. |            | Photoshop: Special Instructions & PUR: Restrictions        |
| MNDTY         | MANDATORY CREDIT                                                                                                          | Preserve the byline and source upon publication.        |            | Photoshop: Special Instructions                            |
| 3TP           | THIS IMAGE HAS BEEN SUPPLIED BY A THIRD PARTY. IT IS DISTRIBUTED, EXACTLY AS RECEIVED BY REUTERS, AS A SERVICE TO CLIENTS | N/A - this is a content advisory                        |            | Photoshop: Special Instructions                            |
| TPSOUT        | NO THIRD-PARTY SALES. NOT FOR USE BY REUTERS THIRD PARTY DISTRIBUTORS                                                     | Do not use by Reuters Third Party Distributors          |            | Photoshop: Special Instructions                            |
| SMOUT         | SENSITIVE MATERIAL. THIS IMAGE MAY OFFEND OR DISTURB                                                                      | N/A - this is a content advisory                        |            | Photoshop: Special Instructions                            |
| COUNTRY OUT   | THIS IMAGE CAN’T BE DISTRIBUTED IN THE MENTIONED COUNTRY                                                                  | Do not publish in the mentioned country                 |            | Photoshop: Special Instructions & PLUS: Region Constraints |

Rules can be created based on the codes applied, e.g., if the NARCH/NARCH30 code is applied to a picture clients can automate its removal from their systems after 30 days, since we do not provide archive rights.

REUTERS

© 2024 Reuters






104
Reuters API

From 27th February 2024 we enhanced our application of IPTC pictures metadata fields.

# Source &#x26; byline

We address the misapplication of the IPTC field of all pictures for the IPTC source field and of the IPTC byline field for all third-party pictures.

| IPTC IIM tag | XMP tag | prior to 27ᵗʰ February 2024 | Sample updated value | Notes                                                                                                                                                                                                          |
| ------------ | ------- | --------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source       | Source  | X02875                      | REUTERS              | For third party pictures we will pass through the source as provided by the third party                                                                                                                        |
| Byline       | Creator | Lehtikuva                   | Mikko Stiig          | For third party pictures we will pass through the byline as it is provided by the third party. For Reuters pictures we will pass through the byline in mixed case (e.g., Hannah McKay instead of HANNAH MCKAY) |

# Geographic restrictions

We currently place all the codes pertaining to content restrictions and warnings in the IPTC “Special Instructions” field, in addition to the XMP Prism Usage Rights (PUR) fields for restrictions, permissions and adultContentWarning.

In February 2024 we start passing through geographic restriction codes into a more appropriate XMP Picture Licensing Universal System (PLUS) namespace as detailed below.

| Category               | Code         | Human readable text             | Proposed XMP field      | Sample value in XMP field                              |
| ---------------------- | ------------ | ------------------------------- | ----------------------- | ------------------------------------------------------ |
| Geographic restriction | E.g., DNKOUT | SALES IN DENMARK.               | Plus: RegionConstraints | \<plus:regionconstraints ConstraintCode=DNKOUT>DENMARK |
|                        |              | OUT. NO COMMERCIAL OR EDITORIAL |                         |                                                        |

However, we will also continue to populate them in IPTC field “Special Instructions” for the time being to ensure that clients who have built automated workflows on these codes have adequate time to migrate to reading the codes from the new XMP fields.

REUTERS
© 2024 Reuters





# Appendix 4 - Video – Machine Readable Restriction types

The video items may contain new codes. It is applied to any video story where there are restrictions. It is also applied to content from partners that is available on the Reuters Connect website marketplace.

# No restrictions

A new code called NORC (No Overall Rights Control) code. It is applied to any story where the restrictions are “Broadcast: None, Digital: None”.

Example use case: This code can be used to return only content that is unrestricted when executing a search query, if the user knows they do not want to spend any time checking restrictions.

| Code | Restrictions meaning           | API parameter | API response              |
| ---- | ------------------------------ | ------------- | ------------------------- |
| NORC | Broadcast: None. Digital: None | signal        | "signal":\[ "sic:NORC", ] |

# Broadcast or Digital restriction

Example use case: Filter out content that cannot be used on television from the search results of a user creating content for a broadcast audience.

| Code  | Restrictions meaning | API parameter | API response               |
| ----- | -------------------- | ------------- | -------------------------- |
| NUDIG | Digital: No use      | signal        | "signal":\[ "sic:NUDIG", ] |
| NUBRC | Broadcast: No use    | signal        | "signal":\[ "sic:NUBRC", ] |

REUTERS © 2024 Reuters






# 106

# Reuters API

# Manual check

| Code  | Restrictions meaning                                                                 | API parameter | API response               |
| ----- | ------------------------------------------------------------------------------------ | ------------- | -------------------------- |
| MANRC | Indicates that this script must be checked manually to determine usage restrictions. | signal        | "signal":\[ "sic:MANRC", ] |

REUTERS

© 2024 Reuters





107
# Reuters API

# Appendix 5 – Live event renditions

# For HLS

| Parameters    | Renditions                              |
| ------------- | --------------------------------------- |
| "code"        | "hls:29.97"                             |
| "name"        | "200Kbps-4Mbps Video: 1080p29.97 h.264" |
| "frameRate"   | "29.97"                                 |
| "scanType"    | "progressive"                           |
| "aspectRatio" | "16:9"                                  |
| "frameSize"   | "1920x1080"                             |
| "minBitrate"  | "200Kbps"                               |
| "maxBitrate"  | "4Mbps"                                 |
| "bitrate"     | null                                    |
| "href"        | null                                    |

# For RTMP and SRT

Bit rate: 200 kbps (416x234; 30 fps)

| Parameters    | Renditions                              |
| ------------- | --------------------------------------- |
| "code"        | "rtmp:29.97:200"                        |
|               | "srt:29.97:200"                         |
| "name"        | "200Kbps-4Mbps Video: 1080p29.97 h.264" |
| "frameRate"   | "29.97"                                 |
| "scanType"    | "progressive"                           |
| "aspectRatio" | "16:9"                                  |
| "frameSize"   | "416x234"                               |
| "minBitrate"  | null                                    |
| "maxBitrate"  | null                                    |

REUTERS

© 2024 Reuters





Reuters API

# Bit rate: 600 kbps (640x360; 30 fps)

| Parameters    | Renditions                       |
| ------------- | -------------------------------- |
| "code"        | "rtmp:29.97:600"                 |
|               | "srt:29.97:600"                  |
| "name"        | "600Kbps Video: 360p29.97 h.264" |
| "frameRate"   | "29.97"                          |
| "scanType"    | "progressive"                    |
| "aspectRatio" | "16:9"                           |
| "frameSize"   | "640x360"                        |
| "minBitrate"  | null                             |
| "maxBitrate"  | null                             |
| "bitrate"     | "600Kbps"                        |

# Bit rate: 1024 kbps (854x480; 30 fps)

| Parameters    | Renditions                        |
| ------------- | --------------------------------- |
| "code"        | "rtmp:29.97:1024"                 |
|               | "srt:29.97:1024"                  |
| "name"        | "1024Kbps Video: 480p29.97 h.264" |
| "frameRate"   | "29.97"                           |
| "scanType"    | "progressive"                     |
| "aspectRatio" | "16:9"                            |
| "frameSize"   | "854x480"                         |
| "minBitrate"  | null                              |
| "maxBitrate"  | null                              |
| "bitrate"     | "1024Kbps"                        |

© 2024 Reuters



109
# Reuters API

# Bit rate: 2048 kbps (1280x720; 30 fps)

| Parameters    | Renditions                        |
| ------------- | --------------------------------- |
| "code"        | "rtmp:29.97:2048"                 |
|               | "srt:29.97:2048"                  |
| "name"        | "2048Kbps Video: 720p29.97 h.264" |
| "frameRate"   | "29.97"                           |
| "scanType"    | "progressive"                     |
| "aspectRatio" | "16:9"                            |
| "frameSize"   | "1280x720"                        |
| "minBitrate"  | null                              |
| "maxBitrate"  | null                              |
| "bitrate"     | "2048Kbps"                        |

# Bit rate: 4096 kbps (1920x1080; 25 fps)

| Parameters    | Renditions                         |
| ------------- | ---------------------------------- |
| "code"        | "rtmp:29.97:4096"                  |
|               | "srt:29.97:4096"                   |
| "name"        | "4096Kbps Video: 1080p29.97 h.264" |
| "frameRate"   | "25"                               |
| "scanType"    | "progressive"                      |
| "aspectRatio" | "16:9"                             |
| "frameSize"   | "1920x1080"                        |
| "minBitrate"  | null                               |
| "maxBitrate"  | null                               |
| "bitrate"     | "4096Kbps"                         |

REUTERS © 2024 Reuters




Reuters API

# Bit rate: 4096 kbps (1920x1080; 30 fps)

| Parameters    | Renditions                         |
| ------------- | ---------------------------------- |
| "code"        | "rtmp:29.97:4096"                  |
|               | "srt:29.97:4096"                   |
| "name"        | "4096Kbps Video: 1080p29.97 h.264" |
| "frameRate"   | "29.97"                            |
| "scanType"    | "progressive"                      |
| "aspectRatio" | "16:9"                             |
| "frameSize"   | "1920x1080"                        |
| "minBitrate"  | null                               |
| "maxBitrate"  | null                               |
| "bitrate"     | "4096Kbps"                         |

# Bit rate: 8000 kbps (1920x1080; 30 fps)

| Parameters    | Renditions                         |
| ------------- | ---------------------------------- |
| "code"        | "rtmp:29.97:8000"                  |
|               | "srt:29.97:8000"                   |
| "name"        | "8000Kbps Video: 1080p29.97 h.264" |
| "frameRate"   | "29.97"                            |
| "scanType"    | "progressive"                      |
| "aspectRatio" | "16:9"                             |
| "frameSize"   | "1920x1080"                        |
| "minBitrate"  | null                               |
| "maxBitrate"  | null                               |
| "bitrate"     | "8000Kbps"                         |

© 2024 Reuters





Reuters API

# Bit rate: 8000 kbps (1920x1080; 25 fps)

| Parameters    | Renditions                      |
| ------------- | ------------------------------- |
| "code"        | "rtmp:25:8000"                  |
|               | "srt:25:8000"                   |
| "name"        | "8000Kbps Video: 1080p25 h.264" |
| "frameRate"   | "25"                            |
| "scanType"    | "progressive"                   |
| "aspectRatio" | "16:9"                          |
| "frameSize"   | "1920x1080"                     |
| "minBitrate"  | null                            |
| "maxBitrate"  | null                            |
| "bitrate"     | "8000Kbps"                      |

REUTERS

© 2024 Reuters



112
# Reuters API

# Technical Support

There are a variety of means by which you can contact Thomson Reuters for support.

One of the easiest is to go to https://liaison.reuters.com/contact-us and complete the request form after which a customer representative should contact you within 15 minutes. No sign-in is required.

Or send an email to ReutersMediaSupport@thomsonreuters.com

REUTERS

© 2024 Reuters

