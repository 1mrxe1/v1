import sys
import subprocess


CACHE_FILE = "xxx"  # اسم ملف الكاش

def install_if_missing(package):
    """
    العراق 🇮🇶  عمك
    """
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def check_cache():
    """
    يتحقق من وجود ملف الكاش.
    """
    return os.path.exists(CACHE_FILE)


def create_cache():
    """
    ينشئ ملف الكاش.
    """
    with open(CACHE_FILE, "w") as f:
        f.write("تم تحميل المكتبات بنجاح.")


if not check_cache():  # التحقق من وجود ملف الكاش
    install_if_missing("pip")

    packages = [
        "googletrans==4.0.0-rc1",
        "telethon",
        "aiocron",        
        "ffmpeg",
        "emoji",
        "time",
        "asyncio",
        "datetime",
        "gpytranslate",
        "pytz",
        "gtts",
        "qrcode",
        "Telegram",
        "aiohttp",
        "fake_useragent",
        "user_agent",
        "hijri_converter"
    ]

    for package in packages:
        install_if_missing(package)

    create_cache()  # إنشاء ملف الكاش

os.system("clear")
