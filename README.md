# Ride with Me Backend

This is the backend API for the Ride with Me App

### Endpoints: ####

#### 1. Get all cities: ####

To get a list of all the cities, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "query": "{ allCities{ name } }"}
```

or the same request in GraphQL query format:
```
query {
    allCities {
        name
    }
}
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

#### 2. Get a ride by id: ####

To get a ride by id, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "query": "{ searchRideById(id:1){ id } }" }
```

or the same request in GraphQL query format:
```
query {
    searchRideById(id:1) {
        id
    }
}
```

More ride information can be requested with additional query parameters like so:

```
{ "query": "{ searchRideById(id:1){ id description mileage price totalSeats departureTime status driver { firstName lastName } endCity { name } startCity { name } } }" }
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

#### 3. Get all available rides: ####

To get a list of all currently available rides, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{"query": "{ availableRides{id}}"}
```

or the same request in GraphQL query format:
```
query {
    availableRides {
        id
    }
}
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>

```
{
    "data": {
        "searchRidesByCities": [
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

### 4. Get all available rides with start and end point and optional date argument: ####

Users can search for Rides by making a request to our graphql endpoint (https://ride-with-me-backend/graphql).

The query is calles "searchRidesByCities" and it accepts 3 arguments:
1. startCityId: type Integer and is required
2. endCityId: type integer and is required
3. departureTime: Date type and is optional. The format is "2019-05-22".

A user can send a POST request to https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "query": "{ searchRidesByCities(startCityId: 1, endCityId:2) { id } }" }
```

or the same request in GraphQL query format:
```
query {
    searchRidesByCities(startCityId:1 endCityId:2) {
        id
    }
}
```

More ride information can be requested with additional query parameters like so:
```
{ "query": "{ searchRidesByCities(startCityId: 1, endCityId:2) { id description mileage price totalSeats departureTime status driver { firstName lastName } endCity { name } startCity { name } } }" }
```
**The header Content-Type should be application/json**

#### Example query with date parameter in GraphQL query format: ####

```
query {
  searchRidesByCities(startCityId: 1, endCityId: 2, departureTime: "2019-05-22") {
    description
    departureTime
  }
}

```

**It can also be sent as the body of a POST request, for which the body would be:**

```
{"query": "{searchRidesByCities(startCityId:1, endCityId: 2, departureTime: \"2019-05-22\"){description }}"}

```

<details>
  <summary>See example</summary>

#### Example of payload ####
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
                "departureTime": "2019-05-22",
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
                "departureTime": "2019-05-23",
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





### Getting the associations of a ride ###

You can also get that ride's associated objects, that is:
- its driver
- startCity
- endCity
- passengers

To get the passengers of a ride, you need to first query the ridePassengerSet for that particular ride and then specify the passenger attribute and the attributes for that passenger that you want back

Post request body of getting associated passengers:

```
{"query": "{searchRidesByCities(startCityId:1, endCityId: 2){description driver {firstName} ridepassengerSet {passenger {firstName}}}}"}
```

### Example of a query on GraphiQL:  ###

<img width="1416" alt="Screen Shot 2019-05-23 at 8 33 41 PM" src="https://user-images.githubusercontent.com/13354855/58298804-19098280-7d9a-11e9-9a5c-b399b86915e4.png">







</details>

### 5. Create a new ride: ####

To get a create a new ride, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "mutation": "{ createRide(driverId:1 startCityId:1 endCityId:2 description:'Going for a ride' mileage:100 price:50.00 totalSeats:4 departureTime:'2019-05-23T12:52:24+00:00'){ id driverId startCityId endCityId description mileage price totalSeats departureTime createdAt updatedAt } }" }
```

or the same request in GraphQL query format:
```
mutation {
   createRide(driverId:1 startCityId:1 endCityId:2 description:"Going for a ride" mileage:100 price:50.00 totalSeats:4 departureTime:"2019-05-23") {
        id
        driverId
        startCityId
        endCityId
        description
        mileage
        price
        totalSeats
        departureTime
        createdAt
        updatedAt
    }
}
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>


```
{
  "data": {
    "createRide": {
      "id": 21,
      "driverId": 1,
      "startCityId": 1,
      "endCityId": 2,
      "description": "Going for a ride",
      "mileage": 100,
      "price": 50,
      "totalSeats": 4,
      "departureTime": "2019-05-23T12:52:24+00:00",
      "createdAt": "2019-05-23T13:31:07.369635+00:00",
      "updatedAt": "2019-05-23T13:31:07.369710+00:00"
    }
  }
}
```
</details>

### 6. Get a driver's pending requests: ####

To retrieve pending requests for a driver, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "query": "{ pendingRequests(driverId:1){ id message status } }" }
```

or the same request in GraphQL query format:
```
query {
  pendingRequests(driverId:1){
    id
    message
    status
  }
}
```

you can also query additional relationship information with more query parameters like so:

```
query {
  pendingRequests(driverId:1){
		ride {
      id
		}
    driver {
      id
      firstName
      lastName
		}
    passenger {
      id
      firstName
      lastName
    }
    id
    message
    status
  }
}
```
The header Content-Type should be application/json

<details>
  <summary>See example</summary>


```
{
  "data": {
    "pendingRequests": [
      {
        "ride": {
          "id": "1"
        },
        "driver": {
          "id": "1",
          "firstName": "Johnny",
          "lastName": "Depp"
        },
        "passenger": {
          "id": "3",
          "firstName": "Jim",
          "lastName": "Carey"
        },
        "id": "2",
        "message": "Room for one more?",
        "status": "pending"
      }
    ]
  }
}
```
</details>

### 7. Change the status of a ride: ####

To change the status of a ride, a user can send a POST request to
    https://ride-with-me-backend.herokuapp.com/graphql with the following query in the body:
```
{ "mutation": "{ changeRideStatus(id:1 status:"new_status"){ id status } }" }
```

or the same request in GraphQL query format:
```
mutation {
  changeRideStatus(id:1 status:"new_status"){
    id
    status
  }
}
```

The header Content-Type should be application/json

<details>
  <summary>See example</summary>


```
{
  "data": {
    "changeRideStatus": {
      "id": 1,
      "status": "new_status"
    }
  }
}
```
</details>
