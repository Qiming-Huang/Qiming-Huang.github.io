# Repository Guidelines

## Project Structure & Module Organization

This is a Jekyll site based on al-folio. Site configuration lives in `_config.yml`. Content pages are in `_pages/`, news entries in `_news/`, projects in `_projects/`, books in `_books/`, and publications in `_bibliography/papers.bib`. Shared templates are in `_layouts/` and `_includes/`; custom Ruby plugins are in `_plugins/`. Styles are in `_sass/` and `assets/css/`; JavaScript, PDFs, JSON, fonts, audio, and images belong under `assets/`. Helper scripts and CI entry points live in `bin/`. Do not edit generated output such as `_site/` or `.jekyll-cache/`.

## Build, Test, and Development Commands

- `bundle install`: install Ruby gems from `Gemfile`.
- `bundle exec jekyll serve`: run the site locally with live rebuilds.
- `bundle exec jekyll build`: build the static site into `_site/`.
- `bin/cibuild`: CI build wrapper; currently runs `bundle exec jekyll build`.
- `npm install`: install formatting dependencies.
- `npx prettier --check .`: check formatting.
- `npx prettier --write .`: format supported files.
- `pre-commit run --all-files`: run configured whitespace, EOF, YAML, and large-file checks.

## Coding Style & Naming Conventions

Use Markdown with YAML front matter for site content. Keep collection filenames descriptive and date-based where the collection already does so, for example `_news/announcement_1.md`. Follow existing Liquid patterns in `_includes/` and `_layouts/`. Use two-space indentation for YAML, Liquid, and Ruby where practical. Prettier is configured with `@shopify/prettier-plugin-liquid`, `printWidth: 150`, and ES5 trailing commas.

## Testing Guidelines

There is no dedicated unit test suite. Treat a clean Jekyll build as the baseline test. For content-only edits, run `bundle exec jekyll build`; for template, Sass, JavaScript, or config changes, also run `npx prettier --check .` and `pre-commit run --all-files`. Verify affected pages locally with `bundle exec jekyll serve`.

## Commit & Pull Request Guidelines

Recent history uses short imperative or summary-style commits such as `update`, `Add Teaching section to CV page`, and `Format workflow and vscode settings`. Prefer specific messages that describe the user-visible change. Pull requests should include a concise description, linked issue when applicable, screenshots for visual changes, and commands run. Do not include generated `_site/` output.

## Agent-Specific Instructions

Keep edits scoped and avoid broad formatting churn. Preserve user content in Markdown, BibTeX, JSON, and YAML files. When modifying templates or config, check the rendered site before reporting completion.
