# Mike Jones
# 05 SEP 20XX
# f-String Adventure Story

hero = input("Enter the hero's name: ")
setting = input("Enter the setting (e.g., forest, city): ")
object_found = input("Enter an object the hero finds: ")

story = f"""Once upon a time, {hero} went on an adventure in a {setting}.
While exploring, {hero} found a mysterious {object_found}.
This discovery changed everything for {hero}."""

print(story)

