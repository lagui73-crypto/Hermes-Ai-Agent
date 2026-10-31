"""Smoke-test the actual terminal entry point without network access."""

import os
from pathlib import Path
import subprocess
import sys
import unittest


class AgentSmokeTest(unittest.TestCase):
    def test_entry_point(self):
        result = subprocess.run(
            [sys.executable, "-m", "src.agent"],
            input="add Buy groceries\nlist\nquit\n",
            text=True,
            capture_output=True,
            cwd=Path(__file__).resolve().parents[1],
            env={**os.environ, "HERMES_AGENT_NAME": "Smoke"},
            timeout=10,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Smoke: Offline daily-task demo.", result.stdout)
        self.assertIn("Smoke: Added: Buy groceries", result.stdout)
        self.assertIn("1. Buy groceries", result.stdout)
        self.assertIn("Smoke: Goodbye!", result.stdout)


if __name__ == "__main__":
    unittest.main()
