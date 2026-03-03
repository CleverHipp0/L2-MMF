# Create file to hold data
file_name = "write_experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")
heading = "=== Bob the magic robot ===\n"
content = '''Once upon a time there was a magic robot called bob.
Bob loved the concept of potatoes but had never had them before.
One summers day Bob the magic robot stumbled upon a field of
potatoes. He rolled around and around and around in the field all
day long until all of his joints were rusty. That's when the light came.
Bob couldn't move because of the rust. He was trapped. The shinning light
got closer and closer until it picked Bob up and took him to outer space
for the rest of eternity.'''
end = "Moral: Potatoes make you go to outer space."



to_write = [heading, content, end]

for item in to_write:
    print(item)
    text_file.write(item)
    text_file.write("\n")

