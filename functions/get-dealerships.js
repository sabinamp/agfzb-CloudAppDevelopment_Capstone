/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
  function main(params) {
  	return {
        params: {
          db: 'dealerships',
          include_docs: true
        }
    };
}

function formatEntries(params){
   if(!params.docs){
        return Promise.reject({ error: "Something went wrong on the server"});
    }else if(params.docs.length == 0){
       return Promise.reject({ error: "The database is empty"});
    }
    return {
        entries: params.docs.map((doc) => {
         return {
            _id: doc._id,
            _rev: doc._rev,
            city: doc.city,
            st: doc.st,
            state: doc.state,
            address: doc.address,
            zip: doc.zip,
            lat: doc.lat,
            long: doc.long,
            short_name: doc.short_name,
            full_name: doc.full_name,
         }
        })
    };
}

  const formatDealership = (doc)=>{
    return {
            _id: doc._id,
            _rev: doc._rev,
            city: doc.city,
            st: doc.st,
            state: doc.state,
            address: doc.address,
            zip: doc.zip,
            lat: doc.lat,
            long: doc.long,
            short_name: doc.short_name,
            full_name: doc.full_name,
         };
}

