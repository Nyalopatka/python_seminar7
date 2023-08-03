def ritm(txt,i):
    count_a = sum(map(lambda x : 1 if "а" in x else 0,txt.split(" ")[i]))
    return count_a

txt = input("введите стих винипуха: ") # парам пам-пам
phrasi = txt.count(" ")

result_set = set()
for i in range(phrasi+1):
    result_set.add(ritm(txt,i))

if len(result_set) == 1:
    print('парам пам-пам')
else:print('пам парам')

