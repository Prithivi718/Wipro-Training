# Open file
file = open("sample_io.txt", "r")

lines = file.readlines()
file.close()

# Meeting time = number of lines
num_lines = len(lines)

if num_lines > 12:
    meeting_time = num_lines - 12
    time_format = "PM"
else:
    meeting_time = num_lines
    time_format = "AM"

# Count word frequency
word_count = {}

for line in lines:
    words = line.split()

    for word in words:
        word = word.strip(".,!?").capitalize()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Find maximum occurring word
meeting_place = max(word_count, key=word_count.get)

print("Meeting time:", meeting_time, time_format)
print("Meeting place:", meeting_place, "Street")