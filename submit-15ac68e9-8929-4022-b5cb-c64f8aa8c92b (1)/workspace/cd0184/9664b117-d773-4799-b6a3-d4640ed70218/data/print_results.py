#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: samarth jain
# DATE CREATED: 29/08/2026
# REVISED DATE:29/08/2026
#
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of
#          misclassified dogs and cases of misclassified breeds of dog.

# TODO 6: Define print_results function

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False,
                  print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if requested.

    Parameters:
      results_dic - Dictionary containing pet image labels, classifier labels,
                    and classification results.

      results_stats_dic - Dictionary containing the calculated result
                          statistics.

      model - CNN model architecture: resnet, alexnet, or vgg.

      print_incorrect_dogs - True prints incorrectly classified dog images.
                             False does not print them.

      print_incorrect_breed - True prints incorrectly classified dog breeds.
                              False does not print them.

    Returns:
      None
    """

    # Print model architecture
    print("\n*** Results Summary for CNN Model Architecture",
          model.upper(), "***")

    # Print overall counts
    print("Number of Images:", results_stats_dic['n_images'])

    print("Number of Dog Images:",
          results_stats_dic['n_dogs_img'])

    print("Number of 'Not-a' Dog Images:",
          results_stats_dic['n_notdogs_img'])

    # Print all percentage statistics
    for key in results_stats_dic:
        if key.startswith('pct'):
            print(key, ":", results_stats_dic[key])

    # Print incorrectly classified dogs
    if print_incorrect_dogs and (
        results_stats_dic['n_correct_dogs'] +
        results_stats_dic['n_correct_notdogs'] !=
        results_stats_dic['n_images']
    ):

        print("\n*** Misclassified Dogs ***")

        for key in results_dic:
            # Pet image and classifier disagree about whether it is a dog
            if sum(results_dic[key][3:]) == 1:
                print("Pet Image Label:",
                      results_dic[key][0],
                      "Classifier Label:",
                      results_dic[key][1])

    # Print incorrectly classified dog breeds
    if print_incorrect_breed and (
        results_stats_dic['n_correct_dogs'] !=
        results_stats_dic['n_correct_breed']
    ):

        print("\n*** Misclassified Dog Breeds ***")

        for key in results_dic:
            # Both labels say dog, but the breeds don't match
            if (sum(results_dic[key][3:]) == 2 and
                    results_dic[key][2] == 0):

                print("Pet Image Label:",
                      results_dic[key][0],
                      "Classifier Label:",
                      results_dic[key][1])