# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
# declare empty list
candidate_options = []
# declare empty dictionary
candidate_votes = {}
# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    #Determine the percentage of votes for each candidate by looping through the counts. 
    #1. Iterate through the candidate list
    for candidate in candidate_votes:
        #2. Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate]
        #3. Calculate the percentage of votes. 
        vote_percentage = int(votes)/int(total_votes) * 100
        #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(f"{candidate}; {vote_percentage:.1f}% ({votes:,})\n")


        # determine winning vote count and candidate
        # determing if the winning votes is greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, then set winning_count = votes and winning_percent = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name. 
            winning_candidate = candidate


    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
        

# Print the candidate vote dictionary.
#print(candidate_votes)
#print(total_votes)









  




