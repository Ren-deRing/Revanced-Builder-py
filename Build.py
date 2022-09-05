from Util import downloader
from Util import EasyJSON
import googletrans, zipfile, os, psutil, sys, time
from win32com.shell import shell

ver = 1.0

translator = googletrans.Translator()
mem = dict(psutil.virtual_memory()._asdict())
patches = []

print("\n\n\n\n\n\n\nRevanced Builder")

if not shell.IsUserAnAdmin() :

    print("\n\n[!] 관리자 권한이 없습니다.\n[ EXIT ] 프로그램을 자동으로 종료합니다.")
    time.sleep(5)
    exit(0)

print("[ UPDATE ] 업데이트 체크 중입니다...")
downloader('https://github.com/Ren-deRing/Revanced-Builder-py/releases/latest/download/ver.txt', './ver.txt')

with open('ver.txt', 'r') as f:

    if str(f.read) != str(ver):

        os.system("del url.json")
        downloader('https://github.com/Ren-deRing/Revanced-Builder-py/releases/latest/download/url.json', './url.json')

        print("[ UPDATE ] URL 업데이트 성공\n")


print("[ Download ] 필요한 파일을 다운로드 중입니다...")

urls = EasyJSON.loadjs(directory="url.json")

url = str(urls['url']['patch'])
downloader.file(url, './revanced-pathes.jar')
url = str(urls['url']['patchlist'])
downloader.file(url, './patches.json')
url = url = str(urls['url']['cli'])
downloader.file(url, './revanced-cli.jar')
url = url = str(urls['url']['unsin'])
downloader.file(url, './app-unsigned.apk')
url = url = str(urls['url']['youtube'])
downloader.file(url, './youtube.apk')
url = url = str(urls['url']['zulu'])
downloader.file(url, './zulu.zip')

zulu_zip = zipfile.ZipFile('./zulu.zip')
zulu_zip.extractall('C:/Program Files')
 
zulu_zip.close()

print("\n[?] 입력할 기능을 선택해 주세요.")

js = EasyJSON.loadjs(directory="./patches.json")

a = 0
res = []

for i in js:
    
    if i['compatiblePackages'][0]['name'] == 'com.google.android.youtube':

        res.append(i['name'])
        result = translator.translate(str(i['description']), dest='ko')
        print(i['name'] + "         - " + result.text)

        if i['excluded'] == True or i['name'] == 'setting' or i['name'] == 'video-ads' or i['name'] == 'general-ads':

            patches.append(i['name'])


print("\n[?] EXIT : 나가기")

i = a

while True:

    ins = input(">")

    if ins == "EXIT" or ins == "exit" or ins == "나가기":
        break
    else:
        if ins in patches:
            print("[!] 이미 적용되어있는 옵션입니다.")
        else:
            if ins in res:
                patches.append(ins)
                print("[ OK ] 적용되었습니다.")
            else:
                print(str("[!] 입력한 기능이 없습니다."))

    i = i + 1



upstring = '-i microg-support'

for i in patches:
    upstring = upstring + " -i " + i

for i in res:
    if i not in patches:
        upstring = upstring + " -e " + i

print("\n[ Build ] 빌드 중입니다...")

os.system('\"C:\Program Files\zulu17.36.19-ca-jdk17.0.4.1-win_i686\\bin\java.exe\" -jar revanced-cli.jar -a youtube.apk -c  -o revanced.apk -b revanced-pathes.jar -m app-unsigned.apk ' + upstring)

print('\n[ OK ] 빌드가 완료되었습니다.\n [?] revanced.apk 파일을 안드로이드 스마트폰에 옮겨 설치해 주세요.')

time.sleep(10)

exit(0)