"""
Generates personalized invitation files from a template and a list of attendees.
"""

import os

def generate_invitations(template, attendees):
    """
    Create invitation files using a string template and attendee data.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): List of dictionaries with attendee information.

    Each output file is named output_X.txt, with missing values replaced by "N/A".
    """
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        try:
            name = attendee.get("name", "N/A")
            title = attendee.get("event_title", "N/A")
            date = attendee.get("event_date") or "N/A"
            location = attendee.get("event_location", "N/A")

            invitation_text = template.replace("{name}", name)
            invitation_text = invitation_text.replace("{event_title}", title)
            invitation_text = invitation_text.replace("{event_date}", date)
            invitation_text = invitation_text.replace("{event_location}", location)

            with open(f"output_{i}.txt", 'w') as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"An error occurred while processing attendee {i}: {e}")
