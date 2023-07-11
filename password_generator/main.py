# https://github.com/dwyl/english-words

import json
import time
import random as rand

def read_txt(file_name):
    with open(file_name, "r") as file:
        return file.read().split("\n")

def read_json(file_name):
    with open(file_name) as file:
        return list(json.load(file))

# Read from file. Split in to list with \n as delimiter.
words = read_txt("words.txt")

# Remove unwanted entries in list. 
words = [e for e in words if e != ""]
words = [e for e in words if len(e) > 2]
words = [e for e in words if len(e) < 7]

# Special characters
specialc = ["!", "@", "$", "%"]

# print(words)

gen_pass = []
for i in range(3):
    gen_pass.append(rand.choice(words))
    gen_pass.append(rand.choice(specialc))

print("".join(gen_pass))


# TODO: Double-check but it seems like reading from a .txt file is faster than reading from a json.

# start_time = time.time()

# x = read_txt("words.txt")
# # x = x.split("\n")
# print(x)

# print("--- %s seconds ---" % (time.time() - start_time))
# x = input()

# start_time = time.time()
# x = read_json("words.json")
# print(x)
# print("--- %s seconds ---" % (time.time() - start_time))