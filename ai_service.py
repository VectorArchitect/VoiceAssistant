"""Small, testable wrapper around the Google GenAI text-generation call."""


def generate_answer(client, command, model="gemini-3-flash-preview"):
    """Return non-empty text generated for a user command."""
    if not isinstance(command, str) or not command.strip():
        raise ValueError("Command must be a non-empty string.")

    response = client.models.generate_content(
        model=model,
        contents=command.strip(),
    )
    answer = getattr(response, "text", None)
    if not isinstance(answer, str) or not answer.strip():
        raise RuntimeError("Gemini returned an empty text response.")

    return answer.strip()
