## LTTS BMW AI BugFix Test Repo

This repo contains a simple reproducible bug scenario for the RCA and Phase A walkthrough.

### Scenario

- JIRA ID: `APP-101`
- Bug: Music details page crashes when no track is selected.
- Root Cause: `selected_track` can be `None`, but code reads `selected_track.title` directly.

### Repo Layout

- `rca/APP-101.json`: sample RCA input payload
- `src/ui/music_page.py`: intentionally buggy implementation
- `src/services/player_service.py`: simple service returning selected track
- `tests/test_music_page.py`: failing tests showing expected behavior

### Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Expected result now: one or more tests fail because bug is still present.

This is intentional and useful for AI bug-fix pipeline testing.
