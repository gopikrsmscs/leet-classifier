import requests
import json

submission_url = "https://leetcode.com/api/submissions/?limit="

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
def fetch_recent_submission(limit=None):
    """
    Fetch details of the most recent submission from the specified URL using headers loaded from a JSON file.

    Returns:
        tuple: A tuple containing problem code, problem title, and problem language.
        
    Raises:
        Exception: If the response status code is not 200 (HTTP OK).
    """
    global submission_url
    if limit != None:
        if limit > 10:
            raise Exception("Max allowed limit is 10 submission.")

        submission_url =submission_url+ str(limit)
    else:
        submission_url = submission_url+ '1'
    response = requests.get(submission_url, headers=load_headers())
    accepted_problems_list = set()
    unique_problems = set()
    if response.status_code == 200:
        data = response.json()
        if 'submissions_dump' in data:
            submissions_dump = data['submissions_dump']
            if submissions_dump:
                for each_submission in submissions_dump:
                    if each_submission.get('status_display') == 'Accepted':
                        problem_code = each_submission.get('code', 'N/A')
                        problem_title = each_submission.get('title_slug', 'N/A')
                        problem_language = each_submission.get('lang', 'N/A')
                        if problem_code not in unique_problems:
                            accepted_problems_list.add((problem_code,problem_title,problem_language))
                            unique_problems.add(problem_code)
                if len(accepted_problems_list) > 0:
                    return accepted_problems_list
                else:
                    raise Exception("No accepted submission found in the response data.")
        raise Exception("No submissions found in the response data.")
    else:
        print(response.json())
        raise Exception(f"Failed to fetch submission details. Status code: {response.status_code}")

if __name__ == "__main__":
    try:
        problem_code, problem_title, problem_language = fetch_recent_submission(10)
        print(f"Problem Code: {problem_code}")
        print(f"Problem Title: {problem_title}")
        print(f"Problem Language: {problem_language}")
    except Exception as e:
        print(f"An error occurred: {e}")
