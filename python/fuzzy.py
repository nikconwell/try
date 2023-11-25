import jaro

known_good = [
    "This is a test string",
    "This is another string",
    "This is something else",
]

str1 = "This is something"
best_match = -1
best_match_index = -1
check_index=0

print(f'Input: {str1}')
for check in known_good:
    difference = jaro.jaro_winkler_metric(str1,check)
    if difference > best_match:
        best_match_index = check_index
        best_match = difference
        if best_match == 1:
            break
    check_index = check_index + 1

print(f'Best match = {(best_match*100):.0f}% {known_good[best_match_index]}')



