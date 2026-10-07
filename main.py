from pyscript import document

club_members = [("olive", "smith"),("adam", "carlsen"),("ahn", "pham"),("malcolm", "browne"),("jeremy", "langley")] # members of the ICT club

def check_member(event): # when button


    first_name = document.getElementById("Fname").value # first name input from user
    last_name = document.getElementById("Lname").value # last name input from user

    candidate_name = (first_name.lower(), last_name.lower()) # so that it wont be case sensitive

    member = candidate_name in club_members # checks if inputted names are part of the list given (return as true if yes)

    messages = (
        f"🧬 Congratulations {first_name.title()} {last_name.title()}! You are now part of the Science club.", 
        f"Sorry {first_name.title()} {last_name.title()}! Your name is not on the list. ☹"
    )

    result = messages[not member]  # not in list = false

    document.getElementById("result").innerText = result #displays result