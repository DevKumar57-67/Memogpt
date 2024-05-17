!pip install reportlab
!pip install pdfminer.six




from pdfminer.high_level import extract_text
text=extract_text('output.pdf')
print(repr(text))
print(text)


# Function to convert text to vector
def text_to_vector(text):
    # Simulated method for converting text to vector
    return np.random.rand(1, 4)  # Replace with your actual method

# Function to get the intent based on input text
def get_intent(input_text):
    input_vector = text_to_vector(input_text)
    best_similarity = -1
    best_intent = None
    for intent, vector in vectors.items():
        similarity = cosine_similarity(input_vector, vector)[0][0]
        if similarity > best_similarity:
            best_similarity = similarity
            best_intent = intent
    return best_intent





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



from sklearn.feature_extraction.text  import TfidfVectorizer
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
        robot_response=robot_response+ "I am sorry.Unable to understand.please use more specific words in your prompt or remove typing error if any!"
        return robot_response
    else:
        robot_response=robot_response+sentence_tokens[idx]
        return robot_response
        
        
        flag = True
print("Hello I am here to make you a bit more creative.Just ask the template text you want for your memes and add this template to your images!")
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


return model
gr.Interface(model,inputs=gr.inputs.Textbox(lines=5,label="Input Text"),
outputs="text").launch()