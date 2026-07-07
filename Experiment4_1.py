# Input two lists of four integers each
lstA = list(map(int, input("Enter four number (interger) for lstA (Use 'Space' to seperate the numbers): ").split()))
lstB = list(map(int, input("Enter four number (interger) for lstB (Use 'Space' to seperate the numbers): ").split()))

# Ensure both lists have exactly four elements
if len(lstA) == 4 and len(lstB) == 4:
    result_dict = dict(zip(lstA, lstB))
    print("Dictionary:", result_dict)
else:
    print("Please enter exactly four integers for each list.")
