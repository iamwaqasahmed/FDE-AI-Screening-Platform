import unittest

from app import health


class HealthTest(unittest.TestCase):
    def test_ok(self) -> None:
        body = health()
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["service"], "patient-access-assistant")


if __name__ == "__main__":
    unittest.main()
