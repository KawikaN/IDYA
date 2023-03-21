from bs4 import BeautifulSoup
import pyautogui
from bs4 import BeautifulSoup
import requests

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
testing = "word"

#ask someone else for their favorite song and click  a button to search the song up and output the result

def song(choice):

    #with open('home.html', 'r') as html_file:
    #    content = html_file.read()
        


    #    soup = BeautifulSoup(content, 'lxml')
    #    tags = soup.find('h5')
    #    print(tags)

    #"Leviathanjptv-chug-jug-with-you-number-one-victory-royale"

    page_to_scrape = requests.get("https://genius.com/" + choice + "-lyrics") #using genius for the lyrics
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    msg = soup.findAll("span", attrs={"class":"ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw"})
    msg2 = soup.findAll("span", attrs={"class":"ReferentFragmentdesktop__ClickTarget-sc-110r0d9-0 jvutUp"}) #not used

    # for msgs in msg:
    #     print(msgs.text)
    #try:
    for i in range(2):
        for msgs in msg:
            if msgs.text[0].lower() in alpha:
                print('is')
                pass
            else:
                print("Could not find the lyrics to this song please enter a different song \n")
                #raise StopIteration
            for letters in msgs:
                try:
                    if(letters[0] == "<"): # if it throws an error (Only throws this error when at the break(<br/> of html coe) *trying to remove the <br/> from output)
                        pass
                except:
                    continue #skips the itteration with the break line in it
                print(letters) #outputs the letters from each line of the lyrics
                continue
        
        #print("Raising ErrorF")
        #raise StopIteration
                # for i in range(len(letters)-1, 0-1, -1):
                #     print(msgs.text[i])
    # except StopIteration:
    #     print('stoping')
    #     pass

# "Leviathanjptv-chug-jug-with-you-number-one-victory-royale"
song("Leviathanjptv-chug-jug-with-you-number-one-victory-royale")