from pyscript import document

nicknames = [["China", "The Middle Kingdom"],["Japan", "The Land of the Rising Sun"],["Mongolia", "The Land of the Blue Sky"],["North Korea", "The Hermit Kingdom"],["South Korea", "The Land of the Morning Calm"],["Taiwan", "The Beautiful Island"],["Hong Kong", "The Fragrant Harbour"],["Macau", "The Las Vegas of Asia"]]

def show_nickname(event):
    country = document.getElementById("country").value.strip()

    for item in nicknames:
        if country.lower() == item[0].lower():
            document.getElementById("result").innerText = "Nickname: " + item[1]
            return

    document.getElementById("result").innerText = "Country not found. Try again!"