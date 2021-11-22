# Viikkokalenteri (backend)

## Database structure
The viikkokalenteri -database consists of documents, where each
document represents a day. Each day -document consists of the following:
1. Id
2. Date
3. Entries

### Visual representation
``` json
// This is an approximate representation of the
// actual database structure in json format.
//
// Keys that are enclosed with "<>" are going
// to be replaced with actual values.

{
	"_id": ObjectId(<unique id>),
	"<date>": {                                    // Value type: object
		"entries": {                               // Value type: object
			"<unique entry id>": {                 // Value type: object
				"subject": "<subject>",            // Value type: string
				"owner": "<entry's owner>",        // Value type: string
				"event_date": "<date>",            // Value type: string
				"event_time": "<time>",            // Value type: string
				"event_location": "<location>",    // Value type: string
				"date_created": "<created>",       // Value type: string
				"time_created": "<time created>",  // Value type: string
				"description": "<description>"     // Value type: string
			}
		}
	}
}
```
