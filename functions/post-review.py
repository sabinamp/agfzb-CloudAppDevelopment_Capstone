#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import datetime


# Prepare the guestbook entry to be persisted

def main(dict):
    name = dict["name"]
    dealer_id = dict["dealership"]
    review = dict["review"]
    car_make = dict["car_make"]
    car_year = dict["car_year"]
    if not name:
        return {'error': 'no name'}
    elif not dealer_id:
        return {'error': 'no dealership'}
    elif not review:
        return {'error': 'no review'}
    elif not car_make:
        return {'error': 'no car make'}
    elif not car_year:
        return {'error': 'no car year'}
    else:
        return {
            "review": {
                "name": name,
                "dealership": dealer_id,
                "review": review,
                "purchase": False,
                "another": "field",
                "purchase_date": datetime.datetime.now(),
                "car_make": car_make,
                "car_model": "Car",
                "car_year": car_year
            }
        }
