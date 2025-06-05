AutoCoder
AutoCoder is a GitHub Action that automates the process of generating code from GitHub Issues using OpenAI's ChatGPT, and creates a pull request with the generated code. It’s designed to streamline feature development and reduce manual coding for well-defined issues.

Features
Parses GitHub issues based on a specific label

Uses OpenAI's ChatGPT API to generate code

Automatically commits code and opens a pull request

Fully configurable and reusable

Inputs
Name	Required	Description
github_token	✅	GitHub token used for authentication and to create pull requests
openai_api_key	✅	API key for accessing the OpenAI API
repository	✅	The target repository where the action is being executed (owner/repo)
issue_number	✅	The issue number that triggered the action
script_path	✅	Path to the script that processes the issue and generates code using ChatGPT
label	✅	Label that triggers this action (default: autocoder-bot)

Outputs
Name	Description
pull_request_url	The URL of the created pull request with the new code

Example Usage
Here is an example of how to use AutoCoder in your workflow:

yaml
Copy
Edit
name: AutoCoder Workflow

on:
  issues:
    types: [labeled]

jobs:
  run-autocoder:
    if: contains(github.event.label.name, 'autocoder-bot')
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Run AutoCoder
        uses: AlyonaKlekovkina/AutoCoder@v1.0.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
          repository: ${{ github.repository }}
          issue_number: ${{ github.event.issue.number }}
          script_path: './scripts/script.sh'
          label: 'autocoder-bot'

Testing & Debugging
To test your action:

Create an issue in your repository with a label (e.g., autocoder-bot).

Ensure your script.sh properly reads and processes the issue description.

Watch the Actions tab to see if a pull request is generated automatically.

Versioning
To use a specific version of this action, use the version tag in the uses field. For example:

yaml
Copy
Edit
uses: AlyonaKlekovkina/AutoCoder@v1.0.0


Contributing
Feel free to fork, improve, and submit pull requests! Feedback and contributions are welcome.

