const states=["AK","AL","AR","AS","AZ","CA","CO","CT","DC", "DE","FL","GA","GU","HI","IA","ID","IL","IN",
                      "KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM",
                      "NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA",
                      "WI","WV","WY"];
function main(params) {
    if (!params.st) {
        return Promise.reject({ error: 'No state has been given.'});
    }
    else if (!states.includes(params.st)){
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
const formatFilteredDealershipEntries=(params)=>{
    let results=[];
    if(!params){
        return Promise.reject({ error: "Something went wrong on the server"});
    }else if(!params.docs){
         return Promise.reject({ error: "Something went wrong on the server."});
    }
    else if(params.docs){
        results=params.docs;
        if(params.docs.length === 0){
            return Promise.reject({ error: "The database is empty"});
        }else{
                results.map(doc=>{ formatDealership(doc);  });
                return { 'entries': results};
        }

    }
}

const formatDealership = (doc)=>{
    return {_id: doc._id,
            city: doc.city,
            st: doc.st,
            id: doc.id,
            state: doc.state,
            address: doc.address,
            zip: doc.zip,
            lat: doc.lat,
            long: doc.long,
            short_name: doc.short_name,
            full_name: doc.full_name,
         };
}