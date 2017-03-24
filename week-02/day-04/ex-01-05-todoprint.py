# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todo_text = ["My todo", " - Buy milk", " - Download games", "    - Diablo"]
def my_list(list):
    for e in list:
        print(e)
my_list(todo_text)
