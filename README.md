# AutoCoder
AutoCoder is an automated code generation tool designed to speed up the software development process by generating boilerplate code, templates, and other repetitive structures based on issues and predefined patterns.

Features

Code Templates: Jumpstart your projects with a variety of language-specific templates;
Customisable Generation: Tailor the generated code to your specific needs by specifying your prompt as a GitHub Issue;
Integration Support: Works as part of your CI/CD pipeline using workflows with GitHub Actions


- name: AutoCoder
  uses: AlyonaKlekovkina/AutoCoder@v1
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    openai_api_key: ${{ secrets.OPENAI_API_KEY }}
    repository: 'AlyonaKlekovkina/AutoCoder'
    issue_number: ${{ github.event.issue.number }}
    script_path: './scripts/script.sh'
    label: 'autocoder-bot'
