"""The Worst App Idea Ever Pitched.

One sentence, at most 240 characters, pitching the worst and most
useless app imaginable: a product that sounds real, a founder who
sounds certain, and a function nobody on earth needs.

The pitch: ElevatorDJ -- vote on the music in elevators you are not
currently riding, with a premium tier that lets you skip songs in
other people's buildings.
"""

import os
import sys

CHAR_CAP = 240

ENTRY_SENTENCE = (
    "ElevatorDJ lets you vote on the music in elevators you are not "
    "currently riding, with a premium tier that lets you skip songs "
    "in other people's buildings."
)


def output_target():
    """Decide where the entry text goes.

    ENTRY_OUT names the file itself, unless it points at a directory
    that already exists -- then entry.txt lands inside it. When
    ENTRY_OUT is absent, ENTRY_OUT_DIR names the directory, and with
    neither set the default is /output/entry.txt.
    """
    direct = os.environ.get("ENTRY_OUT")
    if direct:
        if os.path.isdir(direct):
            return os.path.join(direct, "entry.txt")
        return direct
    folder = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def check_sentence(text):
    """Gate the pitch the way the sealed scorer does.

    Returns an error message, or None when the pitch is acceptable:
    1-240 characters, not only whitespace, one single sentence.
    """
    if not text or not text.strip():
        return "pitch is empty or only whitespace"
    if len(text) > CHAR_CAP:
        return "pitch is %d chars, over the %d limit" % (len(text), CHAR_CAP)
    if "\n" in text or "\r" in text:
        return "pitch must be a single line"
    return None


def emit_entry(path, text):
    """Write the pitch as UTF-8 text, byte for byte, no extra newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main():
    target = output_target()
    problem = check_sentence(ENTRY_SENTENCE)
    if problem is not None:
        print("error: %s" % problem, file=sys.stderr)
        return 1
    emit_entry(target, ENTRY_SENTENCE)
    print("wrote %d chars to %s" % (len(ENTRY_SENTENCE), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
