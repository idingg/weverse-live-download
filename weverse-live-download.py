import subprocess
import sys
import os

print("필요파일 설치확인 중")


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "-q", "install", package])


install("requests")
install("playwright")

from playwright.sync_api import sync_playwright
import requests
import datetime


def main():
    addr = ""
    while addr == "" or addr.startswith("https://weverse.io/") == False:
        addr = input("다운받을 위버스 주소 (입력예 : https://weverse.io/... ) : ")

    playwright = sync_playwright().start()

    print("브라우저 실행 중")
    # browser = playwright.chromium.launch(headless=True)

    try:
        browser = playwright.chromium.launch(headless=True, channel="msedge")
    except:
        try:
            browser = playwright.chromium.launch(headless=True, channel="chrome")
        finally:
            0
    page = browser.new_context().new_page()
    reqs = []
    page.on("request", lambda request: reqs.append([request.method, request.url]))
    print("요청 수집 중")
    page.goto(url=addr, wait_until="networkidle")
    browser.close()
    playwright.stop()

    m3u8_allurl = ""
    print(".m3u8 파일 찾는 중")
    for item in reqs:
        if item[1].find(".m3u8") != -1:
            m3u8_allurl = item[1]
            break

    m3u8_resolutions = requests.get(m3u8_allurl).content.decode().split(",")

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

    resolution_to_get = input(
        "해상도 선택 (기본값 : "
        + resolutions[0]
        + ", 입력예 : 1080 또는 720 또는 1920x1080 또는 1280x720 ... ) : "
    )
    if resolution_to_get == "":
        resolution_to_get = resolutions[0]

    for item in m3u8_resolutions:
        if item.find(resolution_to_get) != -1:
            m3u8_1080filename = item.splitlines()[1]
            break
    end = m3u8_allurl.find(".m3u8") + 4
    start = m3u8_allurl.rfind("/")
    m3u8_1080url = m3u8_allurl.replace(
        m3u8_allurl[start + 1 : end + 1], m3u8_1080filename
    )
    tsfiles = requests.get(m3u8_1080url).content.decode().split(sep=",")
    tsurls = []
    for item in tsfiles:
        if item.find(".ts") != -1:
            tmp = item.splitlines()[1]
            tsurls.append(
                [m3u8_allurl.replace(m3u8_allurl[start + 1 : end + 1], tmp), tmp]
            )

    path = m3u8_allurl[
        m3u8_allurl.find("weverse_") : m3u8_allurl.find(
            "/", m3u8_allurl.find("weverse_")
        )
    ]
    path = m3u8_1080filename.replace(".m3u8", ".ts", 1)
    cnt = 1

    # save to file
    downloadsize = 0
    starttime = datetime.datetime.now()
    with open("./" + path, "wb+") as one_ts:
        for item in tsurls:
            data = requests.get(item[0])
            one_ts.write(data.content)
            downloadsize += data.content.__len__()
            nowtime = datetime.datetime.now()
            etime = nowtime - starttime
            tsurlslen = len(tsurls)
            barsize = 25
            print(
                "\r"
                #                + item[1]
                #                + " "
                + str(etime).split(".")[0]
                + " / "
                + str(etime / cnt * tsurlslen).split(".")[0]
                + " {:4d}".format(cnt)
                + " / "
                + str(tsurlslen)
                + "  {:5}".format(
                    int(downloadsize / (nowtime.timestamp() - starttime.timestamp()))
                    >> 10
                )
                + " KB/s"
                + "  {:6.2f}".format(cnt * 100 / tsurlslen, 3)
                + " %"
                + ("  [{:" + str(barsize) + "s}] ").format(
                    "|" * int((cnt / tsurlslen) * barsize)
                ),
                end="",
            )
            cnt += 1
    input("\n다운로드 완료( " + os.getcwd() + "\\" + path + " )")


if __name__ == "__main__":
    main()
