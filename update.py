# -*- coding: utf-8 -*-
import subprocess

from github import Github
from github.InputFileContent import InputFileContent

from credentials import CREDS
from driver import main
from driver import getlongterm

subprocess.call(["python", "driver.py"])

g = Github(CREDS['TOKEN'])
spotify_gist = g.get_gist(CREDS['GIST_ID'])
spotify_gist_long_term = g.get_gist('20d9ea0342b543a1460fd13be64a7c60')
f = InputFileContent(main())
eggs = InputFileContent(getlongterm())
spotify_gist.edit('🎧 My music activity over the last 4 weeks',
                  {'🎧 My music activity over the last 4 weeks': f})
#spotify_gist_long_term.edit('🎧 My music activity over the last 6 months',
#                  {'🎧 My music activity over the last 6 months': eggs})
spotify_gist.edit('🎧 My music activity over the last 6 months',
                  {'🎧 My music activity over the last 6 months': eggs})
