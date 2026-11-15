# SRM Student Portal

A **front-end-only** student portal desktop app built with **Python Tkinter**.
All data is stored in memory — no backend, no database, no network calls.

## Features

- **Login screen** — demo login (any credentials work)
- **Dashboard** — greeting banner, SGPA / credits / attendance stat cards,
  upcoming deadlines, announcements, today's classes
- **My Courses** — live search, course cards, detail pop-ups
- **Grades** — assessment results table (double-click a row for details),
  per-course standing chart
- **Schedule** — weekly timetable grid with color-coded class blocks
- **Announcements** — filterable by category
- **Profile** — editable details that update across the app

## Requirements

- Python 3.x with Tkinter (`brew install python-tk` on macOS Homebrew Python;
  Tkinter is bundled with python.org and most Linux/Windows installs)

## Run

```bash
python3 student_portal.py
```

## Tech

| Area | Choice |
|---|---|
| Language | Python 3 |
| GUI | `tkinter` + `ttk` only |
| Data | In-memory dicts/lists at the top of the file |
| Backend / DB | None — front end only |

## Notes

Built as a college front-end project by Gottipati Pallavi
(B.Tech CSE, Semester 3, SRM University).
