"""Run with python -m src.agent from the repository root."""

from .config import Settings


def respond(message: str, tasks: list[str]) -> str:
    """Handle demo commands; tasks belong only to the current session."""
    command = message.strip()
    lowered = command.lower()
    if lowered == "help":
        return "Commands: add <task>, list, clear, help, quit (or exit)."
    if lowered == "list":
        if not tasks:
            return "No tasks yet. Try: add Buy groceries"
        return "Tasks:\n" + "\n".join(
            f"{index}. {task}" for index, task in enumerate(tasks, start=1)
        )
    if lowered == "clear":
        tasks.clear()
        return "Cleared all tasks for this session."
    verb, _, task = command.partition(" ")
    if verb.lower() == "add":
        task = task.strip()
        if not task:
            return "Please include a task: add Buy groceries"
        tasks.append(task)
        return f"Added: {task}"
    return "I am an offline demo. Type help for supported commands."


def main() -> int:
    settings = Settings.from_env()
    tasks: list[str] = []
    print(f"{settings.agent_name}: Offline daily-task demo. Type help for commands.")
    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if message.strip().lower() in {"quit", "exit"}:
            break
        if message.strip():
            print(f"{settings.agent_name}: {respond(message, tasks)}")
    print(f"{settings.agent_name}: Goodbye!")
    return 0


# TODO: Add a model response adapter after choosing a provider.
# TODO: Choose a memory backend before saving session data.
# TODO: Route external actions through src.tools after defining permissions.

if __name__ == "__main__":
    raise SystemExit(main())
