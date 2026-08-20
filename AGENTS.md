# AGENTS.md — Workspace Guidelines & Rules

## SECRET HANDLING RULES

1. Never read .env files.
2. Never display API keys.
3. Never print environment variables containing credentials.
4. Never include credentials in source code.
5. Never include credentials in logs or experiment results.
6. Never commit .env files.
7. Never ask the user to paste credentials into chat.
8. API credentials may only be consumed by application runtime code.
9. When debugging API authentication, report only whether a credential is present or absent, never its value.
10. If a secret accidentally appears in terminal output, do not reproduce it in any response or documentation.
