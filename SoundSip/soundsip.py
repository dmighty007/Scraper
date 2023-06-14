# This code is a Python script that downloads audio files from a website called "soundsip.com".
# Specifically, it downloads Bengali audio stories from the "Sunday Suspense" and "Midnight Horror
# Station" categories. The script uses the BeautifulSoup library to parse the HTML content of the
# website, the requests library to make HTTP requests to the website, and the subprocess library to
# run the wget command to download the audio files. The script creates a new directory called "SS" and
# changes the current working directory to that directory. It then loops through the pages of the
# website and extracts the names of the audio files from the HTML content using BeautifulSoup. It
# replaces any spaces in the file names with "%20" to make them compatible with the wget command.
# Finally, it downloads the first 10 files on each page using the wget command.
from bs4 import BeautifulSoup as bs
import requests
import subprocess as sp 
import os

os.mkdir("../SS")
os.chdir('../SS/')

prefix = "https://wish2.soundsip.com/sugarstream/soup/files/Audio%20Stories/Bengali%20Audio%20Stories/Midnight%20Horror%20Station/"
prefix = "https://wish2.soundsip.com/sugarstream/soup/files/Audio%20Stories/Bengali%20Audio%20Stories/Sunday%20Suspense/Higher%20Quality%20-%20128ks/"

for page in range(1, 58):
    r = requests.get(f"https://soundsip.com/sunday-suspense-radio-mirchi-hq-mp3-download.xhtml?page={page}&sort=ff")
    
    soup = bs(r.content)
    n = len(soup.find_all('table'))
    name_list = [soup.find_all('table')[i].find_all('b')[0].text for i in range(n)]
    replaced_name_list = []
    for name in name_list:
        replaced_name_list.append(name.replace(" ", "%20"))

    for i in range(10):
        result = sp.run(
            ["wget", "-c", f"{prefix}{replaced_name_list[i]}"], capture_output=True, text=True)
