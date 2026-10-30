# 05 — Tradeoffs, recommendation, sources

## Recommendation

Adopt `[ALT-A]`. Keep the seeded switch, the case clock, the watermark boundary, `status-short`, `caregiver`, and both checks. Replace pasted oracles with properties, an executed schema, a recorded gate on state, and a usability rubric. Park Pact, promptfoo-as-the-suite, live calls, mutmut, Hijri, and `phone-only` off the blocking path.

## Tradeoffs

| Choice | Gain | Cost |
| --- | --- | --- |
| Examples plus Hypothesis | Friday and Eid keep a story; a new holiday fails with no new expected date | Students read a shrunk counterexample |
| JSON Schema in-process | Uses `sms.yaml`; no broker | Weaker than a partner verifier |
| `[ALT-B]` Pact | Partner replay; state name `receipt-late` | Broker; risk of writing the hidden delay into a pact |
| Recorded gate on push | Offline; no key; watermark stays out of prompts | Blind to model drift |
| `[ALT-C]` live promptfoo on push | Drift is visible | Flake, cost, cache, pressure to `equals` the sentence |
| Injected clock | No sleep, no freezer | A later `datetime.now` escapes; add a freezer then |
| Substring ban on `sleep` | Easy to grade | Comments fail; `wait` can pass |
| CDC rubric in `chk-ux` | One FDE can run it; `delegate` is already in the gold | Not a caregiver study; English length is not Arabic literacy |
| mutmut or Hijri nightly | Finds missed comparisons; matches the advanced layer | Linux; do not block the Gregorian day |

A green `[ALT-A]` gate does not prove a mother understood the SMS, that the live model will keep `intent`, or that the vendor matches `sms.yaml`. The day is done when the mock goes red for a known fault and the recorded path refuses to treat a sentence as a booking.

## Sources

- Hypothesis strategies: https://hypothesis.readthedocs.io/en/latest/reference/strategies.html
- Hypothesis `derandomize`: https://hypothesis.readthedocs.io/en/latest/reference/api.html
- Hypothesis idempotence: https://hypothesis.readthedocs.io/en/latest/reference/integrations.html
- Hypothesis stateful tests: https://hypothesis.readthedocs.io/en/latest/stateful.html
- Pact introduction: https://docs.pact.io/
- Pact FAQ: https://docs.pact.io/faq
- Pact, contract versus functional tests: https://docs.pact.io/consumer/contract_tests_not_functional_tests
- promptfoo CI: https://www.promptfoo.dev/docs/integrations/ci-cd/
- promptfoo GitHub Action: https://www.promptfoo.dev/docs/integrations/github-action/
- promptfoo assertions: https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/
- promptfoo judge guide: https://www.promptfoo.dev/docs/guides/llm-as-a-judge/
- OpenAI eval practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- pytest flaky tests: https://docs.pytest.org/en/latest/explanation/flaky.html
- Freezegun: https://github.com/spulec/freezegun
- pytest-freezer: https://github.com/pytest-dev/pytest-freezer
- mutmut: https://mutmut.readthedocs.io/en/latest/
- CDC plain language: https://www.cdc.gov/health-literacy/php/develop-materials/plain-language.html
- CDC low-literacy tool: https://www.cdc.gov/ccindex/pdf/350129-D_MAN_RTI_CCIModule_508.pdf
- WHO health literacy: https://www.who.int/news-room/fact-sheets/detail/health-literacy
- Algabbani et al. 2022: https://doi.org/10.1016/j.jsps.2022.02.017
- Saudi Ministry of Health: https://www.moh.gov.sa/en/awarenessplateform/educationalseries/pages/default.aspx
- Albougami 2015: https://applications.emro.who.int/imemrf/J_Health_Spec/J_Health_Spec_2015_3_3_166_172.pdf
