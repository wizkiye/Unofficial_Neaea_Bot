import subprocess

scraper_repo = "https://github.com/wizkiye/neaea_scraper.git"
print("Installing neaea_scraper...")
subprocess.call(["pip", "install", "git+" + scraper_repo], stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)
print("Installing dependencies...")
subprocess.call(["pip", "install", "-r", "./requirements.txt"], stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)
print("Done!")
print("run 'python3 main.py' to start the bot.")
print("Bye!")
exit()
