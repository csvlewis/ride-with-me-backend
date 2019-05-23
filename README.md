# Ride with Me Backend

This is the backend API for the Ride with Me App

### Endpoints: ####

#### 1. To get all cities: ####

To get a list of all the cities, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "query": "{ allCities{ name } }"}
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
            body: JSON.stringify({ "query": "{ allCities{ name }" })
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
            ...
```
</details>

#### 2. To get a ride by id: ####

To get a ride by id, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ query { searchRideById(id:1){ id } } }
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>

```
{
  "data": {
    "searchRideById": [
      {
        "id": "1"
      }
    ]
  }
}
```
</details>

#### 3. To get all available rides: ####

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

### 4. To get all available rides with start and end point: ####

To get a list of all currently available rides with a certain start and end city id, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "query": "{ searchByCities(startCityId: 1, endCityId:2) { id } }" }
```

Additional ride information can be added with additional query parameters like so:
```
{ "query": "{ searchByCities(startCityId: 1, endCityId:2) { id description mileage price totalSeats departureTime status driver { firstName lastName } endCity { name } startCity { name } } }" }
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>


```
{
    "data": {
        "searchByCities": [
            {
                "id": "11",
                "description": "Taking a trip",
                "mileage": 15,
                "price": 5,
                "totalSeats": 1,
                "departureTime": "2019-05-22T16:00:00+00:00",
                "status": "available",
                "driver": {
                    "firstName": "Leonardo",
                    "lastName": "DiCaprio"
                },
                "endCity": {
                    "name": "Golden, CO"
                },
                "startCity": {
                    "name": "Denver, CO"
                }
            },
            {
                "id": "1",
                "description": "Looking for two passengers",
                "mileage": 15,
                "price": 5,
                "totalSeats": 2,
                "departureTime": "2019-05-22T16:00:00+00:00",
                "status": "available",
                "driver": {
                    "firstName": "Johnny",
                    "lastName": "Depp"
                },
                "endCity": {
                    "name": "Golden, CO"
                },
                "startCity": {
                    "name": "Denver, CO"
                }
            }
        ]
    }
}
```
</details>
