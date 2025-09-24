def caesar_shift_plus_k(text, k=5):
  result = []
  for ch in text:
    if 'a' <= ch <= 'z':
      # chữ thường
      offset = ord(ch) - ord('a')
      new_char = chr((offset + k) % 26 + ord('a'))
      result.append(new_char)
    elif 'A' <= ch <= 'Z':
      # chữ hoa: xử lý riêng với chữ hoa
      offset = ord(ch) - ord('A')
      new_char = chr((offset + k) % 26 + ord('A'))
      result.append(new_char)
    else:
      # ký tự không phải chữ cái: giữ nguyên
      result.append(ch)
  return ''.join(result)

plaintext = "Khue"
ciphertext = caesar_shift_plus_k(plaintext, k=5)
print("Plaintext:", plaintext)
print("Ciphertext (Z26, +5):", ciphertext)