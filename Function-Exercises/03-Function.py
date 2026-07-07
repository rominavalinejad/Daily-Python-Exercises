# =================================
# Audio Playlist Duration Analyzer
# =================================

def convert_seconds_to_minutes(total_seconds):
    '''
    Convert total seconds into a standard digital clock format (M:SS).
    '''
    # Calculate the full minutes
    total_minutes = total_seconds // 60
    # Calculate the remaining seconds
    remaining_seconds = total_seconds - (total_minutes *60)
    # Return the time formatted with padded zeros for single-digit seconds
    return f"{total_minutes}:{remaining_seconds:02d}"

def calculate_playlist_duration(track_list):
    '''
    Process a list of track durations, print each track formatted, 
    and aggregate the overall album duration.
    '''
    playlist_duration = 0
    track_number = 1
    for i in track_list:
        # Format and display the duration of the current track
        single_track_time = convert_seconds_to_minutes(i)
        print(f"Track {track_number}: {single_track_time}")
        # Accumulate current track's seconds into the total 
        playlist_duration += i
        track_number += 1
    # Convert the final aggregated playlist
    total_album_time = convert_seconds_to_minutes(playlist_duration)
    return total_album_time

# Define a test playlist with various track lengths in seconds
my_album = [75, 120, 253, 202, 129, 255]
print("--- Album Details ---")
total = calculate_playlist_duration(my_album)
print("------------------------------")
print(f"Total Album Duration: {total}")
