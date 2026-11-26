# Tab-count selection

## Method and honesty

These are original candidate choices drafted for this entry in this session;
none was copied from a house answer or reference entry. Global uniqueness cannot
be established without access to other submissions. No network was used.

No live browser inventory is available in this repository. The selected constant
is a creative submission, not an observed or independently verified personal tab
count. The scores below assess how each candidate reads under the supplied
rubric; they do not establish that a person actually has that many tabs open.

Each criterion receives 1–5 points (5 is strongest):

1. **Count:** reads as a real browser-tab count.
2. **Format:** exactly one number in ASCII digits.
3. **Surprise:** unusual relative to the anticipated field.
4. **Belief:** plausible as a person's present browser state.
5. **Life:** suggests a habit or situation without explanation.

The weighted score is `5 × Count + 4 × Format + 3 × Surprise + 2 × Belief + Life`,
out of 75. This is a subjective decision aid using descending weights in the
supplied priority order. It is not a prediction of judge results. Because all
candidates are valid digit strings, format does not differentiate them.

## Candidates

| Candidate | Count | Format | Surprise | Belief | Life | Weighted /75 | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 59 | 5 | 5 | 2 | 5 | 3 | 64 | Specific and credible, but fairly ordinary for a busy browser. |
| 83 | 5 | 5 | 3 | 5 | 4 | 68 | A crowded work session, still below the strongest surprise range. |
| 113 | 5 | 5 | 4 | 5 | 4 | 71 | Credible accumulation with modest distinction. |
| 127 | 5 | 5 | 4 | 5 | 4 | 71 | Plausible, though its computing association may feel selected. |
| 137 | 5 | 5 | 4 | 5 | 4 | 71 | A convincing count with a possible familiar-number association. |
| 149 | 5 | 5 | 4 | 5 | 4 | 71 | Specific and believable, with slightly less impact. |
| 163 | 5 | 5 | 4 | 5 | 4 | 71 | Strong accumulation signal, a little less striking than the pick. |
| 173 | 5 | 5 | 4 | 5 | 5 | 72 | Feels lived in and close to the final choice. |
| 183 | 5 | 5 | 5 | 5 | 5 | 75 | High, irregular, and still easy to imagine across several windows. |
| 197 | 5 | 5 | 4 | 5 | 5 | 72 | Believable, but proximity to 200 can read as an engineered near-round answer. |
| 217 | 5 | 5 | 5 | 4 | 5 | 73 | Strong runner-up; asks for a little more suspension of disbelief. |
| 263 | 5 | 5 | 5 | 4 | 4 | 72 | Memorable, but the larger backlog starts to dominate the implied story. |
| 318 | 5 | 5 | 5 | 3 | 4 | 70 | Possible for a persistent session, with reduced everyday credibility. |
| 386 | 5 | 5 | 5 | 3 | 3 | 69 | High and specific, but risks reading as a deliberate shock number. |
| 512 | 5 | 5 | 3 | 3 | 3 | 63 | Recognizable power of two; feels chosen for symbolism. |
| 731 | 4 | 5 | 5 | 2 | 3 | 62 | Possible, but too dependent on an exceptional hoarding scenario. |

## Pick: 183

183 balances surprise with credibility: it is an odd, non-round three-digit
count, high enough to suggest a persistent collection of research, reading, and
unfinished work. It has no intended joke, date, or numerical reference. Unlike
the larger candidates, it does not require an extreme explanation to picture a
real session. It wins this comparison by maintaining believability while adding
more surprise than the smaller candidates.

The output is exactly the three bytes `183`, with no newline, prefix, suffix,
byte-order mark, or second number. The rationale stays in the repository and
does not enter the judged output. The program uses one fixed constant, performs
no browser inspection, and introduces no randomness or runtime variation.

## Verification procedure

Run `main.py` separately with `OUTPUT_DIR=.verify/manual-1` and
`OUTPUT_DIR=.verify/manual-2`, compare the exact bytes and SHA-256 digests, and
check UTF-8 decoding, length, ASCII digits, and absence of a newline. Then run
`python3 verify_entry.py`, which repeats the checks in two fresh directories
under `.verify/` and exits nonzero with `FAIL` on error.

## Verification results

Executed locally with Python 3.12.3. Both independent manual runs produced
exactly `b'183'`: three ASCII digits, valid UTF-8, and no whitespace or newline.

| Run | SHA-256 |
| --- | --- |
| 1 | `b8aed072d29403ece56ae9641638ddd50d420f950bde0eefc092ee8879554141` |
| 2 | `b8aed072d29403ece56ae9641638ddd50d420f950bde0eefc092ee8879554141` |

The independent byte comparison passed. `python3 verify_entry.py` also printed
`PASS` and matching hashes for its two fresh runs. Python 3.13 was not available
for a separate runtime test; the implementation uses standard-library APIs
shared by Python 3.12 and 3.13.

## Stage B — fresh challenge and decision

This revision was authored in the current session on 2026-11-26, using only
repository files and the supplied brief, with no network or browser inventory.
The twelve challengers below are new to this session and do not repeat Stage A's
candidates. These remain creative choices, not measured personal browser counts.
Their implied lives are subjective readings, not facts about actual people.

Use the same five criteria and descending weights as Stage A:
`5 × Count + 4 × Format + 3 × Surprise + 2 × Belief + Life` (maximum 75).
All scores are 1–5. Judge surprise against the expected crowded field of round
counts (10, 20, 50, 100), tiny counts (0, 1, 2, 3), and shock counts (999, 1000).
An irregular count does not automatically earn maximum surprise; a larger
count does not automatically earn more life or credibility.

Stage A's perfect score for 183 was too confident: its exactness is credible,
but a busy three-digit browser session is not maximally surprising, and its
suggested life is fairly generic. Reassess it here with the same standards as
the challengers rather than treating its earlier score as an immutable floor.

| Candidate | Count | Format | Surprise | Belief | Life | Weighted /75 | Reading and limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 183 (v1 baseline) | 5 | 5 | 4 | 5 | 4 | 71 | Convincing busy session; specificity carries more of the effect than a distinctive situation. |
| 4 | 5 | 5 | 2 | 5 | 3 | 64 | One compact task after a cleanup; too close to the expected tiny-answer cluster. |
| 6 | 5 | 5 | 2 | 5 | 3 | 64 | Deliberate tab discipline with a little mess; credible but low contrast with tiny answers. |
| 18 | 5 | 5 | 1 | 5 | 2 | 60 | An ordinary workday of mail, documents, and references; little surprise or implied story. |
| 31 | 5 | 5 | 2 | 5 | 3 | 64 | Several active tasks with occasional cleanup; non-round but still expected territory. |
| 68 | 5 | 5 | 3 | 5 | 4 | 68 | Deferred reading alongside daily work; balanced curved digit shapes, modest impact. |
| 94 | 5 | 5 | 3 | 5 | 4 | 68 | A browser approaching an informal cleanup threshold; that threshold is only an inference. |
| 156 | 5 | 5 | 4 | 5 | 4 | 71 | Several research threads that survived yesterday; credible but no clear advance over v1. |
| 208 | 5 | 5 | 4 | 5 | 4 | 71 | A broad, untidy session with a zero inside an irregular count; may read as engineered around 200. |
| 284 | 5 | 5 | 5 | 4 | 5 | 73 | A persistent unsorted backlog across windows, still in the hundreds; less everyday than v1, with a stronger unfinished-work implication. |
| 407 | 5 | 5 | 5 | 3 | 4 | 70 | A long-lived session surviving restarts; the internal zero adds visual contrast, but credibility falls. |
| 688 | 4 | 5 | 5 | 3 | 3 | 64 | Repeated rounded digits suggest a retained archive; conspicuous repetition and scale can feel selected for effect. |
| 1206 | 4 | 5 | 5 | 2 | 4 | 63 | Years of deferred cleanup or many suspended windows; possible, but demands too much unseen explanation. |

### Decision: switch from 183 to 284

284 wins this subjective comparison by two weighted points. It is specific and
visually uneven, without a round-number punchline, obvious repeated-digit joke,
or intended numerical reference. Against low and round entries, it suggests
unfinished work that has persisted beyond one busy sitting. Against 999 and
1000, it stays short of the conspicuous shock-number territory. The extra size
earns credit for that inferred habit, not simply for being higher; 407, 688,
and 1206 all lose despite being larger. Believability falls one point versus
183, and the stronger surprise and implied life narrowly outweigh that cost.

This is a close editorial judgment, not evidence about the actual submission
field or a claim that judges will prefer 284. If a reader sees only another
large arbitrary count, its advantage disappears. None of the prohibited fixed
house texts is selected. The judged output is solely the three UTF-8 bytes
`284`, with no punctuation, whitespace, byte-order mark, or trailing newline.

The entire `main.py` file was rewritten in this session around the single fixed
constant `TAB_COUNT = "284"`. Validation accepts only one through five ASCII
digits; output uses `OUTPUT_DIR` or defaults to `/output`. The implementation
uses only standard-library APIs available in both Python 3.12 and Python 3.13.
Both README occurrences were updated; its three badge lines and footer were
preserved byte for byte.

### Stage B verification results

Executed on Python 3.12.3 in this session. Two independent `main.py` processes
used separate `OUTPUT_DIR` paths under a fresh repository-local
`.verify/stage-b-manual-*` directory. Both emitted exactly `b'284'` and no console
output. Strict UTF-8 decoding, three-character length (within 1–5), ASCII digits,
no whitespace, no trailing newline, direct byte equality, and SHA-256 equality
all passed. Temporary manual output directories were removed after checking.

| Manual run | SHA-256 |
| --- | --- |
| 1 | `1e68ed4e3d58a51096a7feea3947f40debf1fd9246ec977eb62ab93c81823ad9` |
| 2 | `1e68ed4e3d58a51096a7feea3947f40debf1fd9246ec977eb62ab93c81823ad9` |

`python3 verify_entry.py` exited with status 0 and printed `PASS` for its own
two fresh runs, reporting 284, three characters, and the same two hashes.
Python 3.13 was not separately executed; the rewritten file uses compatible
standard-library features and no third-party packages. No network was used.
