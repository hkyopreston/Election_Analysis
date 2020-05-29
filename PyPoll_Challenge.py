# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# 6. The voter turnout for each county
# 7. The percentage of votes each county contributed to the election

# add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate/county options and candidate/county votes options.
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage. Track county votes.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county voter turnout and it's percentage
largest_county_turnout = ""
largest_county_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Get the county name from each row. 
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing candidate, add the county to the list
        if county_name not in county_options:
            county_options.append(county_name)
            # Begin tracking the county's voter count
            county_votes[county_name] = 0
        # Add a vote to that county's count. 
        county_votes[county_name] += 1
    
# save the results to txt file
with open(file_to_save, "w") as txt_file:
    # print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n---------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # save the final county vote to the txt file
    for county in county_votes:
        # Retrieve county vote count and percentage
        county_vote = county_votes[county]
        county_percentage = float(county_vote)/float(total_votes)*100
        county_results = (
            f"{county}: {county_percentage:.1f}% ({county_vote:,})\n")
        print(county_results, end="")
        txt_file.write(county_results)

        # Determine winning vote count and candidate
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
    # Print the county with the largest turnout
    largest_county_turnout = (
        f"\n------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"--------------------------\n")
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        # Retrieve vote count and percentages
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine the winner of the election, their vote count, and their winning percentage
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    #save the winning candidate summary to the txt file
    txt_file.write(winning_candidate_summary)

        









  




