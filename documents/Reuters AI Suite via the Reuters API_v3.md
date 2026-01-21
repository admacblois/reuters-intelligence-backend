Reuters
# Reuters AI Suite via the Reuters API

# Contents

- Reuters AI Suite - Video Enrichment via the Reuters API ...................................................2
- videoEnrichment Mutation .........................................................................................3
- How to upload a video/audio file (requesting transcription and translation only) – audio insights. ................................................................................................................4
- How to upload a video/audio file (requesting scene detection and facial recognition only) – video insights .............................................................................................. 5
- How to upload a video/audio file (requesting all audio insights and video insights) ......6
- videoEnrichment endpoint .........................................................................................8
- jobStatus................................................................................................................8
- How to check the upload status. ..........................................................................9
- jobResult ............................................................................................................. 10
- How to get the transcription and translation. ......................................................12
- How to get the scene detection.......................................................................... 14
- How to get the transcription, translation, scene detection and people recognition.15
- serviceUsage ........................................................................................................ 16
- How to get the serviceUsage of the videoEnrichment endpoint. ........................... 16
- Support ......................................................................................................................17






Reuters

# Reuters AI Suite - Video Enrichment via the Reuters API

At Reuters, we are committed to enhancing our customer experience by developing video enrichment features that offers a comprehensive and diverse range of AI capabilities. This video enrichment via the Reuters API is designed to elevate customer video experience through advanced features such as:

- Transcription
- Translation
- Scene detection
- Facial recognition

The process consists of uploading each video/audio that would like to get our enrichment features via the Reuters API.

To perform this process, uploading using a pre-signed URL and via the videoEnrichment mutation is required.

# Prerequisites

- Pre-signed URLs are only allowed.
- Video files must be in mp4 format (lowercase).
- Audio files must be in wav or mp3 format (lowercase).





Reuters

# videoEnrichment Mutation

The videoEnrichment mutation and the createJob parameter should be used as mentioned above to upload the video to the Reuters API using a pre-signed URL.

| PARAMETERS                                                 | DEFINITION                                                                                                                                       | |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |---|
| videoEnrichment                                            | createJob                                                                                                                                        | |
| sourceUrl                                                  |                                                                                                                                                  | |
| jobName                                                    |                                                                                                                                                  | |
| audioInsights                                              | transcription                                                                                                                                    | |
| True | false                                               |                                                                                                                                                  |
| True: Provides transcription of the uploaded video         |                                                                                                                                                  | |
| False: Do not provide a transcription of the uploaded file |                                                                                                                                                  | |
|                                                            | If this value = false, then translation and translationLangs will not be provided.                                                               | |
|                                                            | translation                                                                                                                                      | |
|                                                            | True | false                                                                                                                                     |
|                                                            | True: Provides translation of the uploaded file.                                                                                                 | |
|                                                            | False: Do not provide a translation of the uploaded file.                                                                                        | |
| trasnlationLangs                                           | Provide the translation of the selected languages, or several languages can be selected as an array (must use \[] to select multiple languages). | |
|                                                            | English (en\_GB)                                                                                                                                 | |
|                                                            | Spanish (es\_ES)                                                                                                                                 | |
|                                                            | French (fr\_CH)                                                                                                                                  | |
|                                                            | Japanese (ja\_JP)                                                                                                                                | |
|                                                            | German (de\_AT)                                                                                                                                  | |
|                                                            | Chinese (Simplified) (zh\_CN)                                                                                                                    | |
|                                                            | Portuguese (pt\_BR)                                                                                                                              | |
|                                                            | For multiple languages, should be as \[en\_GB, es\_ES, fr\_CH]                                                                                   | |
| videoInsights                                              | faces                                                                                                                                            | |
| True | false                                               |                                                                                                                                                  |
|                                                            | True: Provides face recognition                                                                                                                  | |
|                                                            | False: Do not face recognition                                                                                                                   | |
| shots                                                      | True | false                                                                                                                                     |
|                                                            | True: Provides scene detection of the uploaded file.                                                                                             | |





Reuters

False: Do not provide scene detection of the uploaded file.

jobId After the video has been uploaded, a jobId will be provided.

# How to upload a video/audio file (requesting transcription and translation only) – audio insights.

The following mutation allows you to upload a video/audio file using a pre-signed URL using the createJob parameter, and request audio insights (transcription and translation only).

To get the translations, the transcription parameter should be set to true.

The translation is set to all languages: English (en_GB), Spanish (es_ES), French (fr_CH), Japanese (ja_JP), German (de_AT), Chinese Simplified (zh_CN), and Portuguese (pt_BR).

mutation MyMutation {
videoEnrichment {
createJob(
jobName: "FileUpload"
audioInsights: {transcription: true, translation: true, translationLangs: [en_GB, es_ES,
fr_CH,ja_JP,de_AT,zh_CN,pt_BR]}
videoInsights: {faces: false, shots: false}
sourceUrl: "https://automated-tests-s3.s3.eu-west-1.amazonaws.com/2025_file.MP4"
) {
jobId
}
}
}





Reuters

# Mutation Response

The mutation response should return a jobID as shown below:

{
"data": {
"videoEnrichment": {
"createJob": {
"jobId": "EU1ME6X00YZ20250811prod"
}
}
}
}

# How to Upload a Video/Audio File (Requesting Scene Detection and Facial Recognition Only) – Video Insights

The following mutation allows you to upload a video/audio file using a pre-signed URL using the createJob parameter, and request video insights (scene detection and facial recognition).

mutation MyMutation {
videoEnrichment {
createJob(
jobName: "FileUpload"
audioInsights: {transcription: false, translation: false, translationLangs: [en_GB, es_ES,
fr_CH,ja_JP,de_AT,zh_CN,pt_BR]}
videoInsights: {faces: true, shots: true}
sourceUrl: "https://automated-tests-s3.s3.eu-west-1.amazonaws.com/2025_file.MP4"
) {
jobId
}
}
}





Reuters

# Mutation Response

The mutation response should return a jobID as shown below:

{
"data": {
"videoEnrichment": {
"createJob": {
"jobId": "EU1M8LZGERK20250323"
}
}
}
}

# How to Upload a Video/Audio File

(requesting all audio insights and video insights)

The following mutation allows you to upload a video/audio file using a pre-signed URL using the createJob parameter, and request audio insights (transcription and translation) and video insights (scene detection and facial recognition).

mutation MyMutation {
videoEnrichment {
createJob(
jobName: "FileUpload"
audioInsights: {transcription: true, translation: true, translationLangs: [en_GB, es_ES,
fr_CH,ja_JP,de_AT,zh_CN,pt_BR]}
videoInsights: {faces: true, shots: true}
sourceUrl: "https://automated-tests-s3.s3.eu-west-1.amazonaws.com/2025_file.MP4"
) {
jobId
}
}
}





Reuters

The mutation response should return a jobID as shown below:

{
"data": {
"videoEnrichment": {
"createJob": {
"jobId": "EU1ME6X00YZ20250811prod"
}
}
}
}

After executing the videoEnrichment mutation, it’s possible to monitor the upload process using the jobStatus parameter within the videoEnrichment endpoint.





Reuters

# videoEnrichment endpoint

The video enrichment endpoint allows you to retrieve all the video enrichment features, such as transcriptions, translation in seven languages (German, English, Spanish, French, Japanese, Portuguese, and Chinese), Scene detection, and facial recognition (not in production yet).

In addition, the jobStatus and serviceUsage endpoints will allow you to monitor the video file upload and the service Usage of the video enrichment, respectively.

# jobStatus

After executing the videoEnrichment mutation, it’s possible to monitor the upload process using the jobStatus parameter within the videoEnrichment endpoint.

| **PARAMETERS**                      |                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **videoEnrichment jobStatus.jobid** | Enter the jobId got in the videoEnrichment mutation.                                                                                                                                                                                                                                                                                                                                                      |
| **audioInsights**                   | True=audio features (translation and transcription) have been provided false=audio features (translation and transcription) have been provided or requested                                                                                                                                                                                                                                               |
| **executionsStatus**                | RUNNING: the job upload is in process. COMPLETED: the job has been uploaded. FAILED: the job has not been uploaded, try again. UNKNOW: Please try again. SUCCEEDED: the job has been processed. TIME\_OUT: the job has not been processed due to time out request. ABORTED: the job has been interrupted. PENDING\_REDRIVE: the job is not processed yet, in queue. IN\_QUEUE: the job will be processed. |
| **jobId**                           | Provides the jobId provided in the jobStatus.jobId                                                                                                                                                                                                                                                                                                                                                        |
| **jobName**                         | Name of the video uploaded or the job name.                                                                                                                                                                                                                                                                                                                                                               |





Reuters

requestValidity: "Prechecker Passed - Valid Request to Trigger Avista"

stage:

- Complete: the createJob has been completed
- Incomplete: the createJob has not been completed

videoInsights:

- True=videoInsights have been provided
- False=videoInsights have not been provided or requested

After the jobStatus.stage is Complete, then make use of the jobResult endpoints to get all the videoEnrichment features.

# How to check the upload status.

The following query provides the createJob status and let you know if the video has been uploaded.

query MyQuery {
videoEnrichment {
jobStatus(jobId: "EU1ME6W8TIH20250811prod") {
aiShotlists
audioInsights
executionStatus
jobId
mediaFile
requestValidity
stage
videoInsights
}
}
}

Response:



Reuters

# Job Result

The following table includes the jobResults parameters related to retrieve the video enrichment features, such as transcription and translation.

| aiShotlists     | false                                               |
| --------------- | --------------------------------------------------- |
| audioInsights   | true                                                |
| executionStatus | SUCCEEDED                                           |
| jobId           | EU1ME6W8TIH20250811prod                             |
| jobName         | TaniaAugust11                                       |
| requestValidity | Prechecker Passed - Valid Request to Trigger Avista |
| stage           | complete                                            |
| videoInsights   | true                                                |





Reuters

# PARAMETERS DEFINITION

| videoEnrichment      | Return the videoEnrichment features                      |
| -------------------- | -------------------------------------------------------- |
| jobResult.jobId      | Enter the jobId received in the videoEnrichment mutation |
| jobId                | Provides the jobId entered in the query                  |
| audioAnalysis        |                                                          |
| transcriptions       |                                                          |
| startTime            | Provides the startTime of the section of the transcript. |
| endTime              | Provides the endTime of the section of the transcript.   |
| transcript           | Provides the video transcriptions.                       |
| native language      | Provides the native language of the video                |
| languageLocale       | Provides the language                                    |
| text                 | Provides the text of the transcript                      |
| translations         | Provides the translations                                |
| languageLocale       | Provides the language name.                              |
| English              |                                                          |
| Spanish              |                                                          |
| French               |                                                          |
| Japanese             |                                                          |
| German               |                                                          |
| Chinese (Simplified) |                                                          |
| Portuguese           |                                                          |
| text                 | Provides the translation of specific language            |
| speaker              |                                                          |
| personIndex          |                                                          |
| people               |                                                          |
| name                 |                                                          |
| videoAnalysis        |                                                          |





Reuters

# Scene detection analysis

# appearances

| startTime   | Start time of the appearances |
| ----------- | ----------------------------- |
| endTime     | End time of the appearances   |
| peopleIndex | Name of the person recognized |

# speakers

| peopleIndices | Display people index          |
| ------------- | ----------------------------- |
| timeline      |                               |
| startTime     | People appearance start time  |
| endTime       | People appearance end time    |
| peopleIndex   | Name of the person recognized |

# How to get the transcription and translation.

The following query provides the translation and transcription of the uploaded file.





Reuters

query MyQuery {
videoEnrichment {
jobResult(jobId: "Enter_your_job_ID") {
jobId
audioAnalysis {
transcriptions {
startTime
endTime
transcript {
native {
language
languageLocale
text
}
translations {
languageLocale
text
}
}
}
}
}
}
}





Reuters

# How to get the scene detection.

The following query provides the scene detection of the uploaded file

query MyQuery {
videoEnrichment {
jobResult(jobId: "Enter_your_job_ID") {
jobId
people {
name
}
videoAnalysis {
scenes {
startTime
endTime
appearances {
peopleIndices
timeline {
startTime
endTime
peopleIndex
}
}
speakers {
peopleIndices
timeline {
startTime
endTime
peopleIndex
}
}
}
}
}
}





Reuters

# How to get the transcription, translation, scene detection and people recognition.

The following query provides the translation, transcription, scene detection and people recognition of the uploaded file

query MyQuery {
videoEnrichment {
jobResult(jobId: "Enter_your_job_ID") {
jobId
audioAnalysis {
transcriptions {
startTime
endTime
transcript {
native {
language
languageLocale
text
}
translations {
languageLocale
text
}
}
speaker {
personIndex
}
}
}
people {
name
}
videoAnalysis {
scenes {
startTime
endTime
appearances {
peopleIndices
timeline {
startTime
endTime
peopleIndex
}
}
speakers {
peopleIndices
timeline {
startTime
endTime
peopleIndex
}
}
}
}
}
}
}





Reuters

# serviceUsage

The serviceUsage is used to get the usage of the videoEnrichment endpoint during a determined date range.

| PARAMETERS      | DEFINITION                                                                  |
| --------------- | --------------------------------------------------------------------------- |
| videoEnrichment |                                                                             |
| serviceUsage    |                                                                             |
| dateRange       | Date range can’t exceed 30 days. Date format is year.month.day (2025.12.05) |
| records         |                                                                             |
| jobId           | jobId of the jobs executed                                                  |
| length          | Video length in seconds                                                     |
| jobName         | Name of the video uploaded                                                  |
| startTimestamp  | Time when the video was uploaded                                            |
| totalSeconds    | Total of seconds of job executed.                                           |

# How to get the serviceUsage of the videoEnrichment endpoint.

The following query shows how to get the serviceUsage of the videoEnrichment endpoint.

query serviceUsage {
videoEnrichment {
serviceUsage(dateRange: "2025.03.18-2025.03.25") {
records {
jobId
length
startTimestamp
jobName
}
totalSeconds
}
}
}





Reuters

Response

{
"data": {
"videoEnrichment": {
"serviceUsage": {
"records": [
{
"jobId": "EU1M8EKC3FE20250318",
"length": 281.98,
"startTimestamp": "2025-03-18T14:03:43.283755",
"mediaFile": "JobVideo2"
},
"totalSeconds": 1765.44
}
}
}
}

# Support

For any product question, please contact: robert.schack@thomsonreuters.com or tania.vivero@thomsonreuters.com

For technical support contact us via: http://liaison.reuters.com/contact-us or send an email to ReutersMediaSupport@thomsonreuters.com

