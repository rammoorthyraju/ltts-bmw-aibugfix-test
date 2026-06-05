from src.models.track import Track


def show_track_details(selected_track: Track | None) -> dict[str, str]:
    # APP-101 BUG: selected_track can be None but is dereferenced directly.
    return {
        "title": selected_track.title,
        "artist": selected_track.artist,
    }
