
![LaTeX build](../../workflows/LaTeX%20build/badge.svg)
[![Latest build of LeoCStein.pdf](https://img.shields.io/badge/LeoCStein.pdf-latest-orange.svg?style=flat)](../gh-action-result/pdflatex/LeoCStein.pdf)
[![Latest build of LeoCStein-NoPubs.pdf](https://img.shields.io/badge/LeoCStein--NoPubs.pdf-latest-orange.svg?style=flat)](../gh-action-result/pdflatex/LeoCStein-NoPubs.pdf)
[![Latest build of LeoCStein-PubsOnly.pdf](https://img.shields.io/badge/LeoCStein--PubsOnly.pdf-latest-orange.svg?style=flat)](../gh-action-result/pdflatex/LeoCStein-PubsOnly.pdf)

# Leo's curriculum vitae LaTeX source

Please feel free to clone this repo if you like the style and want to use it for your CV.  If you're going to customize it, you need to know the layout of the contents:
- [LeoCStein.tex](LeoCStein.tex): The top-level file. Compiling this
  gives the full CV. However the sources for list of publications,
  list of talks, and contact info are in other files (listed below).
- [LeoCStein-NoPubs.tex](LeoCStein-NoPubs.tex): Another top-level file, which just sets a flag and includes the above. Generates a CV without pub list.
- [LeoCStein-PubsOnly.tex](LeoCStein-PubsOnly.tex): Another top-level file. Generates just a publication list (with contact info header).

The following files are included by the above (they can not be compiled by themselves):
- [ContactContent.tex](ContactContent.tex): Contains the contact info header with physical address, email address, web site, office phone
- [PubsContent.tex](PubsContent.tex): Contains list of publications, 
- [TalksContent.tex](TalksContent.tex): Contains list of talks.

If you're going to use this repo as a starting point for your own CV, you'll probably have to change a bunch of filenames.
If you're going to keep it on github and want the github action that builds the PDFs (badge links above) to work, then you'll want to change the corresponding file names in the [.github/workflows/pdflatex.yml](.github/workflows/pdflatex.yml) workflow file.
