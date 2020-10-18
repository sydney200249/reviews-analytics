import time
import progressbar
# data = [] 
# sum_len = 0
# for d in data:
#     sum_len += len(d)
# print('留言平均長度為', sum_len / len(data))

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有', len(new), '筆留言長度小於100')
# print(new[0])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '提到good')
# print(good[1])

#以下新增文字計數及查詢功能
data = [] 
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r')as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
        # if count % 1000 == 0:
        #     print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

#計算文字數量
start_time = time.time()
wc = {} 
for d in data:
    words = d.split() #分割符號不打就是默認使用空白鍵分割，無需另外打' '做分割
    for word in words:
        if word in wc:
            wc[word] += 1 #查找並增加次數
        else:
            wc[word] = 1 #新增key進去wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, '秒')

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請輸入想查找的字(按q離開)：')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為：', wc[word])
    else:
        print('沒有這個字喔')
print('感謝使用本查詢功能')