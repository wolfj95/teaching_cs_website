# Welcome to the repo for our website!

Here are some tips to get started adding content to the website.

 ## Setup

To make changes to the course website, use the Terminal to get to where you want the repository and
run the following commands on Linux, Mac, or Windows Subsystem for Linux. Make sure you already have
a GitHub account that has permission to access the repo.

    git clone https://github.com/jwolf95/teaching_cs_website
    cd teaching_cs_website
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    pelican content
    cd output
    python -m http.server

Nvaigate to http://localhost:8000/ in your favorite web browser to see your local build of the current website in a browser.

## Editing

Generally, you will only need to change files in the `content` directory. These are plain old text
files you can edit with any text editor. They are in a simple langauge called
[Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf);
you can basically just write text. Before you start editing, run `git pull` to make sure you
have the most recent version of the site.
While editing, it is helpful to use the `-r` flag to tell Pelican to rebuilt the site whenever there's a
change:

    pelican -r content

In general, it is helpful to keep one Terminal session running/rebuilding the site and another serving the site (via `python -m http.server` running from `output_local`).
Here's a quick tour of the site's content:

TODO

## Publishing changes

Once you are happy with your changes, you need to commit your work back to the repository,
build the site for publication, and push it to the production server. Before you can do this,
you'll need to add the server credentials to `upload.sh`; they are not included in this repository
because they are not public. Read `upload.sh` for setup instructions.

    git status
    git add [whichever files you changed]
    git commit -m "A message explaining what I changed"
    git push
    pelican content
    chmod a+rx upload.sh                         
    ./upload.sh

## More details

The site is built by a Python library called Pelican. It has [great documentation](http://docs.getpelican.com/en/stable/index.html).

# Credits
This workflow for collaborative website editing and publishing with pelican (as well as it's documentation) draws heavily from the model used by [Chris Proctor](https://github.com/cproctor)
