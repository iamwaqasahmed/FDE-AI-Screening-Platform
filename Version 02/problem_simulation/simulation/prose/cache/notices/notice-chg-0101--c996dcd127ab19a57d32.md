## What happened

Change notice CHG-0101 records the implementation of Registry extract schema v2 from 2022-01-01. The change concerns the structure used for registry extracts and the transition to a revised column format. This notice provides a record of the change and identifies the files affected during the transition.

## Cause

The change was required because Ministry moved to named columns. This replaced the previous column structure and established the schema described in the change notice.

## Effect

December 2021 file uses old columns; March 2022 mixes both. Users reviewing or processing these files should therefore account for the different column structures. The December 2021 file remains in the earlier format, while the March 2022 file contains a combination of the earlier and named-column formats.
