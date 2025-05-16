word = '["some words", "more words"]'



print("".join(c for c in word if c not in ['"','[', ']']))