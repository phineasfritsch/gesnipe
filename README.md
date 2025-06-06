# Easy GE Finder

This repository contains a proof-of-concept project for finding easy General Education courses at UCLA.

- `frontend/` – a React application served as a static site (e.g. Cloudflare Pages).
- `backend/` – example AWS Lambda code for querying course data.

The backend expects a PostgreSQL database populated with grade distributions such as those from [uclagrades.com](https://github.com/nathanhleung/uclagrades.com). Enrollment data can be scraped using `backend/scraper.py`.
