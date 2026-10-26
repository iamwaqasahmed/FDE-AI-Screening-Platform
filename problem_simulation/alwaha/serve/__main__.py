"""python -m alwaha.serve

Running this module starts the seeded mock server. Importing it only pulls in main, so a library import does not bind a port.
"""

from alwaha.serve.app import main

if __name__ == "__main__":
    # A direct run binds the port. Importing this module does not.
    main()
