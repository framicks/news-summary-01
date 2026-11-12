# news-summary-01 entry: copies the summary beside this file to the output
# directory. No network, no clock, no randomness, so both runs write the
# same bytes. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
import os

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(here, "summary.txt"), "rb") as f:
    data = f.read()
text = data.decode("utf-8")
if not (1 <= len(text) <= 2000) or not text.strip():
    raise SystemExit("summary.txt must hold 1-2000 characters, at least one not white space")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "wb") as f:
    f.write(data)
