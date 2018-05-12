#!/usr/bin/env python

# this is a simple program that reads in a gene x sample file and experiment information
# performs differential expression analysis and then plots the top gene

# Version history:
# 2015-08-08    S. Stiegelmeyer    First revision

import sys
import os
import pandas
import scipy.stats


def usage(pname):
    bname=os.path.basename(pname)
    sys.stdout.write("Usage: %s -genes genefile.csv -meta metadata.csv -o geneplot.png\n" % (bname))


def arghandler(args):
    i = 1  # args[0] is always the program name, skip it
    argdict = {}
    mykey = None
    defval = None
    err = False

    while i < len(args):
        # check for argument flag
        if args[i].startswith('-') and mykey is None:
            mykey = args[i]
        elif mykey is not None:
            if not args[i].startswith('-') and mykey not in argdict:
                argdict[mykey] = args[i]
            elif mykey not in argdict:
                argdict[mykey] = defval
            else:
                sys.stderr.write("%s is given multiple times.\n" % mykey)
                err = True
                break
            mykey = None
        else:
            sys.stderr.write("%s given without command argument.\n" % (args[i]))
            err = True
            break
        i += 1

    return argdict, err


def checkParameters(args):
    argdict, err = arghandler(args)
    if not err:
        if '-genes' in argdict:
            if not os.path.exists(argdict['-genes']):
                sys.stderr.write("%s does not exist (-genes).\n" % argdict['-genes'])
                err = True
        else:
            sys.stderr.write("Must specify gene file (-genes).\n")
            err = True
        if '-meta' in argdict:
            if not os.path.exists(argdict['-meta']):
                sys.stderr.write("%s does not exist (-meta).\n" % argdict['-meta'])
                err = True
        else:
            sys.stderr.write("Must specify meta data file (-meta).\n")
            err = True
        if '-o' not in argdict:
            sys.stderr.write("Must specify figure file (-o).\n")
    return argdict, err


def main(args):
    argdict, errmess=checkParameters(args)
    if errmess:
        usage(args[0])
        exit(1)

    sys.stdout.write("Arguments are valid!\n")


if __name__ == "__main__":
    if not sys.argv[1:]:
        usage(sys.argv[0])
        exit(1)
    else:
        main(sys.argv)
