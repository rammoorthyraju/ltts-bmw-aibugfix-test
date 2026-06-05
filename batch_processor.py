from src.services.player_service import get_selected_track
from src.ui.music_page import show_track_details


def process_users(user_ids: list[str]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for user_id in user_ids:
        selected_track = get_selected_track(user_id=user_id)
        output.append(show_track_details(selected_track))
    return output
