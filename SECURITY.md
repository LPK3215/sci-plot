# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in sci-plot, please report it responsibly.

### How to Report

**Email**: 17538703215@163.com

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes (optional)

### Response Time

- **Initial response**: Within 72 hours
- **Status update**: Within 1 week
- **Fix timeline**: Depends on severity (critical issues prioritized)

### Scope

sci-plot is a prompt generation tool that:
- Does not generate images directly
- Does not connect to external services
- Does not handle sensitive data

Security concerns typically relate to:
- Prompt injection vulnerabilities
- File path traversal in content analysis
- Malicious content in generated prompts

### Safe Usage

- Always review generated prompts before using them
- Do not use sci-plot to analyze untrusted or malicious files
- Be cautious when pasting prompts into external image generation services

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Disclosure Policy

- Vulnerabilities will be disclosed publicly after a fix is released
- Reporter will be credited (unless anonymity is requested)
- Security advisories will be published on GitHub
