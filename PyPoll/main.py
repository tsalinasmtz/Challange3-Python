import csv

# Open the CSV file
with open('./Resources/election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    next(reader)
    votes = []
    total_votes = 0

    # Loop 
    for row in reader:
        voter_id = int(row[0])
        candidate = row[2]
        votes.append({"voter_id": voter_id, "candidate": candidate})
        total_votes += 1

    votes_per_candidate = {}

    # Loop 
    for vote in votes:
        candidate = vote["candidate"]
        if candidate in votes_per_candidate:
            votes_per_candidate[candidate] += 1
        else:
            votes_per_candidate[candidate] = 1

    candidates = list(votes_per_candidate.keys())

    vote_percentages = {}

    for candidate in candidates:
        vote_percentage = (votes_per_candidate[candidate] / total_votes) * 100
        vote_percentages[candidate] = vote_percentage

    winner = max(votes_per_candidate, key=votes_per_candidate.get)

    # Print the results in Terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Print the results in Excel
with open("./Analysis/elections.txt", "a") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("-------------------------", file=f)
    for candidate in candidates:
        print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})", file=f)
    print("-------------------------", file=f)
    print(f"Winner: {winner}", file=f)
    print("-------------------------", file=f)
