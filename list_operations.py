participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90

if len(participants) != len(scores):
    print("Error: participants and scores lists must have the same length.")
    exit()

print("\n")
print("1. Display all current participants with their scores:")
for name, score in zip(participants, scores):
    print(f"{name}: {score}")

print("\n")
print("Add a new participant")
new_name = input("Enter participant name: ").strip()

if not new_name:
    print("Error: name cannot be empty.")
else:
    if new_name in participants:
        print(f"Error: {new_name} is already registered.")
    else:
        new_score_str = input("Enter score: ")
        try:
            new_score = float(new_score_str)
        except ValueError:
            print("Error: score must be a number.")
        else:
            if new_score < 0 or new_score > 100:
                print("Error: score must be between 0 and 100.")
            else:
                participants.append(new_name)
                scores.append(new_score)
                print(f"{new_name} has been successfully registered with score {new_score}.")

print("\n")
print("Search for a participant")
search_name = input("Enter participant name to search: ").strip()
if search_name in participants:
    idx = participants.index(search_name)
    score = scores[idx]
    if score > distinction_score:
        qualification = "DISTINCTION"
    elif score > qualification_score:
        qualification = "QUALIFIED"
    else:
        qualification = "NOT QUALIFIED"
    print(f"Found: {search_name}, Score: {score}, Status: {qualification}")
else:
    print(f"{search_name} is not found.")

print("\n")
print("All participants' details:")
for name, score in zip(participants, scores):
    if score > distinction_score:
        qual = "DISTINCTION"
    elif score > qualification_score:
        qual = "QUALIFIED"
    else:
        qual = "NOT QUALIFIED"
    print(f"{name}: Score {score}, Status {qual}")

print("\n")
print("Check distinction and pass status")
has_distinction = any(score > distinction_score for score in scores)
all_pass = all(score >= 50 for score in scores)
print(f"At least one participant with distinction: {has_distinction}")
print(f"All participants passed (score >= 50): {all_pass}")

print("\n")
print("Update a participant's score")
update_name = input("Enter participant name to update: ").strip()
if update_name in participants:
    idx = participants.index(update_name)
    new_score_str = input("Enter new score: ")
    try:
        new_score = float(new_score_str)
    except ValueError:
        print("Error: score must be a number.")
    else:
        if new_score < 0 or new_score > 100:
            print("Error: score must be between 0 and 100.")
        else:
            scores[idx] = new_score
            print(f"{update_name}'s score has been updated to {new_score}.")
else:
    print(f"{update_name} is not found.")

print("\n")
print("Withdraw a participant")
remove_name = input("Enter participant name to remove: ").strip()
if remove_name in participants:
    idx = participants.index(remove_name)
    participants.pop(idx)
    scores.pop(idx)
    print(f"{remove_name} has been withdrawn.")
else:
    print(f"{remove_name} is not found.")

print("\n")
print("Scoreboard (descending order):")
scoreboard = list(zip(participants, scores))
scoreboard.sort(key=lambda x: (-x[1], x[0]))

rank = 1
prev_score = None
for i, (name, score) in enumerate(scoreboard):
    if prev_score is not None and score != prev_score:
        rank = i + 1
    prev_score = score
    print(f"Rank {rank}: {name} - {score}")

print("\n")
print("Statistics:")
if scores:
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Average score: {average:.2f}")
    num_highest = scores.count(highest)
    num_lowest = scores.count(lowest)
    print(f"Number of participants with highest score: {num_highest}")
    print(f"Number of participants with lowest score: {num_lowest}")

    num_distinction = sum(1 for s in scores if s > distinction_score)
    num_qualified = sum(1 for s in scores if qualification_score < s <= distinction_score)
    num_not_qualified = sum(1 for s in scores if s <= qualification_score)
    print(f"Number with DISTINCTION: {num_distinction}")
    print(f"Number QUALIFIED: {num_qualified}")
    print(f"Number NOT QUALIFIED: {num_not_qualified}")
else:
    print("No participants available for statistics.")

print("\n")
print("Final Report:")
if scoreboard:
    rank = 1
    prev_score = None
    for i, (name, score) in enumerate(scoreboard):
        if prev_score is not None and score != prev_score:
            rank = i + 1
        prev_score = score
        if score > distinction_score:
            qual = "DISTINCTION"
        elif score > qualification_score:
            qual = "QUALIFIED"
        else:
            qual = "NOT QUALIFIED"
        print(f"Rank {rank}: {name}, Score {score}, Status {qual}")

    print("\nStatistics Summary:")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Average score: {average:.2f}")
    print(f"Participants with highest score: {num_highest}")
    print(f"Participants with lowest score: {num_lowest}")
    print(f"DISTINCTION count: {num_distinction}")
    print(f"QUALIFIED count: {num_qualified}")
    print(f"NOT QUALIFIED count: {num_not_qualified}")
else:
    print("No participants to report.")
