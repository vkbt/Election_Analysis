# Import csv and os modules

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#with open(file_to_save, 'w') as txt_file:
 #   txt_file.write("Counties in the Election\n-------------------------\n")
  #  txt_file.write("Arapahoe\nDenver\nJefferson")

# Adding total voutes counter variable  
total_votes = 0

# Adding Candidate list
candidate_option = []

# Adding candidate votes dictionary
candidate_votes = {}

# Setting winning candidate to blank and winning count and percentage to 0 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    hdrs = next(file_reader)
    #print(F'{hdrs}')

    # Print each row in the CSV file.
    for row in file_reader:
      # Count total votes
      total_votes +=1
      # Define canddidate name = 3rd column
      candidate_name = row[2]

      # If condition to add only unique candidates to the list    
      if candidate_name not in candidate_option:
        # Add candidates to the list
        candidate_option.append(candidate_name)

        # Adding candidate votes counter and settingit to 0
        candidate_votes[candidate_name] = 0

      # Looping to add candidate votes  
      candidate_votes[candidate_name] +=1

with open(file_to_save, "w") as txt_file:
  
  election_results = (
                  f'\nElection Results\n'
                  f'-------------------------\n'
                  f'Total Votes: {total_votes:,}\n'
                  f'-------------------------\n')
  print(election_results, end = "")
  txt_file.write(election_results)


# Loop to calc vote % for each candidate
  for candidate, votes in candidate_votes.items():
    candidate_results = (f'{candidate}: {votes/total_votes*100:.1f}% ({votes:,})\n')

    print(candidate_results)

    txt_file.write(candidate_results)
  # print(f'{candidate}: {votes/total_votes*100:.1f}% ({votes:,})\n')

  # Defining voter percentage variable
    vote_percentage = votes / total_votes *100

  # If Statement to set winning candidate details
    if (votes > winning_count): #and (vote_percentage > winning_percentage):
          winning_count = votes
          winning_candidate = candidate
          winning_percentage = vote_percentage

# Defining winning candidate summary for printing
  winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

# Printing winning candidate summary
  print(winning_candidate_summary)
  txt_file.write(winning_candidate_summary)
