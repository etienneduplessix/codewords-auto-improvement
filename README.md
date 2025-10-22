# Recreate the CodeWords Auto-Improvement AI Agent  
  
## Goal  
Build a minimal prototype of a self-improving agent that can:  
- Analyze its own Python code  
- Suggest improvements or fixes  
- Apply them automatically (or after human approval)  
- Log reasoning and version changes to a local database  
  
## Architecture  
| Layer | Description |  
| --- | --- |  
| **Frontend (optional)** | Simple dashboard (HTML + JS or React) showing code diff, logs and agent status |  
| **Backend** | FastAPI service orchestrating the loop |  
| **Agent Core** | LangChain (or custom orchestration) running GPT-4 / Claude for reasoning |  
| **Storage** | SQLite or PostgreSQL storing version history and feedback |  
| **Evaluator** | Script comparing output quality pre-/post-update |  
  
## Workflow  
1. Agent loads its own codebase (`/src` folder)  
2. Selects a file to review  
3. Prompts the LLM to analyze and propose edits  
4. Writes the diff and saves a new version  
5. Runs unit tests  
6. Logs the results and repeats periodically  
  
## Milestones  
- FastAPI service skeleton  
- Self-read and propose changes using an LLM  
- Git-like version tracking and test runner  
- Minimal dashboard  
- Automatic iteration loop  
  
## Stretch Goals  
- Implement a competence graph showing which functions improve over time  
- Add evaluation prompts (e.g. "improve speed of X")  
- Connect to GitHub for real commit automation
