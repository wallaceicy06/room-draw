RoomDraw
========

A program to sort groups for room selection by point value, and resolve ties
randomly.

Description
-----------

This program sorts a groups of students for housing selection, resolving point
ties randomly. The output is an ordered list for room selection.  It is
designed specifically to serve [McMurtry College](http://mcmurtry.rice.edu) at
Rice University.

Usage
-----

Provide a plain text file of room groups, each separated by a line feed. Each
line must contain the number of points for each group, followed by a space,
followed by the name of the group. Execute

    roomdraw groupfile outfile

where `groupfile` is your plain text file of room groups, and `outfile` is the
file you want the results written to.

By default, groups are ordered from highest points to lowest points. To sort
in ascending order, pass the `-a` flag.

To adjust the seconds between random choices, use the `-d` flag and pass a
decimal number. By default, the delay is set at 0.5 seconds.

A list of command line options is also provided by passing the `-h` flag.

Sample
------

A sample names file `sample_groups.txt` is provided as part of this package. To
try the program out of the box, execute

    roomdraw sample_groups.txt sample_out.txt

Credits
-------

This program is loosely based on a similar
[program](https://github.com/kevinslin/eligibility_jack) written by Kevin Lin
(Rice '13). It was subsequently adapted for Room Draw by
[Adam Bloom](https://github.com/adam-bloom) (Rice '15).
