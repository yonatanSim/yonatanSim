import hashlib
import itertools
import string

target = "d4d80df2d159f9cb45e2175f47616f94"


charset = string.ascii_lowercase + string.digits


for combo in itertools.product(charset, repeat=6):
    user_input = ''.join(combo)
    md5_hash = hashlib.md5(user_input.encode()).hexdigest()
    
  
    print(f"try {user_input} → MD5: {md5_hash}")
    
    if md5_hash == target:
        print(f"you found it {user_input}")
        break
