# Hermes-Ai-Agent

A small foundation for a conversational assistant for daily tasks.

This version is an offline, rule-based demo, not a configured AI model. It can
add, list, and clear tasks during a terminal session. Tasks disappear on exit.
No network requests, cloud inference, local inference, or external actions are
configured.

## Local setup

Requires Python 3.10 or newer. From a terminal:

```sh
git clone https://github.com/lagui73-crypto/Hermes-Ai-Agent.git
cd Hermes-Ai-Agent
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Then run:

```sh
python -m pip install -r requirements.txt
python -m src.agent
```

If your system uses `python3` instead of `python`, substitute it above.
There are no third-party dependencies or required credentials.

## Configuration

Settings come from the process environment. `.env.example` documents the
optional `HERMES_AGENT_NAME` setting (default: `Hermes`). No variables are
required. A `.env` file is not loaded automatically.

PowerShell example:

```powershell
$env:HERMES_AGENT_NAME = "Hermes"
python -m src.agent
```

macOS/Linux example:

```sh
HERMES_AGENT_NAME=Hermes python -m src.agent
```

Never commit real credentials. Provider-specific settings will be added only
after a provider is selected.

## First run

```text
Hermes: Offline daily-task demo. Type help for commands.
You: add Buy groceries
Hermes: Added: Buy groceries
You: list
Hermes: Tasks:
1. Buy groceries
You: quit
Hermes: Goodbye!
```

Commands: `help`, `add <task>`, `list`, `clear`, and `quit` (or `exit`).
EOF and Ctrl+C also end the session. Other input gets a prompt explaining the
supported commands; free-form AI conversation is a future extension.

## Test

From the repository root:

```sh
python -m unittest discover -s tests -v
```

The smoke test launches the real entry point, adds and lists a task, and exits.

## Structure and next decisions

- `src/agent.py`: terminal loop and small response function.
- `src/config.py`: environment-based settings.
- `src/tools/`: future integration boundary.
- `tests/`: entry-point smoke test.

TODO:
- Choose a model provider and model; add a response adapter and credential
  validation without hardcoding secrets.
- Choose a memory backend and retention policy before persisting any tasks or
  conversation.
- Choose external integrations and define permissions and confirmation behavior
  before enabling actions.
