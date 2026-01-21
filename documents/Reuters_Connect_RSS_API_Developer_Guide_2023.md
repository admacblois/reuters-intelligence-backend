# REUTERS CONNECT RSS API

# DEVELOPER GUIDE

Date of issue: September 2023

Document Version 4.0




Legal Information

© Thomson Reuters 2023. All Rights Reserved.

Thomson Reuters, by publishing this document, does not guarantee that any information contained herein is and will remain accurate or that use of the information will ensure correct and faultless operation of the relevant service or equipment. Thomson Reuters, its agents and employees, shall not be held liable to or through any user for any loss or damage whatsoever resulting from reliance on the information contained herein.

This document contains information proprietary to Thomson Reuters and may not be reproduced, disclosed, or used in whole or part without the express written permission of Thomson Reuters.

Any Software, including but not limited to, the code, screen, structure, sequence, and organization thereof, and Documentation are protected by national copyright laws and international treaty provisions. This manual is subject to U.S. and other national export regulations.

Nothing in this document is intended, nor does it, alter the legal obligations, responsibilities or relationship between yourself and Thomson Reuters as set out in the contract existing between us.

# Reuters Connect RSS API - Developer Guide

Document Version 4.0





Legal Information

# CONTENTS

| 1     | BASIC PROCEDURES AND INSTRUCTIONS                              | 2  |
| ----- | -------------------------------------------------------------- | -- |
| 1.1   | AUDIENCE                                                       | 2  |
| 1.2   | INTRODUCTION                                                   | 2  |
| 1.3   | AUTHENTICATION                                                 | 2  |
| 1.4   | COMMON QUERY STRING PARAMETERS                                 | 2  |
| 1.5   | FREQUENCY RESTRICTIONS                                         | 3  |
| 1.6   | DATE-TIME FORMAT                                               | 3  |
| 2     | SERVICES OFFERED                                               | 4  |
| 2.1   | CHANNELS                                                       | 4  |
| 2.1.1 | Syntax                                                         | 4  |
| 2.1.2 | Parameters                                                     | 4  |
| 2.1.3 | Sample Request & Response                                      | 5  |
| 2.1.4 | Description of Important Output Fields                         | 6  |
| 2.2   | WIRE                                                           | 6  |
| 2.2.1 | Syntax                                                         | 6  |
| 2.2.2 | Parameters                                                     | 6  |
| 2.2.3 | Sample Request & Response                                      | 8  |
| 2.2.4 | Fragment Length & complete Sentences Sample Request & Response | 9  |
| 2.3   | OLR                                                            | 11 |
| 2.3.1 | Syntax                                                         | 11 |
| 2.3.2 | Parameters                                                     | 11 |
| 2.3.3 | Sample Request & Response                                      | 11 |
| 2.4   | BASIC SEARCH                                                   | 13 |
| 2.4.1 | Syntax                                                         | 14 |
| 2.4.2 | Parameters                                                     | 14 |
| 2.4.3 | Sample Request                                                 | 17 |
| 2.4.4 | Sample Response                                                | 17 |
| 3     | RSS OUTPUT FOR DIFFERENT MEDIA TYPES                           | 19 |
| 4     | TECHNICAL SUPPORT                                              | 19 |
| 5     | APPENDIX 1 – COMMON USE CASES FOR THE RSS API                  | 20 |
| 6     | APPENDIX 2 – FREQUENTLY ASKED QUESTIONS (FAQS)                 | 23 |

Reuters Connect RSS API - Developer Guide    1

Document Version 4.0






# Contents

# 1 BASIC PROCEDURES AND INSTRUCTIONS

# 1.1 Audience

This document is targeted towards developers and other users who wish to retrieve Reuters news content via the RSS API.

# 1.2 Introduction

Reuters Connect RSS API provides several convenient ways to access your subscribed feeds. This document is intended to outline the services and methods associated with the latest implementation of Reuters Connect RSS API. It also explains the data elements returned in the responses generated using the service’s methods.

# 1.3 Authentication

HTTP Digest Authentication protocol is used for authentication. The username required for authentication will be the same username the customer has for your Reuters Connect account. However, the password will be a special string called the “RSS key”. The RSS key will be at least 8 characters long, have a mixture of letters and numbers, and will be case sensitive. Users will have the option of requesting a new RSS key through Reuters Connect web site. Requesting a new RSS key will invalidate the existing key for that user and a new key will be emailed to the email address on file for that user.

Note

- Do not pass the username/password in the URL.

# 1.4 Common Query String Parameters

The following are optional query string parameters that may be used by our various feed methods in the RSS API. The methods below will say which of these parameters they support.

- limit – Specifies the maximum number of items to return for a request. By default, methods in this API will set this value to 10. The maximum value can be 100. limit=&#x3C;Positive Number>

Reuters Connect RSS API - Developer Guide    2

Document Version 4.0






# Contents

- maxAge – Specifies the maximum age of items that can be returned for a request. By default, this value is set to 24 hours. The maximum value here can be 7D.
This parameter is used to provide a date limit relative to the current date and time. This filter will be translated into a date range using the current time as the starting point. This parameter should be specified in the format maxAge=&#x3C;Positive Number>&#x3C;Unit>

<unit> can be one of the following:</unit>

- s – for seconds
- m – for minutes
- h – for hours
- D – for days

Default Value: 24h

Examples: maxAge=2D retrieves results for the last 2 days, maxAge=6h retrieves result from the last 6 hours.
- linkType – This value would allow us to provide different types of links in the request. Currently the value for this parameter is:
- raw – Provides links of digested content which will be a simple rendering of plain HTML.

# 1.5 Frequency Restrictions

The Reuters Connect RSS API is intended to provide feeds to be ingested and stored by customers. The methods are NOT to be used to serve website traffic or similar traffic requiring large volumes of requests.

To ensure a high level of service for all customers, method requests are limited to approximately 500 requests per minute. Requests to downloaded binary assets are counted separately and limited to approximately 500 requests per minute.

# 1.6 Date-Time Format

The date and time in the output fields will be standard RSS 2.0 date-time format and RFC-822 compliant.

Examples:

&#x3C;pubDate>Wed, 02 Oct 2019 08:00:00 EST&#x3C;/pubDate>
&#x3C;pubDate>Wed, 02 Oct 2019 13:00:00 GMT&#x3C;/pubDate>
&#x3C;pubDate>Wed, 02 Oct 2019 15:00:00 +0200&#x3C;/pubDate>

Reuters Connect RSS API - Developer Guide    3

Document Version 4.0





Contents

# 2 SERVICES OFFERED

This section describes the methods associated with the Reuters RSS API.

# 2.1 channels

The channels method is used to obtain the list of the channels you are subscribed to in the form of RSS feeds. You can get to know about all your subscribed feeds through this method. Each link output here will be a link to the wire feed method.

# 2.1.1 Syntax

http://rmb.reuters.com/rmd/rss/channels?channelCategory=X&#x26;channelCategory=Y[COMMON-QUERY-STRING-PARAMS]

# 2.1.2 Parameters

The channels method accepts the following parameters:

| PARAMETER                  | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REQUIRED |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| channelCategory            | A channel category is a group of channels containing similar content. This parameter is used to limit results to channels with the specified category id(s). Possible values are: • TXT – for Text • PIC – for Pictures • GRA – for Graphics • OLV – for Online Videos • BRV – for Broadcast Videos • OLR – for Online Reports When multiple categories are supplied, a channel will be returned if it matches at least one of the category filters. Default value: If no value is supplied, all channel categories will be included for searching. | No       |
| COMMON-QUERY-STRING-PARAMS | The following are the common optional parameters that can be used: • limit • maxAge • linkType The common query string parameters supplied here will be passed through to the links provided for each channel in the output.                                                                                                                                                                                                                                                                                                                        | No       |

Example: A request like http://rmb.reuters.com/rmd/rss/channels?limit=5&#x26;maxAge=2D

Reuters Connect RSS API - Developer Guide 4 Document Version 4.0




# Contents

| PARAMETER | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                  | REQUIRED |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
|           | output a list of Available channels with links to the RSS feed for each of the channels via the Wire Feed Method. Since limit was set to 5 and maxAge to 2 days, each of these links will return a maximum of 5 items and whose age has not exceeded 2 days. This is convenient to users since they need not append these common query string parameters to each link provided in the output of this method. |          |

# 2.1.3 Sample Request &#x26; Response

# Request

http://rmb.reuters.com/rmd/rss/channels?channelCategory=olr
# Response

This response provides the list of Online Reports channel subscribed including title, channel link, alias (guid), description, category and pubDate.

&#x3C;?xml version="1.0" encoding="utf-8"?>
&#x3C;rss xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
&#x3C;channel>
&#x3C;title>Available channels&#x3C;/title>
&#x3C;link>http://www.reutersconnect.com&#x3C;/link>
&#x3C;description>Available channels&#x3C;/description>
&#x3C;copyright>(c) Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp&#x3C;/copyright>
&#x3C;lastBuildDate>Tue, 11 Feb 2020 13:29:44 GMT&#x3C;/lastBuildDate>
&#x3C;ttl>5&#x3C;/ttl>
&#x3C;item>
&#x3C;title>Reuters India Online Report World&#x3C;/title>
&#x3C;link>http://rmb.reuters.com/rmd/rss/wire/AGj166&#x3C;/link>
&#x3C;description>Reuters India Online Report World&#x3C;/description>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">OLR&#x3C;/category>
&#x3C;pubDate>Tue, 11 Feb 2020 13:24:18 GMT&#x3C;/pubDate>
&#x3C;guid isPermaLink="false">AGj166&#x3C;/guid>
&#x3C;media:copyright>(c) Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp&#x3C;/media:copyright>
&#x3C;/item>
&#x3C;item>
&#x3C;title>Latam Online Report Sports News&#x3C;/title>
&#x3C;link>http://rmb.reuters.com/rmd/rss/wire/ASI508&#x3C;/link>
&#x3C;description>Latam Online Report Sports News&#x3C;/description>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">OLR&#x3C;/category>
&#x3C;pubDate>Tue, 11 Feb 2020 11:30:06 GMT&#x3C;/pubDate>
&#x3C;guid isPermaLink="false">ASI508&#x3C;/guid>
&#x3C;media:copyright>(c) Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp&#x3C;/media:copyright>
&#x3C;/item>
&#x3C;item>
&#x3C;title>Spain Online Report Entertainment News&#x3C;/title>
&#x3C;link>http://rmb.reuters.com/rmd/rss/wire/AfN325&#x3C;/link>
&#x3C;description>Spain Online Report Entertainment News&#x3C;/description>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">OLR&#x3C;/category>
&#x3C;pubDate>Tue, 11 Feb 2020 07:49:26 GMT&#x3C;/pubDate>
&#x3C;guid isPermaLink="false">AfN325&#x3C;/guid>
&#x3C;media:copyright>(c) Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp&#x3C;/media:copyright>
&#x3C;/item>
&#x3C;/channel>
&#x3C;/rss>






# 2.1.4 Description of Important Output Fields

| FIELDS                                                                                                                                                  | DESCRIPTION   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| channel                                                                                                                                                 | lastBuildDate |
| Timestamp indicating when the last channel was updated. The date-time format will be the standard date format for RSS 2.0 which corresponds to RFC-822. |               |
| \[item {0..N}]                                                                                                                                          | title         |
| The name of the Media Connect channel.                                                                                                                  |               |
|                                                                                                                                                         | link          |
| This link would be a link to the RSS feed for the channel via a Wire Feed Method.                                                                       |               |
|                                                                                                                                                         | description   |
| The name of the Media Connect channel.                                                                                                                  |               |
|                                                                                                                                                         | category      |
| The channel category this particular item belongs to.                                                                                                   |               |
|                                                                                                                                                         | pubDate       |
| The date the particular Media Connect channel was last updated.                                                                                         |               |
|                                                                                                                                                         | guid          |
| The Media Connect channel alias.                                                                                                                        |               |

# 2.2 wire

This method provides an RSS feed for a single channel. It may return one of the following:

- Simple Text
- Pictures
- Graphics
- Online Video
- Broadcast Video
- News Event Packages (NEPs)

Note If you request an OLR channel, only NEPs will be returned. For the rest of the channels, you will get Simple News Items like text, pictures, graphics and videos.

# 2.2.1 Syntax

http://rmb.reuters.com/rmd/rss/wire/{CHANNEL-ALIAS}[?limit=X&#x26;maxAge=Y&#x26;linkType=Z]&#x26;fragmentLenght=ZZ&#x26;completeSentences=true/false

# 2.2.2 Parameters

| PARAMETER                  | DESCRIPTION                                                               | REQUIRED |
| -------------------------- | ------------------------------------------------------------------------- | -------- |
| CHANNEL-ALIAS              | The 6-character identifier for a channel in the Reuters Connect Platform. | Yes      |
| COMMON-QUERY-STRING-PARAMS | • limit                                                                   | No       |
|                            | • maxAge                                                                  |          |
|                            | • linkType                                                                |          |

Reuters Connect RSS API - Developer Guide

Document Version 4.0





Contents

# fragmentLength

This parameter is used to define the length of the fragment to be retrieved. Example: No

fragmentLength=15
Default Value: 200 / Maximum possible value: 400

This parameter only applies to the &#x3C;description> tag. If the fragment length value falls in between a word, all the characters before that word are returned. To be used in conjunctions with a fieldsRef that contains the fragment field.

# completeSentences

This parameter gives you an option to retrieve fragments as complete sentences. No

Possible values are true/false. Default Value: false.

When set to true, any text after the last period or editorial-generated paragraph marks would be stripped away. If no sentence or paragraph markers exist within the fragment length specified, then this parameter is ignored.

To be used in conjunctions with a fieldsRef that contains the fragment field.

# Reuters Connect RSS API - Developer Guide

Document Version 4.0






# Contents

# 2.2.3 Sample Request &#x26; Response

# Request

http://rmb.reuters.com/rmd/rss/wire/STK567?limit=2&#x26;linkType=raw

# Response

The channel alias passed in the request returns a Simple Text item. By default, &#x3C;description> tag retrieves 200 characters. The channel alias passed in the request returns the &#x3C;description> tag with the length of characters in the request. In this case, 200 characters by default even if the length of the &#x3C;description> tag is longer than 200 characters.

&#x3C;rss xmlns:media="http://search.yahoo.com/mrss/" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
&#x3C;channel>
&#x3C;title>Reuters World Service&#x3C;/title>
&#x3C;link>http://www.reutersconnect.com&#x3C;/link>
&#x3C;description>Latest content from Reuters World Service&#x3C;/description>
&#x3C;copyright>
(c) Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp
&#x3C;/copyright>
&#x3C;lastBuildDate>Mon, 10 Feb 2020 16:07:11 GMT&#x3C;/lastBuildDate>
&#x3C;ttl>5&#x3C;/ttl>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">TXT&#x3C;/category>
&#x3C;item>
&#x3C;title>
Smart drones to be tested in battle against E. Africa locust swarms
&#x3C;/title>
&#x3C;link>
http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,2020:newsml_L4N2A33W3:733382832
&#x3C;/link>
&#x3C;description>
By Nita Bhalla NAIROBI, Feb 10 (Thomson Reuters Foundation) - The United Nations is to test drones equipped with mapping sensors and atomizers to spray pesticides in parts of east Africa battling an
&#x3C;/description>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">text&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">TECH&#x3C;/category>
&#x3C;category domain="http://cv.iptc.org/newscodes/subjectcode/">04013000&#x3C;/category>
&#x3C;category domain="http://cv.iptc.org/newscodes/subjectcode/">03001000&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">FLD&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">POL&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">MEAST&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">GEN&#x3C;/category>
…
…
&#x3C;item> … &#x3C;/item>
&#x3C;/channel>
&#x3C;/rss>

Reuters Connect RSS API - Developer Guide 8

Document Version 4.0






# Contents

# 2.2.4 FragmentLength &#x26; completeSentences Sample Request &#x26; Response

# Request

http://rmb.reuters.com/rmd/rss/wire/STK567&#x26;linkType=raw&#x26;fragmentLength=450&#x26;completeSentences=true

# Response

This parameter “fragmentLength” and “completeSentences” only applies to the &#x3C;description> tag. By default, &#x3C;description> tag retrieves 200 characters. If the “completeSentences” is set to “true” the request returns the &#x3C;description> tag as a complete sentence, in other words, any text after the last period would be stripped away. The output will be as follows:

&#x3C;rss xmlns:media="http://search.yahoo.com/mrss/" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
&#x3C;channel>
&#x3C;title>Reuters World Service&#x3C;/title>
&#x3C;link>http://www.reutersconnect.com&#x3C;/link>
&#x3C;description>Latest content from Reuters World Service&#x3C;/description>
&#x3C;copyright>
(c)  Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp
&#x3C;/copyright>
&#x3C;lastBuildDate>Mon, 10 Feb 2020 16:07:11 GMT&#x3C;/lastBuildDate>
&#x3C;ttl>5&#x3C;/ttl>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">TXT&#x3C;/category>
&#x3C;item>
&#x3C;title>
Smart drones to be tested  in battle against E. Africa locust swarms
&#x3C;/title>
&#x3C;link>
http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,2020:newsml_L4N2A33W3:733382832
&#x3C;/link>
&#x3C;description>
By Nita Bhalla NAIROBI, Feb 10 (Thomson Reuters Foundation) - The United Nations is to test drones
equipped  with mapping sensors and atomizers to spray pesticides in parts of east Africa battling an
invasion  of desert locusts that are ravaging crops and exacerbating a hunger crisis.
&#x3C;/description>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">text&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">TECH&#x3C;/category>
&#x3C;category domain="http://cv.iptc.org/newscodes/subjectcode/">04013000&#x3C;/category>
&#x3C;category domain="http://cv.iptc.org/newscodes/subjectcode/">03001000&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">FLD&#x3C;/category>
&#x3C;category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">POL&#x3C;/category>
…
…
&#x3C;item> … &#x3C;/item>

&#x3C;/channel>
&#x3C;/rss>

Reuters Connect RSS API - Developer Guide

Document Version 4.0






# Contents

Request

http://rmb.reuters.com/rmd/rss/wire/STK567&#x26;linkType=raw&#x26;fragmentLength=400&#x26;completeSentences=false

Response

This parameter only applies to the &#x3C;description> tag. By default, &#x3C;description> tag retrieves 200 characters. If the “completeSentences” is set to “false” the request returns the &#x3C;description> tag with the length of characters in the request, in this case 400 characters, even if the extension of the &#x3C;description> tag is longer. Maximum value is 400. The parameter completeSentences is false by default.

&#x3C;rss  xmlns:media="http://search.yahoo.com/mrss/"  xmlns:dc="http://purl.org/dc/elements/1.1/"  version="2.0">
&#x3C;channel>
&#x3C;title>Reuters  World  Service&#x3C;/title>
&#x3C;link>http://www.reutersconnect.com&#x3C;/link>
&#x3C;description>Latest  content   from Reuters World Service&#x3C;/description>
&#x3C;copyright>
(c) Copyright Thomson  Reuters   2013. Check for restrictions at:
http://about.reuters.com/fulllegal.asp
&#x3C;/copyright>
&#x3C;lastBuildDate>Mon,  10 Feb 2020 16:07:11   GMT&#x3C;/lastBuildDate>
&#x3C;ttl>5&#x3C;/ttl>
&#x3C;category  domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">TXT&#x3C;/category>
&#x3C;item>
&#x3C;title>
Smart drones to   be tested  in battle against E. Africa locust swarms
&#x3C;/title>
&#x3C;link>
http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,2020:newsml_L4N2A33W3:733382832
&#x3C;/link>
&#x3C;description>
By Nita Bhalla    NAIROBI, Feb 10 (Thomson Reuters  Foundation)  - The United  Nations is to test
drones  equipped  with mapping sensors and  atomizers  to spray  pesticides in  parts of east
Africa  battling  an invasion  of desert locusts that  are ravaging crops  and  exacerbating a
hunger  crisis.   Hundreds of millions of the voracious insects  have  swept  across Ethiopia,
Somalia and Kenya    in what the U.N. has
&#x3C;/description>
&#x3C;category  domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">text&#x3C;/category>
&#x3C;category  domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">TECH&#x3C;/category>
&#x3C;category  domain="http://cv.iptc.org/newscodes/subjectcode/">04013000&#x3C;/category>
&#x3C;category  domain="http://cv.iptc.org/newscodes/subjectcode/">03001000&#x3C;/category>
&#x3C;/channel>
&#x3C;/rss>
Reuters Connect RSS API - Developer Guide    10

Document Version 4.0






# 2.3 olr

This method looks at the most recent SNEP (link list) for a given channel and returns only the top 10 NEPs as items. A SNEP (Super News Event Package) provides prioritized views of packages in an Online Report as decided by Reuters Editorial staff. This is also called a Link List and it always points to other NEPs.

# 2.3.1 Syntax

http://rmb.reuters.com/rmd/rss/olr/{CHANNEL-ALIAS}[?linkType=X]

# 2.3.2 Parameters

| PARAMETER                  | DESCRIPTION                                                             | REQUIRED |
| -------------------------- | ----------------------------------------------------------------------- | -------- |
| CHANNEL-ALIAS              | The 5-character identifier for a channel in the Media Connect Platform. | Yes      |
| COMMON-QUERY-STRING-PARAMS | • linkType                                                              | No       |

Note maxAge and limit are ignored as the items returned by this method are dictated by the most recent SNEP.

# 2.3.3 Sample Request &#x26; Response

Request

http://rmb.reuters.com/rmd/rss/olr/XBf945?linkType=raw

Response

The channel alias passed in the request returns an Online Report content including the images of the item with each picture rendition as shown below:

<rss xmlns:media="http://search.yahoo.com/mrss/" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
<channel>
# UK Online Report Business News
http://www.reutersconnect.com
<description>Latest content from UK Online Report Business News</description>
<copyright>
(c) Copyright Thomson Reuters 2013. Check for restrictions at: http://about.reuters.com/fulllegal.asp
</copyright>
<lastbuilddate>Tue, 11 Feb 2020 09:22:20 GMT</lastbuilddate>
<ttl>5</ttl>
<category domain="http://xml.media.reuters.com/g2-standards/taxonomies/prodChannel/">OLR</category>
<item>
UK plans to introduce border controls on EU goods after post-Brexit transition

http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,2020:newsml_KBN20425H:2?channel=XBf945

<description>
LONDON (Reuters) - Britain plans to introduce import controls on European Union goods at the border after its post-Brexit transition period ends on Dec. 31 this year, senior minister Michael Gove said
</description>
</item>
</channel>
</rss>




Reuters Connect RSS API - Developer Guide

# Contents

# Categories

- <category domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">composite</category>
- <category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">UK</category>
- <category domain="http://xml.media.reuters.com/g2-standards/taxonomies/N2/">TRD</category>
- <category domain="http://cv.iptc.org/newscodes/subjectcode/">04000000</category>

# Publication Date

Mon, 10 Feb 2020 18:16:21 GMT

# GUID

tag:reuters.com,2020:newsml_KBN20425H:2

# Copyright

(c) Copyright Thomson Reuters 2020. Click For Restrictions - https://agency.reuters.com/en/copyright.html

# Status

State: active, Reason: usable

# Credit

Source: Reuters

Original Provider: Reuters

# Media Group

# Type

StillImage

# Media Content

| File Size | Height | Width | Type       | Medium | URL                                                                                                                                                    |
| --------- | ------ | ----- | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 11505     | 98     | 150   | image/jpeg | image  | Thumbnail    |
| 25427     | 295    | 450   | image/jpeg | image  | View Image   |
| 49459     | 525    | 800   | image/jpeg | image  | Base Image   |
| 4197776   | 2919   | 4451  | image/jpeg | image  | Filed Image |

# Thumbnail

# Creator

Reuters

# Publisher

reuters.com

# Language

en

Document Version 4.0




# 2.4 basicSearch

The basicSearch method is used to obtain a list of news items which matches the criteria you provide. The search can be made against one of the following: fulltext (body, headline, caption), id, topic, signal or slug.

# Stemming

basicSearch supports stemming. So a search for ‘Amy’ will return results matching ‘Amie’ as well. And a search for „mining’ will also return results containing „mine’ and „miners’.

# Maximum date range

This method allows you to retrieve news items as old as 30 days.

maxAge = 30D

# Ingestion Delay

Due to the processing required to analyze and index content, there may be a delay of up to 2 minutes between the time that content is ingested into Reuters systems and when it is made available via the API.

Reuters Connect RSS API - Developer Guide    13

Document Version 4.0



Contents

# 2.4.1 Syntax

http://rmb.reuters.com/rmd/rss/basicSearch?q={search-term}[&#x26;field=value]

# 2.4.2 Parameters

| PARAMETER | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REQUIRED |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| q         | This parameter is used to specify the attributes by which the items returned should be filtered. q=\[search\_term] The query parameter can be used with any of the following filter options. Filter Options- **Phrase searches:** The API supports searching on a collection of one or more terms by surrounding those terms with double quotes (“state of the union”). By placing a series of terms in double quotes, you are requesting that only news items with these exact terms in the precise order you entered be returned. q=”George Bush” will match news items containing George followed immediately by Bush. By contrast, a script containing “George Clooney meets Kate Bush” will not return a match.
- **Wildcards:** The API supports the use of the \* and ? wildcards within search terms. The asterisk character (\*) is used to substitute for zero or more characters. q=geo\* matches George, Geoff, geology, geo-political. The question mark (?) is used to substitute for any single character. For substituting „n‟ characters, use „n‟ number of question marks. q=AT? matches ATM, AT\&T q=defen?e matches defence, defense q=psych????y matches psychology, psychiatry
- **Invalid Usage:** Reuters does not support the use of wildcard characters at the beginning of a single search term or within an explicit phrase. Examples of Invalid Usage: q=?eorge q=”San \*ose” The above queries will not fetch any results.
- **Boolean operators:** Reuters supports the use of AND, OR and NOT to refine the manner in which terms with a search are applied. The Boolean operators are not case-sensitive. q=england AND cricket | Yes      |

Reuters Connect RSS API - Developer Guide    14
Document Version 4.0




# Contents

# PARAMETER

# DESCRIPTION

# REQUIRED

q= england AND cricket

will match only those feeds which contain both „england‟ and „cricket‟

q= england OR cricket

will match feeds which contain either „england‟ or „cricket‟ or both.

q= cricket NOT england

will match feeds which contain „cricket‟ and where the word „england‟ is not present.

If no Boolean operator is specified, „AND‟ is implied. So, searching on „england cricket‟ would be equivalent to “england AND cricket”

# Grouping (nesting)

Reuters allows you to use the parenthesis symbols ( ) to group/nest terms and/or phrases within a search.

q=“bird flu” AND (china OR europe) AND immunizations

will match all feeds containing the phrase bird flu and the term immunizations and either the term China or Europe.

# field

Determines which field the query from the q parameter is executed against.

No

# Possible values:

- main: This is a pre-defined group provided to ease the searching across multiple fields. This is used to specify the keywords that may be contained within one or more of the following fields of the news items that are retrieved: body, headline, caption, id, topic, signal and slug.
- fulltext: This is another pre-defined group and is used to specify the keywords that may be contained within one or more of the following fields of the news items that are retrieved: body, headline, caption.
- headline: used to specify the keywords that should be contained within the headline of the news items that are retrieved.
- topic: used to specify the topic codes (i.e., NewsML News2000 subject codes) associated with the news items to be retrieved.
- slug: used to specify the keywords that should be contained within the slug of the news items that are retrieved.
- signal: used to specify the signal codes (i.e., NewsML signal codes) associated with the news items to be retrieved.
- id: used to specify one of the following news item identifiers by which to retrieve news items. Valid news item identifiers are: id, guid, USN, OTR, IID, SID and editNumber.

# Examples:

- q=uganda&#x26;field=headline
- q=uganda&#x26;field=fulltext

Reuters Connect RSS API - Developer Guide

Document Version 4.0






# Contents

| PARAMETER       | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REQUIRED |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| mediaType       | This parameter is used to specify the media type of the feed to be retrieved. Valid media types are:- T (text)
- P (picture)
- V (video)
- G (graphic)Examples: q=libya\&mediaType=T q=hurricane\&mediaType=P If multiple media types are specified, each should be specified in a separate query string parameter. mediaType=P\&mediaType=T Default Value: All available media types will be considered.                                                           | No       | | |
| channel         | This parameter is used to specify the channel alias for which you wish to retrieve the news feed. To obtain the alias for a given channel, use the channels method. Example: q=irene\&channel=STK567 If multiple channel aliases are specified, each should be specified as a separate query string parameter. channel=ABC\&channel=DEF Default Value: If no channel alias is supplied, results will be returned for all the channels to which you have subscribed. | No       |
| channelCategory | This parameter is used to specify the channel categories to be used when retrieving news items. A channel category is a group of channels containing similar content (Example: TXT, PIC, GRA, OLV, BRV, OLR). Example: q=irene\&channelCategory=PIC Note: When both channel and channelCategory are supplied, all channels matching „channel‟ as well as „channelCategory‟ will be returned i.e., the result will be a union of the criteria passed.                | No       |

Reuters Connect RSS API - Developer Guide

Document Version 4.0






# Contents

# PARAMETER

# DESCRIPTION

# REQUIRED

Default Value: If no value is supplied, all channel categories will be included for searching.

# COMMON-QUERY-STRING-PARAMS

- limit
- maxAge (can be used to retrieve feeds up to a maximum of 30 days)
- linkType

# 2.4.3 Sample Request

http://rmb.reuters.com/rmd/rss/basicSearch?q="red cross"&#x26;field=headline&#x26;linktype=raw&#x26;mediaType=T&#x26;maxAge=7D

# 2.4.4 Sample Response

<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
<channel>
# Basic Search: "red cross"
<description>Basic Search: "red cross"</description>
<copyright>(c) Copyright Thomson Reuters 2011. Check for restrictions at: http://about.reuters.com/fulllegal.asp</copyright>
<lastbuilddate>Tue, 06 Sep 2011 00:16:42 GMT</lastbuilddate>
<ttl>5</ttl>
<item>
# WRAPUP 1-Red Cross visits Syrian jail, raids near Turkey
http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,0000:newsml_L5E7K53U6:1597550438
<description>* Red Cross says let into Damascus central prison * Biggest military push into restive northwest since June * Street protesters not wilting despite military crackdown * Cameron says Assad must go for</description>
<category domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">text</category>
<category> ... </category>
Tue, 06 Sep 2011 00:16:42 GMT</pubdate>
<guid ispermalink="false">tag:reuters.com,0000:newsml_L5E7K53U6:1597550438</guid>
<media:copyright>(c) Copyright Thomson Reuters 2011. Click For Restrictions - http://about.reuters.com/fulllegal.asp</media:copyright>
<media:status state="active" reason="usable">
<media:credit role="origprov" scheme="http://xml.media.reuters.com/g2-standards/taxonomies/cRole/">Reuters</media:credit>
<dc:creator>Reuters</dc:creator>
<dc:publisher>reuters.com</dc:publisher>
<dc:language>en</dc:language>
</media:status></item>
<item>
# WRAPUP 2-Red Cross visits Syrian jail, raids renew near Turkey
http://http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,0000:newsml_L5E7K5398:539541164
<description>* Red Cross says let into Damascus central prison * Biggest military push into restive northwest since June * Street protesters not wilting despite military crackdown * Cameron says Assad must go for</description>
<category domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">text</category>
</item>
</channel>
</rss>




# Contents

<item>
# UPDATE 2-Syria opens prisons for first Red Cross visits-ICRC
http://rmb.reuters.com/rmd/rss/item/tag:reuters.com,0000:newsml_L5E7K5296:201250230
<description>(adds details, background) GENEVA, Sept 5 (Reuters) - Syria has opened its prisons for the first time to the Red Cross whose officials visited detainees in the central prison in Damascus, the</description>
<category domain="http://xml.media.reuters.com/g2-standards/taxonomies/pmt/">text</category>
</item>

Reuters Connect RSS API - Developer Guide

Document Version 4.0




# Contents

# 3 RSS OUTPUT FOR DIFFERENT MEDIA TYPES

This section details the RSS <item> output for each of the various media types that can be returned from this API.</item>

- Text - A text item contains all the fields described below except the media:group set of elements.
- Pictures - A Picture item contains the same metadata elements as text item output and additionally provides media links to renditions of the binary asset.
- Graphics - A Graphic Item will have the same output as the Picture Item Output, except that the media content links will relate to each rendition of the graphic.
- Online Video - An Online Video Item will have the same output as the Picture Item Output, except that the media content links will relate to each rendition of the video, and there will be some additional metadata for audio and picture.
- Broadcast Video - Broadcast Video output is like Online Videos but limited to the picture and flashpreview video.
- Online Reports - A NEP consists of a main text item and an optional picture item. So, the output here is like the Text item output, plus the RSS output of the picture. And the link tag and guid will reference the NEP.

The following table describes in detail the various output fields for each of the media type.

Note: Unless otherwise mentioned, the description of the fields holds good for all media types.

| FIELD       | DESCRIPTION                                                                                                                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| title       | Headline of the item                                                                                                                                                                                                                                                                                                     |
| link        | The link would vary depending on the value passed to linkType. Currently only linkType=raw is supported. ➢ For Text / Online Video / Broadcast Video • With linkType=raw, it will reference the HTML script from the NewsML2 ➢ For Picture & Graphics • With linkType=raw, it will reference the base image from NewsML2 |
| description | ➢ For Text / Online Video / Broadcast Video • Beginning portion of the body ➢ For Picture & Graphics • Caption of the item                                                                                                                                                                                               |

Reuters Connect RSS API - Developer Guide

Document Version 4.0






# Contents

| FIELD           | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| category        | This holds the category value. It has one attribute ‘domain’ which is a URI representing the taxonomy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                 | List possible URIs:- http\://xml.media.reuters.com/g2-standards/taxonomies/pmt (Product Media Type) - defines the type of the item as a string value
* Examples: text / picture / graphic / video
- http\://xml.media.reuters.com/g2-standards/taxonomies/MCC (Media category Code)
* Examples: a / i / I
- http\://xml.media.reuters.com/g2-standards/taxonomies/N2 (News2000 Subject Code)
* Examples: AFR / CWP / DIP / GEN / LY / OEC / PIL
- http\://cv.iptc.org/newscodes/subjectcode (IPTC Subject Reference Code)
* Examples: 11000000 / 11002000 / 16003000 / 16009000 |
| pubDate         | Revision date of the document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| guid            | Unique identifier of an item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| media:copyright | Copyright details of party claiming intellectual property for the content. This will include the copyright holder and copyright notice details.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| media:status    | Status of the media object. It has the following two attributes:- state - can have one of the following values:

* active – the media object is active in the system
* deleted - the media object has been deleted by the publisher
* blocked - the media object is blocked by the publisher

- reason - can have the following values:

* When state = active, reason = usable
* When state = deleted, reason = canceled
* When state = blocked, reason = withheld                                                                                                         |
| media:credit    | The individual(s) or companies responsible for contributing content to the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| media:group     | ➢ Text – Not Applicable ➢ Picture- dc:type – StillImage
- media:content - This contains details of each rendition of the image, namely: base image, thumbnail and view image
- media:description – This contains the picture caption.
- media:thumbnail – This contains attributes and details of the thumbnail                                                                                                                                                                                                                                                                         |






# Contents

# FIELD

# DESCRIPTION

- Graphics
- dc:type – StillImage
- media:content - This contains details of each rendition of the graphic, namely: base image, thumbnail and view image
- media:thumbnail – This contains attributes and details of the thumbnail
- Online Video
An online video file will have a combination of pictures, video files and an audio file. There will be one media:group for each type (picture/video/audio)

- dc:type
- For picture files, the type will be StillImage.
- For video files, the type will be MovingImage.
- For audio files, the type will be Sound.
- media:content - This contains details of each rendition of the graphic, namely: base image, thumbnail and view image
- For picture files, this will contain the rendition of each of the image
- For video files, this will contain the rendition of each type of video
- For audio files, this will contain the rendition of the audio file.
- media:thumbnail - Contains attributes and details of the thumbnail for picture files
- Broadcast Video
The output here is like Online Videos but contains only the picture and flash preview videos. There will be one media:group for each type (picture/video)

- dc:type
- For picture files, the type will be StillImage.
- For video files, the type will be MovingImage.
- media:content - This contains details of each rendition of the graphic, namely: base image, thumbnail and view image
- For picture file, this will contain the rendition of the view image.
- For video file, this will contain the rendition of video
- Online Report
A NEP consists of a main text item and an optional picture item. So the media:group contains the picture item details.

- dc:type – StillImage
- media:content - This contains details of each rendition of the image, namely: base image, thumbnail and view image
- media:description – This contains the picture caption.
- media:thumbnail - Contains attributes and details of the thumbnail

<dc:creator> Party responsible for creating the item</dc:creator>

Reuters Connect RSS API - Developer Guide 21

Document Version 4.0






# Contents

| FIELD           | DESCRIPTION                       |
| --------------- | --------------------------------- |
| \<dc:publisher> | Party providing the item          |
| \<dc:language>  | The language(s) used in the item. |

# Reuters Connect RSS API - Developer Guide

Document Version 4.0




# TECHNICAL SUPPORT

Contact us:

To contact support, go to https://liaison.reuters.com/

Or send an email to ReutersMediaSupport@thomsonreuters.com

Reuters Connect RSS API - Developer Guide

Document Version 4.0





# APPENDIX 1 – COMMON USE CASES FOR THE RSS API

This section provides the typical use cases of RSS API.

1. Listing your subscribed channels:

http://rmb.reuters.com/rmd/rss/channels
2. Listing all the items published within a channel; for example: Reuters World News Service (RWS - STK567) a text channel in the last 4 hours.

http://rmb.reuters.com/rmd/rss/wire/STK567?&#x26;linkType=raw&#x26;mediaType=T&#x26;maxAge=4h
3. Listing the content in a Picture channel; for example: Reuters News Picture Service (RNPS - pwu404)

http://rmb.reuters.com/rmd/rss/wire/pwu404?&#x26;linkType=raw&#x26;mediaType=P
4. Retrieving binary assets such as pictures from a Picture channel. There are four picture renditions: View Image, Thumbnail, BaseImage and LimitedImage as shown below; copy/paste desired rendition to download it.

<media:group>
<dc:type>StillImage</dc:type>
<media:content filesize="47854" height="420" type="image/jpeg" width="640" medium="image" url="http://rmb.reuters.com/rmd/rss/content/tag:reuters.com,2020:newsml_UP1EG1V0RZ0P9:1840056753/tag:reuters.com,2020:binary_UP1EG1V0RZ0P9-VIEWIMAGE">
<media:content filesize="11760" height="98" type="image/jpeg" width="150" medium="image" url="http://rmb.reuters.com/rmd/rss/content/tag:reuters.com,2020:newsml_UP1EG1V0RZ0P9:1840056753/tag:reuters.com,2020:binary_UP1EG1V0RZ0P9-THUMBNAIL">
<media:content filesize="3796541" height="2389" type="image/jpeg" width="3641" medium="image" url="http://rmb.reuters.com/rmd/rss/content/tag:reuters.com,2020:newsml_UP1EG1V0RZ0P9:1840056753/tag:reuters.com,2020:binary_UP1EG1V0RZ0P9-BASEIMAGE">
<media:content filesize="747066" height="2296" type="image/jpeg" width="3500" medium="image" url="http://rmb.reuters.com/rmd/rss/content/tag:reuters.com,2020:newsml_UP1EG1V0RZ0P9:1840056753/tag:reuters.com,2020:binary_UP1EG1V0RZ0P9-LIMITEDIMAGE">
<dc:format>image/jpeg</dc:format>
</media:content></media:content></media:content></media:content></media:group>
5. Listing all the content within an Online Report Channel; for example: Spain Online Report Entertainment News (AfN325) with a maximum number of items to return of 50

http://rmb.reuters.com/rmd/rss/olr/AfN325?linkType=raw&#x26;limit=50
6. Listing content in an Online Video channel; for example: Business Video Online (CLE548) with all video renditions (look for <dc:type>MovingImage</dc:type> of each item:

http://rmb.reuters.com/rmd/rss/wire/CLE548&#x26;linkType=raw

Reuters Connect RSS API - Developer Guide

Document Version 4.0




# Reuters Connect RSS API - Developer Guide

# Document Version 4.0

# Media Content

| Bitrate | Duration | File Size | Height | Sampling Rate | Type        | Width | Medium | URL                                                                                                                                                    |
| ------- | -------- | --------- | ------ | ------------- | ----------- | ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 64.0    | 70       | 700172    | 144    | 8.0           | video/3gpp2 | 176   | video  | Link    |
| 464.0   | 70       | 4529753   | 288    | 44.1          | video/x-flv | 512   | video  | Link   |
| 64.0    | 70       | 700172    | 144    | 8.0           | video/3gpp  | 176   | video  | Link    |
| 268.0   | 70       | 2636361   | 216    | 22.05         | video/mpeg  | 384   | video  | Link   |
| 268.0   | 70       | 2685830   | 216    | 22.05         | video/x-flv | 384   | video  | Link   |
| 5000.0  | 70       | 45539035  | 720    | 44.1          | video/mpeg  | 1280  | video  | Link  |
| 1872.0  | 70       | 17487107  | 432    | 44.1          | video/mpeg  | 768   | video  | Link  |
| 624.0   | 70       | 6146011   | 360    | 44.1          | video/mpeg  | 640   | video  | Link   |
| 604.0   | 70       | 6183669   | 324    | 44.1          | video/x-flv | 576   | video  | Link   |
| 8000.0  | 70       | 69569251  | 1080   | 44.1          | video/mpeg  | 1920  | video  | Link |
| 6500.0  | 70       | 64325632  | 576    | 48.0          | video/mpeg  | 720   | video  | Link  |
| 8000.0  | 70       | 69994765  | 1080   | 44.1          | video/mpeg  | 1920  | video  | Link  |
| 1500.0  | 70       | 19577664  | 720    | 48.0          | video/mp4   | 1280  | video  | Link  |

# Searching for a specific word

Searching for a specific word such as: Olympics within a headline in the channel – Reuters World Service (STK567) in the last 10 days:

Search Link

# Retrieve the channel item’s “description” tag by default:

Retrieve Link

<description>
(Updates death toll to six; adds Taliban denial of responsibility) By Abdul Qadir Sediqi KABUL, Feb 11 (Reuters) - A suicide bomber killed six people near a military academy in the Afghan capital,

</description>






# Retrieve the channel item’s “description” tag with a length of 500 characters

Maximum value is 400; even if it is set to 500 characters, only will show up 400 characters. The parameter “completeSentences” is false by default.

http://rmb.reuters.com/rmd/rss/wire/STK567&#x26;linkType=raw&#x26;fragmentLength=500&#x26;completeSentences=false

<description>
(Updates death toll to six; adds Taliban denial of responsibility) By Abdul Qadir Sediqi KABUL, Feb 11 (Reuters) - A suicide bomber killed six people near a military academy in the Afghan capital, Kabul, on Tuesday, the interior ministry said. The Taliban denied involvement in the blast and there was no immediate claim of responsibility for the attack. The bombing took place near the

</description>

# Retrieve the channel item’s “description” tag as a complete sentence

The “fragmentLength” parameter should be included (using the maximum value for better results).

http://rmb.reuters.com/rmd/rss/wire/STK567?&#x26;linkType=raw&#x26;fragmentLength=400&#x26;completeSentences=true

<description>
(Updates death toll to six; adds Taliban denial of responsibility) By Abdul Qadir Sediqi KABUL, Feb 11 (Reuters) - A suicide bomber killed six people near a military academy in the Afghan capital, Kabul, on Tuesday, the interior ministry said. The Taliban denied involvement in the blast and there was no immediate claim of responsibility for the attack.

</description>

# Retrieve the channel item’s description only with 100 characters

http://rmb.reuters.com/rmd/rss/wire/STK567&#x26;linkType=raw&#x26;fragmentLength=100

Reuters Connect RSS API - Developer Guide

Document Version 4.0






# APPENDIX 2 – FREQUENTLY ASKED QUESTIONS (FAQS)

This section provides the most frequent questions about RSS API

# What version of RSS does Reuters provide?

Reuters Connect RSS uses RSS 2.0 in conjunction with mRSS extensions for pictures, graphics and video content.

# What content is available via Reuters Connect RSS?

Text, Pictures, Graphics, Online Reports, Online Video and Broadcast Video Scripts. Broadcast Video files are not available via RSS.

# I received my welcome email, when I followed the link to register my account, I was in Reuters Connect. What is that?

Reuters Connect is a hosted website providing customers with password-protected access to their content subscriptions. Reuters Connect included as part of your RSS subscription. The tool is browser-based, and no software installation is required. The RSS Configuration section in Reuters Connect (click over your username, then click over “My Settings”) allows you to configure your RSS feeds and access RSS URLs. Reuters Connect also provides access to text newswires, pictures, graphics, broadcast video, online video and online reports.

# How do I log in?

Reuters Connect access is included as part of your RSS subscription. Your welcome email includes:

- A username and password for Reuters Connect
- A username and password for Reuters Connect RSS

Please also note:

- Your username is identical for both Reuters Connect and Reuters Connect RSS. However, passwords are unique for each application.
- Your RSS username is case sensitive.

# Which Internet browsers can I use?

Any browser that is RSS enabled and supports RSS 2.0 and mRSS can be used with Reuters Connect RSS.

# What RSS readers does Reuters support?

Reuters Connect RSS should be compatible with any reader that supports RSS 2.0, mRSS and password authentication.

Reuters Connect RSS API - Developer Guide 23

Document Version 4.0






# Reuters Connect RSS API - Developer Guide

# Is there a minimum recommended hardware configuration?

Reuters Connect RSS only requires an operating system and Web browser. Hardware recommendations specified for Mozilla Firefox and Google Chrome are listed below:

- Windows/Linux:

# Where do I find the RSS links?

These can be found in the RSS Configuration section. You can log in to Reuters Connect web site, click over your username located in the upper-left corner of the page, then click over “My Settings”, then scroll down to the bottom of the page and your RSS links to individual feed subscriptions can be found under their respective category: Text, Pictures, Graphics, Online Video and Online Reports. A single RSS link to all your subscription services is also available.

# How do I configure my Reuters Connect RSS feeds?

- At any time, you can access the RSS Configuration section in Reuters Connect.

# What are my configuration options?

- Maximum number of items:
- - 10
- 50
- 100

Items published in last X hours:
- - 2 hours
- 8 hours
- 24 hours

RSS links to:

# Can I configure on a service-by-service basis?

No, these configuration options apply to all of your services.

# I have just completed my set up and see fresh content on some services, but others still must update?

Not all services are updated frequently. You may wish to consider increasing the time period under the “Items published in last X hours” setting.

# Why have none of my RSS feeds updated in my Internet Browser after I first added them?

Please check your Internet Browsers RSS feed settings. The default refresh rate varies between browsers and may need changing.

# I configured my RSS feed to link to “Item in Reuters Connect” and have already entered my RSS username and password. However, when I click on a headline, I receive a prompt for another username and password?






When you link to the Item in Reuters Connect you must enter your Reuters Connect username and password. Once logged into Reuters Connect you won’t be prompted for this again, until you exit your Reuters Connect session. If you are already logged into Reuters Connect you will not receive the username and password prompt.

# Can I have different configurations between locations or applications, such as between a work PC and a home PC or another Internet Browser?

Yes. Configure these settings in the RSS Configuration section, then copy and paste RSS link URLs into the 1st application/location. Once complete you can reconfigure settings in the RSS Configuration tab and copy &#x26; paste updated RSS link URLs for a 2nd application/location. RSS feeds previously setup on your Internet Browser or Reader are not impacted by any configuration changes made in the RSS Configuration section once they are added to your Internet Browser or Reader.

# I updated the configuration in the RSS Configuration section, and I don’t see any change in my Internet Browser/Reader?

Once added to your Internet Browser or Reader your RSS feeds are not impacted by any configuration changes made in the RSS Configuration section. To reconfigure RSS feeds, first make the desired configuration changes in the RSS Configuration section in Reuters Connect. You will then need to copy &#x26; paste the updated RSS link URLs into your Internet Browser or Reader, replacing the existing URLs. Save your changes and you are finished.

# What formats are text services offered in?

Text services are available for downloading as NewsML G2 or plain text.

# What formats are Online Videos offered in?

# VIDEO FORMATS

Publishers can access a wide range of standardized audio and video compression formats.

| Format Name | Target Bitrates (kb/s) | Video Frame Size (WxH) | RendItion In XML               | FPS   | Video Bitrates (kb/s) | Audio Codec | Audio (S)plit / (M)Ixed |   |
| ----------- | ---------------------- | ---------------------- | ------------------------------ | ----- | --------------------- | ----------- | ----------------------- | - |
| HD 1080     | 8256                   | 1920 x 1080            | stream:8256:16x9:hd1080p30.mp4 | 29.97 | 8000                  | AAC-LC      | S                       |   |
| HD 720      | 5128                   | 1280 x 720             | stream:5128:16x9:hd720p30.mp4  | 29.97 | 5000                  | AAC-LC      | M                       |   |
| MPEG 2      | 6756#                  | 720 x 576              | stream:6756:16x9:mpg           | 25    | 6500                  | MP2         | S                       |   |
| Flash 300   | 300                    | 384 x 216              | stream:300:16x9:flv            | 25    | 268                   | MP3         | M                       |   |
| Flash 512   | 512                    | 512 x 288              | stream:512:16x9:flv            | 25    | 464                   | MP3         | M                       |   |
| Flash 700   | 700                    | 576 x 324              | stream:700:16x9:flv            | 25    | 604                   | MP3         | M                       |   |
| MPEG 4 300  | 300                    | 384 x 216              | stream:300:16x9:mp4            | 25    | 268                   | AAC-LC      | M                       |   |
| MPEG 4 700  | 700                    | 640 x 360              | stream:700:16x9:mp4            |       | 25                    | 624         | AAC-LC                  | M |
| MPEG 4 2000 | 2000                   | 768 x 432              | stream:2000:16x9:mp4           | 25    | 1872                  | AAC-LC      | M                       |   |
| 3GPP2 80    | 80                     | 176 x 144              | stream:80:11x9:3g2             |       | 15                    | 64          | AMR-NB                  | M |
| 3GPP 80     | 80                     | 176 x 144              | stream:80:11x9:3gp             | 15    | 64                    | AMR-NB      | M                       |   |

* Only format with anamorphic pixels, Interlaced, with a 5 seconds slate and key frame interval of 480 milliseconds. All other formats are Progressive, with key frames set after scene change.

Reuters Connect RSS API - Developer Guide 25

Document Version 4.0






# This table lists the audio renditions that are available for use:

# AUDIO FORMATS

Broadcast-ready, high-quality sound files can be readily edited, converted or mixed.

| Rendition              | Format           | Target Bitrates (kb/s) | Extension |
| ---------------------- | ---------------- | ---------------------- | --------- |
| rend:stream:20.050:mp3 | MP3 (audio only) | 56                     | mp3       |

# JPEG formats delivered with Online Videos: Rendition

| Rendition                 | Default Width                     | Default Height              |
| ------------------------- | --------------------------------- | --------------------------- |
| rend:baseImage            | Highest resolution possible       | Highest resolution possible |
| rend:viewImage:450x640    | 450                               | 640                         |
| rend:thumbnail:150x100    | 150                               | 100                         |
| rend:limitedimage:max3500 | Max. 3500 along the longest side. |                             |

# What formats are Pictures offered in?

Pictures are available as jpeg downloads in 4 resolutions:

- Thumbnail – 150 pixels along the longest side
- Medium (view image) – 450 pixels along the longest size
- High resolution (base image) – varies in size
- Limited Image - max 3500 pixels along the longest side

# What formats are Graphics offered in?

Graphics are available as Encapsulated Postscript (EPS) downloads along with thumbnail and medium resolution JPEGS for quick image preview.

# Is Metadata available?

Metadata is delivered with the RSS feed, your ability to see the metadata is dependent on the method you are using to view the RSS feed.

# I subscribe to Reuters Online Reports, why are there 2 RSS links for each service?

You can choose to view the Online Reports either in a packaged Top 10 format (select the Top10 link) or as chronological Newswire showing all the content filed (select All Content).

# I subscribe to Broadcast Video, yet my RSS feed only delivers the scripts and not the video files?

Broadcast video files are not available via RSS, only the associated scripts. You can access your Broadcast Video content via your Reuters Connect account.

# How do I contact you for support?

Reuters Connect RSS API - Developer Guide 26

Document Version 4.0






# Reuters Connect RSS API - Developer Guide

# Document Version 4.0

Please visit: http://liaison.reuters.com/contact-us or send an email to ReutersMediaSupport@thomsonreuters.com

I am not receiving all the product content I expected. Who should I contact?

Please contact Thomson Reuters Customer Support. If this is not a technical issue, they will have your Account Manager contact you.

© 2023 Thomson Reuters. All rights reserved. For more information visit reuters.com/newsagency

Republication or redistribution of Thomson Reuters content, including by framing or similar means, is prohibited without the prior written consent of Thomson Reuters. 'Thomson Reuters' and the Thomson Reuters logo are registered trademarks and trademarks of Thomson Reuters and its affiliated companies.