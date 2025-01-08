# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_names = []
candidate_results = {}
candidate_votes = []
candidate_index = 0
percent_of_vote = 0

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
 #       print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name in candidate_names:
            candidate_index = candidate_names.index(name)
            candidate_votes[candidate_index] += 1
        else:
            candidate_names.append(name)
            candidate_votes.append(0)
            candidate_index = candidate_names.index(name)
            candidate_votes[candidate_index] += 1
 
        # Add a vote to the candidate's count
        candidate_results["name"] = candidate_names
        candidate_results["votes"] = candidate_votes
        
# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------")

    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner
for i in range(len(candidate_results)+1): 

        # Get the vote count and calculate the percentage
    votes = int(candidate_results["votes"][i])
    percent_of_vote = str(round((votes/total_votes*100),3))
 
        # Update the winning candidate if this one has more votes
    if votes > int(candidate_results["votes"][i-1]):
        winner = candidate_results["name"][i]

        # Print and save each candidate's vote count and percentage
    print(f'{candidate_results["name"][i]}: {str(percent_of_vote)}% ({candidate_results["votes"][i]})')

    # Generate and print the winning candidate summary
print("-----------------------------")
print("Winner: " + winner)
print("-----------------------------")

    # Save the winning candidate summary to the text file