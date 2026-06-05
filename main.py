from src.services.player_service import get_selected_track
from src.ui.music_page import show_track_details


def main() -> None:
    selected_track = get_selected_track(user_id="user-123")
    details = show_track_details(selected_track)
    print(details)


if __name__ == "__main__":
    main()
