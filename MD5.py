import hashlib


def hash_password(text_to_hash):

    md5_hasher = hashlib.md5()

    md5_hasher.update(text_to_hash.encode('utf-8'))


    hashed_text = md5_hasher.hexdigest()
    return hashed_text


if __name__ == "__main__":
    text = "Merhabaa Dünya"
    hashed_text = hash_password(text)
    print(f"MD5 Hash: {hashed_text}")
