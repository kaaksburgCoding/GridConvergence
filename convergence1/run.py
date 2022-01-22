from __future__ import print_function
import pandas as pd
#from convergence1 import Convergence1
import interface
import argparse


def main(out_path, analytical=None):

    #returns a 2d-list (4x120) containing tuples of the format (grid size, value) of
    # all possible gridsize combinations and measurement points
    combList = interface.assemble_cominations()

    c_rows = len(combList)
    c_columns = len(combList[0])

    for i in range (c_rows) :

        for j in range (c_columns) :

            grids = [(combList [i][j][0][0], combList[i][j][0][1]),
                     (combList[i][j][1][0], combList[i][j][1][1]),
                     (combList[i][j][2][0], combList[i][j][2][1])]

            print(grids)

            convergence = interface.Convergence1()
            convergence.add_grids(grids)
            print(convergence)  # doctest:+ELLIPSIS

            # Write the report
            with open(out_path, 'w') as f:
                f.write(str(convergence))

            print("First Round")


def cl_interface():


    # Prepare command line parser
    desStr = "Perform grid convergence study on input file."

    parser = argparse.ArgumentParser(description=desStr)

    parser.add_argument("-o", "--out",
                        type=str,
                        help=("output file path"),
                        default='verify_report.txt')

    parser.add_argument("-a", "--analytical",
                        type=str,
                        help=("Expected analytical value"))

    args = parser.parse_args()

    out_path = args.out
    analytical = args.analytical

    main(out_path, analytical)

    return

cl_interface()