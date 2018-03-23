# PyGist

PyGist is a CLI tool to create gists right from your terminal or echo your existing gists to your terminal.

# Installation

This tool depends on [PyGitHub](https://github.com/PyGithub/PyGithub). To install PyGitHub:

    pip install pygithub

Fire up your favorite text editor then edit line 18 according to your GitHub credentials.
 
    github = Github("YourUsername", "YourPassword")

To use it as a binary you have to copy gist.py file to your /usr/bin/ folder and make it executable.

    cp gist.py /usr/bin/gist
    chmod +x /usr/bin/gist

If your distribution's default python version is not 2.7.x then replace python with python2.7 on first line. 

## Listing your gists

    gist -l
    gist --list

Either of these commands will list your gists' filename, description and language.

    .bashrc -> Created from terminal [Shell]  
    NMOS.asc -> LTSpice IV NMOS Schematic [Public Key]  
    localize_date.php -> Localize date from a string using PHP [PHP]

## Searching via description

    gist -sd "Localize date"    

This will list all your gists that contains "Localize date" in their descriptions.

## Searching via filename

    gist -sf *.php

This will list all your gists that matches the given filename. This command supports *NIX like wildcard. 

## Printing contents of a gist

    gist -e file_name

This will echo the contents of the specified file. Redirect the output into a file to create a local copy of it as follows. 

    gist -e myfile.html > myfile.html

## Creating a gist

    gist -c "FileName"

The script takes input from stdin. If you run above command standalone, you can type whatever you want then press "Ctrl + D", your gist will be created with the filename you specified and the input you have given. Or alternatively you can pipe any other commands into this script as follows. 

    cat ~/.bashrc > gist -c ".bashrc"

# Contributing

 1. Fork the project
 2. Create your own branch
 3. Push your changes
 4. Open PR
