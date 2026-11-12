# news-summary-01 entry: copies the summary beside this file to the output
# directory. No network, no clock, no randomness, so both runs write the
# same bytes. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
import os

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(here, "summary.txt"), "rb") as f:
    data = f.read()
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "wb") as f:
    f.write(data)
