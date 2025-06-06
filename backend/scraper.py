import requests
import json

# Fetches enrollment data from UCLA Registrar's public schedule of classes
# This replicates the method described in the blog post

BASE = "https://sa.ucla.edu/ro/Public/SOC/Results/CourseTitlesView"


def fetch_courses(subject="COM SCI", term="24F", page=1):
    model = {
        "subj_area_cd": subject,
        "search_by": "subject",
        "term_cd": term,
        "SubjectAreaName": "",
        "CrsCatlgName": "",
        "ActiveEnrollmentFlag": "n",
        "HasData": "True",
    }
    filter_flags = {
        "enrollment_status": "O,W,C,X,T,S",
        "advanced": "y",
        "meet_days": "M,T,W,R,F",
        "start_time": "8:00 am",
        "end_time": "7:00 pm",
    }
    params = {
        "search_by": "subject",
        "model": json.dumps(model),
        "pageNumber": page,
        "filterFlags": json.dumps(filter_flags),
    }
    r = requests.get(BASE, params=params)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    data = fetch_courses()
    print(json.dumps(data)[:200])
