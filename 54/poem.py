INDENTS = 4

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_hanging_indents(poem):
    lines = poem.strip().split("\n")
    lines = map(str.strip, lines)

    formatted_poem = ""
    is_first_line = True
    indent = " " * INDENTS

    for line in lines:
        if line == "":
            is_first_line = True
            continue
        if is_first_line:
            formatted_poem += line + "\n"
            is_first_line = False
        else:
            formatted_poem += indent + line + "\n"

    print(formatted_poem)


print_hanging_indents(shakespeare_unformatted)
