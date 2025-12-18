Anaconda-Transition White Papers
================================

This repository holds the source and build tooling for the CaRCC Anaconda Transition Working
Group's project to document changes to Anaconda's Terms of Service from 2024-2025.
There are two white papers (here named "A" and "B").

- **White Paper A:** Staff/Researchers
- **White Paper B:** Institutional Leadership


Building
--------

The documents are compiled to PDF outputs from RestructuredText source via LaTeX using the
Sphinx build system. The `PAPERS` directory contains the source and build system for this.
To build the documents you need to run `make latexpdf` with suitable dependencies satisfied
(i.e., Sphinx and LaTeX). Assuming you have LaTeX available on your system, the
[uv](https://astral.sh/uv) package manager is a good approach to run the build:

```sh
uvx --from sphinx make latexpdf
```


Releases
--------

These documents are continually built using a GitHub Action the compiles the PDFs.
These assets are attached to each release here in the repo.
These receive their own DOI via the CaRCC Zenodo publishing platform.


Contributing
------------

We're actively encouraging the research community to participate in the refinement and
continual process of improvement and updates to these documents as it's a moving target.
This should be done either as an Issue or Pull Request. Feel free to open
an Issue to raise an item of concern for discussion. To contribute changes (small are large)
to the papers please open a Pull Request from your own fork to the `main` branch.

Once forked, clone your fork locally to make your changes.

```sh
git clone git@github.com:me/anaconda-transition
cd anaconda-transition
```

Make sure you're also able to pull changes from the upstream repository.

```sh
git remote add upstream git@github.com:carcc/anaconda-transition
git fetch --all
```

Commit your changes with a useful commit message.

```sh
git add --all
git commit -m '[Paper A] Fix description of XYZ'
```

Make sure your branch is up-to-date.

```sh
git pull upstream main
```

If this results in a merge conflict you'll need to resolve those before pushing
to your fork (so-called "origin").

```sh
git push origin main
```

Now you can open a PR by visiting the main repository and selecting your fork.

