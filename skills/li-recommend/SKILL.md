---
name: li-recommend
description: >-
  Write LinkedIn recommendations for other people, ask for them the right way,
  and reply when someone writes one for you. Use when the user says "write a
  recommendation for", "recommend my colleague", "ask for a recommendation",
  "my manager asked me to draft my own recommendation", or wants more social
  proof on their profile.
---

# li-recommend

A recommendation is the only part of a profile the owner did not write. That
is the whole value, and it is why "a pleasure to work with, highly
recommended" is worth nothing. Nobody believes a sentence that could sit under
anyone's name.

## Three modes

Work out which one the user is in before writing anything.

1. **Give** - the user is recommending someone else.
2. **Ask** - the user wants a recommendation from someone.
3. **Draft-my-own** - someone asked the user to write the first draft of their
   own recommendation. This is common and it is allowed. Write it as the other
   person, in their voice, and flag that they must edit it before posting.

## Before writing, get the specifics

Ask for, in one batched question:

1. **The relationship** - manager, report, peer, client, vendor. LinkedIn
   shows it, so the text has to match it.
2. **How long, and on what** - the project, the team, the dates.
3. **One moment** - a specific thing the person did, with the result if there
   was one. "Rebuilt the onboarding flow in three weeks and support tickets
   halved" beats any adjective.
4. **What they want to be hired for next** - a recommendation is read by the
   person's next employer or client, not their last one. Point it there.

If the user cannot name one specific moment, say so. A recommendation with no
moment in it is the one everyone skims.

## The shape (Give and Draft-my-own)

```
{how you know them, in one line} + {the moment} + {what it showed} + {who should hire them}
```

- **80 to 150 words.** Longer gets skimmed, shorter reads as a favour.
- **Open with the relationship, not with praise.** "I managed Priya for two
  years on the payments team" earns the rest of the paragraph.
- **One moment, told properly.** What was wrong, what they did, what changed.
- **One trait, proven by the moment.** Not five traits in a list.
- **End forward.** "If you need someone to own a messy migration, hire her."
- **Never** "it is with great pleasure", "I cannot recommend X highly
  enough", "a true asset to any team", "goes above and beyond", or "rockstar".

```
I managed Priya for two years on the payments team at Northwind. In 2025 our
checkout was failing for about 3% of card payments and nobody could say why.
She spent a week reading logs nobody else wanted to read, found a timeout in
a vendor SDK, and shipped the fix with a test that would have caught it. The
failure rate went to near zero and stayed there. That is how she works: she
goes and finds out. If you need someone to own a problem everyone else has
written off, hire her.
                                                            [96 words]
```

## The ask

People say yes to a recommendation request when it is easy, specific and
reciprocal.

- **Ask people who saw the work directly.** A manager or a client beats a
  famous name who barely knew you.
- **Make it easy:** remind them of the project and the one moment you hope
  they mention. Offer a draft they can rewrite.
- **Offer one back**, and mean it. Write theirs first if you can.
- **Ask in a DM, not through the bare LinkedIn request button.** The default
  request has no context and gets ignored.
- **One follow-up after a week, then let it go.**

```
Hi Dan - I am updating my profile as I look for my next ops role. Would you
be up for writing a short recommendation about the Q3 vendor consolidation?
The part I think mattered most was getting the 14 contracts down to 5 without
losing a supplier. Happy to send a rough draft if that saves you time, and I
would gladly write one for you too.
```

## Replying to one you received

Thank them in a DM, not just a reaction. One line on what it meant, and offer
one back if they do not already have one from you. Then decide whether to show
it: a recommendation that does not point toward what the user wants next can
stay hidden.

## Never

- Never invent a project, a result, a date or a number. If the user has not
  given one, the draft comes back with `{{the result}}` in it and a flag.
- Never write a recommendation for someone the user has not actually worked
  with, and never draft a batch of swap recommendations between people who
  have not. LinkedIn treats fake endorsements as a violation of its User
  Agreement, and readers can tell.
- Never post or request anything on the user's behalf through a browser or a
  third-party tool.

## Output

The recommendation or the ask, with its word count, plus a one-line note on
the moment you chose and why. Humanized through `/li-human` before the user
sees it - a recommendation with an em dash and "seamlessly" in it reads as
generated, and so does the person who posted it. The user sends it by hand.
