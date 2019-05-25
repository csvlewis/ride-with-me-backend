# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_all_cities 1'] = {
    'data': {
        'allCities': [
            {
                'name': 'Denver, CO'
            },
            {
                'name': 'Golden, CO'
            },
            {
                'name': 'Los Angeles, CA'
            },
            {
                'name': 'Austin, TX'
            },
            {
                'name': 'Las Vegas, NV'
            },
            {
                'name': 'Aspen Park, CO'
            },
            {
                'name': 'Milwaukee, WI'
            },
            {
                'name': 'Aurora, CO'
            },
            {
                'name': 'Vail, CO'
            },
            {
                'name': 'Boulder, CO'
            },
            {
                'name': 'Fort Collins, CO'
            },
            {
                'name': 'Eldora, CO'
            },
            {
                'name': 'Orlando, FL'
            },
            {
                'name': 'Houston, TX'
            },
            {
                'name': 'San Diego, CA'
            },
            {
                'name': 'Indianapolis, IN'
            },
            {
                'name': 'San Francisco, IN'
            },
            {
                'name': 'Fort Worth, TX'
            },
            {
                'name': 'El Paso, TX'
            },
            {
                'name': 'Boston, MA'
            },
            {
                'name': 'Omaha, NE'
            },
            {
                'name': 'Miami, FL'
            },
            {
                'name': 'Atlanta, GA'
            },
            {
                'name': 'Oakland, CA'
            },
            {
                'name': 'Jersey City, NJ'
            },
            {
                'name': 'Saint Paul, MN'
            },
            {
                'name': 'Lincoln, NE'
            },
            {
                'name': 'Montgomery, AL'
            },
            {
                'name': 'Detroit, MI'
            },
            {
                'name': 'Columbus, OH'
            },
            {
                'name': 'Phoenix, AZ'
            },
            {
                'name': 'Virginia Beach, VA'
            },
            {
                'name': 'Raleigh, NC'
            },
            {
                'name': 'Tulsa, OK'
            },
            {
                'name': 'New Orleans, LA'
            },
            {
                'name': 'Cincinnati, IA'
            },
            {
                'name': 'Newark, NJ'
            },
            {
                'name': 'Boise City, OK'
            },
            {
                'name': 'Little Rock, AR'
            },
            {
                'name': 'Knoxville, TN'
            },
            {
                'name': 'Philadelphia, PA'
            },
            {
                'name': 'Washington, DC'
            },
            {
                'name': 'Salt Lake City, UT'
            },
            {
                'name': 'Santa Cruz, CA'
            },
            {
                'name': 'Pittsburgh, PA'
            },
            {
                'name': 'Wichita, KS'
            },
            {
                'name': 'Spokane, WA'
            },
            {
                'name': 'Cleveland, OH'
            },
            {
                'name': 'Greeley, CO'
            },
            {
                'name': 'Pueblo, CO'
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
                'id': '3'
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
                'id': '11'
            }
        ]
    }
}

snapshots['test_create_new_ride 1'] = {
    'data': {
        'createRide': {
            'ride': {
                'id': '12'
            }
        }
    }
}

snapshots['test_find_ride_by_id 1'] = {
    'data': {
        'searchRideById': [
            {
                'id': '1'
            }
        ]
    }
}

snapshots['test_pending_requests 1'] = {
    'data': {
        'pendingRequests': [
            {
                'id': '2',
                'message': 'Room for one more?',
                'status': 'pending'
            }
        ]
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
