from os import listdir
import os.path

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
                 
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = {}
   
    # Processes each file in the directory
    for filename in in_files:
        # Skip files that start with '.' (hidden files)
        if filename[0] == ".":
            continue
        
        # Extract the pet label from the filename
        # Remove file extension
        pet_label = os.path.splitext(filename)[0]
        
        # Split filename by underscores to get words
        word_list_pet_image = pet_label.split("_")
        
        # Initialize pet_name as an empty string
        pet_name = ""
        
        # Iterate through words to construct pet_name
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word.lower() + " "
        
        # Strip off trailing whitespace
        pet_name = pet_name.strip()
        
        # Check if filename already exists in dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print("** Warning: Duplicate files exist in directory:", filename)
 
    return results_dic

# Test the function
if __name__ == "__main__":
    # Replace 'path_to_your_images_folder' with the actual path to your images folder
    image_folder = 'path_to_your_images_folder'
    results = get_pet_labels(image_folder)
    print(results)
