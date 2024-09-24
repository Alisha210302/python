import re


def validate_ip(ip_address):
    """
    Validates if the given string is a valid IPv4 address.

    :param ip_address: The IP address string to validate.
    :return: True if the IP address is valid, otherwise False.
    """
    # Regular expression to match valid IPv4 addresses
    ip_pattern = re.compile(
        r'^'
        r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )

    # Check if the input matches the regular expression
    return bool(ip_pattern.match(ip_address))


# Example usage
if __name__ == "__main__":
    test_ips = [
        "192.168.0.1",  # Valid
        "127.0.0.1",  # Valid
        "256.100.50.0",  # Invalid (first octet out of range)
        "192.168.0",  # Invalid (missing one octet)
        "10.0.0.256",  # Invalid (last octet out of range)
        "10.0.0.10"  # Valid
    ]

    for ip in test_ips:
        print(f"{ip}: {validate_ip(ip)}")
