from pyscript import document

club_members = [("Olive", "Smith"),("Adam", "Carlsen"),("Ahn", "Pham"),("Malcolm", "Browne"),("Jeremy", "Langley")]

def check_member(event):

    first_name = document.getElementById("Fname").value
    last_name = document.getElementById("Lname").value

    candidate_name = (first_name, last_name)

    member = candidate_name in club_members

    messages = (
        f"Congratulations {first_name} {last_name}! You are now part of the ICT club.",
        f"Sorry {first_name} {last_name}, your name is not on the list."
    )

    result = messages[not member]

    document.getElementById("result").innerText = result