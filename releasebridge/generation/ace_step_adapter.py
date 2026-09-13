from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class GenerationRequest:
    prompt: str
    output_path: Path
    duration_seconds: int = 240
    bpm: Optional[int] = 124
    key: Optional[str] = None
    instrumental: bool = True
    seed: Optional[int] = None


class AceStepAdapter:
    """Thin boundary around ACE-Step generation.

    Keep ReleaseBridge orchestration isolated from upstream ACE-Step internals.
    The concrete invocation will be wired against the installed ACE-Step API/CLI
    after runtime setup is confirmed.
    """

    def generate(self, request: GenerationRequest) -> Path:
        request.output_path.parent.mkdir(parents=True, exist_ok=True)
        raise NotImplementedError(
            "ACE-Step runtime invocation is not wired yet. "
            "Configure the local/server runtime first."
        )
