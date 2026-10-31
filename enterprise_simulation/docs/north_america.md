# North American setting

Northline is fictional. The people, member ids, and clinical text are synthetic. Nothing here is a real patient's record.

## What was applied

- Addresses use a Vancouver postal code (`V6B 1A1`) and Washington sites. ZIP codes are not mixed into the BC row.
- The member's coverage currency is CAD. The Cedar Ridge site is in WA, so the board states both.
- Times are UTC instants. Local close times on the hours documents use `America/Los_Angeles`. The desk clock for BC is `America/Vancouver`. In January those zones are both UTC−8. The channel log also contains a desk note from the 1 November 2026 fall-back morning with two civil stamps, `01:30-07:00` and `01:30-08:00`. That note is evidence. There is no graded converter.
- `population()` adds referrals from January 2025 through 2026. A mother and a newborn in BC share `604-555-0144`. Twins share `604-555-0199`. `MRN-44190` is reused and then pointed at a replacement person. Washington numbers use `206`. Cedar Ridge replays one nightly file id.
- Office work for the SLA is Monday through Friday. Cedar Ridge can still file a nightly extract on a weekend. Counting that weekend stamp as an office day is a mistake the data allows and the pack does not explain.
- Harbor Coverage can answer yes, no, or time out. A timeout is not coverage. The opening seed's answer is yes inside a window. The hospital cache copies `eligible` and drops the window.
- Clinical text stays in the hospital extract. The student pack is still sensitive synthetic text. It is not a claim that the simulator meets HIPAA or PIPEDA. Those regimes are why the letter is marked audience `clinician` and why a later account template must not receive it. The orientation page in `IDEA/` already says the case does not certify compliance. The same limit holds here.
- The sponsor asks for one number before a long weekend. That is an organizational request, not a statute.

## What was not copied from a statute

No billing code set, no claims adjudication engine, and no cross-border transfer filing. Adding them would look like compliance theater. The engineering problem is authority, clocks, and bytes.
