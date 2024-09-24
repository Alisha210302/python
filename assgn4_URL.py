import re


def find_urls(text):
    """
    Extracts all URLs starting with http:// or https:// from the given text.

    :param text: The text containing URLs.
    :return: A list of URLs found in the text.
    """
    # Regular expression to match URLs starting with http:// or https://
    url_pattern = re.compile(
        r'https?://'  # Match http:// or https://
        r'(?:[\w-]+\.)+[a-zA-Z]{2,}'  # Match domain name (e.g., example.com)
        r'(?:/[\w\-./?&%#=]*)?'  # Match optional paths
    )

    # Find all URLs in the text
    urls = url_pattern.findall(text)
    return urls


# Example usage
if __name__ == "__main__":
    sample_text = """
    Visit our website at http://example.com or our secure site at https://secure.example.com/path/to/resource?query=1.
    For more info, check out https://www.example.org and don't forget our blog at http://blog.example.com.
    """
    urls = find_urls(sample_text)
    print("URLs Found:")
    for url in urls:
        print(url)
