from src.add import add_two_numbers


def test_add_two_numbers():
    import boto3
    
    assert add_two_numbers(1, 2) == 3
