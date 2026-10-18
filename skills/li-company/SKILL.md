---
name: li-company
description: >-
  Run a LinkedIn Company Page - the page About and tagline, page posts that
  people actually engage with, the employee-share kit, and a monthly page
  plan. Use when the user says "company page", "our business page", "post for
  my company", "nobody follows our page", "get employees to share", or manages
  LinkedIn for a brand, startup or agency rather than for themselves.
---

# li-company

People follow people. A company page posting "We are thrilled to announce" to
300 followers reaches almost nobody. The page still matters - it is where
candidates, clients and investors check you are real - but it works when it
sounds like the people inside it, and when those people carry its best posts
to their own networks.

## Before writing, get the specifics

Ask for, in one batched question:

1. **The company** - what it sells, to whom, and the one thing it does that
   competitors do not. Read `~/.claude/linkedin/company.md` if it exists.
2. **The page's job right now** - hiring, sales, trust before a raise, or
   launching something. One job at a time.
3. **The people** - founder and two or three team members who post, or would.
4. **What is true and shareable** - real launches, numbers, customer stories
   the company has permission to name. Nothing invented.

Save the answers to `~/.claude/linkedin/company.md` so the next run starts
from them.

## 1. The page itself

- **Tagline (120 characters).** What you do and for whom, in words a customer
  uses. "Payroll for 10-50 person teams in Pakistan" beats "Empowering the
  future of work".
- **About, first two lines.** The same promise, plus one piece of proof. Under
  1,000 characters in total, ending with how to start (site, demo, careers).
- **Custom button.** Pick the one that matches the page's job: Visit website,
  Contact us, or Learn more. Not all three in rotation.
- **Banner.** One line of positioning and the website. Not a stock skyline.

Show a character count on the tagline and About.

## 2. Page posts that work

Page posts follow `/li-post` rules, with three changes:

- **Write as "we", in a human voice.** Name the person who did the thing.
  "Ayesha rebuilt our onboarding and support tickets fell by a third" beats
  "Our team is proud to share".
- **Show the inside.** Behind-the-scenes, how a decision was made, what went
  wrong, a customer in their own words. Polished announcements are the weakest
  format a page can post.
- **Two to three posts a week is enough.** Daily page posts train followers to
  scroll past.

The formats, strongest first: team spotlight with a real result, customer
story with permission, a lesson from building the product, a hiring post
written by the hiring manager, and only then the announcement.

## 3. The employee-share kit

The page's best post should not live only on the page. For each one, write:

- **Two or three short personal versions** the founder and team can post from
  their own profiles, each from that person's angle, not the same text pasted
  three times. Identical reshares look coordinated because they are.
- **One comment** the team can leave on the page post, in their own words.

Sharing is always optional. Never write anything that pressures staff to post,
and never draft posts that pretend an employee experienced something they did
not.

## 4. The monthly plan

Write `~/.claude/linkedin/company-plan.md`: eight to twelve page posts for the
month, each with the format, the person featured, the date, and who will
reshare it. Leave room for one post that reacts to something real that month.

## Never

- Never invent customers, logos, metrics, awards or testimonials. Missing
  proof comes back as `{{customer quote}}` or `{{number}}` with a flag.
- Never open with "We are thrilled", "We are excited to announce", "Proud
  to share", or "Big news". They are invisible.
- Never post, schedule or reshare through a browser tool or a third-party
  automation. The page admin pastes each post into LinkedIn by hand.

## Output

Whichever parts the user asked for, as copy-ready blocks with character
counts on every field LinkedIn limits. Every post, tagline and About goes
through `/li-human` first - a company page full of "seamless" and "cutting-
edge" reads as a template, and so does the company.
