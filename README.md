# AutoCoder 🤖

A GitHub Action that **automates code generation** from GitHub issues using OpenAI's ChatGPT, then commits the new code and opens a pull request. Think of it as a **feature-by-issue code assistant** right in your CI/CD pipeline! 

---

##  Features

-  **Label-driven automation** — Trigger code generation by labeling an issue (default label: `autocoder-bot`)
-  **ChatGPT-powered coding** — Parses issue descriptions and generates relevant code via OpenAI API
-  **Auto PR creation** — Pushes the generated code and opens a pull request automatically
-  **Fully configurable** — Adapt to your repo’s structure and workflow with ease

---

##  Inputs

| Input Name           | Required | Description |
|----------------------|:--------:|-------------|
| `github_token`       |  Yes    | Token for GitHub authentication (use `${{ secrets.GITHUB_TOKEN }}`) |
| `openai_api_key`     |  Yes    | Your OpenAI API key (`${{ secrets.OPENAI_API_KEY }}`) |
| `repository`         |  Yes    | Target repo in `owner/repo` format (`${{ github.repository }}`) |
| `issue_number`       |  Yes    | The number of the issue triggering the action (`${{ github.event.issue.number }}`) |
| `script_path`        |  Yes    | Path to your script (e.g., `./scripts/script.sh`) that calls ChatGPT |
| `label`              |  No     | Label to watch for (default: `autocoder-bot`) |

---

##  Outputs

- `pull_request_url`: URL of the pull request created with the generated code

---

##  Usage Example

Add the following workflow to your repository (e.g., `.github/workflows/autocoder.yml`):

```yaml
name: AutoCoder Workflow

on:
  issues:
    types: [labeled]

jobs:
  run-autocoder:
    if: contains(github.event.label.name, 'autocoder-bot')
    runs-on: ubuntu-latest

    steps:
      - name: Checkout the repo
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
````

With this setup:

1. Add the `autocoder-bot` label to an issue in your repo.
2. The Action runs, triggering your script to generate code via ChatGPT.
3. A pull request is opened with the suggested code automatically.

---

## Getting Started

1. Copy the workflow snippet above into your repo at `.github/workflows/autocoder.yml`.
2. Create a script (e.g., `scripts/script.sh`) that:

   * Reads the issue content
   * Sends relevant prompts to ChatGPT
   * Saves the returned code into working directory files
3. Set your GitHub secrets:

   * `GITHUB_TOKEN` (provided by GitHub Actions)
   * `OPENAI_API_KEY` (from your OpenAI account)

---

## Benefits & Use Cases

* **Speeds up feature development** — Focus on crafting clear issue descriptions; the Action handles boilerplate generation.
* **Standardizes code scaffolding** — Enforce consistent code patterns generated via prompt.
* **Low-effort setup** — Add the workflow once and let it run indefinitely.
* **Highly expandable** — Customize your scripts, prompt engineering, or repository structure as needed.

---

## Contributing

Your contributions are welcome! To get involved:

1. Fork the repo
2. Make changes (e.g., support additional languages or prompt variations)
3. Submit a pull request

