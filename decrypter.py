import os
error_msg = "User input invalid. Please try again."
word_list = ["the","and","to", "is"]
chr_list = [" ","e","a"]
usr_selection = []
decrypted_msg = ""
key = ""

def startUp():
    global usr_selection
    global decrypted_msg
    global key
    usr_selection = []
    decrypted_msg = ""
    key = ""
    print("******************************************************************************************")
    print("#  ___ _    _  __ _      ___ _      _              ___                       _           #\n# / __| |_ (_)/ _| |_   / __(_)_ __| |_  ___ _ _  |   \\ ___ __ _ _ _  _ _ __| |_ ___ _ _ #\n# \\__ \\ ' \\| |  _|  _| | (__| | '_ \\ ' \\/ -_) '_| | |) / -_) _| '_| || | '_ \\  _/ -_) '_|#\n# |___/_||_|_|_|  \\__|  \\___|_| .__/_||_\\___|_|   |___/\\___\\__|_|  \\_, | .__/\\__\\___|_|  #\n#                             |_|                                  |__/|_|               #")
    print("******************************************************************************************")
    print("Welcome to the Shift Cipher Decrypter. Please choose your input method by entering the option number.\nIf you need help, please choose the help guide option.")
    print("1 Text file upload\n2 Manual input\n3 Help Guide")
    usr_selection.append(rangeValidation("3"))
    menu(1)

def rangeValidation(maxRange):
    input_value = input("Enter number [1-" + maxRange + "]: ")
    while input_value < "1" or input_value > maxRange:
        print(error_msg)
        input_value = input("Enter number [1-"+maxRange+"]: ")
    return int(input_value)

def yesNoValidation(inputMsg):
    confirm = input(inputMsg)
    bool = False
    while confirm != "Y" and confirm != "N" and confirm != "y" and confirm != "n":
        print(error_msg)
        confirm = input(inputMsg)
    if confirm == "Y" or confirm == "y":
        bool = True
    return bool

def menu(option):
    global usr_selection
    if option == 1: 
        if usr_selection[0] == 3:
            print("********************************************************************************************************************************")
            print("Welcome to the help guide. Please follow the requirements below for the decrypter to process your data correctly.\n")
            print("Requirements for text file upload:\n1. All files must be in ASCII character encoding system\n2. The file should contain plain text and in English\n3. The path to the file should be either relative to where the program is run or an absolute path\n")
            print("Requirements for manual input:\n1. All inputs should be in ASCII\n2. Ensure the inputted message is correct with no mistake\n3. The inputted message should be in English\n")
            print("Note: The message should be at least 200 words in length. If the message is too short, it may not be decrypted correctly.")
            print("********************************************************************************************************************************")
            exit_input = input("Press enter to return to the menu\n")
            while exit_input != "":
                print(error_msg)
                exit_input = input("Press enter to return to the menu\n")
            startUp()
        else:
            print("\nEncryption Method:")
            print("1 Only alphabets are encrypted\n2 All characters are encrypted\n3 Encryption method unknown\n4 Return to previous options")
            usr_selection.append(rangeValidation("4"))
            if usr_selection[1] == 4:
                startUp()
                return
            elif usr_selection[1] == 3:
                usr_selection[1] = 1
            if usr_selection[0] == 1:
                print("\nText file upload") 
                print("Please be reminded that your file should be in ASCII and a text file. The path should be relative to where the program is run. Input q to return to previous options.")
            else:
                print("\nManual Input")
                print("Please check if there is no mistake when inputting the message. Input q to return to previous options.")
            inputMsg()    
    else:
        print("Please choose an option:\n1 Save only the decrypted message\n2 Save all statistics and the decrypted message as one text file\n3 Save the decrypted message and statistics as separate files\n4 Do not save")
        usr_selection.append(rangeValidation("4"))
        if usr_selection[2] == 4:
            if yesNoValidation("The decrypted data will be lost. Are you sure leaving without saving? [Y/N] ") == True:
                restart()
            else:
                usr_selection.pop()
                menu(2)

def inputMsg():
    global usr_selection
    if usr_selection[0] == 1:
        path_input = input("Enter path: ")
        while path_input.find(".txt") == -1 or not os.path.exists(path_input):
            if path_input == "q" or path_input == "Q":
                usr_selection.pop()
                menu(1)
                return
            else:
                print("The file path must be correct and the file must be in plain text format.")
                path_input = input("Enter path: ")
        input_msg = open(path_input, "r", encoding="utf-8").read()
    else:
        input_msg = input("Enter message: ")
        while input_msg == "":
            print("You have inputted nothing. Please try again.")
            input_msg = input("Enter message: ")
        if input_msg == "q" or input_msg == "Q":
            usr_selection.pop()
            menu(1)
            return
    while len(input_msg) < 3:
        print("The message is too short. Please try again.")
        inputMsg()
        return
    if len(input_msg.split()) < 200 and len(input_msg) < 1200:
        print("It is suggested that your message should be at least 200 words. The decryption may not be correct.") 
        if yesNoValidation("Do you want to continue? [Y/N] ") == False:
            inputMsg()
            return
    findKey(input_msg.replace("\n", " "))

def lowerCase(word):
    for i in range(len(word)):
        if word[i] <= "Z" and word[i] >= "A":
            word = word.replace(word[i], chr(ord(word[i])+32))
    return word

def posDifference(word):
    pos_list = []
    word = lowerCase(word)
    for i in range(len(word)-1):
        pos_list.append((ord(word[i+1])+26-ord(word[i]))%26)
    return pos_list

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

def findKey(encrypted_msg):
    global key
    global usr_selection
    if usr_selection[1] == 1:
        check_list = []
        for i in range(len(word_list)):
            check_list.append(posDifference(word_list[i]))
        encryptArray = encrypted_msg.split()
        for i in range(len(encryptArray)):
            if len(encryptArray[i]) == 3 or len(encryptArray[i]) == 2:
                msg_list = posDifference(encryptArray[i])
                for j in range(len(check_list)):
                    if msg_list == check_list[j]:
                        encryptArray[i] = lowerCase(encryptArray[i])
                        key = ord(encryptArray[i][0]) - ord(word_list[j][0])
                        break
        if key != "":
            output(decrypt(key, encrypted_msg))
    if usr_selection[1] == 2 or key == "":
        usr_selection[1] = 2
        count_list = frequent(encrypted_msg)
        for i in range(len(chr_list)):
            for j in range(3):
                test_msg = decrypt(ord(count_list[0][j])-ord(chr_list[i]),encrypted_msg)
                test_error = 0
                for p in range(len(test_msg)):
                    if (test_msg[p] != " " and test_msg[p] != "," and test_msg[p] != ".") and test_msg[p] < "0" or test_msg[p] > "Z" and test_msg[p] < "a" or test_msg[p] > "z":
                        test_error += 1
                        if test_error/len(test_msg) > 0.1:
                            break
                if test_error/len(test_msg) < 0.1 and lowerCase(test_msg).find("the") != -1:
                    key = ord(count_list[0][j])-ord(chr_list[i])
                    output(test_msg)
                    return
        if key == "":
            print("Decryption failed. Please check the input and try again.")
            restart()
        
def decrypt(key, msg):
    global decrypted_msg
    for i in range(len(msg)):
        if usr_selection[1] == 1:
            if msg[i] >= "a" and msg[i] <= "z":
                decrypted_msg += chr((26 + ord(msg[i]) - key - 97)%26+97)
            elif msg[i] >= "A" and msg[i] <= "Z":
                decrypted_msg += chr((26 + ord(msg[i]) - key - 65)%26+65)
            else:
                decrypted_msg += msg[i]
        else:
            decrypted_msg += chr((94 + (ord(msg[i]) - key)-32)%94+32)
    return decrypted_msg

def output(msg):
    statistics = ""
    word_frequency = frequent(lowerCase(msg).replace(".","").replace(",","").split())
    chr_frequency = frequent(lowerCase(msg))
    print("\nChoose the sequence of word and character frequency list\n1 From the most frequent to the least frequent\n2 From the least frequent to the most frequent")
    order = rangeValidation("2")
    num_items = input("Please choose the no. of items to be shown: ")
    correct_input = False
    while correct_input == False:
        correct_input = True
        for i in range(len(num_items)):
            if num_items[i] < "0" or num_items[i] > "9":
                print(error_msg)
                correct_input = False
                break
        if correct_input == True:
            if int(num_items) < 0 or int(num_items) > len(word_frequency[0]) or int(num_items) > len(chr_frequency[0]):
                print("Number may have exceeded the number of distinct words. Please try again.")
                correct_input = False
        if correct_input == False:
            num_items = input("Please choose the no. of items to be shown: ")
    num_items = int(num_items)
    statistics += "Key: "+ str(key)
    msg = lowerCase(msg)
    statistics += "\nWord count: "+str(len(msg.split()))+"\nCharacter count: "+str(len(msg))+"\n"
    if order == 1:
        statistics += f"\nMost frequent words:\n    {"Word":<15}\tCount\n"
        for i in range(num_items):
            statistics += f"{i+1:>2}  {word_frequency[0][i]:<15}\t{word_frequency[1][i]}\n"
        statistics += f"\nMost frequent characters:\n    {"Character":<10}\tCount\n"
        for i in range(num_items):
            if chr_frequency[0][i] == " ":
                statistics += f"{i+1:>2}  {"whitespace":<10}\t{chr_frequency[1][i]}\n"
            else:
                statistics += f"{i+1:>2}  {chr_frequency[0][i]:<10}\t{chr_frequency[1][i]}\n"
    else:
        statistics += f"\nLeast frequent words:\n    {"Word":<15}\tCount\n"
        for i in range(len(word_frequency[0])-1, len(word_frequency[0])-1-num_items, -1):
            statistics += f"{len(word_frequency[0])-i:>2}  {word_frequency[0][i]:<15}\t{word_frequency[1][i]}\n"
        statistics += f"\nLeast frequent characters:\n    {"Character":<10}\tCount\n"
        for i in range(len(chr_frequency[0])-1, len(chr_frequency[0])-1-num_items, -1):
            if chr_frequency[0][i] == " ":
                statistics += f"{len(chr_frequency[0])-i:>2}  {"whitespace":<10}\t{chr_frequency[1][i]}\n"
            else:
                statistics += f"{len(chr_frequency[0])-i:>2}  {chr_frequency[0][i]:<10}\t{chr_frequency[1][i]}\n"
    print("******************************************************************************************************************************")
    print("Decrypted message:", decrypted_msg)
    print(statistics)
    print("******************************************************************************************************************************")
    menu(2)
    if usr_selection[2] != 4:
        fileSaving(statistics)

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
    restart()

def restart():
    if yesNoValidation("Restart program? [Y/N] ") == True:
        startUp()
    else:
        print("Program ended.")

startUp()