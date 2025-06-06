# Easy GE Finder Backend

This folder contains example AWS Lambda code for serving course data from a database.

- `handler.py` connects to a PostgreSQL database and returns the top courses ordered by average grade.
- `scraper.py` demonstrates fetching enrollment data from UCLA's Schedule of Classes as described in [Nathan Smith's blog](https://nathansmith.io/posts/scraping-enrollment-data-from-the-ucla-registrar-part-one/).

## Deployment

Package the Python code with dependencies from `requirements.txt` and deploy to AWS Lambda.

The function expects the environment variable `DB_CONN` with a PostgreSQL connection string.
