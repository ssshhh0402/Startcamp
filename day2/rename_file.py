import os
# 1.dummy 들어가기

# 2. 파일들의 파일명을 하나씩 변경한다.
# 3.
os.chdir("./dummy")
print(os.getcwd())

files = os.listdir('.')
print(files)

for file in files:
    os.rename(file, 'SAFFY' + file)

