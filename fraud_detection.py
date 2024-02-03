"""
* Description: Analyzes Iran 2008 election data. Finds if the election was a
* fraud elections. Compares Data to USA 2009 election.
"""

import utils
import csv
import matplotlib.pyplot as plt
import random

def extract_election_votes(filename, column_names):
    """
    filename represents the given csv file.
    column_nmaes represent list names extracting data for.
    Extracts a file and returns a list of intgers containing
    values that correspond to the column names on evey row.
    """
    num_votes = []
    with open(filename, encoding="iso-8859-1") as f:
        reader = csv.DictReader(f)
        for lines in reader:
            for names in column_names:
                votes = lines[names].replace(',', '')
                if votes != '':
                    num_votes.append(int(votes))
    return num_votes


def ones_and_tens_digit_histogram(numbers):
    """
    Given a list of numbers return a new lists of size 10 where each value in
    the new list represent the frequency of the first two digit in numbers
    divided by the amount of 2 digit number in numbers. If a number is less
    than 10 a 0 should be added to the front so the number can be 2 digits
    long.
    """
    origin_length = len(numbers) * 2
    ten_list = [0] * 10
    correct_ten = []
    filter_list = []
    for i in numbers:
        filter_list.append(str(i % 100))
    for j in filter_list:
        if int(j) < 10:
            ten_list[0] += 1
            ten_list[int(j)] += 1
        else:
            first_num = int(j[0])
            second_num = int(j[1])
            ten_list[first_num] += 1
            ten_list[second_num] += 1
    for k in ten_list:
        correct_ten.append(k / origin_length)
    return correct_ten


def plot_iran_least_digits_histogram(histogram):
    """
    histogram represents the data from ones_and_tens_digit_histogram.
    Plot a graphs of a histogram of ones and tens frequencies in the Iranian
    elction data.
    """
    plt.title("Distribution of the last two digits in Iranian dataset")
    plt.plot([0.1 for i in range(10)], label="Ideal")
    plt.plot(histogram, label="Iran")
    plt.legend(loc="upper left")
    plt.ylabel("Frequency")
    plt.xlabel("Digit")
    plt.savefig('iran-digits.png')
    plt.show()
    plt.clf()


def plot_dist_by_sample_size():
    """
    Plot a graph of a histogram of ones and tens frequencies of different
    random sample sizes in the Iranian election data.
    """
    plt.title("Distribution of last two digits in randomly generated samples")
    plt.plot([0.1 for i in range(10)], label="Ideal")
    for i in [10, 50, 100, 1000, 10000]:
        sizes = [random.randint(0, 99) for j in range(i)]
        new_rand_graph = ones_and_tens_digit_histogram(sizes)
        plt.plot(new_rand_graph, label=str(i) + " random numbers")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.legend(loc="upper left")
    plt.savefig("random-digits.png")
    plt.show()
    plt.clf()


def mean_squared_error(numbers1, numbers2):
    """
    numbers1 represents a value .
    numbers2 represents a value.
    returns mean square errors of 2 list of integers.
    """
    error = 0
    for i in range(len(numbers1)):
        value = numbers1[i]
        value2 = numbers2[i]
        error += ((value - value2)**2)/len(numbers1)
    return error


def calculate_mse_with_uniform(histogram):
    """
     histogram represents the data from ones_and_tens_digit_histogram.
    returns the mean square error of the histogram.
    """
    ideal_list = [0.1 for i in range(10)]
    return mean_squared_error(histogram, ideal_list)


def helper_comapres_mse(means_score, numper_points, change):
    """
    means_score represents mse score.
    number_points represents number of data points in a graph.
    change is a given string.
    Helper function for compare_iran_mse_to_samples and
    compare_us_mse_to_samples. Compares the mse scores to samples.
    Finds how many mse_samples are above the actual MSE score.
    Prints out the results in the end.
    """
    rand_groups = []
    samples = []
    greaters = 0
    smallers = 0
    for i in range(10000):
        rand_groups = (([random.randint(0, 99) for i in range(numper_points)]))
        ones_func = ones_and_tens_digit_histogram(rand_groups)
        samples = ((calculate_mse_with_uniform(ones_func)))
        if samples >= means_score:
            greaters += 1
        elif samples < means_score:
            smallers += 1
    print(change + " election MSE: " + str(means_score))
    print("Quantity of MSEs larger than or equal to the " + change +
          " election MSE: " + str(greaters))
    print("Quantity of MSEs smaller than the " + change +
          " election MSE: " + str(smallers))
    print(change + " election null hypothesis rejection level p: " +
          str((greaters / 10000)))


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    """
    iran_mse represents the actual iran_mse score.
    numbers_of_iran_datapoints represents number of data points in the iran
    graph.
    Compare how many random sample values is above the MSE for the given data
    and how many are below the MSE and caclates p-value.
    """
    helper_comapres_mse(iran_mse, number_of_iran_datapoints, "2009 Iranian")


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    """
    us_mse represents the actual iran_mse score.
    number_of_us_datapoints represents number of data points in the US
    graph.
    Compare how many random sample values is above the MSE for the given data
    and how many are below the MSE and caclates p-value.
    """
    helper_comapres_mse(us_mse, number_of_us_datapoints, "2008 United States")

# The code in this function is executed when this
# file is run as a Python program

def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    iran_candidates = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    iran_votes = extract_election_votes("election-iran-2009.csv",
                                        iran_candidates)
    hist_votes_iran = ones_and_tens_digit_histogram(iran_votes)
    plot_iran_least_digits_histogram(hist_votes_iran)
    plot_dist_by_sample_size()
    iran_mse = calculate_mse_with_uniform(hist_votes_iran)
    compare_iran_mse_to_samples(iran_mse, len(iran_votes))
    print()
    usa_candidate = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    votes_usa = extract_election_votes("election-us-2008.csv", usa_candidate)
    hist_votes_usa = ones_and_tens_digit_histogram(votes_usa)
    mse_usa = calculate_mse_with_uniform(hist_votes_usa)
    compare_us_mse_to_samples(mse_usa, len(votes_usa))


if __name__ == "__main__":
    main()
