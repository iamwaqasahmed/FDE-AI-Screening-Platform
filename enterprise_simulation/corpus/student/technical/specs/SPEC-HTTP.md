---
id: SPEC-HTTP
title: Local read API for extracts
date: 2027-01-04
type: specification
author: Bobbi Tran
systems:
  - local-read-api
access: student
---

# Local read API for extracts

I am Bobbi Tran. This specification is the local HTTP reader for the student extracts. The date is 4 January 2027. The process is local Python in the `access` package. The command is `python -m access serve`. The optional flag `--port` chooses the port. When the flag is omitted, the port is 8088. The server is a `ThreadingHTTPServer` bound to `127.0.0.1` and that port. It does not bind a public interface. It does not open a remote account. On start it prints `http://127.0.0.1:<port>/extracts` and then serves until the process is stopped.

The reader loads JSON files from `student_pack/extracts` under the `enterprise_simulation` directory. It builds that bundle by listing `*.json` in the directory, sorting the paths, and parsing each file as UTF-8 JSON. The key for a file is the stem, the file name with `.json` removed. `hospital.json` is the key `hospital`. `student_pack/sponsor.json`, `student_pack/organization.json`, and `student_pack/README.md` sit beside the extracts directory and are not part of the bundle. Files under `student_pack/bytes/` are not part of the bundle. The reader does not open `var/log.sqlite` and does not open `var/proj/hospital.sqlite`, `channel.sqlite`, or `payer.sqlite`. A request is answered from the extract files on disk. Each request reads the directory again, so a file that has been replaced on disk is what the next GET returns.

The handler implements `GET`. Responses that succeed send status 200 and the header `Content-Type: application/json`. The process does not write a request log line. There is no write API. The routes below are the whole interface.

## GET /health

`GET /health` returns the JSON object `{"status":"up"}`. The body is that compact object. `GET /` returns the same object and the same status. Both mean the process is accepting reads. The status field on this object is the string `up`. It is not a document status, a host panel, or a coverage answer. A path that is not exactly `/` or exactly `/health` does not take this branch. `/health/` is not this route.

## GET /extracts

`GET /extracts` returns one JSON object, the whole bundle. Each key is a stem. Each value is the JSON value parsed from that file, written again with the standard JSON encoder. A file that holds a list comes back as a JSON array. A file that holds an object comes back as a JSON object. Key order inside an object follows the order in the file. The route is an exact path match. `/extracts/` is not this route. It falls through to the single-extract rule with an empty name.

After `python -m access init` or `reset`, the extract directory contains these stems: `asks`, `assistant_screen`, `audit`, `boards`, `byte_index`, `calibration`, `calls`, `channel`, `desk`, `documents`, `focus`, `host`, `hospital`, `identity_graph`, `legacy_desk`, `monthly_volume`, `payer`, `served_document`, `shadow`, and `site_feeds`. The bundle includes every `*.json` file in the directory, sorted by path. Adding another JSON file in that directory adds another key on the next GET. Removing a file removes its key. The reader does not keep a second copy of the bundle in memory across requests.

`hospital`, `channel`, and `payer` are the projected document lists. `documents` is the list of hospital `DocumentChanged` payloads with `occurred_at` copied onto each object. `boards` is the board list. The other keys are the other JSON files in the same folder. This route returns them together. It does not filter by referral.

## GET /extracts/\<name\>

`GET /extracts/<name>` returns the one bundle value whose key equals `<name>`. The name is the path text after `/extracts/`, with a query string removed if a `?` is present. The name is compared as that text. The reader does not strip a trailing slash, and it does not decode a percent-encoded character before the comparison. `GET /extracts/hospital` returns the hospital array. `GET /extracts/documents` returns the documents array. `GET /extracts/host` returns the host object. `GET /extracts/hospital?verbose=1` uses the name `hospital`, because the query is cut off before the lookup.

When the name is not a key in the bundle, the response is status 404. That response has no JSON body and does not set `Content-Type`. An unknown stem, a stem with a slash still attached, and a file that lives outside `student_pack/extracts` are all misses. The route never creates a file to satisfy a miss, and it never returns an empty object in place of a missing extract.

The body of a hit is the JSON value of that one file, encoded as UTF-8. Callers that want every extract use `GET /extracts`. Callers that want one file use this route. The two responses are the same JSON value for that key. The single-file route does not wrap the value in an envelope.

## GET /ref/\<ref\>

`GET /ref/<ref>` returns one JSON object with two fields: `ref`, the text that was requested, and `hits`, a list. The referral text is the path after `/ref/`, with a query string removed. The same rule applies as for extract names: the characters are used as they appear on the path, without a separate decode step. An unknown referral is not a 404. The response is still status 200, with `hits` an empty list, and `ref` set to the text that was asked for.

A hit is an object `{"extract": <stem>, "row": <row>}`. The stem is the bundle key in which the row was found. The row is the JSON object that matched. Hits are collected by walking the bundle in sorted stem order, and by walking each file in its stored order. The walk treats a JSON array as a list of objects. It treats a JSON object as a candidate row, and it also walks nested objects and nested arrays, except that it does not descend into a property named `payload`. A nested `payload` is still visible on the row that contains it. It is not walked as a separate row of its own.

A row matches when any of the following is true. The row's `ref` equals the requested text. The row's `stream_id` equals the requested text. The row's `stream_ref` equals the requested text. The row's `stream` equals the requested text when `stream` is a string. The row's `stream` is an object whose `ref` equals the requested text. The row's `payload` is an object whose `ref` equals the requested text. Other strings on the row do not match. A referral that appears only inside a letter's prose, and not in one of those fields, is not a hit.

The hospital extract is a list of projection documents. A mart row, a nightly-file row, a cache row, and an event row match on `ref` when that field equals the request. A document event whose payload carries `ref` can also match through the payload rule, because the event document keeps `payload` on the row even though the walk does not descend into it. The payer extract matches coverage rows the same way. `GET /ref/REF-4417` therefore returns the hits whose fields name `REF-4417`, each labeled with the extract stem it came from. `GET /ref/REF-2290` returns the hits for that referral, including the coverage row whose `answer` is `timeout`. The route does not join those hits into one object and does not drop a hit because another extract disagrees with it. The list is the matches.

## Status codes and methods

| Request | Result |
| --- | --- |
| `GET /` | 200, `{"status":"up"}` |
| `GET /health` | 200, `{"status":"up"}` |
| `GET /extracts` | 200, bundle object |
| `GET /extracts/<name>` when `<name>` is a stem | 200, that JSON value |
| `GET /extracts/<name>` when `<name>` is unknown | 404, empty body |
| `GET /ref/<ref>` | 200, `{"ref","hits"}`, hits possibly empty |
| any other path | 404, empty body |

Any other path, including a misspelled route, is status 404 with the same empty body as an unknown extract name. The reader then returns without writing a JSON error object.

There is no write API. The handler class defines `GET` and does not define a post, put, patch, or delete method. Those methods are not routes that append a log command, replace an extract, or edit a projection. The server does not accept a body as a command. It does not call the log writer, and it does not call the projector. A client that needs a new log row uses the local Python writer against `var/log.sqlite`, which is a different entry point from this process. A client that needs a new projection runs the projector locally. Neither of those steps is an HTTP route on this server.

The process does not import the sealed release module or the sealed holdout module. Holdout inputs are not copied into `student_pack`, and this reader cannot serve a file that is not in `student_pack/extracts`. What a caller can read is the JSON that is already in that directory, by the four read URLs above: `/health`, `/extracts`, `/extracts/<name>`, and `/ref/<ref>`.
