#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#


def main(dict):
    dealer_id = dict['dealerId']
    if dealer_id:
        return get_query(dealer_id)
    else:
        return {'error': 'dealerId does not exist'}


def get_query(dealer_id):
    return {'query': {
        "selector": {
            "dealership": {
                "$eq": dealer_id
            }
        },
        "fields": [
            "_id",
            "_rev",
            "name",
            "dealership",
            "review",
            "purchase",
            "purchase_date",
            "car_make",
            "car_model",
            "car_year"
        ],
        "use_index": "dealership-index"
    }}


# format review returned by the query above
def format_review_entries(dict):
    reviews = dict["docs"]
    if reviews:
        results = []
        for doc in reviews:
            dealer_review = format_review_entry(doc)
            results.append(dealer_review)
        return {'entries': results}
    elif len(reviews) == 0:
        return {'error': "The database is empty"}
    else:
        return {'error': "Something went wrong on the server"}


def format_review_entry(doc):
    return {'_id': doc["_id"],
            'dealership': doc["dealership"],
            'name': doc["name"],
            'review': doc["review"],
            'purchase': doc["purchase"],
            'purchase_date': doc["purchase_date"],
            'car_make': doc["car_make"],
            'car_model': doc["car_model"],
            'car_year': doc["car_year"]
            }
