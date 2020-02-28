import requests, re,os,shutil


def get_ver():
    html = requests.get("https://github.com/qwerttqq95/698SP_CL/blob/master/ver").content
    q = re.compile(r'ver=\d{6}')
    qw = q.findall(str(html))
    if qw is None:
        return None
    ver = qw[0][4:]
    print("The new is " + ver)
    return ver


def loal_ver():
    f = open(".\\attach\\ver", 'r')
    text = f.read()
    q = re.compile(r'\d{6}')
    ver = q.findall(text)
    if ver is None:
        return None
    return ver.pop()


def update(new_ver):
    try:
        r = requests.get("https://github.com/qwerttqq95/698SP_CL/raw/master/cmake-build-release/698SP_CL.exe")
        with open(".\\attach\\698SP_CL.exe", "wb") as f:
            f.write(r.content)
        l = open(".\\attach\\ver", 'w')
        l.write("ver="+str(new_ver))
        print("下载完成...")
        return True
    except:
        print("网络遇到问题")
        return False


def delete():
    print("移除旧版...")
    try:
        os.system('taskkill /f /im %s' % '698SP_CL.exe')
        os.remove("698SP_CL.exe")
    finally:
        shutil.move(".\\attach\\698SP_CL.exe", "./")
        print("Update ok")


def main():
    new_ver = get_ver()
    local_ver = loal_ver()
    if new_ver is None or local_ver is None:
        print("升级检测失败")
    if new_ver == local_ver:
        print("无新版")
    elif int(new_ver) > int(local_ver):
        print("发现新版,开始升级...")
        if update(new_ver) is False:
            print("升级检测失败")
            return
        delete()
    else:
        print("????")


if __name__ == '__main__':
    main()
    os.system("pause")
