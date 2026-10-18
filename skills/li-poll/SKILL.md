---
name: li-poll
description: >-
  Write LinkedIn polls that start an argument worth having and produce a result
  worth posting about - the question, the four options, the post text, and the
  follow-up post once the votes are in. Use when the user says "make a poll",
  "ask my audience", "poll idea", or wants to know what their network thinks.
---

# li-poll

Most polls are a question nobody has an opinion on, with a fourth option that
says "Other (comment below)". They get votes and no conversation. A good poll
is a disagreement your audience already has, made clickable.

## Before writing, ask

1. **What the user wants to learn**, or the argument they want to start. A
   poll that tests a real belief beats a poll for reach.
2. **Who should vote** - the poll is worthless if the wrong people answer it.
3. **What they will do with the result.** If nothing, the follow-up post is
   the reason to run it, so plan that now.

## The rules LinkedIn sets

- Question: **140 characters** max.
- Options: **2 to 4**, each **30 characters** max.
- Duration: 1 day, 3 days, 1 week or 2 weeks. Default to **1 week**.
- Count the characters and show the count for the question and every option.

## Writing the question

- **One variable.** "Which matters more for a first hire: skill or attitude?"
  not "What do you think about hiring?"
- **Make every option defensible.** If one option is obviously right, the poll
  is a quiz and nobody argues.
- **No "Other" or "It depends".** That is where the opinion goes to hide. The
  post text can invite the nuance in the comments.
- **Concrete over abstract.** Real numbers, real situations, real tradeoffs.

## The post text

The post above the poll does the work the poll cannot:

- State why you are asking, in one or two lines.
- Say your own answer, or say you will share it when it closes. Polls where
  the author takes a side get more comments.
- Invite the reason, not just the vote: "Vote, then tell me the case where
  your answer is wrong."

## The follow-up post

When the poll closes, the result is the content. Draft it as a `/li-post`:
the result as the hook, what surprised you, the best comments with credit,
and what you will change because of it. Note that poll voters are
self-selected followers, so the result is a signal, not a survey. Say that in
the post.

## Never

- Never present poll results as research or statistics about an industry.
- Never run engagement-bait polls ("Which emoji are you today?").
- Never vote, comment or post automatically. The user creates the poll in
  LinkedIn by hand.

## Output

```
POLL                                              duration: 1 week
Q   Which matters more for a first hire?                     [36/140]
1   Skill they already have                                  [23/30]
2   Speed they learn at                                      [19/30]
3   Who they have worked with                                [25/30]
4   How they handle being wrong                              [27/30]

POST TEXT
...

FOLLOW-UP (draft, fill in when the poll closes)
...
```

Post text and follow-up go through `/li-human` before the user sees them.
