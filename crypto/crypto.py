def encrypt(text, key):
    """
    Encrypts the given text using a Caesar cipher with the provided key.

    Parameters:
        text (str): The text to be encrypted.
        key (int): The key used for encryption.

    Returns:
        str: The encrypted text.

    Example:
        >>> encrypt("hello", 2)
        'jgnnq@A#,0&,'
    """
    secret = "@A#,0&,"
    text += secret
    return ''.join(chr((ord(c) + key) % 256) for c in text)

def decrypt(text, key):
    """
    Decrypts the given text using a Caesar cipher with the provided key.

    Parameters:
        text (str): The text to be decrypted.
        key (int): The key used for decryption.

    Returns:
        str: The decrypted text.
    """
    secret = "@A#,0&,"
    decrypted_text = ''.join(chr((ord(c) - key) % 256) for c in text)
    
    # Remove the secret at the end
    if decrypted_text.endswith(secret):
        decrypted_text = decrypted_text[:-len(secret)]
    return decrypted_text


print(encrypt("hello",2))
print(decrypt(encrypt("hello",2),2))