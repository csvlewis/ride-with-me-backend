# Ride with Me Backend

This is the backend API for the Ride with Me App

### Endpoints: ####

All endpoints can be accessed by sending a POST request to https://ride-with-me-backend.herokuapp.com/graphql. Each request should have a parameter of 'query', which should have a value set to the desired GraphQL query.

#### 1. Get all cities: ####

To get a list of all cities, a user can make the GraphQL query:
```
query {
  allCities {
    name
  }
}
```
or the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{allCities{name}}

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
            ...
```
</details>

#### 2. Get a ride by id: ####

To get a ride by id, a user can make the GraphQL query:
```
query {
  searchRideById(id:1) {
    id
  }
}
```
or the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{searchRideById(id:1){id}}

More ride information can be requested with additional query parameters like so:

```
query {
  searchRideById(id:1) {
    id
    description
    mileage
    price
    totalSeats
    departureTime
    status
    driver {
      id
      firstName
      lastName
    }
    ridepassengerSet {
      passenger {
        id
        firstName
        lastName
      }
    }
    endCity {
      id
      name
    }
    startCity {
      id
      name
    }
  }
}
```
    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{searchRideById(id:1){id,description,mileage,price,totalSeats,departureTime,status,driver{id,firstName,lastName}ridepassengerSet{passenger{id,firstName,lastName}}endCity{id,name}startCity{id,name}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "searchRideById": [
      {
        "id": "1",
        "description": "Looking for two passengers",
        "mileage": 15,
        "price": 5,
        "totalSeats": 2,
        "departureTime": "2019-05-22",
        "status": "cancelled",
        "driver": {
            "id": "1",
            "firstName": "Johnny",
            "lastName": "Depp"
        },
        "ridepassengerSet": [
            {
                "passenger": {
                    "id": "4",
                    "firstName": "Emma",
                    "lastName": "Watson"
                }
            }
        ],
        "endCity": {
            "id": "2",
            "name": "Golden, CO"
        },
        "startCity": {
            "id": "1",
            "name": "Denver, CO"
        }
      }
    ]
  }
}
```
</details>

#### 3. Get all available rides: ####

To get all available rides, a user can make the GraphQL query:
```
query {
  availableRides {
    id
  }
}
```
or the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{availableRides{id}}

More ride information can be requested with additional query parameters like so:
```
query {
  availableRides {
    id
    description
    mileage
    price
    totalSeats
    departureTime
    status
    driver {
      id
      firstName
      lastName
    }
    ridepassengerSet {
      passenger {
        id
        firstName
        lastName
      }
    }
    endCity {
      id
      name
    }
    startCity {
      id
      name
    }
  }
}
```

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{availableRides{id,description,mileage,price,totalSeats,departureTime,status,driver{id,firstName,lastName}ridepassengerSet{passenger{id,firstName,lastName}}endCity{id,name}startCity{id,name}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "availableRides": [
      {
        "id": "7",
        "description": "Looking to take one passenger",
        "mileage": 930,
        "price": 175,
        "totalSeats": 1,
        "departureTime": "2019-05-27",
        "status": "available",
        "driver": {
            "id": "7",
            "firstName": "Natalie",
            "lastName": "Portman"
        },
        "ridepassengerSet": [],
        "endCity": {
            "id": "2",
            "name": "Golden, CO"
        },
        "startCity": {
            "id": "4",
            "name": "Austin, TX"
        }
      },
      {
        "id": "11",
        "description": "Taking a trip",
        "mileage": 15,
        "price": 5,
        "totalSeats": 1,
        "departureTime": "2019-05-22",
        "status": "available",
        "driver": {
            "id": "5",
            "firstName": "Leonardo",
            "lastName": "DiCaprio"
        },
        "ridepassengerSet": [],
        "endCity": {
            "id": "2",
            "name": "Golden, CO"
        },
        "startCity": {
            "id": "1",
            "name": "Denver, CO"
        }
      },
      ...
```
</details>

#### 4. Get all available rides with start and end point and optional date: ####

To search rides with a certain start and end point, a user can make the GraphQL query:
```
query {
  searchRidesByCities(startCityId:1 endCityId:2 departureTime:"2019-05-22") {
    id
  }
}
```

The startCityID and endCityID fields are required, while the departureTime field is optional.

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{searchRidesByCities(startCityId:1,endCityId:2,departureTime:"2019-05-22"){id}}

More ride information can be requested with additional query parameters like so:
```
query {
  searchRidesByCities(startCityId:1 endCityId:2 departureTime:"2019-05-22") {
    id
    description
    mileage
    price
    totalSeats
    departureTime
    status
    driver {
      id
      firstName
      lastName
    }
    ridepassengerSet {
      passenger {
        id
        firstName
        lastName
      }
    }
    endCity {
      id
      name
    }
    startCity {
      id
      name
    }
  }
}
```

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{searchRidesByCities(startCityId:1,endCityId:2,departureTime:"2019-05-22"){id,description,mileage,price,totalSeats,departureTime,status,driver{id,firstName,lastName}ridepassengerSet{passenger{id,firstName,lastName}}endCity{id,name}startCity{id,name}}}

<details>
  <summary>See example</summary>
```
  {
    "data": {
      "searchRidesByCities": [
        {
          "id": "11",
          "description": "Taking a trip",
          "mileage": 15,
          "price": 5,
          "totalSeats": 1,
          "departureTime": "2019-05-22",
          "status": "available",
          "driver": {
              "id": "5",
              "firstName": "Leonardo",
              "lastName": "DiCaprio"
          },
          "ridepassengerSet": [],
          "endCity": {
              "id": "2",
              "name": "Golden, CO"
          },
          "startCity": {
              "id": "1",
              "name": "Denver, CO"
          }
        },
        {
          "id": "21",
          "description": "Going for a ride",
          "mileage": 100,
          "price": 50,
          "totalSeats": 4,
          "departureTime": "2019-05-23",
          "status": "available",
          "driver": {
              "id": "1",
              "firstName": "Johnny",
              "lastName": "Depp"
          },
          "ridepassengerSet": [],
          "endCity": {
              "id": "2",
              "name": "Golden, CO"
          },
          "startCity": {
              "id": "1",
              "name": "Denver, CO"
          }
        },
        ...
```
</details>

#### 5. Create a new ride: ####

To create a new ride, a user can make the GraphQL query:
```
mutation {
	createRide(driverId:1 startCityId:1 endCityId:2 description:"Going for a ride" mileage:100 price:50.00 totalSeats:4 departureTime:"2019-05-23") {
		ride {
			id
    }
  }
}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{createRide(driverId:1,startCityId:1,endCityId:2,description:"Going for a ride",mileage:100,price:50.00,totalSeats:4,departureTime:"2019-05-23"){ride{id}}}

More ride information can be requested with additional query parameters like so:
```
query {
  searchRidesByCities(startCityId:1 endCityId:2 departureTime:"2019-05-22") {
    id
    description
    mileage
    price
    totalSeats
    departureTime
    status
    driver {
      id
      firstName
      lastName
    }
    ridepassengerSet {
      passenger {
        id
        firstName
        lastName
      }
    }
    endCity {
      id
      name
    }
    startCity {
      id
      name
    }
  }
}
```

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{createRide(driverId:1,startCityId:1,endCityId:2,description:"Going for a ride",mileage:100,price:50.00,totalSeats:4,departureTime:"2019-05-23"){ride{id,description,mileage,price,totalSeats,departureTime,status,driver{id,firstName,lastName}ridepassengerSet{passenger{id,firstName,lastName}}endCity{id,name}startCity{id,name}}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "searchRidesByCities": [
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
        "id": "21",
        "description": "Going for a ride",
        "mileage": 100,
        "price": 50,
        "totalSeats": 4,
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
      },
      ...
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
    ride {
      id
      status
    }
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
