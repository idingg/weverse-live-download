# weverse-live-download  <br>
Python code to download weverse live video on you PC.  <br>
You need Python3.8+, Google Chrome or Microsoft Edge or Mozilla Firefox browser on Windows 10+, MacOS 12 Monterey, 13 Ventura, Debian 11, Ubuntu 20.04 or 22.04 PC.  <br>
Install Python, download files, run .bat file or .py file directly.  <br>
You can install easily python3.8+ at the [Microsoft Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=ko-kr&gl=kr)  <br>
or [https://www.python.org/](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)  <br>
  <br>
위버스 라이브 다운로드용 파이썬 코드입니다.  <br>
크롬 또는 엣지 또는 파이어폭스 브라우저와 파이썬 3.8 이상 버전과 함께 Windows 10 이상, MacOS 12 Monterey, MacOS 13 Ventura, Debian 11, Ubuntu 20.04 or Ubuntu 22.04 가 설치된 컴퓨터에서 실행 가능합니다.  <br>
  <br>
사용방법  <br>
1. [크롬](https://www.google.com/intl/ko_kr/chrome/) 또는 [엣지](https://www.microsoft.com/ko-kr/edge/download) 또는 [파이어폭스](https://www.mozilla.org/ko/firefox/windows/) 브라우저 설치  <br>
2. 코드 실행을 위한 파이썬 설치  <br>
　2-1. [마이크로소프트 스토어(추천)](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=ko-kr&gl=kr)  <br>
　2-2. [파이썬 공식 홈페이지](https://www.python.org/downloads/)  <br>
3. 코드파일 다운로드  <br>
4. 파이썬을 통해 코드 실행(택1)  <br>
　4-1.　.py,　.bat 다운로드 후 .bat 실행(추천)  <br>
　4-2.　.py 만 다운로드 후 명령 프롬프트 창에서 python (다운로드 폴더 경로)\weverselivedown.py(엔터) 입력  <br>
　　4-2-1. 입력 예 : python C:\Users\username1\Downloads\weverselivedown.py  <br>
5. "'python'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다." 와 같은 오류 발생 시 재부팅 후 4번부터 진행  <br>
6. 첫 실행 시 추가코드 다운로드 진행 대기  <br>
7. 다운받을 위버스 주소 입력  <br>
　7-1. 입력 예 : https://weverse.io/xxxxx/live/xxxxxxxxxxx (엔터)  <br>
8. 다운받을 해상도 입력(택1)  <br>
　8-1. 선택가능 해상도 : 1920x1080 1280x720 854x480 640x360 480x270 256x144 로 나올 때  <br>
　　8-1-1. (엔터) -> 화면에 표시되는 (기본값 : 1920x1080) 해상도로 다운로드  <br>
　　8-1-2. 1920x1080(엔터) ─┬─ 1920x1080 해상도로 다운로드  <br>
　　　　　 1920(엔터)　　　─┤  <br>
　　　　　 1080(엔터)　　　─┘  <br>
　　　　　 1280x720(엔터)　─┬─ 1280x720 해상도로 다운로드  <br>
　　　　　 1280(엔터)　　　─┤  <br>
　　　　　 720(엔터)　　　 ─┘  <br>
　　　　　 854x480(엔터)　 ─┬─ 854x480 해상도로 다운로드  <br>
　　　　　 854(엔터)　　　 ─┤  <br>
　　　　　 480(엔터)　　　 ─┘  <br>
　　　　　 640x360(엔터)　 ─┬─ 640x360 해상도로 다운로드  <br>
　　　　　 640(엔터)　　　 ─┤  <br>
　　　　　 360(엔터)　　　 ─┘  <br>
　　　　　 480x270(엔터)　 ─┬─ 480x270 해상도로 다운로드  <br>
　　　　　 480(엔터)　　　 ─┤  <br>
　　　　　 270(엔터)　　　 ─┘  <br>
　　　　　 256x144(엔터)　 ─┬─ 256x144 해상도로 다운로드  <br>
　　　　　 256(엔터)　　　 ─┤  <br>
　　　　　 144(엔터)　　　 ─┘  <br>
9. 화면의 정보가 ( 0:00:23 / 0:03:05　103 / 806　 4298 KB/s　 12.78 %　[|||　　　　　　　　　　　] ) 일 때  <br>
　　　　　　　　1　　　 2　　　3　　 4　　　 5　　　　　6　　　　　　　　　7  <br>
　　9-1. 경과 시간  <br>
　　9-2. 예상 시간  <br>
　　9-3. 받은 파일 용량  <br>
　　9-4. 전체 파일 용량  <br>
　　9-5. 다운로드 속도  <br>
　　9-6. 진행률  <br>
　　9-7. 진행률 표시 바  <br>
10. 코드 파일이 있는 폴더에 저장되며 완료 시 파일경로 표시  <br>
　10-1. 출력 예 : 다운로드 완료( C:\Users\user1\Downloads\xxxxxxxxxxxxxxxxxxxx.ts )  <br>
　10-2. 현재 라이브 중인 경우 현재까지의 영상 다운로드 후 '30초 간 대기, 30초 간 확인된 추가영상을 한번에 다운로드'를 라이브 종료 시까지 반복합니다.  <br>
  <br>

## run example(실행 예)
첫번째 실행 이후에는 7번으로 가주세요.  <br>
after first launch, go to step 7.  <br>
1. 파이썬 설치 install python, example for Microsoft Store  <br>
![01](https://github.com/idingg/weverse-live-download/assets/48832274/e9838c4f-9da8-41fa-abc8-2b1ea024cb8d)  <br>
2. 다운로드 클릭 Click download  <br>
![02](https://github.com/idingg/weverse-live-download/assets/48832274/c30af5f8-e400-4273-a987-744d12e5936b)  <br>
3. 코드 파일 다운로드 Download code file from github page  <br>
![03](https://github.com/idingg/weverse-live-download/assets/48832274/f35aca76-240a-413e-aee3-2b320127c3a8)  <br>
4. 압축 해제 Unzip file  <br>
![04](https://github.com/idingg/weverse-live-download/assets/48832274/0a5b939c-e450-4b9a-a85e-da7fc7a1d96e)  <br>
5. bat 파일 실행 Run batch file(.bat)  <br>
![05](https://github.com/idingg/weverse-live-download/assets/48832274/7d9856db-3b42-4f3b-9617-dc7989c80ca0)  <br>
6. 첫 실행시 모듈 설치, 재실행 해주세요 Install modules on first launch, plaese restart  <br>
![06](https://github.com/idingg/weverse-live-download/assets/48832274/5d1c9f97-ab8d-4bc8-a00b-da92f04145ad)  <br>
### 첫번째 실행 이후(after first launch)  <br>
7. 위버스 라이브 주소 복사 Copy weverse live url  <br>
![07](https://github.com/idingg/weverse-live-download/assets/48832274/88117660-519f-46f8-8b86-3dbfca80e95f)  <br>
8. bat 파일 실행, 주소 붙여넣기 run batch file and paste url  <br>
![08](https://github.com/idingg/weverse-live-download/assets/48832274/c9edad2b-3c96-4898-98b4-2bb960f469a5)  <br>
9. 해상도. 그냥 엔터 입력시 최대 해상도 선택, 또는 표시된 해상도 중 선택 가능  <br>
Resolution. Press just enter for maximum resolution, or select between available resolutions then enter  <br>
![09](https://github.com/idingg/weverse-live-download/assets/48832274/bb60584c-e0fc-4391-9e52-58b647ebcde2)  <br>
10. 다운로드 정보 Download infermation  <br>
영상 파일은 코드 파일과 같은 폴더에 저장됩니다.
The downloader stores the video in the same folder where the code file is located   <br>
![10](https://github.com/idingg/weverse-live-download/assets/48832274/575f7a97-0cb2-458a-8208-c8e5dda6f5f9)  <br>
11. 다운로드 완료 시 파일 위치 표시  <br>
When download completed, The location of the file is displayed  <br>
![11](https://github.com/idingg/weverse-live-download/assets/48832274/28ecbcd8-2099-4454-9e15-dcca2f5e35d3)  <br>
12. You got video file. <br>
![12](https://github.com/idingg/weverse-live-download/assets/48832274/3f17387e-2304-41c3-8bbd-20b367b5fb23)  <br>
