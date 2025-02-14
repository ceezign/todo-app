contents = ["i love pussy but i cant die for it",
           "im going to achieve all i want to achieve",
           "fuck the whole world no matter who is involve"]

filenames = ["doc.txt", "presentation.txt" "report.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", "w")
    file.write(content)