def all_variants(text):
    b = 1
    while b <= len(text):
        a = 0
        while a < len(text) and a+b <= len(text):
            yield text[a:a+b]
            a += 1
        b += 1

a = all_variants('abc')
for i in a:
    print(i)