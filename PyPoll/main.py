# PyPoll
# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
percent_of_vote = 0 # Track the percentage of total vote 

# Define lists and dictionaries to track candidate names and vote counts
candidate_names = []
candidate_votes = []
candidate_results = {}
candidate_index = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is already in the candidate list, update the index and increment their vote count
        if name in candidate_names:
            candidate_index = candidate_names.index(name)
            candidate_votes[candidate_index] += 1
        else:
            # If the candidate is NOT already in the candidate list, add them plus an initial vote counter, 
            # update the index and increment their vote count
            candidate_names.append(name)
            candidate_votes.append(0)
            candidate_index = candidate_names.index(name)
            candidate_votes[candidate_index] += 1
 
        # Update the candidate's results
        candidate_results["name"] = candidate_names
        candidate_results["votes"] = candidate_votes
        
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Generate the header and total vote count
    total_vote_count = (
        f'Election Results\n\n'
        f'-----------------------------\n\n'
        f'Total Votes: {total_votes}\n\n'
        f'-----------------------------\n\n'
    )
    # Print the total vote count (to terminal)
    print (total_vote_count)
    
    # Write the total vote count to the text file
    txt_file.write(total_vote_count)

    # Loop through the candidates to determine vote percentages and identify the winner
    for i in range(len(candidate_results)+1): 

        # Get the vote count and calculate the percentage
        votes = int(candidate_results["votes"][i])
        percent_of_vote = str(round((votes/total_votes*100),3))
    
        # Update the winning candidate if this one has more votes
        if votes > int(candidate_results["votes"][i-1]):
            winner = candidate_results["name"][i]

        # Print and save each candidate's vote count and percentage
        candidate_vote_counts = (f'{candidate_results["name"][i]}: {str(percent_of_vote)}% ({candidate_results["votes"][i]})\n\n')

        print(candidate_vote_counts)
        
        txt_file.write(candidate_vote_counts)

    # Generate and print the winning candidate summary
    winner_summary = (
        f'-----------------------------\n\n'
        f'Winner: {winner}\n\n'
        f'-----------------------------\n'        
    )
    print(winner_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winner_summary)