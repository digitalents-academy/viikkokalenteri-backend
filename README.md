# Viikkokalenteri (backend)

## Database structure
The viikkokalenteri -database consists of documents, where each
document represents a day. Each day -document consists of the following:
1. Id
2. Date
3. Entries

### Visual representation
``` json
{
    "_id": <day id>,
    "<date>": {
        "entries": {
            "<entry id>": {
                "subject": "<subject>",
                "owner": "<entry's owner>",
                "event_date": "<date>",
                "event_time": "<time>",
                "event_location": "<location>",
                "date_created": "<created>",
                "time_created": "<time created>",
                "description": "<description>"
            }
        }
    }
}
```
