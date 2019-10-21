# Imports
import math

import spotipy
import spotipy.util as util
from credentials import CREDS

# Global variables
CLIENT_ID = CREDS['CLIENT_ID']
CLIENT_SECRET = CREDS['CLIENT_SECRET']
USERNAME = 'Your username'
SCOPE = 'user-top-read'  # user-read-recently-played


def generateBarChart(fraction, size):
    syms = " ▏▎▍▌▋▊▉█"

    frac = size * 8 * fraction
    barsFull = frac // 8
    semi = round(frac % 8)
    barsEmpty = size - barsFull - 1

    return('|' + (syms[8] * int(barsFull)) + syms[semi:semi+1] +
           (syms[0] * int(barsEmpty)) + '|')


def main():
    # Token generation
    token = util.prompt_for_user_token(USERNAME, scope=SCOPE,
                                       client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri='http://localhost/')

    # Driver code
    if token:
        sp = spotipy.Spotify(auth=token)
        artists = {}
        final = ''
        results = sp.current_user_top_tracks(50, time_range='short_term')
        for t, res in enumerate(reversed(results['items']), start=1):
            for r in res['artists']:
                if(r['name'] in artists):
                    artists[r['name']] += math.log2(t)
                else:
                    artists[r['name']] = math.log2(t)
        artists = sorted(artists.items(), key=lambda x: (x[1], x[0]),
                         reverse=True)[:10]
        freq = sum(x[1] for x in artists)
        for i, j in artists:
            bar = generateBarChart(j/freq, 20)
            final += '{:<20} {:^20} {:>8.2f}%\n'.format(
                i, bar, j/freq*100)
        return final
    else:
        return("Can't get token for", USERNAME)
