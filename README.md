# Pre-requirements

1. Install `uv` python package manager
   ```shell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

# Set up Guide

Installation guide for a Windows Operating system

1. Create env: `uv venv`
2. Activate env: `source .venv/Scripts/activate`
3. Install dependencies `uv pip install .`
4. Set up environment variables `mv .env.example .env`
   ```.env
    GEMINI_API_KEY=your_gemini_api_key // Get it from: https://aistudio.google.com/apikey
    GOOGLE_API_KEY=your_gemini_api_key
    MODEL=gemini/gemini-2.0-flash
    SERPER_API_KEY=your_serper_api_key // Get it from: https://serper.dev/
    OPENAI_API_KEY=your_openai_api_key // Get it from: https://platform.openai.com/api-keys
    OPENAI_MODEL=gpt-3.5-turbo
    // The following ENV variables are extracted from the course Jupiter files:
    TRELLO_API_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcHAiLCJleHAiOjE3OTk5OTk5OTksInN1YiI6MzI1NzU4OCwiYXVkIjoiV0VCIiwiaWF0IjoxNjk0MDc2ODUxfQ.J2y5f5YfuKjC7JzYCskbUzgB87ZpVsWFQHQN_zuBynI
    TRELLO_API_TOKEN = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcHAiLCJleHAiOjE3OTk5OTk5OTksInN1YiI6MzI1NzU4OCwiYXVkIjoiV0VCIiwiaWF0IjoxNjk0MDc2ODUxfQ.J2y5f5YfuKjC7JzYCskbUzgB87ZpVsWFQHQN_zuBynI
    TRELLO_BOARD_ID = 66c305eacab50fcd7f19c0aa
    DLAI_TRELLO_BASE_UR = http://jupyter-api-proxy.internal.dlai/rev-proxy/trello
   ```

# Execute lesson example

## Lesson 1: Automated Plan Project

```bash
uv run python -m src.automated_project.main
```

## Lesson 2: Project Process Report

```bash
uv run python -m src.project_process_report.main
```
