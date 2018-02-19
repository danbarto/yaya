# yaya

Tools that help converting histograms from root files to YAML. Latex functions might follow in the future.

Instructions for ROOT6 installation on OSX (using [homebrew](https://brew.sh/)).
First check:
`brew info root6`

Install the missing dependencies and requirements again using brew. Most likely `cmake` is missing, in this case do

`brew install cmake`

Then one can simply install ROOT6 using

`brew install root6`

Afterwards, add the following line to your bash_rc or bash_profile:

`source $(brew --prefix)/bin/thisroot.sh`
