from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class NLPModelInterface(App):
    
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Text input field for user query
        self.query_input = TextInput(hint_text='Enter your text here')
        layout.add_widget(self.query_input)
        
        # Button to trigger model prediction
        predict_button = Button(text='Predict', on_press=self.predict)
        layout.add_widget(predict_button)
        
        # Label to display prediction result
        self.prediction_label = Label(text='')
        layout.add_widget(self.prediction_label)
        
        return layout
    
    def predict(self, instance):
        user_query = self.query_input.text
        # Call your NLP model to predict based on the user query
        # Replace this with your actual NLP model prediction code
        !pip install reportlab
        !pip install pdfminer.six
        
        from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(text, output_file):
    # Create a canvas with letter size
    c = canvas.Canvas(output_file, pagesize=letter)

    # Set up the font and size
    c.setFont("Helvetica", 12)

    # Split text into lines and write to the canvas
    lines = text.split('\n')
    y = 750  # Starting y position
    for line in lines:
        c.drawString(50, y, line)
        y -= 15  # Adjust vertical position for the next line

    # Save the canvas as a PDF file
    c.save()

# Example usage:
raw_text = """


Chennai Super Kings (CSK) is an Indian professional cricket franchise based in Chennai, Tamil Nadu. The team competes in the Indian Premier League (IPL) and was one of the eight franchises incorporated when the league was established in 2008. The team plays its home matches at the M. A. Chidambaram Stadium in Chennai and is owned by Chennai Super Kings Cricket Limited.Super Kings is the most successful IPL franchise having won a record five IPL titles (shared with Mumbai Indians). In the IPL, they have appeared in a record 10 finals and qualified for the playoff stages 12 times out of the 14 seasons they have played, more than any other team. Super Kings have also won the Champions League Twenty20 in 2010 and 2014. The team is currently captained by Ruturaj Gaikwad and coached by Stephen Fleming.
The team was suspended for two years from the IPL starting July 2015 due to the involvement of its owners in the 2013 IPL betting case. Super Kings re-joined IPL for the 2018 season and won the title in its comeback season. The team has a significant fan following. In January 2022, CSK became India's first unicorn sports enterprise. As of 2022, it was the second most valuable IPL franchise with a valuation of $1.15 billion
BeacheseditMarina Beach is a 13-km-long urban beach along the Bay of Bengal that runs from Fort St. George in the north up to Foreshore Estate in the south. It is India's longest beach and one of the world's longest beaches and attracts around 50,000 visitors during weekends. Attractions at the Marina include the Chennai Lighthouse, MGR Memorial, Anna Memorial and Jayalalitha Memorial. The Marina's 6 km promenade includes statues of several historical figures including Mahatma Gandhi, Annie Besant, Robert Caldwell, Thiruvalluvar, Bharathiyar and Kamrajar.

Elliot's Beach, also known as Besant Nagar beach begins where the Marina ends. The beach is famous for its calm atmosphere and is preferable among morning walkers. The iconic Karl Schmidt memorial, named after the Dutch sailor who lost his life in the process of saving others from drowning is located at the heart of Elliot's beach.Blue Flag BeachMuseumseditGovernment Museum, Egmore Established in 1851, the museum consisting of six buildings and 46 galleries covers an area of around 16.25 acres (66,000 m2) of land. The objects displayed in the museum cover a variety of artifacts and objects covering diverse fields including archeology, numismatics, zoology, natural history, sculptures, palm-leaf manuscripts and Amravati paintings. The Government Museum Complex in Egmore also houses the Connemara Public Library and the National Art Gallery. Connemara Public Library is one of the four National Depository libraries which receive a copy of all books, newspapers and periodicals published in India. The National Art Gallery building is one of the finest Indo-sarcenic type of architectures in the country.
Chennai Rail Museum a railway museum in Perambur which has a rich rail heritage of India with the host of both technical and heritage exhibits with a sizable collection of steam engines belonging to various decades of the British Raj. The museum was opened on 16 April 2002 and located on 6.25 acres on the premises Integral Coach Factory near Villivakkam. Most of the older models were manufactured by the North British Locomotive Company[1] and some of the collection dates back more than one hundred years as it covers the railway history of South India.[2] A toy train offers rides around the premises on regular days. Museum remains open from 10.00 am to 6.00 pm (Last entry 5.30 pm) Tuesday to Sunday and remains closed on every Monday and National Holidays. The Indoor Art Gallery is now fully renovated and opened to the public.Birla Planetarium, a modern planetarium that provides a virtual tour of the night sky and holding cosmic shows on a specially perforated hemispherical aluminium inner dome. It is located inside the Periyar Science and Technology Centre campus at Kotturpuram which has 8 galleries showcasing over 500 exhibits. The planetarium conducts sky shows including Solar System, eclipses, Earth, Man on Moon, comets, shooting meteoroids, stellar cycle and the deep sky every day at different times in both English and Tamil. The planetarium's 360-degree sky theatre is the first of its kind in India. The planetarium organises a special show on every second Saturday of the month to view the night sky from 7:00 pm to 9:00 pm.Historical MonumentseditVivekanandar Illam or Vivekananda house is remembered as the place where Swami Vivekananda stayed for nine days when he visited Chennai (then Madras) in 1897. Vivekananda House now houses a permanent exhibition on Indian Culture. Located on the busy Kamrajar Salai along the Marina Beach, it has become an important spiritual tourist attraction in the city.
Valluvar Kottam is a popular monument in Chennai, dedicated to the classical Tamil poet, philosopher, and saint, Thiruvalluvar who wrote his famous Thirukkural some 2,000 years ago. All 133 chapters and 1330 verses of the Thirukkural are inscribed on bas-relief in the front hall's corridors. A life-size statue of Thiruvalluvar has been installed in the 39 m high chariot.
Historic Government BuildingseditFort St. George is the name of the first British fortress in India, founded in 1639[15] at the coastal city of Madras. The fort is a stronghold with 6-meter-high (20 ft) walls that withstood a number of assaults in the 18th century. It is a feasible contention to say that the city evolved around the fortress. The fort currently houses the Tamil Nadu legislative assembly and other official buildings. The Fort Museum contains many relics of the Raj, including portraits of many of the Governors. Other monuments present inside the fort are St. Mary's Church, the oldest Anglican church in India, and Wellesley House, which holds the paintings of the Governor of the Fort and other high officials of the Regime.Ripon Building, commissioned in 1913 and named after Lord Ripon, Governor General of India and father of local self-government. It is the headquarters of the city's municipal body Greater Chennai Corporation, the world's 2nd oldest municipal corporation after the City of London Corporation. The building is a fine example of the Neoclassical style of architecture, a combination of, Ionic and Corinthian. The Ripon Building is an all-white structure and is located near the iconic Chennai Central railway station.Victoria Public Hall, or the Town Hall, is a historical building located in between the Ripon Building and the Chennai Central Railway Station and is seen as one of the finest examples of British architecture in Chennai. Built in 1888 as a town hall for the city of Madras and named after Queen Victoria to commemorate the golden jubilee.
considered as the largest mosque in the city of Chennai.ShoppingeditSpencer Plaza is one of the oldest and largest shopping malls in Chennai.
Chennai has some unique places to offer for shopping. Art and crafts, contemporary and traditional artwork, antiques, jewellery are available in the city. Traditional items like the leaf and palmyra-fiber handicrafts from Tirunelveli, bronze and brass castings and traditional jewellery from Kumbakonam, metal works from Thanjavur, stone carvings from Mahabalipuram, silks from Kanchipuram are for sale in shops and boutiques.
T. Nagar, the neighbourhood is the shopping hub of the city. Two main areas are Pondy Bazaar and Ranganathan Street which are home to several multi-storey stores, unique to Chennai, which deals mainly in textiles and silks or gold, silver and diamond jewellery.George Town and Parrys Corner are wholesale markets of the city where one can purchase almost anything.Mint Street plays host to communities from Rajasthan and Gujarat and is where north Indian snacks can be sampled along with textiles, kitchenware, and jewellery.Burma Bazaar is famous for its counterfeit electronic goods and media.Moore Market in Central is known for its large number of bookstores.The city also has a number of shopping malls spread across the landscape including the oldest Spencer Plaza and several other modern malls that include Express Avenue, Phoenix Market City, Forum Vijaya Mall, Ampa Skywalk, Abirami Mega Mall, Mayajaal, Spectrum Mall.Entertainmentedit
There are four large amusement parks, MGM Dizzee World, VGP Universal Kingdom, Queen's Land near Poonnamalle and Kishkinta Located near Mudichur in Chennai. The city also houses a paintball centre and water sports club on the east coast road. There are also a large number of beach resorts all along the East Coast Road highway to Mahabalipuram. The city is home to the Tamil movie industry, has over 100+ large cinema theatres including a few multiplexes which screen Tamil, English, Hindi, Telugu, Kannada and Malayalam films.[18] The city has a large number of restaurants offering a variety of Tamil, Indian and international cuisines.[19] The nightlife in Chennai is vibrant and growing ranging from bars to pool parlours to lounges and clubs.[20]


"""

output_file = "output.pdf"
text_to_pdf(raw_text, output_file)

from pdfminer.high_level import extract_text
text=extract_text('output.pdf')
print(repr(text))
print(text)

import nltk
import numpy as np
import random
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
sentence_tokens=nltk.sent_tokenize(raw_text)
word_tokens=nltk.word_tokenize(raw_text)
lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
    
greet_inputs=('hello','hi','whassup','namaste','kemchoo','how are you')
greet_responses=('hi','hey there',' i am fine', 'good','me too')
def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)
            
sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robot_response= ' '
    TfidVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
    tfidf=TfidVec.fit_transform(sentence_tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()
    flat.sort()
    req_tfidf=flat[-2]
    if(req_tfidf==0):
        robot_response=robot_response+ "I am sorry.Unable to understand!"
        return robot_response
    else:
        robot_response=robot_response+sentence_tokens[idx]
        return robot_response
        
        flag = True
print("Hello I am retreivel learning chatbot please type your text after greeting to me for ending convo type bye!")
while(flag==True):
    user_response=input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thank you' or user_response=='thanks'):
            flag=False
            print('Bot: You are welcome!')
        else:
            if(greet(user_response) !=None):
               print('Bot:' + greet(user_response))
            else:
               sentence_tokens.append(user_response)
               word_tokens=word_tokens+nltk.word_tokenize(user_response)
               final_words=list(set(word_tokens))
               print('Bot:',end='')
               print(response(user_response))
               sentence_tokens.remove(user_response)
    else:
               flag = False
               print('Bot: Goodbye!')


    
    def predict_with_nlp_model(self, user_query):
        # Example: Echo the user query
        return user_query

if __name__ == "__main__":
    NLPModelInterface().run()
