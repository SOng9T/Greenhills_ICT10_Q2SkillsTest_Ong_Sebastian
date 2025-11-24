from pyscript import document

clubs = [
    {"id": "chess", "name": "Chess Club", "description": "A club for chess enthusiasts to play, learn, and compete in chess games.", "meeting_time": "Every Saturday at 3 PM", "location": "Room 101, Community Center", "moderator": "John Doe", "members": 25, "class": ""},
    {"id": "math", "name": "Math Club", "description": "A club for students interested in exploring mathematical concepts and problem-solving.", "meeting_time": "Every Wednesday at 4 PM", "location": "Room 202, Science Building", "moderator": "Jane Smith", "members": 30, "class": ""},
    {"id": "science", "name": "Science Club", "description": "A club for students passionate about science experiments and discoveries.", "meeting_time": "Every Friday at 5 PM", "location": "Lab 3, Science Building", "moderator": "Dr. Albert", "members": 20, "class": ""}
]

clubs_by_id = {c["id"]: c for c in clubs}

display_data = {
    "": {"name": "", "description": "", "meeting_time": "", "location": "", "moderator": "", "members": "", "class": "hidden"},
    **clubs_by_id
}

select = document.getElementById("clubSelect")
details = document.getElementById("details")

for c in clubs:
    opt = document.createElement("option")
    opt.value = c["id"]
    opt.textContent = c["name"]
    select.appendChild(opt)

def show_club(e=None):
    selection = str(select.value)
    club_data = display_data[selection]

    document.getElementById("clubName").textContent = club_data["name"]
    document.getElementById("clubDesc").textContent = club_data["description"]
    document.getElementById("clubTime").textContent = club_data["meeting_time"]
    document.getElementById("clubLocation").textContent = club_data["location"]
    document.getElementById("clubModerator").textContent = club_data["moderator"]
    document.getElementById("clubMembers").textContent = str(club_data["members"])

    details.className = club_data["class"]

select.onchange = show_club
