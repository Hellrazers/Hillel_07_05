

new_row = 'Hello word'

new_row_encode = new_row.encode('windows-1252')
print(new_row)
print(new_row_encode)

new_row_decode = new_row_encode.decode('windows-1252')
print(new_row_decode)
