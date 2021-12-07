#REST API epam weather application

This is api documentation

### Install

### Run the app

### Run tests

##Rest API

#### Get weather for city moscow
###Request
`/api/v1/weather/?city=moscow`
###Response
`{
"temperature": -1.6499999999999773,
"city": "moscow"
}`

#### Get weather for city saint-petersburg in fahrenheits
###Request
`/api/v1/weather/?city=saint%20petersburg&f=true`
###Response
`{
"temperature": 3.7280000000000086,
"city": "saint petersburg"
}`




