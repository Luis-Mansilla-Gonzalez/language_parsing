from sudachipy import dictionary, tokenizer

tokenizer_obj = dictionary.Dictionary().tokenizer()

# choose a Split Mode (A, B, or C)
text = "国家公務員になりました。"
mode = tokenizer.Tokenizer.SplitMode.A

tokens = tokenizer_obj.tokenize(text, mode)

for m in tokens:
    print(f"Surface: {m.surface()} \t Part of Speech: {m.part_of_speech()}")
