#!/usr/bin/env python
from github import Github
from github.InputFileContent import InputFileContent
import argparse
import urllib2
import fnmatch
import sys

parser = argparse.ArgumentParser(prog="gist", description="Search your GitHub Gists from terminal")
parser.add_argument("-l", "--list", help="List all of your gists", action="store_true")
parser.add_argument("-sf", "--search-filename", type=str, help="Search your gists via filename (wildcard supported)")
parser.add_argument("-sd", "--search-description", type=str, help="Search your gists via description")
parser.add_argument("-e", "--echo", type=str, help="Echo contents of specified file")
parser.add_argument("-c", "--create-gist", help="Create gist from stdin")
args = parser.parse_args()

#edit below line according to your credentials
github = Github("YourUsername", "YourPassword")
gists = github.get_user().get_gists()

if args.list:
	for gist in gists:
		for file_name in gist.files:
			if gist.files[file_name].language is not None:
				print file_name + " -> "  + gist.description + " [" + gist.files[file_name].language + "]"
			else:
				print file_name + " -> "  + gist.description

	quit()

if args.create_gist:
	data = sys.stdin.read()
#	create_gist(public boolean, file content in string, description)
	github.get_user().create_gist(True, {args.create_gist: InputFileContent(data)}, "Created from terminal")
	quit()

if args.search_filename is not None and len(args.search_filename) > 0:
	for gist in gists:
		for file_name in gist.files:
			if fnmatch.fnmatch(file_name, args.search_filename):
				print gist.description + " -> "  + file_name + " [" + gist.files[file_name].language + "]"
	quit()

if args.search_description is not None and len(args.search_description) > 0:
	for gist in gists:
		for file_name in gist.files:
			if args.search_description in gist.description:
				print gist.description + " -> "  + file_name + " [" + gist.files[file_name].language + "]"

	quit()

if args.echo:
	for gist in gists:
		for file_name in gist.files:
			if file_name == args.echo:
				print urllib2.urlopen(gist.files[file_name].raw_url).read()

	quit()

parser.print_help()
