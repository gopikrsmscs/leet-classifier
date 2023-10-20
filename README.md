# Leet-Classifier

**Leet-Classifier** is an open-source Python project designed to automate the process of classifying and organizing your LeetCode submissions. It extracts tags and difficulty information from your code and stores your submissions in well-structured directories. This project aims to assist you in effectively managing your LeetCode solutions, making it easier to find and review your code.

## Prerequisites

Before you get started with **Leet-Classifier**, ensure you have the following prerequisites:

- Python 3.x installed on your system.

## Installation

You can clone the repository to your local machine and set up the project using the following commands:

1. Clone the repository:

```bash
git clone https://github.com/gopikrsmscs/leet-classifier.git
```
2. Change the working directory to the project folder:

```bash
cd leet-classifier
```
## Configuration
To use leet-classifier, you need to configure it with your LeetCode cookie. Here's how you can do it:
Inside cookie.json, add your LeetCode cookie as follows:
```json
{
    "Cookie": "your_leetcode_cookie_here"
}
```
Ensure that you replace "your_leetcode_cookie_here" with your actual LeetCode cookie. You can obtain your LeetCode cookie by inspecting your browser's developer tools while logged in to LeetCode.

## Usage
Once you've configured the tool with your LeetCode cookie, you can run the script to fetch, classify, and store your recent LeetCode submissions.

```bash
python leet_classifier.py
```

## Contributing
We welcome contributions to make this project even better. If you have suggestions, bug reports, or feature requests, please follow these steps:

Open an issue to discuss your ideas or report a problem.
Create a pull request if you'd like to contribute code improvements.
Your contributions will help the leet-classifier to enhance experience.

## Acknowledgments
If you find this project useful, please consider giving it a star. Your support encourages further development and helps other leetcode entuasists discover this tool.

## License
This project is licensed under the MIT License. For more details, please refer to the LICENSE file in this repository.



