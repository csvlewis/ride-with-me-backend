# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_all_cities 1'] = {
    'data': {
        'allCities': [
            {
                'name': 'Aspen Park, CO'
            },
            {
                'name': 'Atlanta, GA'
            },
            {
                'name': 'Aurora, CO'
            },
            {
                'name': 'Austin, TX'
            },
            {
                'name': 'Boise City, OK'
            },
            {
                'name': 'Boston, MA'
            },
            {
                'name': 'Boulder, CO'
            },
            {
                'name': 'Cincinnati, IA'
            },
            {
                'name': 'Cleveland, OH'
            },
            {
                'name': 'Columbus, OH'
            },
            {
                'name': 'Denver, CO'
            },
            {
                'name': 'Detroit, MI'
            },
            {
                'name': 'El Paso, TX'
            },
            {
                'name': 'Eldora, CO'
            },
            {
                'name': 'Fort Collins, CO'
            },
            {
                'name': 'Fort Worth, TX'
            },
            {
                'name': 'Golden, CO'
            },
            {
                'name': 'Greeley, CO'
            },
            {
                'name': 'Houston, TX'
            },
            {
                'name': 'Indianapolis, IN'
            },
            {
                'name': 'Jersey City, NJ'
            },
            {
                'name': 'Knoxville, TN'
            },
            {
                'name': 'Las Vegas, NV'
            },
            {
                'name': 'Lincoln, NE'
            },
            {
                'name': 'Little Rock, AR'
            },
            {
                'name': 'Los Angeles, CA'
            },
            {
                'name': 'Miami, FL'
            },
            {
                'name': 'Milwaukee, WI'
            },
            {
                'name': 'Montgomery, AL'
            },
            {
                'name': 'New Orleans, LA'
            },
            {
                'name': 'Newark, NJ'
            },
            {
                'name': 'Oakland, CA'
            },
            {
                'name': 'Omaha, NE'
            },
            {
                'name': 'Orlando, FL'
            },
            {
                'name': 'Philadelphia, PA'
            },
            {
                'name': 'Phoenix, AZ'
            },
            {
                'name': 'Pittsburgh, PA'
            },
            {
                'name': 'Pueblo, CO'
            },
            {
                'name': 'Raleigh, NC'
            },
            {
                'name': 'Saint Paul, MN'
            },
            {
                'name': 'Salt Lake City, UT'
            },
            {
                'name': 'San Diego, CA'
            },
            {
                'name': 'San Francisco, IN'
            },
            {
                'name': 'Santa Cruz, CA'
            },
            {
                'name': 'Spokane, WA'
            },
            {
                'name': 'Tulsa, OK'
            },
            {
                'name': 'Vail, CO'
            },
            {
                'name': 'Virginia Beach, VA'
            },
            {
                'name': 'Washington, DC'
            },
            {
                'name': 'Wichita, KS'
            }
        ]
    }
}

snapshots['test_all_available_rides 1'] = {
    'data': {
        'availableRides': [
            {
                'id': '1'
            },
            {
                'id': '2'
            },
            {
                'id': '4'
            },
            {
                'id': '5'
            },
            {
                'id': '6'
            },
            {
                'id': '7'
            },
            {
                'id': '9'
            },
            {
                'id': '10'
            },
            {
                'id': '11'
            },
            {
                'id': '12'
            }
        ]
    }
}

snapshots['test_create_new_ride 1'] = {
    'data': {
        'createRide': {
            'ride': {
                'id': '13'
            }
        }
    }
}

snapshots['test_change_ride_status 1'] = {
    'data': {
        'changeRideStatus': {
            'ride': {
                'id': '1',
                'status': 'new_status'
            }
        }
    }
}

snapshots['test_searchable_cities 1'] = {
    'data': {
        'searchableCities': [
            {
                'id': '4',
                'name': 'Austin, TX'
            },
            {
                'id': '10',
                'name': 'Boulder, CO'
            },
            {
                'id': '1',
                'name': 'Denver, CO'
            },
            {
                'id': '2',
                'name': 'Golden, CO'
            },
            {
                'id': '14',
                'name': 'Houston, TX'
            },
            {
                'id': '5',
                'name': 'Las Vegas, NV'
            },
            {
                'id': '3',
                'name': 'Los Angeles, CA'
            },
            {
                'id': '7',
                'name': 'Milwaukee, WI'
            },
            {
                'id': '24',
                'name': 'Oakland, CA'
            },
            {
                'id': '26',
                'name': 'Saint Paul, MN'
            },
            {
                'id': '44',
                'name': 'Santa Cruz, CA'
            }
        ]
    }
}

snapshots['test_user_by_id 1'] = {
    'data': {
        'searchUserById': {
            'createdAt': '2019-05-20T16:23:00.067741+00:00',
            'email': 'johnnydepp@gmail.com',
            'firstName': 'Johnny',
            'id': '1',
            'lastName': 'Depp',
            'updatedAt': '2019-05-20T16:23:00.067741+00:00',
            'uuid': 'c96808f0-8195-11e9-93f6-88e9fe6e9b8e'
        }
    }
}

snapshots['test_ride_by_id 1'] = {
    'data': {
        'searchRideById': [
            {
                'id': '1'
            }
        ]
    }
}

snapshots['test_available_ride_search 1'] = {
    'data': {
        'searchRidesByCities': [
            {
                'id': '1'
            },
            {
                'id': '11'
            }
        ]
    }
}

snapshots['test_driver_pending_requests 1'] = {
    'data': {
        'pendingRequests': [
            {
                'id': '2'
            }
        ]
    }
}

snapshots['test_create_request 1'] = {
    'data': {
        'createRequest': {
            'request': {
                'id': '11',
                'message': 'Test message',
                'passenger': {
                    'id': '1'
                },
                'ride': {
                    'id': '5'
                }
            }
        }
    }
}

snapshots['test_change_request_status 1'] = {
    'data': {
        'changeRequestStatus': {
            'request': {
                'id': '1',
                'status': 'new_status'
            }
        }
    }
}

snapshots['test_delete_ridepassenger 1'] = {
    'data': {
        'deleteRidePassenger': {
            'message': 'The passenger with id 2 has been deleted from the ride with id 8. Now the ride has 1 available seat(s).',
            'ok': True
        }
    }
}

snapshots['test_add_ridepassenger 1'] = {
    'data': {
        'createRidePassenger': {
            'message': 'The passenger with id 1 has been added to the ride with id 6. Now the ride has 1 available seat(s).',
            'ok': True
        }
    }
}

snapshots['test_get_my_rides 1'] = {
    'data': {
        'myRides': [
            {
                'description': "I'm taking a trip to Golden this weekend, room for two passengers!",
                'id': '1'
            }
        ]
    }
}

snapshots['test_login_user 1'] = {
    'data': {
        'loginUser': {
            'user': {
                'email': 'johnnydepp@gmail.com',
                'firstName': 'Johnny',
                'id': '1',
                'lastName': 'Depp',
                'uuid': 'c96808f0-8195-11e9-93f6-88e9fe6e9b8e'
            }
        }
    }
}

snapshots['test_register_user 1'] = {
    'data': {
        'loginUser': {
            'user': {
                'email': 'newuser@gmail.com',
                'firstName': 'New',
                'id': '11',
                'lastName': 'User',
                'uuid': 'd9cf94a2-822a-11e9-bca0-88e9fe6e9b8e'
            }
        }
    }
}
