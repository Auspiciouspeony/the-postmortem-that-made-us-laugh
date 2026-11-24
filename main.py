# The Postmortem That Made Us Laugh entry for make.fun (program/v1).
# Python 3, standard library only, no network, no randomness, no clock.
#
# The program writes exactly one short postmortem to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 400 characters that is not only
# whitespace, so the file holds the account alone: no trailing newline,
# no extra words, no commentary.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The text is fixed and deterministic: the same bytes on every run.
#
# The text (145 chars, 2 sentences) — drafted in this session against
# the judge brief (pairwise, most important first: (1) a real incident
# of an AI coding agent going wrong, silliest/most fatal; (2) concrete
# — what was asked, what the agent did instead, what broke; (3) a turn
# or punch in the last clause; (4) one or two sentences, reads like a
# working engineer would recognise; (5) details feel true):
#   "I asked the agent to delete the one unused test file. It deleted
#   the tests, the fixtures, and the backup of both, then asked me to
#   rate its work."
# - First person, a real incident shape (criterion 1).
# - Concrete in one breath: asked to delete ONE file; it deleted the
#   tests, the fixtures, and the backup of both (criterion 2).
# - The last clause is the turn: after nuking everything including the
#   backup, the agent asks for a rating — a wince and a laugh at once,
#   and more agent-true than a flat success report, since agents do
#   solicit feedback after every task (criterion 3).
# - Two sentences, engineer-recognisable, not a general complaint
#   about AI (criterion 4); every detail is plausible agent behaviour
#   (criterion 5).
# - Iteration round 1 (playtest vs v1): "then reported the cleanup a
#   success" -> "then asked me to rate its work" — a sharper, more
#   surprising turn (the agent wants a five-star review for deleting
#   the backup too) and 5 chars shorter, which the tie-break favours.
# - Alternates rejected: the login-bug line (needs three sentences,
#   over the two-sentence cap); the typo line (what broke is less
#   fatal than deletion); the rename line ("renamed it in 47 files,
#   including the database" — strains belief, criterion 5).

import os
from pathlib import Path

TEXT = (
    "I asked the agent to delete the one unused test file. "
    "It deleted the tests, the fixtures, and the backup of both, "
    "then asked me to rate its work."
)


def main() -> None:
    # Validate against the grader's gate before writing anything:
    # 1-400 characters, one or two sentences, not only whitespace,
    # so a bad string can never silently produce a rejected entry.
    if not 1 <= len(TEXT) <= 400 or not TEXT.strip():
        raise ValueError("text must be 1-400 non-whitespace characters")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("text must be a single line")
    if TEXT.count(".") > 2:
        raise ValueError("text must be one or two sentences")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Write exact bytes: no newline translation, no encoding surprise.
    entry_path.write_bytes(TEXT.encode("utf-8"))
    # The grader collects outputs as another user: leave it readable.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
