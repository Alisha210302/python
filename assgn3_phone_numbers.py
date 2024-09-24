import re


def extract_phone_numbers(text):

    phone_pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}')


    phone_numbers = phone_pattern.findall(text)
    return phone_numbers


# Example usage
if __name__ == "__main__":
    sample_text = """
    Call me at (123) 456-7890 or (987) 654-3210.
    Another number: (555) 555-5555.
    """
    phone_numbers = extract_phone_numbers(sample_text)
    print("Phone Numbers Found:")
    for number in phone_numbers:
        print(number)

import re


def extract_hashtags(text):

    hashtag_pattern = re.compile(r'#\w+')


    hashtags = hashtag_pattern.findall(text)

    unique_hashtags = set(
        hashtag.lower() for hashtag in hashtags if len(hashtag) > 4
    )

    return sorted(unique_hashtags)


# Example usage
if __name__ == "__main__":
    sample_post = """
    #hello all #students
    """
    hashtags = extract_hashtags(sample_post)
    print("Unique Hashtags Found:")
    for hashtag in hashtags:
        print(hashtag)


