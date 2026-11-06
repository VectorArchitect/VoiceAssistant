import unittest
from types import SimpleNamespace

from ai_service import generate_answer


class FakeModels:
    def __init__(self, response_text):
        self.response_text = response_text
        self.calls = []

    def generate_content(self, *, model, contents):
        self.calls.append((model, contents))
        return SimpleNamespace(text=self.response_text)


class GenerateAnswerTests(unittest.TestCase):
    def test_returns_trimmed_text_and_passes_command_to_client(self):
        models = FakeModels("  Hello from Gemini.  ")
        client = SimpleNamespace(models=models)

        answer = generate_answer(client, "  What time is it?  ")

        self.assertEqual(answer, "Hello from Gemini.")
        self.assertEqual(
            models.calls,
            [("gemini-3-flash-preview", "What time is it?")],
        )

    def test_rejects_empty_commands_before_calling_client(self):
        models = FakeModels("unused")
        client = SimpleNamespace(models=models)

        with self.assertRaises(ValueError):
            generate_answer(client, "   ")

        self.assertEqual(models.calls, [])

    def test_rejects_empty_model_responses(self):
        client = SimpleNamespace(models=FakeModels("  "))

        with self.assertRaises(RuntimeError):
            generate_answer(client, "Say hello")


if __name__ == "__main__":
    unittest.main()
