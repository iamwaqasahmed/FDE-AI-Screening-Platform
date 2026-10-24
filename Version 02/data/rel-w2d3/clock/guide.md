# Clock

`PUT /clock` with a JSON body `{"at": "<timestamp>"}` pins the case clock. `GET /clock` reads it back.

A receipt sent at the pinned time is due only after that clock moves by the minutes in [receipt.json](receipt.json). Advance the pinned time. Do not sleep.

`receipt-late` holds the receipt pending after that move.
