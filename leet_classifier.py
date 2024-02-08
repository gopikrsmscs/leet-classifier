import os
import re
import sys
import argparse
import fetch_recent_submission
import fetch_problem_id_by_slug

FILE_STORE_FOLDER = os.getcwd() + '/classification/'

def read_tags_from_code(code: str, problem_title: str) -> list:
    """
    Extract tags from the code.

    Args:
        code (str): The code containing tags.

    Returns:
        list: A list of extracted tags.
    """
    pattern = r'lct\s*:\s*([^;]+);'
    match = re.search(pattern, code)
    tags_list = []
    if match:
        tags_list = list(match.group(1).strip().split(','))
    else:
        print("Tag missing- Add tags to the leet code submission: "+ problem_title)
    return tags_list

def read_problem_category_from_code(code: str) -> str:
    """
    Extract difficulty information from the code.

    Args:
        code (str): The code containing difficulty information.

    Returns:
        str: Extracted difficulty information.
    """
    pattern = r'lcd\s*:\s*([^;]+);'
    match = re.search(pattern, code)
    difficulty = ""
    if match:
        difficulty = match.group(1).strip()
    else:
        pass
        ##print("Add difficulty to the leetcode submission: ")
    return difficulty

def get_the_file_name(problem_id: str, nameslug: str, lang: str) -> str:
    """
    Generate a file name based on problem ID, name slug, and programming language.

    Args:
        problem_id (str): Problem ID.
        nameslug (str): Name slug.
        lang (str): Programming language.

    Returns:
        str: Generated file name.
    """
    if lang in ('python3', 'python'):
        return f"{problem_id}-{nameslug}.py"
    elif lang == 'java':
        return f"{problem_id}-{nameslug}.java"
    elif lang == 'cpp':
        return f"{problem_id}-{nameslug}.cpp"
    elif lang == 'c':
        return f"{problem_id}-{nameslug}.c"
    elif lang == 'csharp':
        return f"{problem_id}-{nameslug}.cs"
    elif lang == 'javascript':
        return f"{problem_id}-{nameslug}.js"
    elif lang in ('mysql', 'mssql'):
        return f"{problem_id}-{nameslug}.sql"

def create_directory(logical_path: str):
    """
    Create a directory with the specified logical path.

    Args:
        logical_path (str): The logical path for the directory.
    """
    path = os.path.join(FILE_STORE_FOLDER, logical_path)
    if not os.path.exists(path):
        os.makedirs(path)

def create_file_and_copy_content(filename: str, logical_path: str, content: str):
    """
    Create a file in the specified directory and copy content to it.

    Args:
        filename (str): Name of the file to be created.
        logical_path (str): Logical path to the directory.
        content (str): Content to be written to the file.
    """
    path = os.path.join(FILE_STORE_FOLDER, logical_path)
    file_path = os.path.join(path, filename)
    with open(file_path, 'w') as file:
        file.write(content)

def parse_arguments():
    """
    Parse command line arguments to set the limit on how many recent submissions to classify.

    This function uses argparse to handle command line arguments. It expects an optional
    positional argument 'limit', which specifies the number of recent submissions to process.
    If 'limit' is not provided, it defaults to 1.

    Returns:
        int: The limit on the number of recent submissions to classify.
    """
    parser = argparse.ArgumentParser(description="Classify submissions based on tags and difficulty.")
    parser.add_argument('limit', type=int, nargs='?', default=1,
                        help='Number of recent submissions to classify. Defaults to 1.')
    args = parser.parse_args()
    return args.limit

def generate_filename(problem_id, title_slug, language, difficulty):
    """
    Generate a filename for saving the submission code, incorporating problem ID, title slug, language, and difficulty.

    The filename is constructed using the problem ID, title slug, and the programming language of the submission.
    If a difficulty level is provided (e.g., 'Easy', 'Medium', 'Hard'), it is prefixed to the filename for easier identification.

    Parameters:
        problem_id (str): The unique identifier for the problem.
        title_slug (str): A slugified version of the problem title.
        language (str): The programming language of the submission.
        difficulty (str): The difficulty level of the problem.

    Returns:
        str: The generated filename for the submission.
    """
    filename = get_the_file_name(problem_id, title_slug, language)
    if difficulty:
        filename = f"{difficulty}-{filename}"
    return filename



def process_submissions(limit):
    """
    Process and classify a specified number of recent submissions.

    This function fetches recent submissions up to the specified limit, classifies them based on tags
    and difficulty, and saves the code to the appropriate directory structure. It prints out the progress
    and results of classification.

    Parameters:
        limit (int): The maximum number of recent submissions to process and classify.
    """
    print("--------------------------------------------")
    print("Classifying the Submissions.\n")
    submitted_problems_list = fetch_recent_submission.fetch_recent_submission(limit)
    print(f"There are only {len(submitted_problems_list)} accepted submission(s) out of {limit}\n")

    for submission in submitted_problems_list:
        title_slug = submission[1]
        print(f"Working on problem: {title_slug}")

        tags = read_tags_from_code(submission[0], title_slug)
        difficulty = read_problem_category_from_code(submission[0])
        problem_id = fetch_problem_id_by_slug.get_problem_frontend_id(title_slug)

        filename = generate_filename(problem_id, title_slug, submission[2], difficulty)

        directory = '/'.join(tags)
        create_directory(directory)
        create_file_and_copy_content(filename, directory, submission[0])
        print()


def main():
    """
    The main function orchestrating the classification and saving of submissions.

    It parses command line arguments to determine the number of recent submissions to classify,
    processes and classifies those submissions, and provides a summary of the actions taken.
    """
    limit = parse_arguments()
    process_submissions(limit)
    print("--------------------------------------------")
    print(f"Check directory: {FILE_STORE_FOLDER}")
    print("Done going to sleep :)")

if __name__ == "__main__":
    main()