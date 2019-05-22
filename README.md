# Ride with Me Backend

This is the backend API for the Ride with Me App

### Endpoints: ####

#### 1. To get all cities: ####

To get a list of all the cities, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{query: "{ allCities{name}}"}
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>


```javascript
fetch('https://ride-with-me-backend.herokuapp.com/graphql', {
            method: "POST",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(query: '{
                                        allCities{
                                             name
                                        }'
                                   })
          })
        .then(function(response) {
            if (response.status >= 400) {
                throw new Error("Bad response from server");
            }
            return response.json();
        })

```

Example of the payload you should get:

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

#### 2. To get all available rides: ####

To get a list of all currently available rides, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{"query": "{ availableRides{id}}"}
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>


```
{
    "data": {
        "availableRides": [
            {
                "id": "1"
            },
            {
                "id": "3"
            },
            {
                "id": "4"
            },
            {
                "id": "5"
            },
            {
                "id": "6"
            },
            {
                "id": "7"
            }
        ]
    }
}
```
</details>
