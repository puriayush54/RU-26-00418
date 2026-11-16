import json
import os
from datetime import datetime

# File used to store all diary notes
FILE_NAME = "diary.txt"


def load_notes():
    """Load notes from diary.txt. Return an empty list if the file is missing."""
    notes = []

    if not os.path.exists(FILE_NAME):
        return notes

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    note = json.loads(line)
                    if (
                        isinstance(note, dict)
                        and isinstance(note.get("date"), str)
                        and isinstance(note.get("text"), str)
                    ):
                        notes.append(note)
                    else:
                        print(f"Warning: Invalid note format on line {line_number}.")
                except json.JSONDecodeError:
                    print(f"Warning: Could not read line {line_number} in {FILE_NAME}.")

    except OSError as error:
        print(f"Error reading diary file: {error}")
        return notes


def save_notes(notes):
    """Save all notes to the text file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for note in notes:
                file.write(json.dumps(note, ensure_ascii=False) + "\n")
        return True
    except OSError as error:
        print(f"Error saving notes: {error}")
        return False


def get_valid_date():
    """Ask for a date and validate the YYYY-MM-DD format."""
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            parsed_date = datetime.strptime(date_text, "%Y-%m-%d")
            # Round-trip check rejects non-zero-padded dates on platforms
            # where strptime may accept them.
            if parsed_date.strftime("%Y-%m-%d") != date_text:
                raise ValueError
            return date_text
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (example: 2026-10-10).")


def add_note(notes):
    """Add a new dated note."""
    print("\n--- ADD NOTE ---")
    note_date = get_valid_date()
    note_text = input("Enter note text: ").strip()

    if not note_text:
        print("Note text cannot be empty.")
        return

    new_note = {
        "date": note_date,
        "text": note_text
    }

    notes.append(new_note)

    if save_notes(notes):
        print("\nNote saved.")
        print_note(len(notes), new_note)


def print_note(number, note):
    """Display one note in the required format."""
    print(f"{number} | {note['date']} | {note['text']}")


def view_all_notes(notes):
    """Display every saved note."""
    print("\n--- ALL NOTES ---")

    if not notes:
        print("No notes found. Your diary is empty.")
        return

    for number, note in enumerate(notes, start=1):
        print_note(number, note)


def search_notes(notes):
    """Search note text using a case-insensitive keyword."""
    print("\n--- SEARCH NOTES ---")

    if not notes:
        print("No notes found. Your diary is empty.")
        return

    keyword = input("Enter keyword to search: ").strip()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    matches = []

    for number, note in enumerate(notes, start=1):
        if keyword.lower() in note["text"].lower():
            matches.append((number, note))

    if not matches:
        print("No matching notes found.")
        return

    print(f"\nFound {len(matches)} note(s):")
    for number, note in matches:
        print_note(number, note)


def delete_note(notes):
    """Delete a note by its current displayed number."""
    print("\n--- DELETE NOTE ---")

    if not notes:
        print("No notes found. Your diary is empty.")
        return

    view_all_notes(notes)

    number_text = input("\nEnter note number to delete: ").strip()

    try:
        note_number = int(number_text)
    except ValueError:
        print("Invalid note number. Please enter a whole number.")
        return
    
    if note_number < 1 or note_number > len(notes):
        print(f"Note number {note_number} not found.")
        return

    deleted_note = notes.pop(note_number - 1)

    if save_notes(notes):
        print(f"Note {note_number} deleted. Notes left: {len(notes)}")
    else:
        # Restore the note in memory if saving failed.
        notes.insert(note_number - 1, deleted_note)
        print("Delete could not be saved. The note has been restored.")


def display_menu():
    """Display the main menu."""
    print("\n========== DIGITAL DIARY / NOTES MANAGER ==========")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")
    print("===================================================")


def main():
    """Main program."""
    notes = load_notes()

    print("Welcome to Digital Diary / Notes Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_all_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            print("Thank you for using Digital Diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
