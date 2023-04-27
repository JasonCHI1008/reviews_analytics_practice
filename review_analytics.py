data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))            
print(len(data))
#word count------------------
wc = {} #dictionary
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #add new word in wc

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input("what word are you looking for:")
    if word == "q":
        break
    if word in wc:
        print(word, " appears", wc[word], "times")
    else:
        print('This word does not exist')











# sum_len = 0
# for d in data:
#     sum_len += len(d)
# ave = sum_len / 1000000
# print("the average of commment is", ave)

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('There are', len(new),'smaller than 100')
