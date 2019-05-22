# Ride with Me Backend

This is the backend API for the Ride with Me App

### Endpoints: ####

#### 1. To get all cities: ####

To get a list of all the cities, a user can send a POST request to 
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{"query": "{ allCities{name}}"}
```
The Content-Type should be application/json

<details>
  <summary>See example</summary>
  
  
```
{
    "data": {
        "allCities": [
            {
                "name": "Prairie Ridge, WA"
            },
            {
                "name": "Edison, WA"
            },
            {
                "name": "Packwood, WA"
            },
            {
                "name": "Wautauga Beach, WA"
            },
            {
                "name": "Harper, WA"
            },
            {
                "name": "Telma, WA"
            }
            ]
```
</details>


