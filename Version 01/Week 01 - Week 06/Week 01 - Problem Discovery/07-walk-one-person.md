# Walk one person

**Day 4.** Pick five people from the registry and try to follow each one through every system that should know them. The point is the break, not the success.

The keys are the ones you listed under `no_master_key`:

| Key | Where it shows up |
|---|---|
| Registry number | Registry, warehouse |
| Local screening id | Registry, grader, letters, ophthalmology messages |
| Hospital number (MRN) | PACS, ophthalmology messages, clinic letters |
| Lab patient id | The HbA1c feed |
| Booking id | Appointments, SMS receipts, the access log |

Names, dates of birth, and postcodes can link a row when the keys do not. Dates of birth are in more than one format. The same district is spelled more than one way. A shared phone number is a household, not a person.

For each person, write one line per system: linked, not linked, or linked to someone else. Note the first place the chain breaks. You do not have to resolve the whole register this week. You do have to be able to say, with an example, why a join on the registry number is not a join on a person.

The software engineer owns the walk. The data engineer owns the rule the walk implies for Friday's count.

**Finish.** Five traces, and a sentence that says there is no master key.

Next: [Size the problems](08-size-the-problems.md).
