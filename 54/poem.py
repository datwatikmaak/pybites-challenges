INDENTS = 4

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_hanging_indents(poem):

    result = "\n".join([x.strip(" ") for x in "".join(poem).split("\n")])

    print(result)
    print(repr(result))


print_hanging_indents(shakespeare_unformatted)
