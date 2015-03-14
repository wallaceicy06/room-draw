import argparse
import random
import time
import sys

parser = argparse.ArgumentParser('roomdraw')
parser.add_argument('infile', \
         help='the file containing the list of room groups to randomly sort')
parser.add_argument('outfile', \
         help='the file to output the results to')
parser.add_argument('-d', '--delay', metavar='seconds', required=False, \
         type=float, default=0.5, help='the delay between selections in '
         'decimal seconds (0.5 by default)')
parser.add_argument('-a', '--ascending', required=False, \
         action='store_true', default=False, help='sort in ascending order ' + \
         '(descending by default)')

MCM_CREST = """
   `/:.                                            .:+.
    `///.           McMURTRY COLLEGE             .///. ``
      .///.                                    .///- ``
        -///.        .-:////+ooo+/:-.        .///-```
          -///.  .:oyhhdyyddshydhydhhyo:.  .///-````
           `-/++sydyysddshhdsshddoyddddhys++/-````
            `/hhhsyhsyhddyyyhhysshdddhsdhdhh/```
           .shdssyohhhyo//+////+//+yhhhyyosyys-
          :yyyyy   . +    /+sssyo     .   yyyhy:
         :hhsyh    .sdho:+sdddddm+ os .    hhhhh:
        .hdsyyh    `oddyoyymdmmdds ydd/``-:hyhhdy.
        ohhdhhd    `.:ddmdddddddd- + o-.   hdssyy/
       `hdhyyhh     -`-ymmmddddms..s--     hdhhhdh.
       -hdyhydh     /o:/mdmdmmdy:  :h+     hyyyhhh:
       -hdshydd    /ymddhhhoydhohy/:+h     dhyyyhh:
       `hdsyyddo    /s+o-+hhhdmddddooy    +ddysydh.
        sdhhhddh/      ` +ddd+sdddy/+/    yddhyyh+`
        .hdhyyyyys:  .oyoydddo-+ddhs/.   +ydddhyy-
         +hsyhhddho` :yhodoo+yssddds.   sddyyyhh/
         +yyddhhdddy.`.-:/::+ymdhs:`` +hddhyhyy/
      :-``/shddddddddyo+/+oso+s++ooosdddhyhddy:```-:
      -oo::/+shdddddddddddddddddhdddddhyhdhyo///:+o:
       `sdhs-``/ydddhdddddddhhddddddhyhdhs:``-ohds.-.
     `+hdy:+o-  `:ohhddddddddddddddyhhho.   -o+:yho+.`
   `:hdy:   -o.     -/oyhdddddddhyso:.     `o-   :ydh:`
 `oyds-                 :hydddhoy:                 -omyo.
 -yh+                   -yyhs:+yy:                   +hh-
                         sys///ss`
                         `+osso+`
"""

def welcome():
    """
    Prints the McMurtry crest to stdout. Returns when the user confirms the
    start of the program by typing any key.

    Arguments:
        none

    Returns:
        none
    """

    print MCM_CREST
    print 'Welcome to McMurtry College Room Draw.'
    print 'This program will sort rooms for selection by highest points, ' + \
          'resolving ties randomly.'
    print 'Hit ENTER to begin...'
    raw_input('')

def compare_with_ties(a, b):
    """
    """
    diff = cmp(a, b)
    return diff if diff else random.choice([-1,1])

def run_roomdraw(names_file, delay=0.5, is_desc=False):
    """
    Orders the provided room groups by point value, with ties resolved randomly.
    Groups with highest points will be selected first.

    Arguments:
        names_file - the path of the file containing a line separated list of
            rooms. Each line must contain the number of points for a room
            followed by the name of the group separated by one space.
        delay (optional) - the delay between successive picks, default is 0.5

    Returns:
        the list of room groups, ordered by points and ties resolved randomly
    """

    draw_order = []

    try:
        with open(names_file, 'r') as groups_f:
            lines = groups_f.readlines();

            groups = []

            for line in lines:
                l = line.split()
                groups.append((float(l[0]), (' '.join(l[1:]).strip())))

            draw_order = sorted(groups, key=lambda g: g[0], \
                                cmp=compare_with_ties, reverse=is_desc)

            for i in xrange(len(draw_order)):
                pts, group = draw_order[i]

                print str(i + 1) + ': ' + group + ' (' + str(pts) + ')'
                time.sleep(delay)

            return draw_order

    except IOError:
        print >> sys.stderr, 'There was an error opening the specified ' + \
                'file \'' + names_file +'\' for read.'
    except ValueError:
        print >> sys.stderr, 'There was an error in the format of the ' + \
                 'groups file.'

    sys.exit(-1)


def write_results(out_file, draw_order):
    """
    Writes the specified groups to a file in the same format that run_roomdraw
    prints to stdout.

    Arguments:
        out_file - the path of the file to write the results to
        draw_order - the list of group tuples (points, name) in selection order

    Returns:
        none
    """

    try:
        with open(out_file, 'w') as out_f:
            out_f.write('Selection Order:\n')

            for i in xrange(len(draw_order)):
                pts, group = draw_order[i]
                out_f.write(str(i + 1) + ': ' + group + ' (' + str(pts) + ')\n')

    except IOError:
        print >> sys.stderr, 'There was an error opening the specified' + \
                ' file \'' + out_file +'\' for write.'

# Main runner for the program.
if __name__ == '__main__':
    args = parser.parse_args();

    welcome()
    draw_order = run_roomdraw(args.infile, args.delay, not args.ascending)

    write_results(args.outfile, draw_order)
