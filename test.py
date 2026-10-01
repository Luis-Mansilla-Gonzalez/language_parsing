from sudachipy import dictionary, tokenizer

# 1. Create a dictionary instance and setup the tokenizer
tokenizer_obj = dictionary.Dictionary().tokenizer()

# 2. Define your text and choose a Split Mode (A, B, or C)
text = "国家公務員になりました。"
mode = tokenizer.Tokenizer.SplitMode.A

# 3. Tokenize the text
tokens = tokenizer_obj.tokenize(text, mode)

# 4. Extract token details
for m in tokens:
    print(f"Surface: {m.surface()} \t Part of Speech: {m.part_of_speech()}")
