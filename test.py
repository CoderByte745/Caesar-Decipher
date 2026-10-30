import os
error_msg ="error"
key = 5
usr_selection = [1, 2, 3]
decrypted_msg = "This is a decrypted message."
def yesNoValidation(inputMsg):
    confirm = input(inputMsg)
    bool = False
    while confirm != "Y" and confirm != "N" and confirm != "y" and confirm != "n":
        print(error_msg)
        confirm = input(inputMsg)
    if confirm == "Y" or confirm == "y":
        bool = True
    return bool
def frequent(msg):
    count_list = [[msg[0]],[1]]
    for i in range(1, len(msg)):
        found = False
        for j in range(len(count_list[0])):
            if msg[i] == count_list[0][j]:
                count_list[1][j] += 1
                found = True
                break
        if found == False:
            count_list[0].append(msg[i])
            count_list[1].append(1)
    for i in range(len(count_list[1])):
        max = i
        for j in range(i+1, len(count_list[1])):
            if count_list[1][j] > count_list[1][max]:
                max = j
        temp = count_list[1][i]
        count_list[1][i] = count_list[1][max]
        count_list[1][max] = temp
        temp = count_list[0][i]
        count_list[0][i] = count_list[0][max]
        count_list[0][max] = temp
    return count_list
def lowerCase(word):
    for i in range(len(word)):
        if word[i] <= "Z" and word[i] >= "A":
            word = word.replace(word[i], chr(ord(word[i])+32))
    return word

def fileSaving(statistics):
    filename = input("Input filename for the decrypted message: ").replace(".txt", "")
    if os.path.exists(filename+".txt"):
        if yesNoValidation("File already exists. Do you want to replace it? [Y/N] ") == False:
            fileSaving(statistics)
            return
    ouput_file = open(filename+".txt", "w")
    if usr_selection[2] == 1:
        ouput_file.write("Decrypted message:\n" + decrypted_msg + "\nKey: "+str(key))
    elif usr_selection[2] == 2:
        ouput_file.write("Decrypted message:\n"+ decrypted_msg + "\n")
        ouput_file.write(statistics)
    else:
        ouput_file.write(decrypted_msg)
        stat_filename = input("Input filename for statistics: ").replace(".txt", "")
        if os.path.exists(stat_filename+".txt"):
            if yesNoValidation("File already exists. Do you want to replace it? [Y/N] ") == False:
                temp = stat_filename
                stat_filename = input("Input the correct filename again: ")
                while stat_filename == temp or stat_filename == temp+".txt":
                    stat_filename = input("Use a different filename. Input the correct filename again: ")
        stat_file = open(stat_filename+".txt", "w")
        stat_file.write(statistics)
        stat_file.close()
    ouput_file.close()
    print("All files are saved successfully.")
    print("Restart?")
