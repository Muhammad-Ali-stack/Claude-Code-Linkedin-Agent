---
name: li-network
description: >-
  Grow a personal LinkedIn network on purpose - decide who to connect with,
  build a short list of people worth knowing, and keep in touch with the ones
  who matter without being a pest. Use when the user says "grow my network",
  "who should I connect with", "I only know my colleagues", "how do I network
  on LinkedIn", "reconnect with old contacts", or "I just moved into a new
  field".
---

# li-network

A big network is not the goal. The goal is the 50 to 150 people who would
reply if you messaged them tomorrow. Most people collect connections and
never talk to them, which is the same as not having them.

## Before planning, ask

1. **The goal** - a new job, clients, moving into a new field, learning from
   seniors, or a local community. One at a time.
2. **The field and place** - role, industry, city or remote.
3. **The starting point** - roughly how many connections, and who they are
   (classmates, colleagues, random).
4. **Time** - realistic minutes per week. Fifteen is enough.

## Build the list

Write `~/.claude/linkedin/network.md` with four groups, 5 to 10 names each.
The user finds the people; this skill tells them where to look and why:

| group | who | where to find them |
| --- | --- | --- |
| **Peers** | same role, 0-3 years ahead | people commenting on the same posts, alumni, past colleagues |
| **Seniors** | 5-10 years ahead in the target role | speakers, writers, hiring managers at target companies |
| **Bridges** | people who know many others in the field | community organisers, recruiters in the niche, newsletter writers |
| **Old ties** | people the user already knows but lost touch with | former classmates, managers, teammates |

Old ties are the most valuable and the most ignored. A reply rate from
someone who knows you is many times higher than from a stranger.

## The weekly routine (15 minutes)

1. **Comment on 3 posts** from people on the list, through `/li-comment`.
   Comments come before connection requests. A name they recognise gets
   accepted.
2. **Send 3 to 5 connection requests**, each with a note through `/li-dm`.
   Never more than 20 in a week while the account is small.
3. **Message 1 old tie** with a real reason: congratulate a milestone, share
   something useful, or ask a small question. No "long time no see, let's
   catch up" with nothing after it.
4. **Log it** in `network.md`: name, date, what was said, what is next.

## Keeping in touch

- **Give before asking.** An intro, an article that fits their problem, a
  public mention of their work.
- **Every 2 to 3 months** is enough for most of the list. Use the log to see
  who is overdue.
- **When you do ask, make it small and specific.** "Could you tell me how
  your team hires juniors?" gets answered. "Can you help me find a job?" does
  not.

## Never

- Never use connection-growth tools, auto-invite extensions or "pods".
  Automation breaks LinkedIn's User Agreement and gets accounts restricted.
- Never add people in bulk with no note, and never send a pitch as the first
  message after someone accepts.
- Never scrape profiles or export other people's contact details.

## Output

The four-group list template with where to look for each group, the weekly
routine with this week's first actions, and any notes or messages the user
asked for, run through `/li-human`. The user sends everything by hand.
