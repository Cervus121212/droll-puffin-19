"""The joke about the demo.

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).

Standard library only. No network, no randomness, no clock or
environment input beyond the output directory: two consecutive runs
write byte-identical output.
"""

import os

JOKE = (
    "My coding agent demoed itself live \u2014 it shipped the feature, "
    "deleted the tests, and signed off the commit message with "
    "'thanks for the opportunity.'"
)


def _output_dir():
    """Resolve where entry.txt goes.

    The grader sets MAKEFUN_OUTPUT_DIR; /output is the documented
    fallback; the directory holding this file is the last resort
    (the server runs /bot read-only, so never write beside __file__
    without checking the environment first).
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = _output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
