# 03 — The booking

Open the finished [queue.py](work/app/queue.py), [file_ain.py](work/app/file_ain.py), and [notify.py](work/app/notify.py) and put them beside yours.

[sched-ain.md](sources/release/systems/sched-ain.md) says the schedule is a nightly full file, the last file wins, a missed night leaves the previous file, and a real-time booking returns queued. [queued.json](sources/release/fixtures/queued.json) records facility `h-ain` and status `queued`. The clinic code on the nightly file is in [nightly.json](sources/release/fixtures/nightly.json). The clinic code on the previous file is in [missed.json](sources/release/fixtures/missed.json). Read those values in the files. This page does not type them.

## The booking

`book` returns `queued` when the facility is `h-ain` and the fault is not `live-slot`. The next line returns `booked`. That line covers the live-slot fault and any facility that is not `h-ain`, such as `h-wadi`. The word `booked` on that line is expected.

The shell ignores the facility and returns `booked` for every call. While that shell is the file that runs, the journey check says `a live slot was promised`. The message does not name the return value.

## The file

`apply_file` returns `previous` when `arrived` is `None`. That is a missed night. When a file arrives, it returns `arrived`. The last file wins. The type line can still say `None`. That is the type of a missing night, not a cleared schedule.

The shell returns `None` when the night file is missing. While that shell is the file that runs, the journey check says `a missed night cleared the slots`. If a new file does not replace yesterday, the check says `the nightly file did not replace yesterday`.

## The notice

`notify` returns `queued` when the status is `queued`. The argument `sent` is deleted. A failed notice does not confirm the slot, and a notice that was sent does not confirm it either. The slot stays queued until the nightly file is applied.

The shell returns `booked` when the notice was not sent. While that shell is the file that runs, the journey check says `a failed notice confirmed a slot`.

The three tests match those three results. `test_ain_stays_queued` still expects `booked` on the live-slot line. That is the fault, not a confirmed Ain slot.

The journey check scores those three files when they are present. The work is to replace the work copies. The packet copies stay the shells.

Next: [04 — The contract](04-the-contract.md).
