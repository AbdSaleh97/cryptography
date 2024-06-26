# test_encryption.py
import pytest
from crypto.crypto import encrypt, decrypt

def test_encrypt_case1():
    assert encrypt("hello", 2) == ''.join(chr((ord(c) + 2) % 256) for c in "hello@A#,0&,") 

def test_encrypt_case2():
    assert encrypt("OpenAI", 5) == ''.join(chr((ord(c) + 5) % 256) for c in "OpenAI@A#,0&,")

def test_encrypt_case3():
    assert encrypt("Encrypt! This.", 10) == ''.join(chr((ord(c) + 10) % 256) for c in "Encrypt! This.@A#,0&,")

def test_decrypt_case1():
    encrypted_text = encrypt("hello", 2)
    assert decrypt(encrypted_text, 2) == "hello"

def test_decrypt_case2():
    encrypted_text = encrypt("OpenAI", 5)
    assert decrypt(encrypted_text, 5) == "OpenAI"

def test_decrypt_case3():
    encrypted_text = encrypt("Encrypt! This.", 10)
    assert decrypt(encrypted_text, 10) == "Encrypt! This."

if __name__ == "__main__":
    pytest.main()
