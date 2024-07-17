from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
def main():
    # Measure total program runtime by collecting start time
    start_time = time()
    
    # Fetch command line arguments
    in_arg = get_input_args()

    # Placeholder for get_pet_labels() - Replace with actual implementation
    results = get_pet_labels(in_arg.dir)

    # Placeholder for classify_images() - Replace with actual implementation
    classify_images(in_arg.dir, results, in_arg.arch)

    # Placeholder for adjust_results4_isadog() - Replace with actual implementation
    adjust_results4_isadog(results, in_arg.dogfile)

    # Placeholder for calculates_results_stats() - Replace with actual implementation
    results_stats = calculates_results_stats(results)

    # Placeholder for print_results() - Replace with actual implementation
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measure end time
    end_time = time()
    
    # Calculate overall runtime in seconds
    tot_time = end_time - start_time
    
    # Print overall runtime in seconds
    print("\nTotal Elapsed Runtime:", tot_time, "seconds.")
    
    # Format runtime into hh:mm:ss format
    hours = int(tot_time // 3600)
    minutes = int((tot_time % 3600) // 60)
    seconds = int((tot_time % 3600) % 60)
    print("\nTotal Elapsed Runtime:", f"{hours:02}:{minutes:02}:{seconds:02}")

# Call to main function to run the program
if __name__ == "__main__":
    main()
