# Quarto-starter
This project should help you get into writing beautifull (interactive) reports using quarto.

## Intro
**Main Reasons To Use Quarto:**
(later edit:) "Quarto is the god of code notebooks".
Quarto is a kind of document formating tool (like LaTeX (In fact LaTeX is part of the Quarto Toolchain)) that enables the creation of (interactive) reports in HTML-, PDF-, Presentation-formats from code notebooks like jupyter, marimo or RMarkdown.

**Main Interface**
Quarto is controled through commands (in a YAML format) that you write as comments in your Notebook. This has the benefit that you can (additionally to the Principle "code is documentation") live by the Principle "code is vizualization and documentation formatting". Enabelingyou to becomethe true "All the work in one single File" kind of person.

## Installations required from you (sadly)
For now it looks like you need to set up a few things that are not automatically installed by the beautifull package manager [`uv`](https://docs.astral.sh/uv/).

If you don't have uv installed yet then check follow this [Installation guide](https://docs.astral.sh/uv/getting-started/installation/) and after installation got to this projects root directory and run:
```bash
uv sync
```
This should automatically install all dependencies **except the ones below:**

### Quarto
Install Quarto for your OS with [this Installation Guide](https://quarto.org/docs/get-started/)

When you are done with that run:
```bash
quarto check
```
To see which tools from below you still need to install.
