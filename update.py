# -*- coding: utf-8 -*-
import subprocess

from github import Github
from github.InputFileContent import InputFileContent

from credentials import CREDS
from driver import main

subprocess.call(["python", "driver.py"])

g = Github(CREDS['TOKEN'])
spotify_gist = g.get_gist(CREDS['GIST_ID'])
f = InputFileContent(main())
spotify_gist.edit('🎧 My music activity over the last 4 weeks',
                  {'🎧 My music activity over the last 4 weeks': f})
