def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classify pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
                            
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                    name (starting with 'pct' for percentage or 'n' for count)
                    and the value is the statistic's value.
    """        
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    # Sets all counters to initial values of zero so that they can 
    # be incremented while processing through the images in results_dic 
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    # Process through the results dictionary
    for key in results_dic:
         
        # Count when both labels match
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # TODO: 5a. Count number of correctly classified dog breeds
        # Pet Image Label is a Dog AND Labels match- counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        
        # TODO: 5b. Count number of dog images
        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # TODO: 5c. Count number of correctly classified NOT dog images
        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog (& pet image isn't a dog)
            # counts number of correct NOT dog classifications
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate total number of images
    results_stats_dic['n_images'] = len(results_dic)

    # Calculate number of not-a-dog images using total images and dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] -
                                          results_stats_dic['n_dogs_img'])

    # Calculate percentages
    
    # Calculate percentage of correctly matched images
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] /
                                      results_stats_dic['n_images']) * 100.0 if results_stats_dic['n_images'] > 0 else 0.0

    # Calculate percentage of correctly classified dog images
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] /
                                             results_stats_dic['n_dogs_img']) * 100.0 if results_stats_dic['n_dogs_img'] > 0 else 0.0

    # Calculate percentage of correctly classified dog breed images
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] /
                                              results_stats_dic['n_dogs_img']) * 100.0 if results_stats_dic['n_dogs_img'] > 0 else 0.0

    # Calculate percentage of correctly classified non-dog images
    results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img']) * 100.0 if results_stats_dic['n_notdogs_img'] > 0 else 0.0

    # Return the results statistics dictionary
    return results_stats_dic
