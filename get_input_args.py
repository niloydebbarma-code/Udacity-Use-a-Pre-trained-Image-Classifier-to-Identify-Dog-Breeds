import argparse

def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user.
    """
    parser = argparse.ArgumentParser(description="Classify pet images using a pretrained CNN model.")
    
    # Argument 1: Folder that contains pet images
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='Path to the folder of pet images')

    # Argument 2: CNN model architecture to use
    parser.add_argument('--arch', type=str, default='vgg', choices=['resnet', 'alexnet', 'vgg'], 
                        help='CNN Model Architecture (resnet, alexnet, vgg)')

    # Argument 3: File that contains list of valid dog names
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='Text file that contains list of valid dog names')

    return parser.parse_args()
