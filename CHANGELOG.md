# Changelog

This is the changelog file of `web-projects`. All notable changes to
this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The format will be:
- Added
- Changed
- Fixed
- Removed
- Security
- Refactored
- Performance
- Documentation

## Unreleased

### Added
- Added GitHub sponsorship information in the repository.
- Included a sitemap for the website.

### Changed
- **Dependency Changes:** Updated `fastapi`.
- Edited HTML metadata in the web pages.
- Edited the content in the `/about` page.

### Fixed
- Fixed an issue where the HTML pages weren't loading due to a `TemplateResponse` bug in `jinja2`.

### Removed
- Deleted the redundant `/fonts` directory.

## [0.1.0] - 2026-07-16

### Added
- Initialized the FastAPI server entry point in `server.py`.
- Configured deployment settings for Vercel via `vercel.json`.
- Added project metadata including `LICENSE.txt` (Apache 2.0), `CREDITS.md`, and `.gitignore`.
- Established `requirements.txt` with core dependencies (FastAPI, Jinja2).

---
[0.1.0]: https://github.com/anikethchavare/web-projects/releases/tag/v0.1.0