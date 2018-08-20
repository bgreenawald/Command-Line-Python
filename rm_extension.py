# Author: Ben Greenawald
# Removes all files in calling directory with extension

# Imports
import sys
import os

def rm_extension(extension, test = False):
    """ Deletes all files in directory with given extension

    Args:
        extension: Extension to remove.
        test: Whether this is being run from test
    """
    directory = os.getcwd()

    resp = "y"
    if not test:
        resp = input("Are you sure you want to deleted all files " + \
                        "in {0} with extension {1}? y/n: "\
                        .format(directory, extension))
    if resp != "y":
        sys.exit(0)
    else:
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                if not test:
                    print("Deleting " + \
                        str(os.path.join(directory, filename)))
                    os.remove(os.path.join(directory, filename))

if __name__=="__main__":
    try:
        extension = sys.argv[1]
        rm_extension(extension)
    except IndexError:
        print("Extension required")