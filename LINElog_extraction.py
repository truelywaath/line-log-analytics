#ファイル読み込み
uploaded = open("LINElog.txt","r")
text = uploaded.read()

#参加者のコメントを抽出
comments_list=[]

i_prev=0
for i in range(len(text)):
  # '12:34'の形式を探し、その間にある話者・コメントを抜き出す
  window=text[i:i+5]
  if window[0:2].isnumeric() and window[2]==':' and window[3:].isnumeric():
    comments_list.append(text[i_prev:i])
    i_prev=i


#コメントごとに発話者のリストを作成
name_list=[]

for comment in comments_list:
  name=comment[6:][:comment[6:].find('\t')]
  name_list.append(name)

name_list

#発言内容を抽出
contents_list=[]
for comment in comments_list:
  content=comment[6:][comment[6:].find('\t')+1:]
  contents_list.append(content)

contents_list

# 参加者のリストを作成する（発話者リストから「～が参加しました」「～がメッセージを取り消しました」などの要素を削除する）

pure_name_list=[]

for name in name_list:
  if '\r' not in name:
    pure_name_list.append(name)

name_set=list(set(pure_name_list))

name_set

#各人の毎にコメント内容を集積し、dict（辞書）を作成する
user_contents_dict={}

for target_name in name_set:
    filename='output_{0}.txt'.format(target_name)
    output = open(filename,"w")
    contents_temp=[]
    for i,name in enumerate(name_list):
        if name==target_name:
            contents_temp.append(contents_list[i])
    output.write(str(contents_temp))
    output.close()
    user_contents_dict[target_name]=contents_temp

uploaded.close()
