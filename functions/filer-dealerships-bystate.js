const states=["AK","AL","AR","AS","AZ","CA","CO","CT","DC", "DE","FL","GA","GU","HI","IA","ID","IL","IN",
                      "KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM",
                      "NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA",
                      "WI","WV","WY"];
function main(params) {
    if (!params.st) {
        return Promise.reject({ error: 'No state has been given.'});
    }
    else if (states.indexOf(params.st) === -1){
        return Promise.reject({ error: "The state doesn't exist."});
    }
	return {
	    'query': {
	          "selector": {
                  "st": {
                     "$eq": params.st
                  }
               },
               "fields": [
                  "_id",
                  "_rev",
                  "city",
                  "state",
                  "st",
                  "address",
                  "zip",
                  "lat",
                  "long",
                  "short_name",
                  "full-name"
               ],
               "use_index": "dealership-st-index",
               "skip": 0
            }
	    };
}
