import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user.
    """

    # Create Argument Parser object
    parser = argparse.ArgumentParser()

    # Argument 1: Image folder
    parser.add_argument(
        '--dir',
        type=str,
        default='pet_images/',
        help='path to the folder of pet images'
    )

    # Argument 2: CNN architecture
    parser.add_argument(
        '--arch',
        type=str,
        default='vgg',
        help='CNN model architecture to use'
    )

    # Argument 3: Dog names file
    parser.add_argument(
        '--dogfile',
        type=str,
        default='dognames.txt',
        help='path to the file of dog names'
    )

    return parser.parse_args()