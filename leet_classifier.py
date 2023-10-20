import os
import re
import fetch_recent_submission
import fetch_problem_id_by_slug


FILE_STORE_FOLDER = os.getcwd() + '/classification/'

def read_tags_from_code(code: str) -> list:
    """
    Extract tags from the code.

    Args:
        code (str): The code containing tags.

    Returns:
        list: A list of extracted tags.
    """
    pattern = r'lct\s*:\s*([^;]+);'
    match = re.search(pattern, code)
    tagslist = []
    if match:
        tagslist = list(match.group(1).strip().split(','))
    else:
        print("Add tags to the leetcode submission: ")
    return tagslist

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
        print("Add difficulty to the leetcode submission: ")
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


# Get submission details
recent_submission_code, recent_submission_titleslug, problem_lan = fetch_recent_submission.fetch_recent_submission()
# Extract tags
tags = read_tags_from_code(recent_submission_code)
# Extract difficulty
difficulty = read_problem_category_from_code(recent_submission_code)
# Get problem ID
problem_id = fetch_problem_id_by_slug.get_problem_frontend_id(recent_submission_titleslug)
print("Problem ID:", problem_id)

# Generate the file name
filename = get_the_file_name(problem_id, recent_submission_titleslug, problem_lan)
filename = difficulty+'-'+filename
# Create directories and save the file
create_directory('/'.join(tags))
create_file_and_copy_content(filename, '/'.join(tags), recent_submission_code)
print("Success")
