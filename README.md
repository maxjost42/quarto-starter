# Quarto-starter
This project should help you get into writing beautiful (interactive) reports using quarto. Example projects are:
* [A basic simple jupyter like code notebook](#rendering-the-test-quarto-notebook-containing-only-python)
* [A more advanced notebook that produces either a jupyter like HTML output or a LaTeX pdf](#more-advanced-notebook-example-for-a-beautiful-latex-pdf-report)

The explanations are editor independent and require only CLI-commands, to better how quarto is used, but there is also a vscode quarto extension, that maybe will make your life a bit easier.

## Intro
**What is Quarto:**
Quarto is a code notebook Tool like `jupyter-notebooks`. The main differences are:

* that quarto also has the capabilities for converting your notebook into a nice PDF report with most of the formatting, cross referencing and image/math/text alignment features you already know from LaTeX (In fact LaTeX is part of the quarto Toolchain therefore quarto most likely converts it's simpler commands into LaTeX commands on the Backend)
* that the plain quarto notebook files, are not unreadable jibberish like jupyters files, but they are written in plain Markdown, where the Markdown code blocks are the actual code cells of your notebook. This makes quarto notebook files exceptionally nice to read and makes them perfectly compatible with git.
* You can use multiple programming Languages in the same Notebook. The possible options are python, R, Julia and Observable
* You can define multiple output File types for your quarto notebooks, two of them are  HTML (useful if you wan't to publish your notebook as a dynamic or static website) and PDF (useful If you have to do assignment/work/lab/development reports).

So you can think of quarto as the LaTeX under the code notebook tools. And it's workflow is also the same: You write your `.qmd` (abbrev. for Quarto Markdown) File like the `test.qmd` in this repo and then you call `quarto preview test.qmd` to render a preview of your output File types or use `quarto render test.qmd` to generate the final output files.

**Main Reasons To Use Quarto:**
"Quarto is the god of code notebooks" - Max 2025 driving with the hype train

**Main Interface**
Quarto is controlled through commands (in a YAML format) that you write as comments in your Notebook. This has the benefit that you can (additionally to the Principle "code is documentation") live by the Principle "code is visualization and documentation formatting". Enabling you to become the true "All the work in one single File" kind of person (Which obviously isn't perfect for every situation). For further explanations on the quarto commands, read through the comments in `test.qmd`

## Installations required from you (sadly)
For now it looks like you need to set up a few things that are not automatically installed by the beautiful package manager [`uv`](https://docs.astral.sh/uv/).

If you don't have uv installed yet then check follow this [Installation guide](https://docs.astral.sh/uv/getting-started/installation/) and after installation got to this projects root directory and run:
```bash
uv sync
```
This should automatically install all dependencies **except the ones below:**

### Quarto
Install Quarto for your OS with [this Installation Guide](https://quarto.org/docs/get-started/). For Windows, this means just downloading the msi Installer, restarting your PC once and everything should be working already.

When you are done with that run (you should do this with your python venv activated):
```bash
quarto check
```
To see which tools from below you still need to install (but no need to install them for the `test.qmd` notebook).

### TinyTex
If you have not already installed a LaTeX distribution on your machine, quarto will not be able to render PDF outputs. In this case install tinytex:
```bash
quarto install tinytex
```

## rendering the test quarto notebook containing only python
In this project there already exists a `test.qmd` File, which includes a basic plot and some Text, to check if your installation is working. But the following steps apply to your own new quarto notebooks as well.

You need a virtual environment containing `jupyter` (quarto uses jupyter in it's toolchain, therefore it is a must have for quarto notebooks) and of course the packages which are imported in your notebook. For this project a venv is provided by uv already containing all the required packages.

Then you have to activate the environment before you run quarto by:
```bash
# on Linux
source .venv/bin/activate
# use 'deactivate' if you want  to deactivate the environment again
```
```PowerShell
# on windows
.\.venv\Scripts\activate
# also use 'deactivate' if you want to deactivate the environment again
```

And then run
```bash
quarto preview test.qmd
```

## more advanced Notebook example for a beautiful LaTeX-PDF report
The more advanced Notebook is located at `latex_pdf_example/authoring.qmd` and needs two additional files, namely:
* `latex_pdf_example/references.bib` A typical BibLaTeX references file with citations
* `latex_pdf_example/mathjax.html` A mathjax Configuration file, which is needed to make Equation cross referencing work both for HTML and PDF output (For the more interested ones of you: this is a solution for a very annoying problem taken from [here](https://github.com/quarto-dev/quarto-cli/issues/4136)).

The Example includes:
- Basic Document style settings for LaTeX
- various basic text types (Lists, Sections, Math, ...)
- Cross referencing of Section, Figures, Equations
- One citation of a funny paper
- hidden/shown code snippets with hidden/shown outputs

To render the pdf version run:
```bash
quarto render .\latex_pdf_example\authoring.qmd --to html
```
More explanation to come...

## PS: Read this if you like the structure of this project
The structure of this project was solely created locally by running:
```bash
cd ~/myrepos
uv init --package quarto-starter
nvim README.md
git add *
git add .gitignore
git commit -m "Initial commit"
gh repo create
```
Where `~/myrepos` is just my local path where I store git repositories, `uv init --package name` creates the following project structure:
```bash
quarto-starter
├── .gitignore
├── pyproject.toml
├── README.md
├── src
│   └── quarto_starter
│       └── __init__.py
└── uv.lock
```
With `nvim` I edited the contents of the README. The `git` commands add all the files above to the local git repo (you can delete the `.python-version` File since it's just there to define the python version and that is already handled by uv in the `pyproject.toml`).
And finally `gh repo create` (Github-CLI Tool) adds the local repo to your Github repository list.
**And you never have to leave the Terminal ^^**
