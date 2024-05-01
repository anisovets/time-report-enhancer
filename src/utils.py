from datetime import datetime

def generate_filename(base_filename):
    """
    Generates a new filename based on the base filename with the current date and time appended.
    Format: filename_mmddyyyy_hhmm.ext where ext is derived from the base filename.
    """
    current_time = datetime.now()
    date_time_str = current_time.strftime("%m%d%Y_%H%M")
    # Extract the extension from the base filename
    name_part, extention = base_filename.rsplit('.',1)
    full_filename = f"{name_part}_{date_time_str}.{extention}"

    return full_filename