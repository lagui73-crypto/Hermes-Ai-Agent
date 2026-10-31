"""Read settings from the process environment; never store secrets here."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    agent_name: str = "Hermes"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(agent_name=os.getenv("HERMES_AGENT_NAME", "").strip() or "Hermes")


# TODO: Add provider-specific settings after choosing a model provider.
