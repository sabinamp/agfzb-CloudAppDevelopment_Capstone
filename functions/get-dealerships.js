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
  if(!params.rows){
        return Promise.reject({ error: "Something went wrong on the server"});
    }else if(params.rows.length == 0){
       return Promise.reject({ error: "The database is empty"});
    }
	return {
        entries: params.rows.map((row) => {
         return {
            _id: row.doc._id,
            _rev: row.doc._rev,
            city: row.doc.city,
            st: row.doc.st,
            state: row.doc.state,
            address: row.doc.address,
            zip: row.doc.zip,
            lat: row.doc.lat,
            long: row.doc.long,
            short_name: row.doc.short_name,
            full_name: row.doc.full_name,
         }
        })
    };
  }