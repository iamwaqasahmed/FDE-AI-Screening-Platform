"""Day 3 of Week 3 retrieval checks.

Guards the retrieval checker, the hybrid checker, and the access checker.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. The optional vision, conflict, and catalog modules must match the
reference rules and then may be removed. Each shell swap restores one unfinished
retrieval module and expects a different pair of checkers to fire. A vector
search rewritten to behave like hybrid must clear retrieval and fail the hybrid
slice. Sprint order, the refusal and audience notes, and the knowledge page are
required. A pasted watermark must fail without echoing a held question.
"""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.acl_w3 import acl_problems
from alwaha.check.agent_run import WATERMARK
from alwaha.check.hybrid_w3 import CLEARS, hybrid_problems
from alwaha.check.load_app import load_module
from alwaha.check.rag_w3 import (
    DRAFT,
    FEED,
    INFLIGHT,
    REFUSE,
    SPAN,
    STAFF,
    UNAUTH,
    V4_SCOPE,
    rag_problems,
)
from alwaha.config.profile import load
from alwaha.engagement.w3d3 import gold
from alwaha.engagement.w3d3_corpus import extras, photo
from alwaha.engagement.w3d3_docs import catalog_rows
from alwaha.engagement.w3d3_rules import booking, lookup, vision_clause
from alwaha.paths import W3D3_APP, W3D3_WORK


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts a stale index, a staff document shown to a
    patient, or a search that only copies the hybrid path.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree.

        The gold object is the generator's, and one field is compared with a second
        call so a drift in the changed-document list fails before the swaps run.
        """
        # A temporary pack. The gold object comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d3 import write_w3d3

        write_w3d3(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree. The changed-document list must already agree with a second call.
        self.work = root / "work"
        shutil.copytree(W3D3_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        self.assertEqual(self.gold["changed"], gold(self.profile)["changed"])

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _rag(self) -> list[str]:
        """Run the retrieval checker."""
        return rag_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hybrid(self) -> list[str]:
        """Run the hybrid checker."""
        return hybrid_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _acl(self) -> list[str]:
        """Run the access checker."""
        return acl_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, a held question, or a
        held span and its document id.
        """
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        for row in self.gold["held"]:
            self.assertNotIn(row["question"]["text"], joined)
            expect = row["expect"]
            if "span" in expect:
                self.assertNotIn(expect["span"], joined)
                self.assertNotIn(expect["doc_id"], joined)

    def _swap(self, name: str) -> None:
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W3D3_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a retrieval, hybrid, or access problem."""
        self.assertEqual(self._rag(), [])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
        """Fails when vision, conflict, or catalog disagrees with the reference rule, or
        when deleting those modules makes a passing tree fail.
        """
        vision = load_module(self.work / "app", "vision")
        conflict = load_module(self.work / "app", "conflict")
        catalog = load_module(self.work / "app", "catalog")
        _safety, cluster, safra = extras()
        self.assertEqual(vision.clause(photo()), vision_clause(photo()))
        self.assertEqual(conflict.booking([cluster, safra], "h-safra"), booking([cluster, safra], "h-safra"))
        self.assertEqual(catalog.lookup(catalog_rows(), "endo"), lookup(catalog_rows(), "endo"))
        for name in ("vision.py", "conflict.py", "catalog.py"):
            (self.work / "app" / name).unlink()
        self.assertEqual(self._rag(), [])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [])

    def test_shell_chunk_drops_the_span(self) -> None:
        """Fails when the unfinished chunker, which drops the span, is accepted by
        retrieval. Hybrid and access should stay quiet.
        """
        self._swap("chunk.py")
        problems = self._rag()
        self.assertEqual(problems, [SPAN])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [])
        self._hidden(problems)

    def test_shell_embed_lets_vector_clear(self) -> None:
        """Fails when the unfinished embedding lets vector search clear the hybrid slice,
        or when retrieval and access do not still see the dropped span.
        """
        self._swap("embed.py")
        self.assertEqual(self._rag(), [SPAN])
        self.assertEqual(self._hybrid(), [CLEARS])
        self.assertEqual(self._acl(), [SPAN])
        self._hidden(self._rag())

    def test_shell_index_is_empty(self) -> None:
        """Fails when an empty index is accepted by any of the three checkers."""
        self._swap("index.py")
        self.assertEqual(self._rag(), [SPAN])
        self.assertEqual(self._hybrid(), [SPAN])
        self.assertEqual(self._acl(), [SPAN])

    def test_shell_search_cites_the_unauthorized_circular(self) -> None:
        """Fails when retrieval or access reject a search whose only fault is citing the
        unauthorized circular, or when hybrid does not catch that citation.
        """
        self._swap("search.py")
        self.assertEqual(self._rag(), [])
        self.assertEqual(self._hybrid(), [UNAUTH])
        self.assertEqual(self._acl(), [])
        self._hidden(self._hybrid())

    def test_shell_filter_shows_staff_to_a_patient(self) -> None:
        """Fails when a filter that shows a staff document to a patient is accepted by
        retrieval or access. Hybrid should stay quiet.
        """
        self._swap("filter.py")
        self.assertEqual(self._rag(), [STAFF])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [STAFF])
        self._hidden(self._rag())

    def test_shell_bind_restarts_in_flight_work(self) -> None:
        """Fails when a bind step that restarts in-flight work, keeps a draft, or widens
        the draft's scope is accepted.
        """
        self._swap("bind.py")
        self.assertEqual(self._rag(), [INFLIGHT, DRAFT, V4_SCOPE])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [])
        self._hidden(self._rag())

    def test_shell_cite_returns_the_nearest_chunk(self) -> None:
        """Fails when a citer that returns the nearest chunk is accepted. Retrieval should
        see the unauthorized circular, the draft, the scope, the staff leak, and the
        missing refusal. Access should see the staff leak.
        """
        self._swap("cite.py")
        self.assertEqual(self._rag(), [UNAUTH, INFLIGHT, DRAFT, V4_SCOPE, STAFF, REFUSE])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [STAFF])
        self._hidden(self._rag())

    def test_shell_sync_ignores_the_feed(self) -> None:
        """Fails when a sync that ignores the change feed is accepted by retrieval, or when
        access does not still see the dropped span.
        """
        self._swap("sync.py")
        self.assertEqual(self._rag(), [FEED, SPAN])
        self.assertEqual(self._hybrid(), [])
        self.assertEqual(self._acl(), [SPAN])
        self._hidden(self._rag())

    def test_vector_search_that_copies_hybrid_clears_the_slice(self) -> None:
        """Fails when making vector search behave like hybrid is rejected by retrieval, or
        accepted by the hybrid checker.
        """
        path = self.work / "app" / "search.py"
        text = path.read_text(encoding="utf-8").replace('mode == "hybrid"', 'mode in {"hybrid", "vector"}')
        path.write_text(text, encoding="utf-8")
        self.assertEqual(self._rag(), [])
        self.assertEqual(self._hybrid(), [CLEARS])
        self._hidden(self._hybrid())

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts the memo first is accepted. The index has to be
        sequenced, and the draft has to stay limited to the specialties the notice names.
        """
        (self.work / "sprint.md").write_text("# Sprint\n\nThe memo comes first.\n", encoding="utf-8")
        problems = self._rag()
        self.assertEqual(
            problems,
            ["sprint.md does not sequence the index", "sprint.md does not limit v4 to three specialties"],
        )
        self._hidden(problems)

    def test_refusal_and_audience_notes_are_required(self) -> None:
        """Fails when an empty refusal page or an audience page that lets a patient see a
        staff document is accepted.
        """
        (self.work / "refusal.md").write_text("# Refusal\n", encoding="utf-8")
        (self.work / "audience.md").write_text("# Audience\n", encoding="utf-8")
        problems = self._rag()
        self.assertEqual(
            problems,
            ["the refusal copy is missing", "the audience note lets a patient see a staff document"],
        )
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder knowledge answers are accepted in place of what makes a
        document in force and who may see a staff document.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._rag()
        self.assertEqual(
            problems,
            [
                "knowledge.md does not say what makes a document in force",
                "knowledge.md does not say who may see a staff document",
            ],
        )
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored by any checker,
        or when a problem message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._rag(), self._hybrid(), self._acl()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
