import os
import sys

# 하나로 합칠 파일들이 저장된 폴더 이름을 시스템으로부터 입력
directory = sys.argv[1]

# 하나로 합쳐진 파일의 이름을 정의
outfile_name = "합친_파일.csv"

# 결과물 파일을 생성
output_file = open(outfile_name, "w")

# 폴더의 내용물을 열람해서 목록을 생성
input_files = os.listdir(directory)

# 헤더를 분리하기 위한 변수를 정의
# 밑에 for 문이 한 번 실행된 후 False 전환 예정
outfile_header = False

# 폴더의 내용물을 하나 하나 불러와서 합치는 작업을 수행
for filename in input_files:
    # csv 파일이 아닌 것은 걸러줌
    if ".csv" not in filename:
        continue
    
    # csv 파일이 맞다면, 파일을 읽어옴
    # 샘플_폴더/파일명
    file = open(directory + "/" + filename)
    
    # 첫 번째 줄 헤더를 정의
    # 포커스가 헤더 다음 줄에 맞춰짐
    header = file.readline()
    
    # 첫 번재 줄 헤더를 파일에 입력, 최초 1회만 실행
    if not outfile_header:
        output_file.write(header.strip())
        outfile_header = True
        
    # 결과물 파일에 내용물을 입력
    output_file.write("\n" + file.read())
    
    # 읽어온 파일들을 종료
    file.close()
    
# 결과물 파일을 종료
output_file.close()