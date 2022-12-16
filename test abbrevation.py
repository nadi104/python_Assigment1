import re
name = "Smooth-leaved Elm"
def abbreviation(name):
    """divided each word into 3 letter abbrivation"""
    print(name)
    mystr = name.upper()
    REPLACE_APS = re.compile(r"[\']")
    mystr = REPLACE_APS.sub("", mystr)
    my_list = re.findall(r'[\w]+', mystr)
    print(my_list)
    list_count = len(my_list)
    newstr = ""
    val_tip = ()
    for i in range(list_count):
        val_name = my_list[i]
        val_tip = val_tip + (val_name[0], 0)
        val_name_count = len(val_name)

        for j in range(1, val_name_count - 1):
            if (j == 1):
                letter_val = count_value(val_name[j], 1)
                val_tip = val_tip + (val_name[1], letter_val)
            elif (j == 2):
                letter_val = count_value(val_name[j], 2)
                val_tip = val_tip + (val_name[2], letter_val)
            else:
                letter_val = count_value(val_name[j], 3)
                val_tip = val_tip + (val_name[j], letter_val)
        if (val_name[-1] == "E"):
            val_tip = val_tip + (val_name[-1], 25)
        else:
            val_tip = val_tip + (val_name[-1], 5)

    #   print(val_tip)
    val_tip_count = len(val_tip)
    abr_str_ar = []
    abr_num_ar = []
    for i in range(2, val_tip_count, 2):
        for j in range(i + 2, val_tip_count, 2):
            abstr = val_tip[0] + val_tip[i] + val_tip[j]
            abnum = val_tip[i + 1] + val_tip[j + 1]
            abr_str_ar.append(abstr)
            abr_num_ar.append(abnum)
    print(abr_str_ar)
    print(abr_num_ar)

#    task_1_list=remove_row_duplicate(abr_num_ar,abr_str_ar)

# Write data in the text file
#   print("Task one list")
#   print(task_1_list)
#  dic[name]=task_1_list
def count_value(letter, val):
    """If the letter neither first letter of the word nor the end the calculate the value for each letter"""
    count = 0
    val_tup = [];
    values_file = open("values.txt", "r")
    for line in values_file:
        val_tup.append([line.split()[0], line.split()[1]])
    for i in range(26):
        if (val_tup[i][0] == letter):
            count = int(val_tup[i][1]) + val
            break
    return count

abbreviation(name)