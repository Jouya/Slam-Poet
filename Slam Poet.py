"""
Jouya Mahmoudi
11/11/2019
"""
import pyttsx3
import random
import glob
import random
from pygame import mixer
import nltk
import urllib
import inflect
# can be commented out after running the program for the first time
#nltk.download('wordnet')
from nltk.corpus import wordnet
# feel free to add more!
RAND_LIST = ["amazing","test","powerful","magic","sad","cold","creative"]


def present(string):
    """ Reads the poem at different speeds and voices """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_choice = random.randint(0,1)
    speed = random.randint(100,140)
    engine.setProperty('voice', voices[voice_choice].id) 
    engine.setProperty('rate', speed)
    #print(speed)
    engine.say(string)
    engine.runAndWait() 

def metaphor_magnet(word):
    """ Returns a list of words that matches properties to words according 
    to Google bigrams."""
    try:
        link = "http://ngrams.ucd.ie/metaphor-magnet-acl/q?kw=" + word
        f = urllib.request.urlopen(link)
        myfile = f.read()
        myfile = myfile.decode()
        data = myfile[myfile.index("data.setCell"):myfile.rindex("data.setCell")]
        data = data.split("data.setCell")
        choice = 1
        magnet_list = []
        while choice < len(data)-1:
            words = data[choice][data[choice].index("\"")+1:data[choice].rindex(",")]
            magnet_list.append(words)
            choice +=3                                      
    
        return magnet_list
    # if nothing is found, try again with a different word
    except ValueError:
        choice = random.randint(0,len(RAND_LIST)-1)
        return metaphor_magnet(RAND_LIST[choice])
        
        
def poem_generation(magnet,topic):
    """ Creates the poem line by line by randomly deciding on similarities or
    differences """
    e = inflect.engine()
    antonyms = []
    synonyms = []
    poem = ""
    verb = ""
    # plural
    if (e.singular_noun(topic) is False):
        verb = "is"
    else:
        verb = "are"
        
    for syn in wordnet.synsets(topic):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    if (len(set(antonyms)) < 1):
        for syn in wordnet.synsets(RAND_LIST[random.randint(0,len(RAND_LIST)-1)]):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
    topic = topic.capitalize()
    for i in range(0,random.randint(5,12)):
        verse = random.randint(0,6)
        # antonyms
        if (verse < 2) and len(antonyms) > 0:
            ant_magnet = metaphor_magnet(antonyms[random.randint(0,len(antonyms)-1)])
            choice = random.randint(0,len(ant_magnet)-1)
            detail = ant_magnet[choice].split(":")
            if (detail[0][0] in ['a','e','i','o','u']):
                poem += topic + " " + verb + " not like an " + detail[0] + " " + detail[1] + "\n" 
            else:
                poem += topic + " " + verb + " not like a " + detail[0] + " " + detail[1] + "\n" 
                                         
        else:
            choice = random.randint(0,len(magnet)-1)
            detail = magnet[choice].split(":")
            if (detail[0][0] in ['a','e','i','o','u']):
                poem += topic + " " + verb + " like an " + detail[0] + " " + detail[1] + "\n" 
            else:
                poem += topic + " " + verb + " like a " + detail[0] + " " + detail[1] + "\n"    
            
    return poem
                    
def main():   
    topic = str(input("What do you want the poem to be about?\n"))
    magnet = metaphor_magnet(topic)
    poem = poem_generation(magnet,topic)
    mixer.init()
    mixer.music.load("test1.mp3")
    mixer.music.play()
    mixer.music.set_volume(.2)
    print(poem)
    poem = poem.split("\n")
    for sentence in poem:
        present(sentence)
    mixer.music.fadeout(3000)

if __name__ == "__main__":
    main()
    



    


     





