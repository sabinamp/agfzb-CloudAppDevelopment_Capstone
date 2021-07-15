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
# sample param
# {
# "review":
# {
# "name": "Upkar Lidder",
# "dealership": 15,
# "review": "Great service!",
# "purchase": false,
# "another": "field",
# "purchase_date": "02/16/2021",
# "car_make": "Audi",
# "car_model": "Car",
# "car_year": 2021
# }
# }
def main(dict):
    if not dict or not dict["review"]:
        return {'error': 'no review given'}
    else:
        rew = dict["review"]
        name = rew["name"]
        dealer_id = rew["dealership"]
        review = rew["review"]
        car_make = rew["car_make"]
        car_year = rew["car_year"]
        car_model = rew["car_model"]
        purchase_date = rew["purchase_date"]
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
        elif not car_model:
            return {'error': 'no car model'}
        else:
            return {
                "doc": {
                    "name": name,
                    "dealership": dealer_id,
                    "review": review,
                    "purchase": False,
                    "purchase_date": purchase_date,
                    "car_make": car_make,
                    "car_model": car_model,
                    "car_year": car_year
                }
            }
