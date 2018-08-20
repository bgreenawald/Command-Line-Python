# Author: Ben Greenawald
# Removes all files in calling directory with extension

# Imports
import sys
import os

def add_extension_rec(extension, directory = os.getcwd(), test = False):
    """ Adds given extension to all files in directory recursively.

    Args:
        extension: Extension to add.
        test: Whether this is being run from test
    """

    resp = "y"
    if not test:
        resp = input("Are you sure you want to add the extension" + \
                    " {0} to all files in {1}? y/n: "\
                    .format(extension, directory))
    if resp != "y":
        sys.exit(0)
    else:
        for (dirpath, _, filenames) in os.walk(directory):
            for filename in filenames:
                if not test:
                    print(str(os.path.join(dirpath, filename)) + " --> " + \
                            str(os.path.join(dirpath, filename)) +  extension)
                os.rename(os.path.join(dirpath, filename),
                        os.path.join(dirpath, filename) + extension)

if __name__=="__main__":
    try:
        extension = sys.argv[1]
        add_extension_rec(extension)
    except IndexError:
        print("Extension required")