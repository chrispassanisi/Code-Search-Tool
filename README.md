# GitHub Code Search
This Python script allows you to search for Python code files across GitHub repositories using the GitHub API. By providing a query, the script searches GitHub for files containing the specified code, and outputs the URLs of the results.

---

### Features
Sorts results by the most recently indexed code.
Outputs file names and direct URLs to the found code.


Edit the query variable in the main() function to specify your code.
Example:

python
Copy code
query = "Input your code here." + " is extension:py"
Run the script:

bash
Copy code
python github_code_search.py
The script will print out the names of the Python files that match your query, along with direct URLs to view them on GitHub.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.
