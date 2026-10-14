<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-en-dark.svg">
  <img alt="Lucas Matias: Software Engineering student at IFG and notary clerk in Goiás, Brazil" src="assets/banner-en-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://linkedin.com/in/matiaslucas"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-14294D?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMC40NDcgMjAuNDUyaC0zLjU1NHYtNS41NjljMC0xLjMyOC0uMDI3LTMuMDM3LTEuODUyLTMuMDM3Yy0xLjg1MyAwLTIuMTM2IDEuNDQ1LTIuMTM2IDIuOTM5djUuNjY3SDkuMzUxVjloMy40MTR2MS41NjFoLjA0NmMuNDc3LS45IDEuNjM3LTEuODUgMy4zNy0xLjg1YzMuNjAxIDAgNC4yNjcgMi4zNyA0LjI2NyA1LjQ1NXY2LjI4NnpNNS4zMzcgNy40MzNhMi4wNiAyLjA2IDAgMCAxLTIuMDYzLTIuMDY1YTIuMDY0IDIuMDY0IDAgMSAxIDIuMDYzIDIuMDY1bTEuNzgyIDEzLjAxOUgzLjU1NVY5aDMuNTY0ek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyMiAweiIvPjwvc3ZnPg%3D%3D"></a>
  <a href="mailto:lucasmatiias2208@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-14294D?style=flat&logo=gmail&logoColor=white"></a>
  <a href="mailto:matias.lucas@estudantes.ifg.edu.br"><img alt="Academic email (IFG)" src="https://img.shields.io/badge/Academic_email-14294D?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDcgNDQ3Ij48Y2lyY2xlIGN4PSIxMjIiIGN5PSIxMjQiIHI9IjkyIiBmaWxsPSIjQzkwQzBGIi8%2BPHJlY3QgeD0iMjQzIiB5PSI0NiIgd2lkdGg9IjE2NiIgaGVpZ2h0PSIxNTYiIHJ4PSIyNCIgZmlsbD0iIzM1OTgzMCIvPjxyZWN0IHg9IjQwIiB5PSIyMzciIHdpZHRoPSIxNjYiIGhlaWdodD0iMTU2IiByeD0iMjQiIGZpbGw9IiMzNTk4MzAiLz48cmVjdCB4PSIyNDMiIHk9IjIzNyIgd2lkdGg9IjE2NiIgaGVpZ2h0PSIxNTgiIHJ4PSIyNCIgZmlsbD0iIzM1OTgzMCIvPjwvc3ZnPg%3D%3D"></a>
  <a href="https://instagram.com/lucasmatias.ll"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-14294D?style=flat&logo=instagram&logoColor=white"></a>
</p>

<p align="center"><a href="https://github.com/matias-lucas">Português</a> | <b>English</b></p>

## About me

I study Software Engineering at the **Federal Institute of Goiás (IFG)** in Brazil, currently in my 4th semester. I also work as a **notary clerk** at a registry office and handle the **finances of two land subdivisions**.

That routine is where my projects come from: when a process is repetitive, confusing or easy to get wrong, I try to turn it into software. Classdays started as a way to organize my class schedule; the payment slip automation, as a way to stop settling payments by hand.

I use AI (Claude Code) in my day-to-day development. It speeds up writing code. My part is understanding the problem, defining the business rules, reviewing what goes in and testing before anything ships.

**I'm looking for a web development internship.** If your team has an opening, let's talk.

## Featured project: Classdays

**[Classdays](https://classdays.net)** is a class's academic calendar behind one public link: weekly classes, exams, deadlines and cancellations, easy to read on a phone. Whoever updates it doesn't have to fill in a form: they type a sentence in Portuguese, such as *"na próxima terça não haverá aula de banco de dados"* (no Database class next Tuesday), and the app turns it into an event.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/classdays-demo-en-dark.gif">
  <img alt="Classdays demo: in the admin panel, the class rep types 'na próxima terça não haverá aula de banco de dados' (no Database class next Tuesday), the app shows the cancellation already filled in for review and, once saved, next week's schedule shows the cancelled class" src="assets/classdays-demo-en-light.gif" width="100%">
</picture>

- **Natural language input:** the sentence goes to the Claude API with *structured outputs*, so the schema guarantees the shape of the response. Without an API key, a rule-based Portuguese parser takes over.
- **Nothing is saved unreviewed:** every event goes through an editable preview before it reaches the database.
- **Built for the class:** no login to check the schedule, light and dark themes, AA contrast, keyboard navigation and 44 px touch targets.
- **245 automated tests** covering relative dates, cancellations, holidays and the parser.

**Stack:** Next.js 16, React 19, TypeScript, Supabase (Postgres with RLS), Claude API and Vercel.

**[Open Classdays](https://classdays.net)** | [View the code](https://github.com/matias-lucas/Classdays)

## Other projects

**[Matias Imóveis website](https://github.com/matias-lucas/matiasimoveis-site)** *(in development)*<br>
Website for a real estate agency in Itaberaí, Goiás: property search with filters, WhatsApp contact that already names the listing, and a panel where brokers upload photos and videos. Next.js, TypeScript and Supabase.

**Payment slip automation** *(in use, private repository)*<br>
A Windows program used by both land subdivisions: it reads the bank statement, calculates interest and late fees and settles each payment in the billing system, always with an on-screen review before confirming. It was built with AI from the business rules I gathered at work.

**[proj_algb](https://github.com/matias-lucas/proj_algb)** *(academic project, discontinued)*<br>
A pair project for my Linear Algebra course, written in C: it reads, solves and classifies linear systems (unique, infinite or no solution) and saves them to a file.

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img alt="Stack: Next.js, React, TypeScript, JavaScript, HTML, CSS, Supabase, PostgreSQL, Claude API, Vercel, Git and C" src="assets/stack-light.svg" width="100%">
</picture>

## Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/stats-en-dark.svg">
  <img alt="GitHub activity over the last 12 months: contributions, commits, pull requests, days with contributions, longest streak and public repositories" src="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/stats-en-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/snake-dark.svg">
  <img alt="Animation of the contribution graph for the last year" src="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/snake-light.svg" width="100%">
</picture>

<sub>Both are generated daily by a [GitHub Action](https://github.com/matias-lucas/matias-lucas/blob/main/.github/workflows/profile-stats.yml) in this repository, with no external services involved.</sub>

---

<p align="center">Looking for a web development internship and happy to talk about automation and software for real-world problems.<br>
The quickest way to reach me is on <a href="https://linkedin.com/in/matiaslucas">LinkedIn</a> or by <a href="mailto:lucasmatiias2208@gmail.com">email</a>.</p>
