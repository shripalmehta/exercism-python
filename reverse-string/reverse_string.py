def reverse(text=""):
    new_text = ""
    for i in text.strip():
        new_text = i + new_text
    # print(new_text)
    return new_text

