---
name: li-job
description: >-
  Run a job search on LinkedIn - match the profile to a target role, write the
  note to a recruiter or hiring manager, tailor the application to one posting,
  and write the "I'm looking" post. Use when the user says "I'm job hunting",
  "help me apply", "message this recruiter", "open to work", "tailor my profile
  to this job", or pastes a job description.
---

# li-job

Applying through the button is the lowest-odds way to get a job on LinkedIn.
The posting gets hundreds of applicants in a day. A short, specific message to
the person who owns the hire gets read. This skill does the parts that move
the odds and leaves the volume game to everyone else.

## Before anything, get the target

Ask for, in one batched question:

1. **The role** - title, level, and two or three companies they would love.
2. **The job description**, if there is a specific posting. Pasted text, not
   a URL - do not scrape LinkedIn.
3. **The proof** - three results from past work they can stand behind, with
   numbers if they have them. Read `~/.claude/linkedin/voice.md` first; the
   proof section may already be there.
4. **Constraints** - location, remote, notice period, and whether the current
   employer can know. If they cannot, never suggest the public #OpenToWork
   frame; LinkedIn has a recruiters-only setting for that.

## The four jobs

### 1. Match the profile to the role

Pull the 8-12 words and skills the job descriptions repeat. Compare against
the headline, About and recent experience. Return the gaps, then hand the
rewrite to `/li-profile` with the target role as context. The headline should
name the role they want, not only the one they have.

### 2. Tailor to one posting

For a single job description, give:

- **The three requirements that matter**, read from the description - usually
  the ones repeated or listed first, not the full list.
- **One line of proof for each**, from the user's real results.
- **The gaps**, honestly, and whether they are dealbreakers. Do not tell the
  user to apply for everything.

### 3. The message to the human

Find out who owns the hire: the hiring manager is better than the recruiter,
the recruiter is better than the button. Then write, through `/li-dm` rules:

```
{the role, by name} + {one result that maps to their top requirement} + {one small ask}
```

Under 300 characters for a connection note, 4 sentences for a message. The
ask is small: "Is this still open, and are you the right person to talk to?"
Never attach a CV unrequested in the first message.

### 4. The "I'm looking" post

Only if the user can search publicly. Hook from `/li-post`, then: the role
and level wanted, the proof in two lines, the kind of team, and the specific
ask ("an intro to anyone hiring a platform lead in Toronto"). Specific posts
get shared. "Open to new opportunities!" gets sympathy likes.

## Tracker

Keep `~/.claude/linkedin/jobs.md` - one line per application: date, company,
role, who was contacted, status, next follow-up date. One follow-up after five
working days, with something new. Then let it go.

## Never

- Never invent experience, titles, dates, degrees or numbers, and never
  stretch a result past what the user said. Missing proof comes back as
  `{{your result}}` with a flag. A CV claim that breaks in an interview costs
  more than the gap did.
- Never auto-apply, scrape job listings, or send messages in bulk. Automated
  activity violates LinkedIn's User Agreement and gets accounts restricted.
- Never write a message that pretends to a connection or a referral the user
  does not have.

## Output

Whichever of the four the user asked for, with character counts on anything
going into a LinkedIn field. Every message and post is humanized through
`/li-human` - recruiters read hundreds of AI-written notes a week and they
can spot the em dash from across the room. The user sends everything by hand.
