# Slam-Poet
Slam Poet is a program that generates poetry based on a given topic by the user. The programs then makes a web service call to Metaphor Magnet and uses the result to generate poems with a bit of random structure. The poems are then evaluated through nltk similaity function to see how much the "describing words of the topic" are related to each other. The highest-scored poem is then presented "dynamically"
# Setup
The code was developed for Windows specification, so please run on a Windows machine if any problems rise on a Mac machine.
Download all the libraries that are imported + the mp3 file.
If running the program for the first time, uncomment "#nltk.download('wordnet')"
Run the program and follow the prompt!
# Challange
The challenging aspect of this project was to figure out what approach to use to generate and evaluate a poem. I initially wanted to go through famous poems and create new poems based on their diction, style, and structure. However, after a while, I decided against it because it proved to be difficult to understand style and structure of poem, and what I had was more pastiche than creative. This realization was pretty late on, so I had to pull an all-nighter to get to where the program is now :)))!
# Inspiration
I looked at the following for "Inspiration" (did not really get close to any haha):
1. https://blog.upperlinecode.com/making-a-markov-chain-poem-generator-in-python-4903d0586957
2. http://ccg.doc.gold.ac.uk/wp-content/uploads/2016/09/colton_iccc12.pdf
3. https://www.learntechlib.org/p/151840/
4. https://era.ed.ac.uk/handle/1842/3460
