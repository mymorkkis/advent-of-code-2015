import hashlib


def lowest_positive_number_that_produces_hash(secret_key: str, no_of_zeros: int) -> int:
    current_number, lowest_positive_number = 0, 0
    while True:
        bytes_value_to_hash = (secret_key + str(current_number)).encode()
        md5_hexadecimal_hash = hashlib.md5(bytes_value_to_hash).hexdigest()
        if md5_hexadecimal_hash.startswith('0' * no_of_zeros):
            lowest_positive_number = current_number
            break
        current_number += 1
    return lowest_positive_number
