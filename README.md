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
    "_id": "<day id>",
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

### Datatypes
This section describes the datatypes of the
values from the representation shown above.

| Key             | Value         | Type      |
| --------------: | :-----------: | :-------- |
| \_id            | id            | ObjectId  |
| date            | Object        | Object    |
| entries         | Object        | Object    |
| entry           | Object        | Object    |
| subject         | Subject       | String    |
| owner           | Owner         | String    |
| event\_date     | Date          | String    |
| event\_time     | Time          | String    |
| event\_location | Location      | String    |
| date\_created   | Created       | String    |
| time\_created   | Time created  | String    |
| description     | Description   | String    |

## Authors
- [Niklas Larsson](https://github.com/nikkelarsson)
- [Aki Sartolahti](https://github.com/donqnr)

