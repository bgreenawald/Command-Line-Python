# Author: Ben Greenawald
# Removes all files in calling directory with extension

# Imports
import sys
import os

def add_extension(extension, directory = os.getcwd(), test = False):
    """ Adds given extension to all files in directory

    Args:
        extension: Extension to add.
        test: Whether this is being run from test
        directory: Directory of interest
    """

    resp = "y"
    if not test:
        resp = input("Are you sure you want to add the extension" + \
                    " {0} to all files in {1}? y/n: "\
                    .format(extension, directory))
    if resp != "y":
        sys.exit(0)
    else:
        for filename in os.listdir(directory):
            if not os.path.isfile(os.path.join(directory, filename)):
                continue

            if not test:
                print(str(os.path.join(directory, filename)) + " --> " + \
                        str(os.path.join(directory, filename)) +  extension)
            os.rename(os.path.join(directory, filename),
                    os.path.join(directory, filename) + extension)

if __name__=="__main__":
    try:
        extension = sys.argv[1]
        add_extension(extension)
    except IndexError:
        print("Extension required")