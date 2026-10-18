---
name: li-newsletter
description: >-
  Write LinkedIn newsletter issues and long-form articles - the title, the
  subscriber-facing opener, the body, and the share post that announces it.
  Use when the user says "write my newsletter", "turn this into an article",
  "LinkedIn article", "next issue", or wants to go deeper than a post allows.
---

# li-newsletter

A post is read in the feed. A newsletter issue lands in an inbox and a
notification, which means the reader chose it. That raises the bar: an issue
that could have been a post is a broken promise to everyone who subscribed.

## Before writing, get the specifics

Ask for, in one batched question:

1. **The newsletter** - its name and what it promises subscribers. If this is
   the first issue, help write that one-line promise first, because every
   issue gets judged against it.
2. **The one idea** for this issue, and why now.
3. **The material** - notes, a transcript, a post that did well, data, a story.
   The best issue is usually a post that worked, taken three levels deeper.
4. **The ask** - what the reader should do at the end, if anything.

## The shape

```
TITLE         under 60 characters, specific, reads fine without the subtitle
SUBTITLE      the promise of this issue in one sentence
OPENER        3-5 lines that earn the scroll - a scene, a number, or a claim
BODY          3-5 sections with plain-language subheads
CLOSE         the one thing to remember, then the ask
```

- **800 to 1,500 words.** Shorter is a post. Longer needs a reason.
- **Subheads say something.** "Why the second hire is harder" beats "Challenges".
- **One idea per issue.** A roundup of five ideas is a list, not an issue,
  unless the newsletter promised roundups.
- **Use the full width of the format**: a table, a short numbered process, a
  pulled quote, a screenshot the user supplies. Things a post cannot hold.
- **Paragraphs of 1 to 4 sentences.** It is read on a phone.

## The cover and the share post

LinkedIn shows a cover image and a share post in the feed when the issue goes
out. Give the user:

- **Cover image brief** - one line of text for the image, under 8 words, and
  what the image should show. Do not generate stock-photo descriptions.
- **The share post** - written as a post in its own right, using a hook from
  `/li-post`. "New issue is out!" gets no clicks. Give the best idea from the
  issue away in the share post, and the click comes from wanting the rest.

## Series memory

Keep `~/.claude/linkedin/newsletter.md` with the newsletter's promise and one
line per issue: date, title, the idea. Read it before writing so issues do
not repeat, and so a new issue can point back to an old one when it builds on
it.

## Never

- Never pad to hit a word count. If the idea is a post, say so and hand it to
  `/li-post`.
- Never invent data, quotes, sources or case studies. Missing evidence comes
  back as `{{source}}` with a flag.
- Never publish. The user pastes the issue into LinkedIn's editor and presses
  send themselves.

## Output

Title, subtitle, the full issue in markdown, the cover image brief, and the
share post. All of it run through `/li-human` before the user sees it -
long-form is where the slop vocabulary piles up, because there is more room
for it.
