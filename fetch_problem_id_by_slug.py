import requests

problem_details_url = "https://leetcode.com/graphql/"

query = '''
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
  }
}

'''

# Function to fetch a question's frontend ID
def get_problem_frontend_id(title_slug: str):
    """
    Fetch the frontend ID of a question from LeetCode using its title slug.

    Args:
        title_slug (str): The title slug of the question.

    Returns:
        str: The frontend ID of the question.

    Raises:
        Exception: If the response status code is not 200 (HTTP OK) or if the data is missing.
    """
    variables = {"titleSlug": title_slug}
    payload = {"query": query, "variables": variables}

    response = requests.post(problem_details_url, json=payload)

    if response.status_code == 200:
        data = response.json()
        question_data = data.get('data', {}).get('question', {})
        frontend_id = question_data.get('questionFrontendId')

        if frontend_id:
            return frontend_id
        else:
            raise Exception("Question frontend ID not found in the response data.")
    else:
        raise Exception(f"Failed to fetch problem details. Status code: {response.status_code}")

if __name__ == "__main__":
    try:
        title_slug = "your_question_title_slug_here"  # Replace with the actual title slug
        frontend_id = get_problem_frontend_id(title_slug)
        print(f"Frontend ID for '{title_slug}': {frontend_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
