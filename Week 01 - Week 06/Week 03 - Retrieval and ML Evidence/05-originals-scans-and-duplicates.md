# Originals, scans, and duplicates

**Day 2. Data engineer.** Most corpus documents have a Markdown file and one original under `<family>/originals/`. The Markdown is the export. It is not always the record. A board pack's per-site table is in the PDF and not in the Markdown. A quality audit's per-grader table is on the `table` sheet of the spreadsheet and not in the Markdown. A scan is the same PDF writer with damage applied. A file whose id ends in `-fwd` is a forward, not a second event.

## Read the originals

Count the files. A name ending in `.scan.pdf` is a scan, not a PDF. The rest are `.pdf`, `.docx`, and `.xlsx`.

The PDF is uncompressed text. Each line sits in parentheses, and the table rows are set in a monospace font. You do not need a PDF library. A DOCX file is a zip; the words are in `word/document.xml`. An XLSX file opens in pandas. The audit table is the sheet named `table`.

Pick one scan and the Markdown of the same document. Diff them. The damage is a small set of swaps, applied to some words and not others. Record the swaps. They are the same on every seed.

## Forwards

A forward shares almost all of its text with another document and changes the title. Cite the original. The question that says so is still asking for the original's document id, not the forward's. Find the pairs by the text, and confirm the id suffix.

The table questions ask for a number or a grader id that the Markdown does not contain. If your index only reads `.md`, those questions stay wrong no matter how good the ranking is.

## Fill these findings

| Item | What it holds |
|---|---|
| `originals` | `pdf`, `docx`, `xlsx`, and `scan` counts |
| `table_only` | `boards` whose site table is only in the PDF, and `audits` whose grader table is only in the spreadsheet |
| `scan_damage` | `pairs` such as `l>1`, one string per swap |
| `near_duplicates` | `count` of forwards, and `suffix` |

**A miss that looks like progress.** Indexing the Markdown and calling the corpus done. The board question is still wrong.

**Finish.** The four findings are filled from the files. You can open a board PDF and read one backlog cell the Markdown does not have.

Next: [Cite, refuse, and resist](06-cite-refuse-and-resist.md).
