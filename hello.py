word = input("enter your pasword ")
key = input("shhhhh enter the secret key ")

if len(key) < len(word):
    key = (key * (len(word) // len(key) + 1))[:len(word)]

result = ""
for w_char, k_char in zip(word, key):
    total_ascii = ord(w_char) + ord(k_char)
    new_char = chr(total_ascii % 256)
    result += new_char
print("the yonatan atzpanot is" + result)
