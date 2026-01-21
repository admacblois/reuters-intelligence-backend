Reuters

# How to push a live video stream via SRT using the Reuters API

# Contents

- Live API ........................................................................................................................ 2
- liveEvents Method ..................................................................................................... 2
- liveEventsSubscriptions Method.................................................................................6
- Mutation Method for Lives .......................................................................................... 7
- How to subscribe and push a live stream via SRT ......................................................8
- How to unsubscribe to a live event ..........................................................................9
- Support ......................................................................................................................10





Reuters
# Live API

This section is designed to be used by developers, who will write and implement the code that interfaces with the Reuters Live video streams. The Reuters API includes a reference implementation of the Live Production Exchange (LPX) recommendation for live video.

Reuters Live streams are currently available for HLS, RTMP and, SRT protocols.

# liveEvents Method

The liveEvents method obtains all the live event information via the API, such as status, headline, usage terms, event details (duration, start date, end date), and more.

| PARAMETERS        | TYPE   | DEFINITION                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | JSON REPRESENTATION                                             |
| ----------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| channels          | String | Filter based on the customer-subscribed channels.                                                                                                                                                                                                                                                                                                                                                                                                                                       | "jbh288"                                                        |
| cursor            | String | The cursor parameter is used to specify the start position of the next page based on the query and sort criteria. Each search page returns a limited number of matching documents, and the "pageInfo" field tracks the pagination result across the search results based on current search queries and sort criteria. Repeat the same query and sort with the "endCursor" value on the last page until "hasNextPage" returns false to the page through a more extensive set of results. | "WzE3MTgxMDA1NDAxXJzL mNvbSwyMDI0Om5ld3NtbF9L QkU5OVQwM1kiXQ==" |
| dateRange         | String | To filter using dates. The date range should be specified as \<start\_date>-\<end\_date>. Date format. YYYY-MM-DD.                                                                                                                                                                                                                                                                                                                                                                      | "2024.01.01-2024.02.02"                                         |
| event Identifiers | Scalar | To filter using a live event by id, uri or usn.                                                                                                                                                                                                                                                                                                                                                                                                                                         | "uri": "9767edef-d472-4109-aaa5-1260424bd0d3"                   |
| limit             | Int    | This parameter is used to designate the maximum number of news items to be retrieved.                                                                                                                                                                                                                                                                                                                                                                                                   | "10"                                                            |




Reuters
current limit is 100, but Reuters reserves the right to change this value at any time. If no limit is specified, the default number of news items returned will be 20.

# page

This parameter is used to designate a specific page of search results to retrieve. The first page is 1 and if no value is specified for the page parameter, the default is 1. The maximum number of news items returned per page is constrained by the limit parameter. The maximum number of page is constrained by the combination of page and limit, page * limit must be less than 2500. If the cursor parameter is specified, the page parameter will be ignored.

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

"copyrightNotice": “(c) 2024 Thomson Reuters, unless otherwise identified. Full statement available at https://www.thomsonreuters.com/en/policies/copyright.html”
# eventDetails

Object Property containing details of the event.

eventDetails:{}
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



Reuters
# Event Status

| Enum           | Status of the event, categories are:       |
| -------------- | ------------------------------------------ |
| "eventStatus": | Cancelled, Scheduled, Live, and Completed. |

# Genre

|         |        | Object                       | Genre codes indicate the nature of the live event, not specifically its content. |
| ------- | ------ | ---------------------------- | -------------------------------------------------------------------------------- |
| name    | String | Genre name                   | "Sport news"                                                                     |
| code    | String | Genre topic or category code | N2: SPO                                                                          |
| literal | String | Genre literal name           |                                                                                  |

# Headline

| String       | A brief and snappy introduction to the content, designed to catch the reader's attention. |
| ------------ | ----------------------------------------------------------------------------------------- |
| “headline” : | “Nikki Haley bus tour in Bamberg, South Carolina                                          |

# ID

| String | Live event stream unique identifier    |
| ------ | -------------------------------------- |
| "id":  | "9767edef-d472-4109-aaa5-1260424bd0d3" |

# Language

| String      | language of the live item |
| ----------- | ------------------------- |
| "language": | "en"                      |

# Location

| String       | The location where the live event happens. |
| ------------ | ------------------------------------------ |
| “location” : | “BAMBERG, SOUTH CAROLINA                   |

# Renditions

| Object                                          | An array of objects, each of which is a rendition of the event. |
| ----------------------------------------------- | --------------------------------------------------------------- |
| The Appendix 5 contains all the rendition list. |                                                                 |

# Aspect Ratio

| String | Live event aspect ratio. We only offer a 16:9 aspect ratio. |
| ------ | ----------------------------------------------------------- |
| "16:9" |                                                             |

# Bitrate

| String     | Signal bitrate. There are different options. |
| ---------- | -------------------------------------------- |
| "8000Kbps" |                                              |

# Code

| String      | Live video profile code. There are different options. Unique identifier |
| ----------- | ----------------------------------------------------------------------- |
| "hls:29.97" |                                                                         |

# Frame Rate

| String  | Live event frame rate. There are different options. |
| ------- | --------------------------------------------------- |
| "29.97" |                                                     |

# Frame Size

| String      | Live event frame Size |
| ----------- | --------------------- |
| "1920x1080" |                       |

# Minimum Bitrate

| String    | Minimum bitrate provided |
| --------- | ------------------------ |
| "200Kbps" |                          |

# Maximum Bitrate

| String  | Maximum bitrate provided |
| ------- | ------------------------ |
| "4Mbps" |                          |

# Name

| String                | Live video profile name. |
| --------------------- | ------------------------ |
| "200Kbps-4Mbps Video: | 1080p29.97 h.264"        |

# Scan Type

| String        | Live event scan type. We only offer progressive scan type. |
| ------------- | ---------------------------------------------------------- |
| "progressive" |                                                            |

# Slugline

| String      | Item slug or short name used to identify an event. Slugs are a Reuters editorial mechanism used to standardize content by event. |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| “slugline”: | “NATO-DEFENCE/STOLTENBERG”                                                                                                       |




Reuters

topic String Indicates subject of the event “Topic” : “Politics / International Affairs”

uri String Live event story unique number "uri": "tag:reuters.com,2024: Newsml_ADKQ4TP20"

usageTerms String Usage terms of the live event, it will display the live event restrictions. "usageTerms": "Broadcast: No use UK, Digital: No use UK"

usn String Live event story unique number. "usn": "ADKQ4TP20" Same identifier as the uri

version String Version of the live event "version": "681326751"

versionCreated Scalar Date when the current version was created "versionCreated": "2024-02-14T17:55:06.000Z"

pageInfo Object Search results page information

endCursor String endCursor token information "WzE3MTgxMDA1NDAxXJzLmNvbSwyMDI0Om5ld3NtbF9LQkU5OVQwM1kiXQ=="

hasNextPage Boolean if the search has next page or not: true or false

totalHits Scalar Total number of findings "8"





Reuters

# liveEventsSubscriptions Method

The liveEventSubscriptions method is used to provide information about existing live event subscriptions of an API user.

| PARAMETERS     | TYPE   | DEFINITION                                                                               | JSON REPRESENTATION                    |
| -------------- | ------ | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| dateRange      | String | To filter using dates. The date range should be specified as -. Date format. YYYY-MM-DD. |                                        |
| eventIds       | Scalar | To filter using live event ids (unique identifiers per event)                            | "2554f23f-05a1-435c-ab5b-adf614025d20" |
| types          | Enum   | To filter based on the type of subscription (HLS, HDS, RTMP)                             |                                        |
| eventId        | String | The unique identifier of the event                                                       |                                        |
| subscriptions  | Object | Property containing details of subscriptions                                             |                                        |
| renditionCode  | String | Identifier of a particular rendition of an event                                         | "hls:29.97"                            |
| rtmpUserName   | String | Username parameter for the RTMP destination in a push subscription request               |                                        |
| subscriptionId | String | Unique identifier of the event                                                           | "3c9802025ee68bdb120f"                 |
| url            | String | Location to the content rendition for a pull rendition (e.g HLS)                         |                                        |





Reuters

# Mutation Method for Lives

The mutation method used for lives allows you to subscribe and unsubscribe to a live event.

# PARAMETERS

| TYPE   | DEFINITION           | JSON REPRESENTATION                                                                                                                                                       |
| ------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object | liveEventSubscribe   |                                                                                                                                                                           |
| Scalar | eventId              | "1140e03a-05e1-4d80-b4a0-89698434b028"                                                                                                                                    |
| String | renditionCode        | "hls:29.97"                                                                                                                                                               |
| String | rtmpDestinationUrl   |                                                                                                                                                                           |
| String | rtmpPassword         |                                                                                                                                                                           |
| String | rtmpUserName         |                                                                                                                                                                           |
| String | srtDestinationUrl    | srt://your.server.com:portnumber/your.stream.key                                                                                                                          |
| String | srtKeyLength         | Your encryption key length with algorithm, e.g. AES\_128, AES\_192, AES\_196, need to match your receivers setting                                                        |
| String | srtPassPhrase        | Encryption passphrase                                                                                                                                                     |
| String | subscriptionId       | "c6d2af76b714bcb6490a"                                                                                                                                                    |
| String | url                  | "https\://d3cgfqae8o6oiw\.cloudfront.net/RL/smil:EU-1140e03a-05e1-4d80-b4a0-89698434b028.smil/38563249092345113707536214628957630wsauy2xfxsfl8y9viamv8579l/playlist.m3u8" |
| Object | liveEventUnsubscribe |                                                                                                                                                                           |
| String | subscriptionId       | "1140e03a-05e1-4d80-b4a0-89698434b028"                                                                                                                                    |
| String | message              | "Subscription c6d2af76b714bcb6490a is removed"                                                                                                                            |





Reuters

# How to subscribe and push a live stream via SRT

Use the following steps to subscribe to an event and push an event via SRT.

To subscribe to a current live event, it’s required to have the “eventId" and the rendition “code” using the liveEvents method as shown below.

To get the “eventId" and the rendition “code”, use the following query:

query liveEvents {
liveEvents(eventStatuses: MidEvent) {
events {
id
headline
renditions {
code
}
}
}
}

To subscribe to an event, it’s required to have the “eventId" and the rendition “code”.

For example,

- eventId: "c090966c-27be-46f0-a0f7-b6f26593c00b"
- code: "srt:29.97:2048"

And it’s required to provide the SRT destination URL, passphrase and Key Length.

The “srtDestinationUrl” should be structured as: SRT destination URL + SRT stream key, such as: srt://your.server.com:portnumber/your.stream.key





Reuters

For example, the following mutation is to push a stream, where the:

- SRT destination server URL: srt://a.srt.example.com:2010/shgx-m46t-jjfj-fu64-ayt2
- PassPhrase: pp-3fbd-3fe3-fb4f-0d78
- srtKeyLength: AES_128

# Mutation Example

mutation MyMutation {
liveEventSubscribe(
eventId: "c090966c-27be-46f0-a0f7-b6f26593c00b"
renditionCode: "srt:29.97:2048"
srtDestinationUrl: "srt://a.srt.example.com:2010/shgx-m46t-jjfj-fu64-ayt2"
srtKeyLength: AES_128
srtPassPhrase: "pp-3fbd-3fe3-fb4f-0d78"
) {
subscriptionId
url
}
}

# How to Unsubscribe to a Live Event

To unsubscribe to an event, it’s required to use the “subscriptionId” provided on the mutation response of “liveEventSubscribe”. See the preview query.

# Unsubscribe Mutation Example

mutation MyMutation2 {
liveEventUnsubscribe(subscriptionId:
"3c9802025ee68bdb120f") {
message
}
}





Reuters
Support

For any product question, please contact: tania.vivero@thomsonreuters.com

For technical support contact us via: http://liaison.reuters.com/contact-us or send an email to ReutersMediaSupport@thomsonreuters.com