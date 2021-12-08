# REST API epam weather application

This is api documentation for epam testing

## GOAL

Develop a REST service for receiving weather forecasts based on the Latin name of a city (for example, Moscow). The service should take the forecast for the selected city via API from any open source.

Add a parameter to the query to return the result in Celsius and Fahrenheit.

### Install
1. install docker docker compose if not installed
2. create folder (for example "APP")
3. download docker-compose.yml and secret(folder)
4. make pull vdobrokhotov/epam_weather:v1.2 (docker pull vdobrokhotov/epam_weather:v1.2)
### Run the app

1. move to created folder, where you stored docker-compose.yml and secret folder
2. run docker-compose -d

# Rest API

#### Authentication and getting token
### Request

`/api/v1/token/` 
#### with body x-www-form-urlencoded and keys username and password

### Response

`{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzOTAzOTUyOSwiaWF0IjoxNjM4OTUzMTI5LCJqdGkiOiJlNjI1NzMzODUwZjY0ZWEyYWRmOWQyZmVhZTIwNmQ1YSIsInVzZXJfaWQiOjF9.1Ihg5krTZPiN0Ifq-9_smOxT6F6rBecbCNvf1ckPlcA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4OTUzNDI5LCJpYXQiOjE2Mzg5NTMxMjksImp0aSI6Ijg1OWY1YjQzMTMzZDQzZjliZWQ5Mzk4MjVkMWZhNzY1IiwidXNlcl9pZCI6MX0.FmqxhitG9DyCmTPNGsHdU8kvIhMwhGJXfxaZin-E5cg"
}`

#### Refreshing token

### Request

`/api/v1/token/refresh` 

#### with Headers Content-Type: application/json and body refresh: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzOTAzOTUyOSwiaWF0IjoxNjM4OTUzMTI5LCJqdGkiOiJlNjI1NzMzODUwZjY0ZWEyYWRmOWQyZmVhZTIwNmQ1YSIsInVzZXJfaWQiOjF9.1Ihg5krTZPiN0Ifq-9_smOxT6F6rBecbCNvf1ckPlcA


#MAIN USAGE

##### on this requests put in Headers 
`Authorization: Bearer {access token}`

#### Get weather for city moscow
### Request
`/api/v1/weather/?city=moscow`
### Response
`{
"temperature": -1.6499999999999773,
"city": "moscow"
}`

#### Get weather for city saint-petersburg in fahrenheits
### Request
`/api/v1/weather/?city=saint%20petersburg&f=true`
### Response
`{
"temperature": 3.7280000000000086,
"city": "saint petersburg"
}`




