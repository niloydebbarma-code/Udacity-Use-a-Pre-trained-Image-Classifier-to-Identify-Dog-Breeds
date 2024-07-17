# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
        # Create the full path to the image file
        image_path = images_dir + '/' + key
       
        # Runs classifier function to classify the images classifier function 
        # inputs: path + filename  and  model, returns model_label 
        # as classifier label
        model_label = classifier(image_path, model)

        # Processes the results so they can be compared with pet image labels
        # Set labels to lowercase (lower) and strip off whitespace (strip)
        model_label = model_label.lower().strip()
              
        # Define truth as pet image label 
        truth = results_dic[key][0]

        # Compare pet image label with classifier label
        if truth in model_label:
            # If pet image label found in classifier label, it's a match
            results_dic[key].extend([model_label, 1])
        else:
            # If pet image label not found in classifier label, it's not a match
            results_dic[key].extend([model_label, 0])

        # Note: results_dic is mutable, so no return is needed
