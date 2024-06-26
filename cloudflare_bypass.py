#Ｈｅｌｌｔａｋｅｒ ｃ３ｒｂ



import time
from DrissionPage import ChromiumPage, ChromiumOptions


def pass_cycle(_driver: ChromiumPage):

    try:
        if _driver('xpath://div/iframe').s_ele(".ctp-checkbox-label") is not None:
            _driver('xpath://div/iframe').ele(".ctp-checkbox-label", timeout=0.1).click()
    except:
        pass


if __name__ == '__main__':

    browser_path = "/usr/bin/google-chrome"

    options = ChromiumOptions()
    options.set_paths(browser_path=browser_path)

    arguments = [
        "-no-first-run",
        "-force-color-profile=srgb",
        "-metrics-recording-only",
        "-password-store=basic",
        "-use-mock-keychain",
        "-export-tagged-pdf",
        "-no-default-browser-check",
        "-disable-background-mode",
        "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
        "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
        "-deny-permission-prompts",
        "-disable-gpu"
    ]

    for argument in arguments:
        options.set_argument(argument)

    driver = ChromiumPage(addr_driver_opts=options)

    driver.get('https://nowsecure.nl')

    while True:
        pass_cycle(driver)
        try:
            ele = driver.s_ele('xpath://h3')
            if ele.text == "nowSecure.nl":
                break
        except:
            time.sleep(.1)
    time.sleep(5)
 
    driver.quit()
    print("Done")














#Ｈｅｌｌｔａｋｅｒ ｃ３ｒｂ
