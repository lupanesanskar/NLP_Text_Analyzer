from tkinter import *
from my_db import Database
from tkinter import messagebox
from gliner import GLiNER
from huggingface_hub import login
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect, detect_langs


class NLPApp:
    def __init__(self):

        self.dbo=Database()
        self.root = Tk()  # generate gui
        self.root.title("NLP Text Analyzer")
        self.root.iconbitmap('images/favicon.ico')
        self.root.geometry("350x600")
        self.root.geometry('500x700')
        self.root.configure(bg='#1E293B')
        self.login()
        self.root.mainloop()  # holding gui on screen\


    def login(self):

        self.clear()

        heading = Label(self.root,text="NLP Text Analyzer")
        heading.pack(pady=(50,50))
        heading.configure(font=("Inter",24,'bold'),bg='#1E293B',fg='#F7E5D4')

        heading1=Label(self.root,text="Enter Email:",bg='#1E293B',fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40,10))

        self.email_input=Entry(self.root,width=60,bg='#1E293B',fg='white',insertbackground="white")
        self.email_input.pack(pady=(3,10),ipady=3)

        heading1=Label(self.root,text="Enter Password:",bg='#1E293B',fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40,10))

        self.password_input=Entry(self.root,width=60,bg='#1E293B',fg='white',insertbackground="white",show="*")
        self.password_input.pack(pady=(3,10),ipady=3)

        login_btn=Button(self.root,text="Login",width=20,height=1,bg='#1E3A8A',fg='#F8FAFC',command=self.perform_login)
        login_btn.pack(pady=(30,10))

        heading2=Label(self.root,text="Not a Member ?",bg='#1E293B',fg='#F8FAFC')
        heading2.configure(font=("Inter", 12))
        heading2.pack(pady=(40,10))

        register_btn=Button(self.root,text="Register",width=20,height=1,bg='#1E3A8A',fg='#F8FAFC',command=self.register)
        register_btn.pack(pady=(5,5))

    def register(self):
        self.clear()
        heading = Label(self.root, text="NLP Text Analyzer")
        heading.pack(pady=(50, 50))
        heading.configure(font=("Inter", 24, 'bold'), bg='#1E293B', fg='#F7E5D4')

        heading0 = Label(self.root, text="Enter Name:", bg='#1E293B', fg='#F8FAFC')
        heading0.configure(font=("Inter", 12))
        heading0.pack(pady=(40, 10))

        self.name_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white")
        self.name_input.pack(pady=(3, 10), ipady=3)

        heading1 = Label(self.root, text="Enter Email:", bg='#1E293B', fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40, 10))

        self.email_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white")
        self.email_input.pack(pady=(3, 10), ipady=3)

        heading1 = Label(self.root, text="Enter Password:", bg='#1E293B', fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40, 10))

        self.password_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white", show="*")
        self.password_input.pack(pady=(3, 10), ipady=3)

        register_btn = Button(self.root, text="Register", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.perform_registration)
        register_btn.pack(pady=(30, 10))

        heading2=Label(self.root,text="Already a Member ?",bg='#1E293B',fg='#F8FAFC')
        heading2.configure(font=("Inter", 12))
        heading2.pack(pady=(20,5))

        login_btn=Button(self.root,text="Login",width=20,height=1,bg='#1E3A8A',fg='#F8FAFC',command=self.login)
        login_btn.pack(pady=(10,10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        responce = self.dbo.add_data(name,email,password)
        if responce:
            messagebox.showinfo("Success!!", "Registration Successful")
            self.login()
        else:
            messagebox.showerror("Error!!", "Registration Failed")

    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        responce=self.dbo.search(email,password)
        if responce:
            messagebox.showinfo("Success!!", "Login Successful")
            self.home()
        else:
            messagebox.showerror("Error!!", "Incorrect Email/Password")

    def home(self):
        self.clear()

        heading = Label(self.root,text="NLP Text Analyzer")
        heading.pack(pady=(50,50))
        heading.configure(font=("Inter",24,'bold'),bg='#1E293B',fg='#F7E5D4')

        ner_btn = Button(self.root, text="Name Entity Recognition", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.perform_ner)
        ner_btn.configure(font=("Inter", 16))
        ner_btn.pack(pady=(30, 25))

        sentiment_btn = Button(self.root, text="Semantic Analysis", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.perform_semantic)
        sentiment_btn.configure(font=("Inter", 16))
        sentiment_btn.pack(pady=(30, 25))

        language_btn = Button(self.root, text="Language Detection", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.perform_language)
        language_btn.configure(font=("Inter", 16))
        language_btn.pack(pady=(30, 25))

        logout_btn = Button(self.root, text="Logout", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.login)
        logout_btn.pack(pady=(30, 10))

    def perform_ner(self):
        self.clear()
        heading = Label(self.root,text="NLP Text Analyzer")
        heading.pack(pady=(50,50))
        heading.configure(font=("Inter",24,'bold'),bg='#1E293B',fg='#F7E5D4')

        heading0 = Label(self.root,text="Name Entity Recognition")
        heading0.pack(pady=(30,30))
        heading0.configure(font=("Inter",18),bg='#1E293B',fg='#F7E5D4')

        heading1 = Label(self.root, text="Enter the text:", bg='#1E293B', fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40, 10))

        self.text_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white")
        self.text_input.pack(pady=(3, 10), ipady=3)

        heading2 = Label(self.root, text="What would you like to search:", bg='#1E293B', fg='#F8FAFC')
        heading2.configure(font=("Inter", 12))
        heading2.pack(pady=(40, 10))

        self.entity_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white")
        self.entity_input.pack(pady=(3, 10), ipady=3)

        self.ner_result=Label(self.root,text='',bg='#1E3A8A',fg='white')
        self.ner_result.configure(font=("Inter",16))
        self.ner_result.pack(pady=(10, 10))

        analyse_btn = Button(self.root, text="Result", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.result_ner)
        analyse_btn.pack(pady=(30, 10))

        goback_btn = Button(self.root, text="Go Back", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.home)
        goback_btn.pack(pady=(30, 10))


    def perform_semantic(self):
        self.clear()
        heading = Label(self.root,text="NLP Text Analyzer")
        heading.pack(pady=(50,50))
        heading.configure(font=("Inter",24,'bold'),bg='#1E293B',fg='#F7E5D4')

        heading0 = Label(self.root,text="Semantic Analysis")
        heading0.pack(pady=(30,30))
        heading0.configure(font=("Inter",18),bg='#1E293B',fg='#F7E5D4')

        heading1 = Label(self.root, text="Enter the text:", bg='#1E293B', fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40, 10))

        self.text_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white")
        self.text_input.pack(pady=(3, 10), ipady=3)

        self.sa_result=Label(self.root,text='',bg='#1E3A8A',fg='white')
        self.sa_result.configure(font=("Inter",16))
        self.sa_result.pack(pady=(10, 10))

        analyse_btn = Button(self.root, text="Result", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.result_semantic)
        analyse_btn.pack(pady=(30, 10))

        goback_btn = Button(self.root, text="Go Back", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.home)
        goback_btn.pack(pady=(30, 10))

    def perform_language(self):
        self.clear()
        heading = Label(self.root,text="NLP Text Analyzer")
        heading.pack(pady=(50,50))
        heading.configure(font=("Inter",24,'bold'),bg='#1E293B',fg='#F7E5D4')

        heading0 = Label(self.root,text="Language Detection")
        heading0.pack(pady=(30,30))
        heading0.configure(font=("Inter",18),bg='#1E293B',fg='#F7E5D4')

        heading1 = Label(self.root, text="Enter the text:", bg='#1E293B', fg='#F8FAFC')
        heading1.configure(font=("Inter", 12))
        heading1.pack(pady=(40, 10))

        self.text_input = Entry(self.root, width=60, bg='#1E293B', fg='white', insertbackground="white")
        self.text_input.pack(pady=(3, 10), ipady=3)

        self.ld_result=Label(self.root,text='',bg='#1E3A8A',fg='white')
        self.ld_result.configure(font=("Inter",16))
        self.ld_result.pack(pady=(10, 10))

        analyse_btn = Button(self.root, text="Result", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.result_language)
        analyse_btn.pack(pady=(30, 10))


        goback_btn = Button(self.root, text="Go Back", width=20, height=1, bg='#1E3A8A', fg='#F8FAFC',command=self.home)
        goback_btn.pack(pady=(30, 10))

    def result_ner(self):

        login()
        text=self.text_input.get()
        search=self.entity_input.get()
        model = GLiNER.from_pretrained("urchade/gliner_base")
        entities = model.predict_entities(text, [search])
        result=[]
        if entities:
            for entity in entities:
                print(entity["text"])
                result.append(entity["text"])
            self.ner_result['text']=",".join(result)
        else:
            self.ner_result['text']="That type of Entity is not present in sentence."

    def result_semantic(self):
        text=self.text_input.get()

        analyzer = SentimentIntensityAnalyzer()

        scores = analyzer.polarity_scores(text)

        # Compound ranges from -1 (very negative) to +1 (very positive)
        if scores['compound'] >= 0.05:
            sentiment = "Positive"
        elif scores['compound'] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        self.sa_result["text"]="Sentiment:{}".format(sentiment)

    def result_language(self):
        text=self.text_input.get()
        LANG_NAMES = {
            "en": "English", "fr": "French", "es": "Spanish", "de": "German",
            "it": "Italian", "pt": "Portuguese", "nl": "Dutch", "ru": "Russian",
            "zh": "Chinese", "ja": "Japanese", "ko": "Korean", "hi": "Hindi"
        }
        decode=detect(text)
        if decode in LANG_NAMES:
            self.ld_result['text']=LANG_NAMES[decode]
        else:
            self.ld_result['text']="Failed to Identify."
nlp=NLPApp()