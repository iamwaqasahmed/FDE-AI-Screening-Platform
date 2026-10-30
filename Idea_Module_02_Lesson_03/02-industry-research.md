# 02 — Industry research

Pages below were fetched from the publishers (CDC checklist July 2025; WHO fact sheet 22 December 2025; promptfoo CI page 30 October 2026).

## Calendar properties and idempotency

Hypothesis draws from strategies and shrinks failures. `st.dates` shrinks toward 1 January 2000 ([strategies](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html)). On CI, `derandomize` defaults to true ([settings](https://hypothesis.readthedocs.io/en/latest/reference/api.html)).

Properties an FDE can write alone: the result’s weekday is in `working_days`; its ISO date is absent from `holidays`; the count of such days from the start through the result equals `count`; a larger count lands later; Friday and Saturday stay out when the working set omits them, including across March 2027. `[ADD]` Keep `thursday` and `eid` as examples. The property fails a third holiday without a new expected date.

Ghostwriter `--idempotent` checks `f(x) == f(f(x))` ([integrations](https://hypothesis.readthedocs.io/en/latest/reference/integrations.html)). That fits a normalizer. It does not fit `add_working_days`. The receipt property is purity: the same arguments return the same `pending` or `due` on a second call. A state machine that pins, sends, advances, and reads is `[NIGHTLY]` ([stateful](https://hypothesis.readthedocs.io/en/latest/stateful.html)). Hijri weekend exclusion stays off `chk-tests` until the Gregorian property is in the gate.

## Pact and schema tests

Pact checks each side in isolation. The consumer records concrete examples; the provider replays them. Pact calls this contract by example. OpenAPI lists possible states and does not prove the consumer calls them ([introduction](https://docs.pact.io/)). The FAQ refuses a pact generated from a schema ([FAQ](https://docs.pact.io/faq)). A contract checks the message. A functional test checks the side effect ([contract versus functional](https://docs.pact.io/consumer/contract_tests_not_functional_tests)).

The consumer is the assistant. The provider is the SMS partner outside `zone-private`. `sms.yaml` already names 202 and 200. Provider state `receipt-late` is the Pact name of the switch. `[ALT-A]` executes a JSON Schema (`intent` in a closed set, `text` a string that may be empty) and maps `pending`↔202, `due`↔200. `[ALT-B]` is a pact the partner verifies. Use it when that verifier exists.

## LLM eval in CI

promptfoo runs `npx promptfoo@latest eval`, supports `--fail-on-error`, writes JUnit, and caches with `PROMPTFOO_CACHE_PATH` ([CI/CD](https://www.promptfoo.dev/docs/integrations/ci-cd/)). The GitHub Action evaluates changed prompts ([action](https://www.promptfoo.dev/docs/integrations/github-action/)). Assertions include `equals`, `is-json` plus schema, and `javascript` ([deterministic](https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/)). The judge guide says one right answer has many wordings, so string match splits them ([judge](https://www.promptfoo.dev/docs/guides/llm-as-a-judge/)). OpenAI says the same input can yield different text, and names BLEU-only metrics and “it seems to work” as anti-patterns ([best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

pytest pattern: `@pytest.mark.recorded` loads the pack fixture or a JSONL tape and asserts `intent` plus state. `@pytest.mark.live` stays off the push job. A golden transcript is that tape of contract fields. pytest treats a flake as uncontrolled state and warns against a permanent `xfail` quarantine ([flaky](https://docs.pytest.org/en/latest/explanation/flaky.html)). `[GATE]` recorded and offline. `[NIGHTLY]` live, cached, schema assertions only. A cache hit is a saved answer, weak evidence the model still behaves.

## Time, literacy, snapshots, mutation

`receipt_state` already takes `now`. That injection is the control. Freezegun and pytest-freezer freeze `datetime.now`; a real sleep does not move a frozen clock unless you `tick` ([freezegun](https://github.com/spulec/freezegun), [pytest-freezer](https://github.com/pytest-dev/pytest-freezer)). Add a freezer only if code calls the wall clock. Do not add a sleep for the freezer to cancel. Disable Hypothesis deadlines on heavy properties. Do not hide a wait with reruns.

CDC: plain language is understood the first time; important message first; active voice; about 20 words and one idea per sentence ([plain language](https://www.cdc.gov/health-literacy/php/develop-materials/plain-language.html)). The low-literacy tool adds one action per screen and says a checklist is not user testing ([IDD/ELL tool](https://www.cdc.gov/ccindex/pdf/350129-D_MAN_RTI_CCIModule_508.pdf)). WHO: health literacy is access, understanding, appraisal, and use, mediated by the service, including language ([fact sheet](https://www.who.int/news-room/fact-sheets/detail/health-literacy)).

Algabbani et al. studied 130 caregivers in Riyadh pediatric clinics (47% mothers). An Arabic Newest Vital Sign put 43% (n=56) at “a possibility of limited health literacy.” Pictograms raised mean correct leaflet answers from 4.38 to 5.25 ([Algabbani et al., 2022](https://doi.org/10.1016/j.jsps.2022.02.017)). Ministry of Health series say the text is for non-specialists ([MOH](https://www.moh.gov.sa/en/awarenessplateform/educationalseries/pages/default.aspx)). Albougami finds that a few Arabic words are not enough for patients in Saudi hospitals ([Albougami, 2015](https://applications.emro.who.int/imemrf/J_Health_Spec/J_Health_Spec_2015_3_3_166_172.pdf)).

Automate length, one imperative, a control name, and caregiver outcome `delegate` with `booked` false. A green linter is not a caregiver study. English length is not Arabic comprehension. `phone-only` stays the advanced channel.

`[DO NOT SNAPSHOT]` Prose (`equals`, BLEU, “The visit is booked”); the watermark; wall-clock stamps; the hidden delay and due dates; a promptfoo cache entry treated as a fresh call; Hijri display strings (store `1448-07-29` if a value is stored); generated ids. `[KEEP]` exact: `intent`, `booked`, `pending`/`due` at a pinned clock, weekday membership, `sms.yaml` status codes.

mutmut needs `fork`, so Windows means WSL ([mutmut](https://mutmut.readthedocs.io/en/latest/)). `[GATE]` is the seeded always-due mutant: the suite goes red while `receipt-late` is on. `[NIGHTLY]` on Linux may mutate `receipt_state` and `schema_ok` only.
