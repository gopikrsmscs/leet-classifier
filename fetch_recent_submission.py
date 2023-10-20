import requests
import json

submission_url = "https://leetcode.com/api/submissions/?offset=0&limit=1"

# Function to load headers from a JSON file
def load_headers():
    """
    Load headers from a JSON file and return them as a dictionary.

    Returns:
        dict: The headers read from the JSON file.
    """
    with open('cookie.json') as json_file:
        headers = json.load(json_file)
        return headers

# Function to fetch submission details
def fetch_recent_submission():
    """
    Fetch details of the most recent submission from the specified URL using headers loaded from a JSON file.

    Returns:
        tuple: A tuple containing problem code, problem title, and problem language.
        
    Raises:
        Exception: If the response status code is not 200 (HTTP OK).
    """
    response = requests.get(submission_url, headers=load_headers())
    
    if response.status_code == 200:
        data = response.json()
        if 'submissions_dump' in data:
            submissions_dump = data['submissions_dump']
            if submissions_dump:
                submission = submissions_dump[0]
                problem_code = submission.get('code', 'N/A')
                problem_title = submission.get('title_slug', 'N/A')
                problem_language = submission.get('lang', 'N/A')
                return problem_code, problem_title, problem_language
        raise Exception("No submissions found in the response data.")
    else:
        raise Exception(f"Failed to fetch submission details. Status code: {response.status_code}")

if __name__ == "__main__":
    try:
        problem_code, problem_title, problem_language = fetch_recent_submission()
        print(f"Problem Code: {problem_code}")
        print(f"Problem Title: {problem_title}")
        print(f"Problem Language: {problem_language}")
    except Exception as e:
        print(f"An error occurred: {e}")
