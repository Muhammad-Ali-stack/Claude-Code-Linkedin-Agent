---
name: li-interview
description: >-
  Prepare for an interview using the job description and the interviewer's
  LinkedIn profile - likely questions, stories from the user's real
  experience, questions to ask them, and the thank-you message after. Use
  when the user says "I have an interview", "prepare me for this interview",
  "what will they ask", "research my interviewer", "mock interview", or
  "write a thank-you note after my interview".
---

# li-interview

LinkedIn tells you more about an interview than most candidates use: who the
interviewer is, what they posted last month, what the team ships, and who
held the job before. This skill turns that into a plan, from the user's real
experience only.

## Before preparing, ask for

1. **The job description**, pasted.
2. **The interviewer's profile** - headline, about, current role, and any
   recent posts, pasted or as a screenshot. Do not scrape LinkedIn or open
   the profile on the user's behalf.
3. **The company** - its LinkedIn page About and recent posts, pasted.
4. **The user's experience** - their profile, CV, or `~/.claude/linkedin/voice.md`.
5. **The interview type** - recruiter screen, technical, hiring manager,
   final, and how long.

## The prep sheet

```
1. WHAT THEY CARE ABOUT     the 3 requirements that matter, from the job description
2. WHO YOU ARE TALKING TO   the interviewer's background, what they posted, a natural opener
3. LIKELY QUESTIONS         8-10, tied to the requirements and the interview type
4. YOUR STORIES             4-5 stories from your real work, each mapped to questions
5. QUESTIONS FOR THEM       3-4, specific to the team and the interviewer
6. RED FLAGS TO PREPARE FOR gaps, job changes, a missing skill, and an honest answer to each
```

**Stories** use a short STAR shape: situation in one line, the task, what the
user did (the longest part), and the result with a number if there is one.
Each story should answer two or three different questions.

**Questions for them** should show the user did the homework: "Your post on
moving to event-driven billing said the hard part was retries. Is that still
the main problem the team is solving?" Never "What does a typical day look
like?" as the only one.

## Mock interview

If the user asks, run it: one question at a time, wait for their answer,
then give short feedback - what landed, what to cut, and a tighter version
of their own answer. Do not answer for them first.

## After the interview

Write the thank-you message for LinkedIn or email, within 24 hours:

- Three to five sentences.
- Thank them for one specific thing from the conversation.
- Add one thing the user wished they had said, briefly.
- No pleading, no "I would be a perfect fit".

Connect with the interviewer only after the process ends or if they offer.

## Never

- Never invent experience, results or stories. If the user has no story for
  a requirement, say so and help them answer the gap honestly.
- Never use the interviewer's personal details beyond their public
  professional profile and posts.
- Never write answers meant to be read out during a live interview.

## Output

The prep sheet, then the mock interview or the thank-you message if asked.
The thank-you goes through `/li-human` before the user sends it by hand.
