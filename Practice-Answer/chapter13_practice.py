# 다음 file 을 읽어서 가장 빈번하게 나타나는 top 10 단어들을 출력 
f = open('poet.txt')
counts = dict()

for line in f:
    for word in line.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
count_lst = []
for k, v in counts.items():
    count_lst.append((v, k))
    
print(sorted(count_lst, reverse=True)[:10])