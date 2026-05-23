# Security & Sanitization Guidelines

## Never Commit

- API credentials
- LWA client secrets
- AWS access keys
- refresh tokens
- production SQL
- company schemas
- vendor pricing
- customer information
- internal business rules

## Recommended Public Portfolio Approach

Share:

- sanitized screenshots
- architecture diagrams
- mock datasets
- high-level extraction patterns
- documentation of approach

Do not share:

- raw production code
- proprietary backend logic
- internal database structures
- confidential vendor workflows

## Environment Variables

Use environment variables or a local `.env` file that is excluded from Git.

Example `.gitignore` entries:

```text
.env
*.key
*.pem
credentials.json
config.local.json
exports/latest/*.csv
exports/archive/
```
