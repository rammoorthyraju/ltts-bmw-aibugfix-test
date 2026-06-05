from src.models.track import Track
from src.ui.music_page import show_track_details


def test_show_track_details_happy_path() -> None:
    track = Track(title="Skyline", artist="Sample Artist")
    details = show_track_details(track)
    assert details == {"title": "Skyline", "artist": "Sample Artist"}


def test_show_track_details_handles_none_selection() -> None:
    # Desired behavior for APP-101 after fix.
    details = show_track_details(None)
    assert details == {"title": "", "artist": ""}
