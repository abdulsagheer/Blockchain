from backend.util.crypto_hash import crypto_hash


def test_crypto_hash():
    """
    It should create the same hash with arguements of different data types in any order
    """
    assert crypto_hash(1,[2],'three') == crypto_hash('three',1,[2])
    assert crypto_hash('sagheer') == '61020c88823bc62e4b4046f2d8902ff1009e1ebf6f4ca05744e4cbba2514d092'
