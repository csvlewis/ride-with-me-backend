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

#### 2. Get searchable cities: ####

To get a list of all cities associated with a ride, a user can make the GraphQL query:

```
query {
  searchableCities {
    endCities {
      id
      name
    }
    startCities {
      id
      name
    }
  }
}
```

<details>
  <summary>See example</summary>

```
{
  "data": {
    "searchableCities": {
      "endCities": [
        {
          "id": "4",
          "name": "Austin, TX"
        },
        {
          "id": "1",
          "name": "Denver, CO"
        },
        {
          "id": "29",
          "name": "Detroit, MI"
        },
        {
          "id": "2",
          "name": "Golden, CO"
        },
        {
          "id": "5",
          "name": "Las Vegas, NV"
        },
        {
          "id": "3",
          "name": "Los Angeles, CA"
        }
      ],
      "startCities": [
        {
          "id": "4",
          "name": "Austin, TX"
        },
        {
          "id": "1",
          "name": "Denver, CO"
        },
        {
          "id": "2",
          "name": "Golden, CO"
        },
        {
          "id": "5",
          "name": "Las Vegas, NV"
        },
        {
          "id": "3",
          "name": "Los Angeles, CA"
        }
      ]
    }
  }
}
```
</details>

#### 3. Get a user by id: ####

To information about a user, you can can make the GraphQL query:
```
query {
  searchUserById(id:1){
    id
    firstName
    lastName
    email
    phoneNumber
    apiKey
    createdAt
    updatedAt
  }
}
```

<details>
  <summary>See example</summary>

```
{
  "data": {
    "searchUserById": {
      "id": "1",
      "firstName": "Johnny",
      "lastName": "Depp",
      "email": "johnnydepp@gmail.com",
      "phoneNumber": 1234567890,
      "apiKey": "key_1",
      "createdAt": "2019-05-20T16:23:00.067741+00:00",
      "updatedAt": "2019-05-20T16:23:00.067741+00:00"
    }
  }
}
```
</details>
#### 4. Get a ride by id: ####

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

#### 5. Get all available rides: ####

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

#### 6. Get all available rides with start and end point and optional date: ####

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

#### 7. Create a new ride: ####

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
  createRide(driverId:1 startCityId:1 endCityId:2 description:"Going for a ride" mileage:100 price:50.00 totalSeats:4 departureTime:"2019-05-23") {
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
    "createRide": {
      "ride": {
        "id": "69",
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
      }
    }
  }
}
```
</details>

#### 8. Change a ride's status: ####

To change the status of a ride, a user can make the GraphQL query:
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

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{changeRideStatus(id:1 status:"new_status"){ride {id,status}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "changeRideStatus": {
      "ride": {
        "id": "1",
        "status": "new_status"
      }
    }
  }
}
```
</details>

#### 9. Get pending requests: ####

To get pending requests for a user, a user can make the GraphQL query:
```
query {
  pendingRequests(driverId:1){
    id
  }
}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{pendingRequests(driverId:1){id}}

More ride information can be requested with additional query parameters like so:
```
query {
  pendingRequests(driverId:1){
    id
    ride {
      id
    }
    passenger {
      firstName
      lastName
    }
    message
    status
    createdAt
  }
}
```

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{pendingRequests(driverId:1){id,ride{id}passenger{firstName,lastName}message,status,createdAt}}

<details>
  <summary>See example</summary>
```
{
  "data": {
    "pendingRequests": [
      {
        "id": "2",
        "ride": {
          "id": "1"
        },
        "passenger": {
          "firstName": "Jim",
          "lastName": "Carey"
        },
        "message": "Room for one more?",
        "status": "pending",
        "createdAt": "2019-05-20T16:23:00.067741+00:00"
      }
    ]
  }
}
```
</details>

### 10. Create a Request ###

To send a request to a driver, a user can make the GraphQL query:
```
mutation($driverId: Int!, $message: String!, $passengerId:Int!, $rideId: Int!){
  createRequest(driverId: $driverId, message: $message, passengerId: $passengerId, rideId: $rideId){
  	request {
      id
    }
  }
},
variables: {"driverId": 1, "message": "Message test sending request", "passengerId": 2, "rideId": 3}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation($driverId:Int!,$message:String!,$passengerId:Int!,$rideId:Int!){createRequest(driverId:$driverId,message:$message,passengerId:$passengerId,rideId:$rideId){request{id,message}}}&variables={"driverId":1,"message":"Message test sending request","passengerId":2,"rideId":3}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "createRequest": {
      "request": {
        "id": "14",
        "message": "Message test sending request"
      }
    }
  }
}
```
</details>

#### 11. Change a request's status: ####

To change the status of a requests, a user can make the GraphQL query:
```
mutation {
  changeRequestStatus(id:1 status:"new_status"){
    request {
      id
      status
    }
  }
}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{changeRequestStatus(id:1status:"new_status"){request {id,status}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "changeRideStatus": {
      "ride": {
        "id": "1",
        "status": "new_status"
      }
    }
  }
}
```
</details>



#### 12. Delete a RidePassenger (When a passenger cancels a ride): ####

A user can cancel an upcoming Ride. The ride's status should now be "available", if it was previously full. The RidePassenger associated with that user and that ride should be deleted.

To cancel an upcoming Ride, a user can send the following GraphQL mutation:


```graphql
mutation($passengerId: Int! $rideId: Int!){
  deleteRidePassenger(passengerId:$passengerId, rideId:$rideId){
    ok
    message
  }
}
```
**ok** and **message** are custom fields that get returned to let the user know if the mutation worked. When ok=True, it worked. The message explains what got deleted.

Example of variables sent with that mutation:

```
{"passengerId": 8, "rideId":2}

```


<details>
  <summary>See example</summary>

If the mutation is successful (there was a ride with the given rideId that had a passenger with the given passengerId), you should see this a response similar to this:

```graphql
{
  "data": {
    "deleteRidePassenger": {
      "ok": true,
      "message": "The passenger with id 8 has been deleted from the ride with id 2. Now the ride has 3 available seat(s)."
    }
  }
}

```

If the mutation is unsuccessful, you should see a response similar to this:

```graphql
{
  "data": {
    "deleteRidePassenger": {
      "ok": false,
      "message": "There is no passenger with id 88 in ride with id 2"
    }
  }
}

```

</details>

#### 13. Add a RidePassenger (When a driver accepts a ride request): ####

A driver can add a passenger to a ride by accepting a ride request. When they do so, a relationship is created between the ride and the passenger, and the related request's status is changed to 'accepted'. If the ride is already full when the driver tries to accept the request, the passenger will not be added and the request's status will remain 'pending'.

To add a passenger to a ride, a user can send the following GraphQL mutation:


```graphql
mutation($passengerId: Int! $rideId: Int!) {
  createRidePassenger(passengerId:$passengerId, rideId:$rideId){
    ok
    message
  }
}
```
**ok** and **message** are custom fields that get returned to let the user know if the mutation worked. When ok=True, it worked. The message explains what got created.

Example of variables sent with that mutation:

```
{"passengerId": 8, "rideId":2}

```


<details>
  <summary>See example</summary>

If the mutation is successful (there was a ride with the given rideId that had a passenger with the given passengerId), you should see this a response similar to this:

```graphql
{
  "data": {
    "createRidePassenger": {
      "ok": true,
      "message": "The passenger with id 2 has been added to the ride with id 15. Now the ride has 3 available seat(s)."
    }
  }
}
```

If the mutation is unsuccessful, you should see a response similar to this:

```graphql
{
  "data": {
    "createRidePassenger": {
      "ok": false,
      "message": "The ride with id 1 is already full"
    }
  }
}
```

</details>
