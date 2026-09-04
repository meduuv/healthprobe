from collections.abc import Mapping

def healthy(check: Mapping[str, object]) -> bool:
    """Return whether a health result explicitly reports success."""
    status=str(check.get("status", "")).strip().lower()
    return status in {"ok", "healthy", "pass", "passed"}
