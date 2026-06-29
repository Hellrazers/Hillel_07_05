

with open('img.png', 'rb') as f:
    content = f.read()
    print(content)
    print(type(content))

with open('img2.png', 'wb') as f:
    f.write(content)