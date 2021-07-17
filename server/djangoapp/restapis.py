from typing import List

import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from .localsettings import URL_DEALERSHIP_API, URL_REVIEW_API


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))

def get_request(url, **kwargs):
    print("GET from {} ".format(url))
    print(kwargs)
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, params=kwargs, headers={'Content-Type': 'application/json'})

    except:
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(**kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(URL_DEALERSHIP_API)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
        # For each dealer object
        for dealer in dealers:
            print(dealer)
            # Get its content in `doc` object
            dealer_obj = CarDealer(_id=dealer.get("id"), address=dealer.get("address"), city=dealer.get('city'),
                                   st=dealer.get("st"),
                                   full_name=dealer.get("full_name"),
                                   short_name=dealer.get("short_name"),
                                   lat=dealer.get("lat"),
                                   long=dealer.get("long"),
                                   zip=dealer.get("zip")
                                   )
            results.append(dealer_obj)
    return results


def get_dealers_by_state(st):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(URL_DEALERSHIP_API, st=st)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
        # For each dealer object
        for dealer in dealers:
            print(dealer)
            # Get its content in `doc` object
            dealer_obj = CarDealer(_id=dealer.get("id"), address=dealer.get("address"), city=dealer.get('city'),
                                   st=dealer.get("st"),
                                   full_name=dealer.get("full_name"),
                                   short_name=dealer.get("short_name"),
                                   lat=dealer.get("lat"),
                                   long=dealer.get("long"),
                                   zip=dealer.get("zip")
                                   )
            results.append(dealer_obj)
    return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf(dealer_id):
    results = []
    json_result = get_request(URL_REVIEW_API, dealerId=dealer_id)
    if json_result:
        # Get the row list in JSON as reviews
        print(json_result)
        if json_result.get("error"):
            return []
        else:
            reviews = json_result.get("entries")
            for rev in reviews:
                print(rev)
                review_obj = DealerReview(_id=rev.get("_id"),
                                          car_make=rev.get("car_make"),
                                          car_model=rev.get("car_model"),
                                          car_year=rev.get("car_year"),
                                          dealership=rev.get("dealership"),
                                          name=rev.get("name"),
                                          purchase=rev.get("purchase"),
                                          purchase_date=rev.get("purchase_date"),
                                          review=rev.get("review"))
                results.append(review_obj)
    return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
