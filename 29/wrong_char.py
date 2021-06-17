import string


def get_index_different_char(chars):
    string_of_chars = ''.join(str(char) for char in chars)
    # alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'



    alpha = ""
    non_alpha = ""
    for char in string_of_chars:
        if char.isalpha() or char.isdigit():
            alpha += char
        elif char == "":
            non_alpha += "*"
        else:
            non_alpha += char

    print(alpha)
    print(non_alpha)
    # if len(alpha) == 1:
    #     return string_of_chars.index(alpha)
    # if len(non_alpha) == 1:
    #     return string_of_chars.index(non_alpha)

    if len(alpha) == 1:
        print(string_of_chars.index(alpha))
    if len(non_alpha) == 1:
        print(string_of_chars.index(non_alpha))


# get_index_different_char(['A', 'f', '.', 'Q', 2])  # 2
# get_index_different_char(['.', '{', ' ^', '%', 'a'])  # 4
# get_index_different_char([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'])  # 1
get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'])  # 5
