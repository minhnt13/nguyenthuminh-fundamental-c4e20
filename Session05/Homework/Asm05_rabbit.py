months = 0
initial_pair = 1
total_pairs = 1
while months < 5:
    print("Month {}: {} pair(s) of rabbit".format(months,total_pairs))    
    initial_pair, total_pairs = total_pairs, initial_pair + total_pairs
    months += 1
