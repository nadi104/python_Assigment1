import re
dic={}

#This is the main function of the code which read data from trees.txt file and send them to the other operations.
def main():
    """Read the given text file ex:-trees.txt and pass readed values to abbrevation function and finally to the remove duplicate fun and fin_min """
    #outF = open("Task_one.txt", "w")
    #outF.close()
    trees_file = open("trees.txt", "r")
    trees_list = trees_file.readline()
    while(trees_list):
        abbreviation(trees_list)
        trees_list = trees_file.readline()

    trees_file.close()
    #print(dic)
    remove_duplicate(dic)
    find_min(dic)

#This funtion remove all duplicated abbrevation created by different names

def remove_duplicate(dic):
    """Remove all duplicates in the created abbrevation set"""
    list_keys = list(dic.keys())
    print(list_keys)
    len_keys = len(list_keys)
    for i in range(len_keys):
        name = dic[list_keys[i]][:]
        print(name)
        for start_abb in name:
            duplicate = False
            for k in range(i + 1, len_keys):
                name2 = dic[list_keys[k]][:]
                for check_abb in name2:
                    print(start_abb[0] + "->" + check_abb[0])
                    if start_abb[0] == check_abb[0]:
                        duplicate = True
                        dic[list_keys[k]].remove(check_abb)

                        # list_keys[k].remove(check_abb)

            if duplicate:
                dic[list_keys[i]].remove(start_abb)
    print(dic)

#Find the minimum value relavent to the each word.
def find_min(dic):
    """Find the minimum value correspond to th each word """
    f = open("wijesinghe_trees_abbrevs.txt", "w")
    f.write(" ")
    list_keys = list(dic.keys())
    print(list_keys)
    len_keys = len(list_keys)
    for i in range(len_keys):
        name = dic[list_keys[i]][:]
        min = 1000
        min_abbrevation = []
        for abbrevation in name:
            print(abbrevation)
            if (abbrevation[1] < min):
                min = abbrevation[1]

        print(list_keys[i])
        for abbrevation in name:
            if (abbrevation[1] == min):
                min_abbrevation.append(abbrevation[0])
        f.write("\n")
        f.write(list_keys[i])

        if (min == 1000):
            print("--------------------------")
            f.write("--------------------------" + "\n")
        else:
            print(min)
            print(min_abbrevation)
            f.write(str(min_abbrevation)+"\n")


    f.close()




# If the letter neither first letter of the word nor the end the calculate the value for each letter. Read the values from values.txt file and assign corespondend value
# and position value to letter
def count_value(letter,val):
    """If the letter neither first letter of the word nor the end the calculate the value for each letter"""
    count=0
    val_tup = [];
    values_file = open("values.txt", "r")
    for line in values_file:
        val_tup.append([line.split()[0], line.split()[1]])
    for i in range(26):
        if (val_tup[i][0]==letter):
            count=int(val_tup[i][1])+val
            break
    return count



def abbreviation(name):
    """divided each word into 3 letter abbrivation"""
    print(name)
    mystr = name.upper()
    REPLACE_APS = re.compile(r"[\']")
    mystr = REPLACE_APS.sub("", mystr)
    my_list = re.findall(r'[\w]+', mystr)
    print(my_list)
    list_count=len(my_list)
    newstr = ""
    val_tip=()
    for i in range(list_count):
        val_name=my_list[i]
        val_tip=val_tip+(val_name[0],0)
        val_name_count=len(val_name)


        for j in range(1,val_name_count-1):
            if(j==1):
                letter_val=count_value(val_name[j],1)
                val_tip = val_tip + (val_name[1], letter_val)
            elif(j==2):
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
    val_tip_count=len(val_tip)
    abr_str_ar=[]
    abr_num_ar=[]
    for i in range(2,val_tip_count,2):
        for j in range(i+2, val_tip_count,2):
            abstr=val_tip[0]+val_tip[i] + val_tip[j]
            abnum=val_tip[i+1]+val_tip[j+1]
            abr_str_ar.append(abstr)
            abr_num_ar.append(abnum)
    task_1_list=remove_row_duplicate(abr_num_ar,abr_str_ar)

    #Write data in the text file
    print("Task one list")
    print(task_1_list)
    dic[name]=task_1_list


#If some word have same abbrevaton then check the minimum value and remove others

def remove_row_duplicate(numary,strary):
    """Remove duplicate created my same word and assign minimum value to that abbrevation"""
    strary_count=len(strary)
    print(strary[strary_count-1])
    for i in range(strary_count):
        for j in range(i + 1, strary_count):
            str1 = strary[i]
            str2 = strary[j]
            num1 = numary[i]
            num2 = numary[j]

            if (str1 == str2):
                if (num1 <= num2):
                    numary[j] = numary[i]
                else:
                    numary[i] = numary[j]

    merged_list = [(strary[i], numary[i]) for i in range(0, len(strary))]
    merged_list = set(merged_list)
    merged_list=list(merged_list)
    return merged_list


