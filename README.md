<p align="center">
  <img src="assets/linkedin.svg" alt="LinkedIn" width="64" height="64">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/claude-code.svg" alt="Claude Code" width="64" height="64">
</p>

<h1 align="center">LinkedIn Agent Skill</h1>

<p align="center">
  <a href="https://claude.com/claude-code"><img src="https://img.shields.io/badge/Claude_Code-skills-D97757?logo=claude&logoColor=white" alt="Claude Code skills"></a>
  <img src="https://img.shields.io/badge/LinkedIn-content_agent-0A66C2" alt="LinkedIn content agent">
  <img src="https://img.shields.io/badge/skills-15-informational" alt="15 skills">
  <img src="https://img.shields.io/badge/python-no_dependencies-3776AB?logo=python&logoColor=white" alt="Python, no dependencies">
</p>

Fifteen Claude skills that run a LinkedIn account: posts, comments, replies,
profile, planning, DMs, inbox, carousels, repurposing, audits,
recommendations, newsletters, polls, job search, and a humanizer that strips
the AI fingerprint from every draft.

No signup, no API key, nothing to connect.

> **Nothing gets posted until you say yes.** These skills write. You post.

## Contents

- [Features](#features)
- [Installation](#installation)
- [Setup: your voice profile](#setup-your-voice-profile)
- [Skills](#skills)
- [The humanizer](#the-humanizer)
- [Design principles](#design-principles)
- [Project structure](#project-structure)
- [Development](#development)
- [Author](#author)

## Features

- **Posts from 21 hook formulas.** Three hook options and one full draft per idea.
- **Engagement that sounds like a person.** Comments and replies picked by what
  the post actually says, never "Great post!".
- **A profile score out of 100**, with rewrites in fix-first order.
- **A weekly plan** covering what to post, when, and who to engage with.
- **Outreach and inbox triage**, with connection notes, follow-ups and lead sorting.
- **Recommendations.** Write them, ask for them, and draft your own when asked.
- **Long-form and polls.** Newsletter issues with their share post, and polls
  built to start a real argument.
- **Job search.** Tailor to a posting, message the hiring manager, and track
  every application.
- **A humanizer that runs locally.** Two dependency-free Python scripts clean
  each draft and score it before you see it.

## Installation

### Option 1: let Claude do it

Paste this into Claude:

```
https://github.com/Muhammad-Ali-stack/Claude-Code-Linkedin-Agent

Install this skill, then confirm /li-post works.
```

### Option 2: Claude Code, manually

```bash
git clone https://github.com/Muhammad-Ali-stack/Claude-Code-Linkedin-Agent.git
cp -r Claude-Code-Linkedin-Agent/skills/li-* ~/.claude/skills/
```

To install for one project only, copy the same folders into that repo's
`.claude/skills/` instead.

### Option 3: as a plugin

```
/plugin marketplace add Muhammad-Ali-stack/Claude-Code-Linkedin-Agent
/plugin install linkedin-agent
```

### Without Claude Code

Paste any single `SKILL.md` at the top of a chat and it runs as a mode. You
lose the two Python tools used by `/li-human`, but everything else works.

## Setup: your voice profile

Every skill reads your voice profile. Without it, drafts sound like everyone
else's.

1. Copy [`templates/voice.md`](templates/voice.md) to `~/.claude/linkedin/voice.md`.
2. Fill it in. It takes about ten minutes.

Alternatively, paste three of your own posts into Claude and say
*"write my voice.md from these"*.

## Skills

| Command | What it does |
| --- | --- |
| `/li-post` | Turns one idea into a post: three hook options from [21 formulas](skills/li-post/hooks.json), one full draft, humanized. |
| `/li-comment` | Comments on other people's posts. Nine comment types, picked by what the post actually is. |
| `/li-reply` | Handles the thread under your own post. Sorts comments into lead / substance / peer / support / noise and replies in that order. |
| `/li-profile` | Scores your profile against a [12-part rubric](skills/li-profile/rubric.json) out of 100, then rewrites in fix-first order. |
| `/li-plan` | Plans the week: what to post, when, and the 10 people to engage with. Writes `~/.claude/linkedin/plan.md`. |
| `/li-human` | The humanizer. Cleans a draft and scores it on a five-check panel. See [below](#the-humanizer). |
| `/li-carousel` | Document posts: slide-by-slide copy, a cover that earns the swipe, and the PDF to upload. |
| `/li-repurpose` | Turns one video, newsletter or transcript into a week of standalone posts. |
| `/li-dm` | Writes the 200-character invite note, the first message, and two follow-ups. |
| `/li-inbox` | Triages the inbox into lead / recruiter / peer / ask / spam, and flags automated sequences. |
| `/li-audit` | A post-mortem on published posts, ranked by engagement rate and reach multiple rather than impressions. |
| `/li-recommend` | Writes recommendations you give, the message that asks for one, and your own draft when someone says "write it yourself". |
| `/li-newsletter` | Newsletter issues and articles: title, opener, a body built for long-form, the cover brief, and the share post. |
| `/li-poll` | Polls with character counts, four defensible options, the post above the poll, and the follow-up once votes are in. |
| `/li-job` | Job search: match your profile to a role, tailor to one posting, message the hiring manager, and track applications. |

## The humanizer

`/li-human` ships two Python scripts with no dependencies. They run on your
machine, and nothing is uploaded.

```bash
python3 humanize.py draft.txt --report      # clean the draft and list every change
python3 detect.py draft.txt                  # score it on five checks
python3 detect.py before.txt after.txt       # compare before and after
```

Both need Python 3.9 or newer and nothing else. On Windows, use `python`
instead of `python3`. `detect.py` exits with code 0 on PASS and 1 otherwise,
so it can gate a script or CI step. Add `--json` to either script for
machine-readable output.

### Fixed automatically

- **Invisible characters.** Zero-width spaces and joiners, word joiners, soft
  hyphens, byte-order marks, Unicode tag characters, and non-breaking and
  narrow spaces.
- **Typography.** Em dashes become commas, en dashes become hyphens, curly
  quotes become straight, and ellipses become three dots.
- **Stock vocabulary.** 113 overused words and phrases ("delve", "leverage",
  "seamless", "in today's fast-paced world") get plain-English replacements.
  Capitalisation is preserved and URLs are left alone. The list lives in
  [`slop.json`](skills/li-human/slop.json) and is meant to be edited.

### Flagged for you to rewrite

"It's not just X, it's Y" constructions, rule-of-three lists, one-word
rhetorical questions, hashtag walls, engagement bait, and uniform sentence
length. Fixing these takes judgement, so the script points them out instead of
forcing a regex rewrite.

### The five checks

Each check is scored 0-100, and higher means more human.

| Check | What it measures |
| --- | --- |
| BURSTINESS | Variation in sentence length |
| SPECIFICITY | Numbers, names and concrete details per 100 words |
| SLOP DENSITY | Stock-vocabulary hits per 100 words |
| FINGERPRINT | Invisible characters, em dashes and curly quotes per 1,000 characters |
| VOICE | Contractions, point of view and structural tells |

The final score weights the average at 60% and the **weakest single check** at
40%, because a detector only needs one signal to fire.

**Example: a deliberately bad draft**

```
  BURSTINESS    ##################......  73.0
  SPECIFICITY   ######################## 100.0
  SLOP DENSITY  ........................   0.0    19 stock terms, 24.1 per 100 words
  FINGERPRINT   ........................   0.0    1 invisible, 1 em dash, 3 curly quote
  VOICE         ########................  33.3    3 structural tells
  ------------------------------------------------------------
  HUMAN SCORE   ######..................  24.8   FLAGGED
```

**After `humanize.py`, with the flagged structures not yet rewritten:**

```
  HUMAN SCORE   #################.......  69.7   REVIEW    (+44.9)
```

The script leaves the last stretch to PASS for you to rewrite.

## Design principles

**No automated posting.** LinkedIn has no official API for posting to a
personal profile without an approved partner app. Automating the site with a
browser or a third-party tool violates the
[LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement) and
gets accounts restricted. Every skill ends with a copy-ready block that you
paste yourself.

**Local heuristics, not detector APIs.** The five checks are modelled on the
signals public AI detectors look for, and they run entirely on your machine.
They do not call GPTZero, Originality, Copyleaks, Winston or Turnitin, and they
cannot promise those tools' verdicts. Fixing what the checks measure tends to
improve those scores, because both measure the same underlying signals. No
tool can honestly promise "undetectable" text.

**A narrow fingerprint pass.** The invisible-character pass removes the
zero-width and formatting characters that end up in generated text and survive
copy-paste. It makes no claim about defeating cryptographic watermarking.

**Nothing is fabricated.** No invented metrics, clients or outcomes go out
under your name. If a draft needs a number you haven't provided, it comes back
with a `{{your number}}` placeholder and a flag.

## Project structure

```
.claude-plugin/                  plugin and marketplace manifests
skills/li-*/SKILL.md             one folder per skill
skills/li-post/hooks.json        21 hook formulas with templates, examples and failure modes
skills/li-human/slop.json        113 stock terms, 17 invisible-character classes, 11 structural tells
skills/li-human/humanize.py      the cleaning passes
skills/li-human/detect.py        the five-check scoring panel
skills/li-profile/rubric.json    the 100-point profile rubric
templates/voice.md               your voice profile (fill this in first)
assets/                          logos used in this README
tests/                           unit tests for the scripts and the skill files
```

## Development

The tests use only the Python standard library:

```bash
python -m unittest discover -s tests -v
```

They cover the cleaning passes, the scoring panel, both command-line tools
(including on a Windows console), and checks that every skill folder has a
valid `SKILL.md`, appears in this README, and that every JSON file parses.
They run on Linux and Windows for each push via GitHub Actions.

## Author

Created and maintained by **Muhammad Ali**.
