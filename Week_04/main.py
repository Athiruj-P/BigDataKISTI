print("#"*30)
print("#"*10 +" Week 04 " + "#"*10)
print("#"*30)
print()

def talk_to_your_computer():
    input_text = input("     Plase input some text: ")
    print()

    if input_text == "How are you?" or input_text == "how are you?":
        input("Fine, what about you?: ")
    elif input_text == "how are you":
        print("     The input is: {}".format(input_text))
    else:
        print("     Wrong queation!!")

def open_file():
    read_text = open("readMe.txt", "r")
    text = read_text.read()
    print(text)
    read_text.close()

def read_line():
    read_text = open("readMe_02.txt", "r")
    for line in read_text:
        print(line)
    read_text.close()

def using_if_find(name):
    text = "Athiruj"
    result = text.find(name)
    print(result)

using_if_find("test")