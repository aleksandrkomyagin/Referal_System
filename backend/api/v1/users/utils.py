import base64


def encrypt(id: str, expiration_date: str):
    try:
        encrypt_id = base64.urlsafe_b64encode(id.encode("utf-8")).decode()
        encrypt_expiration_date = base64.urlsafe_b64encode(
            expiration_date.encode("utf-8")
        ).decode()
        encrypt_referal_code = encrypt_id + "-" + encrypt_expiration_date
    except Exception as e:
        raise e
    return encrypt_referal_code


def decrypt(referal_code: str):
    try:
        decrypt_id = base64.urlsafe_b64decode(referal_code.split("-")[1])
        decrypt_expiration_date = base64.urlsafe_b64decode(
            referal_code.split("-")[2]
        )
    except Exception as e:
        raise e
    return decrypt_id.decode(), decrypt_expiration_date.decode()
