def caesar_encrypt(text, k):
  k = k % 26  # đảm bảo vòng 26 chữ cái
  result = []
  for ch in text:
    if 'A' <= ch <= 'Z':
      # chữ hoa
      offset = ord('A')
      new_ch = chr((ord(ch) - offset + k) % 26 + offset)
      result.append(new_ch)
    elif 'a' <= ch <= 'z':
      # chữ thường
      offset = ord('a')
      new_ch = chr((ord(ch) - offset + k) % 26 + offset)
      result.append(new_ch)
    else:
      # giữ nguyên ký tự không phải chữ cái
      result.append(ch)
  return ''.join(result)

text = "Khue"
encrypted = caesar_encrypt(text, 5)
print(encrypted)