"""Create a PostIt class that has
a backgroundColor, a text on it and a textColor.
Create a few example post-it objects:
an orange with blue text: "Idea 1"
a pink with black text: "Awesome"
a yellow with green text: "Superb!"""

class PostIt():
    backgroundColor = ""
    text = ""
    textColor = ""

note1 = PostIt()
note2 = PostIt()
note3 = PostIt()

note1.backgroundColor = "orange"
note2.backgroundColor = "pink"
note3.backgroundColor = "yellow"
note1.textColor = "blue"
note2.textColor = "black"
note3.textColor = "green"
note1.text = "'Idea 1'"
note2.text = "'Awesome'"
note3.text = "'Superb!'"

print("This is an " + note1.backgroundColor + " post-it saying " + note1.text + " with " + note1.textColor + " letters.")
print("This is a " + note2.backgroundColor + " post-it saying " + note2.text + " with " + note2.textColor + " letters.")
print("This is a " + note3.backgroundColor + " post-it saying " + note3.text + " with " + note3.textColor + " letters.")
