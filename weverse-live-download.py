import datetime
from time import sleep
import os
import sys
import subprocess
from multiprocessing import Pool
import asyncio


def install(package):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "-qq", "install", package])


def downloadts(url: str):
    from requests import get
    return get(url)


async def getcontentlen_async(urls):
    import aiohttp
    sum = 0
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with await session.head(url) as response:
                sum += int(response.headers['Content-Length'])
    return sum


def run_getcontentlen_async(urls):
    return asyncio.run(getcontentlen_async(urls))


def getcontentlen(url):
    from requests import head
    return int(head(url).headers['Content-Length'])


def main():
    from playwright.sync_api import sync_playwright
    import aiohttp
    import requests
    playwright = sync_playwright().start()
    try:
        browser = playwright.chromium.launch(
            headless=True, channel="chrome")
    except:
        try:
            browser = playwright.chromium.launch(
                headless=True, channel="msedge")
        except:
            try:
                browser = playwright.firefox.launch(headless=True)
            except:
                print("브라우저가 발견되지 않아 전용 크롬 모듈을 설치합니다.")
                subprocess.check_call(
                    [sys.executable, "-m", "playwright", "install", "chromium"])
                browser = playwright.chromium.launch(headless=True)

    page = browser.new_context().new_page()
    reqs = []
    page.on("request", lambda request: reqs.append(
        [request.method, request.url]))
    addr = ""
    while addr == "" or addr.startswith("https://weverse.io/") == False:
        addr = input(
            "다운받을 위버스 라이브 주소 (입력예 : https://weverse.io/... [엔터]) : ")

    print("라이브 데이터 수집 중")
    page.goto(url=addr, wait_until="networkidle")
    browser.close()
    playwright.stop()

    print("라이브 데이터 분석 중")
    m3u8_allurl = ""
    for item in reqs:
        if item[1].find(".m3u8") != -1:
            m3u8_allurl = item[1]
            break
    m3u8_resolutions = requests.get(
        m3u8_allurl).content.decode().split(",")

    print("선택가능 해상도 : ", end="")
    resolutions = []
    for item in m3u8_resolutions:
        resstr = item.splitlines()[0]
        if resstr.find("RESOLUTION=") != -1:
            resolutions.append(resstr.split("=")[1])
            print(resstr.split("=")[1], end=" ")
    print()

    if len(resolutions) > 1 and int(resolutions[0].split("x")[0]) < int(resolutions[1].split("x")[0]):
        resolutions.reverse()

    m3u8_1080filename = ""
    while m3u8_1080filename == "":
        resolution_to_get = input(
            "해상도 선택 (기본값 : "
            + resolutions[0]
            + ", 입력예 : 1080[엔터], 1920[엔터], 1920x1080[엔터], ... ) : "
        )
        if resolution_to_get == "":
            resolution_to_get = resolutions[0].split("x")[-1]

        for item in m3u8_resolutions:
            res1 = str(item.splitlines()[0].split("x")[0].split("=")[-1])
            res2 = str(item.splitlines()[0].split("x")[-1])
            if res1 == resolution_to_get or res2 == resolution_to_get:
                m3u8_1080filename = item.splitlines()[1]
                break
    end = m3u8_allurl.find(".m3u8") + 5
    start = m3u8_allurl[:end].rfind("/")
    m3u8_1080url = m3u8_allurl.replace(
        m3u8_allurl[start + 1: end], m3u8_1080filename)

    first_content = b""
    new_content = requests.get(m3u8_1080url).content

    # save to file
    if m3u8_1080url.find("live") != -1:
        path = new_content[
            new_content[: new_content.find(b".ts") + 3].rfind(b"\n")
            + 1: new_content.find(b".ts")
            + 3
        ].decode()
    elif m3u8_1080url.find("VOD") != -1:
        path = m3u8_1080filename[m3u8_1080filename.rfind("/") + 1:].replace(
            ".m3u8", ".ts", 1
        )

    one_ts = open("./" + path, "wb+")
    while new_content != first_content:
        tsfiles = new_content.replace(
            first_content, b"", 1).decode().split(sep=",")
        if m3u8_1080url.find("live") != -1:
            end = len(m3u8_1080url)
        elif m3u8_1080url.find("VOD") != -1:
            end = m3u8_1080url.find(".m3u8") + 5
        start = m3u8_1080url[: m3u8_1080url.find(".m3u8")].rfind("/")

        tsurls = []
        for item in tsfiles:
            if item.find(".ts") != -1:
                tmp = item.splitlines()[1]
                tsurls.append(m3u8_1080url.replace(
                    m3u8_1080url[start + 1: end], tmp))

        cnt = 0
        filesize = 0
        downloadsize = 0
        poolsize = os.cpu_count()
        start = 0
        end = start+poolsize
        download_starttime = datetime.datetime.now()

        print("파일용량 계산 중 ... ", flush=True)
        with Pool(poolsize) as p:
            tsurls_sliced = []
            for i in range(poolsize):
                tsurls_sliced.append(
                    tsurls[int(len(tsurls)*i/poolsize):int(len(tsurls)*(i+1)/poolsize)])
            filesize = sum(p.map(run_getcontentlen_async, tsurls_sliced))
        # with Pool(poolsize) as p:
        #     filesize = sum(p.map(getcontentlen, tsurls))
        # print("{:d}MB".format(filesize >> 20))

        with Pool(poolsize) as p:
            tsurlslen = len(tsurls)
            while start < len(tsurls):
                tsurls_part = tsurls[start:end]
                download_part_size = 0
                part_starttime = datetime.datetime.now()
                for item in p.map(downloadts, tsurls_part):
                    one_ts.write(item.content)
                    download_part_size += item.content.__len__()
                    cnt += 1
                nowtime = datetime.datetime.now()
                downloadsize += download_part_size
                etime = nowtime - download_starttime
                barsize = 25
                print(
                    "\r"
                    #                + item[1]
                    #                + " "
                    + str(etime).split(".")[0]
                    + " / "
                    + str(etime / cnt * tsurlslen).split(".")[0]
                    # + " {:4d}".format(cnt)
                    # + " / "
                    # + "{:4d}".format(tsurlslen)
                    + " {:4d}".format(downloadsize >> 20)
                    + " /"
                    + " {:4d} MB".format(filesize >> 20)
                    + " {:5.1f}".format((float)(int(download_part_size / (
                        nowtime.timestamp() - part_starttime.timestamp())) >> 10) / 1000)
                    + " MB/s"
                    + " {:6.2f}".format(cnt * 100 / tsurlslen, 3)
                    + " %"
                    + (" [{:" + str(barsize) + "s}]").format(
                        "|" * int((cnt / tsurlslen) * barsize)
                    ),
                    end="",
                )
                start = end
                end = start+poolsize

        if m3u8_1080url.find("live") != -1:
            print("\n30초간 이어지는 영상이 있는지 확인 후 저장합니다. 라이브 종료까지 반복됩니다.")
            one_ts.close()
            sleep(30)
            one_ts = open("./" + path, "ab+")
        first_content = new_content
        new_content = requests.get(m3u8_1080url).content
    one_ts.close()

    print("\n다운로드 완료( " + os.getcwd() + "\\" + path + " )")


if __name__ == "__main__":
    print("\n* 저작권자의 동의 없이 콘텐츠를 무단 배포 및 가공하는 행위는 저작권 침해에 해당합니다.")
    print("* Unauthorized or illegal distribution of paid contents, which are available exclusively to those who paid for the subscription, is punishable by law.\n")

    print("필수모듈 설치확인 중")
    isinstalled = False
    try:
        from playwright.sync_api import sync_playwright
        import aiohttp
    except:
        print("라이브 데이터 수집모듈이 발견되지 않아 설치합니다.")
        install("playwright")
        install("aiohttp")
        isinstalled = True
    try:
        import requests
    except:
        print("라이브 데이터 다운로더가 발견되지 않아 설치합니다.")
        install("requests")
        isinstalled = True
    if isinstalled == True :
        print("\n새로운 모듈이 설치되었습니다. 다시 시작해주세요.")
        print("Enviroment changed. Please restart.")
        exit()
    main()
