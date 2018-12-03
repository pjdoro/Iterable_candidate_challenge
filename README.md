Instructions for running scripts
In this package there are two scripts to call the single user update and bulk user update API endpoints and an input csv doccument.
To run singleUpdate you must indicate which user record to post to by specifying the row number of the csv input file to post to
To run bulkUpdate you must indicate which user records to post to by specifying a comma seperated list of integers if up to 50 rows in the csv input file
There is also a placeholder variable in both scripts Called 'api_key' which should be updated to a valid key and passed into the requests function

