from pyscript import document

clubs = [
    {
        "id": "chess",
        "name": "Chess Club",
        "description": "A club for chess enthusiasts to play, learn, and compete in chess games.",
        "meeting_time": "Every Saturday at 3 PM",
        "location": "Room 101, Community Center",
        "moderator": "John Doe",
        "members": 25
    },
    {
        "id": "math",
        "name": "Math Club",
        "description": "A club for students interested in exploring mathematical concepts and problem-solving.",
        "meeting_time": "Every Wednesday at 4 PM",
        "location": "Room 202, Science Building",
        "moderator": "Jane Smith",
        "members": 30
    },
    {
        "id": "science",
        "name": "Science Club",
        "description": "A club for students passionate about science experiments and discoveries.",
        "meeting_time": "Every Friday at 5 PM",
        "location": "Lab 3, Science Building",
        "moderator": "Dr. Albert",
        "members": 20
    }
]


clubs_by_id = {c["id"]: c for c in clubs}

select = document.getElementById("clubSelect")
details = document.getElementById("details")


for c in clubs:
    opt = document.createElement("option")
    opt.value = c["id"]
    opt.textContent = c["name"]
    select.appendChild(opt)

default_club = {
    "name": "",
    "description": "",
    "meeting_time": "",
    "location": "",
    "moderator": "",
    "members": ""
}


display_map = {'': 'none'}

def show_club(e=None):
    selection = select.value
    club = clubs_by_id.get(selection, default_club)

    document.getElementById("clubName").textContent = club["name"]
    document.getElementById("clubDesc").textContent = club["description"]
    document.getElementById("clubTime").textContent = club["meeting_time"]
    document.getElementById("clubLocation").textContent = club["location"]
    document.getElementById("clubModerator").textContent = club["moderator"]
    document.getElementById("clubMembers").textContent = str(club["members"])

    
    details.style.display = display_map.get(selection, 'block')


select.addEventListener("change", show_club)
show_club()
