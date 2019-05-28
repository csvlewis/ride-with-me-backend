# Ride with Me Backend

This is the backend API for the Ride with Me App

### Endpoints: ####

All endpoints can be accessed by sending a POST request to https://ride-with-me-backend.herokuapp.com/graphql. Each request should have a parameter of 'query', which should have a value set to the desired GraphQL query.

#### 1. Get all cities: ####

To get a list of all cities, a user can make the GraphQL query:
```
{
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
        "name": "Aspen Park, CO"
      },
      {
        "name": "Atlanta, GA"
      },
      {
        "name": "Aurora, CO"
      },
      {
        "name": "Austin, TX"
      },

...continued
```
</details>

#### 2. Get searchable cities: ####

To get a list of all cities associated with a ride, a user can make the GraphQL query:

```
{
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
          "id": "10",
          "name": "Boulder, CO"
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
{
  searchUserById(id: 1) {
    id
    firstName
    lastName
    email
    uuid
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
      "uuid": "key_1",
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
{
  searchRideById(id: 1) {
    id
  }
}

```
or the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{searchRideById(id:1){id}}

More ride information can be requested with additional query parameters like so:

```
{
  searchRideById(id: 1) {
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
        "price": 5.0,
        "totalSeats": 2,
        "departureTime": "2019-05-22",
        "status": "new_status",
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
          },
          {
            "passenger": {
              "id": "2",
              "firstName": "Arnold",
              "lastName": "Schwarzenegger"
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
{
  availableRides {
    id
  }
}
```
or the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{availableRides{id}}

More ride information can be requested with additional query parameters like so:
```
{
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
        "id": "3",
        "description": "Anyone need a ride this weekend?",
        "mileage": 1000,
        "price": 200.0,
        "totalSeats": 1,
        "departureTime": "2019-05-29",
        "status": "available",
        "driver": {
          "id": "2",
          "firstName": "Arnold",
          "lastName": "Schwarzenegger"
        },
        "ridepassengerSet": [],
        "endCity": {
          "id": "3",
          "name": "Los Angeles, CA"
        },
        "startCity": {
          "id": "2",
          "name": "Golden, CO"
        }
      },
      {
        "id": "4",
        "description": "Looking to pick up two passengers",
        "mileage": 922,
        "price": 175.0,
        "totalSeats": 2,
        "departureTime": "2019-05-20",
        "status": "available",
        "driver": {
          "id": "3",
          "firstName": "Jim",
          "lastName": "Carey"
        },
        "ridepassengerSet": [],
        "endCity": {
          "id": "4",
          "name": "Austin, TX"
        },
        "startCity": {
          "id": "1",
          "name": "Denver, CO"
        }
      },

...continued
```
</details>

#### 6. Get all available rides with start and end point and optional date: ####

To search rides with a certain start and end point, a user can make the GraphQL query:

```
{
  searchRidesByCities(startCityId: 1, endCityId: 2, departureTime: "2019-05-22") {
    id
  }
}
```

The startCityID and endCityID fields are required, while the departureTime field is optional.

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{searchRidesByCities(startCityId:1,endCityId:2,departureTime:"2019-05-22"){id}}

More ride information can be requested with additional query parameters like so:
```
{
  searchRidesByCities(startCityId: 1, endCityId: 2, departureTime: "2019-05-22") {
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
mutation ($driverUuid: String!, $startCityId: Int!, $endCityId: Int!, $description: String!, $mileage: Int!, $price: Float!, $totalSeats: Int!, $departureTime: Date!) {
  createRide(driverUuid: $driverUuid, startCityId: $startCityId, endCityId: $endCityId, description: $description, mileage: $mileage, price: $price, totalSeats: $totalSeats, departureTime: $departureTime) {
    ride {
      id
    }
  }
}

```
Example of variables sent with that mutation:

```
{
	"driverUuid": "key_1",
	"startCityId": 1,
	"endCityId": 2,
	"description": "Going for a ride",
	"mileage": 200,
	"price": 50,
	"totalSeats": 3,
	"departureTime": "2019-05-22"
}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{createRide(driverId:1,startCityId:1,endCityId:2,description:"Going for a ride",mileage:100,price:50.00,totalSeats:4,departureTime:"2019-05-23"){ride{id}}}

More ride information can be requested with additional query parameters like so:
```
mutation ($driverUuid: String!, $startCityId: Int!, $endCityId: Int!, $description: String!, $mileage: Int!, $price: Float!, $totalSeats: Int!, $departureTime: Date!) {
  createRide(driverUuid: $driverUuid, startCityId: $startCityId, endCityId: $endCityId, description: $description, mileage: $mileage, price: $price, totalSeats: $totalSeats, departureTime: $departureTime) {
    ride {
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
        "id": "76",
        "description": "Going for a ride",
        "mileage": 200,
        "price": 50.0,
        "totalSeats": 3,
        "departureTime": "2019-05-22",
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
mutation ($id: Int!, $status: String!) {
  changeRideStatus(id: $id, status: $status) {
    ride {
      id
      status
    }
  }
}

```

Example of variables sent with this request:
```
{
	"id": 1,
	"status": "completed"
}
```

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{changeRideStatus(id:1 status:"new_status"){ride {id,status}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "changeRideStatus": {
      "ride": {
        "id": "1",
        "status": "completed"
      }
    }
  }
}
```
</details>

#### 9. Get a driver's pending requests: ####

To get pending requests for a driver, a user can make the GraphQL query:
```
{
  pendingRequests(driverUuid: "key_1") {
    id
  }
}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=query{pendingRequests(driverId:1){id}}

More ride information can be requested with additional query parameters like so:
```
{
  pendingRequests(driverUuid: "key_1") {
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
        "id": "21",
        "ride": {
          "id": "1"
        },
        "passenger": {
          "firstName": "Arnold",
          "lastName": "Schwarzenegger"
        },
        "message": "This is a new request",
        "status": "pending",
        "createdAt": "2019-05-28T18:22:59.014297+00:00"
      },
      {
        "id": "20",
        "ride": {
          "id": "1"
        },
        "passenger": {
          "firstName": "Arnold",
          "lastName": "Schwarzenegger"
        },
        "message": "This is a new request",
        "status": "pending",
        "createdAt": "2019-05-28T18:22:58.469016+00:00"
      },

...continued
```
</details>

### 10. Create a Request ###

To send a request to a driver, a user can make the GraphQL query:

```
mutation ($message: String!, $passengerUuid: String!, $rideId: Int!) {
  createRequest(message: $message, passengerUuid: $passengerUuid, rideId: $rideId) {
    request {
      id
      message
      passenger {
        id
      }
      ride {
        id
      }
    }
  }
}

```
Example of variables sent with that mutation:

```
{
	"message": "Message test sending request",
	"passengerUuid": "key_1",
	"rideId": 3
}
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
        "id": "26",
        "message": "Message test sending request",
        "passenger": {
          "id": "1"
        },
        "ride": {
          "id": "3"
        }
      }
    }
  }
}
```
</details>

#### 11. Change a request's status: ####

To accept or deny a ride request, a driver can make the GraphQL query:
```
mutation($id: Int!, $status: String!) {
  changeRequestStatus(id:$id status:$status){
    request {
      id
      status
    }
  }
}
```

Example of variables sent with that mutation:

```
{
	"id": 1,
	"status": "accepted"
}
```

Here is the same request in HTTP format:

    https://ride-with-me-backend.herokuapp.com/graphql/?query=mutation{changeRequestStatus(id:1status:"new_status"){request {id,status}}}

<details>
  <summary>See example</summary>

```
{
  "data": {
    "changeRequestStatus": {
      "request": {
        "id": "1",
        "status": "accepted"
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
mutation($passengerUuid: String! $rideId: Int!){
  deleteRidePassenger(passengerUuid:$passengerUuid, rideId:$rideId){
    ok
    message
  }
}
```

Example of variables sent with that mutation:

```
{
  "passengerUuid": "key_1",
   "rideId":2
 }
```

**ok** and **message** are custom fields that get returned to let the user know if the mutation worked. When ok=True, it worked. The message explains what got deleted.

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
{
  "passengerId": 8,
  "rideId":2
}

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

#### 14. Get Rides associated with a User: ####

A user can get a list of all rides that they are associated with (as a driver or passenger) by sending the following GraphQL query:

```graphql
{
  myRides(userUuid: "key_1") {
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

<details>
  <summary>See example</summary>

```
{
  "data": {
    "myRides": [
      {
        "id": "1",
        "description": "Looking for two passengers",
        "mileage": 15,
        "price": 5.0,
        "totalSeats": 2,
        "departureTime": "2019-05-22",
        "status": "completed",
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
          },
          {
            "passenger": {
              "id": "2",
              "firstName": "Arnold",
              "lastName": "Schwarzenegger"
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
      },
      {
        "id": "21",
        "description": "Going for a ride",
        "mileage": 100,
        "price": 50.0,
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
...continued
```
</details>

#### 15. Login User: ####

To login or register a user, send the following GraphQL mutation:

```graphql
mutation ($email: String!, $firstName: String!, $lastName: String!) {
  loginUser(email: $email, firstName: $firstName, lastName: $lastName) {
    user {
      id
      firstName
      lastName
      email
      uuid
    }
  }
}

```

Example of variables sent with this request:

```
{
	"email": "new_user@gmail.com",
	"firstName": "First",
	"lastName": "Last"
}

```


<details>
  <summary>See example</summary>

A uuid will be generated and returned for the user and required for all further requests that need authorization.

```
{
  "data": {
    "loginUser": {
      "user": {
        "id": "11",
        "firstName": "First",
        "lastName": "Last",
        "email": "new_user@gmail.com",
        "uuid": "cdbadd56-8181-11e9-bfdc-9a2c58adc569"
      }
    }
  }
}
```
</details>
