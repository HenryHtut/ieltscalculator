from tkinter import *
import customtkinter



def clean_frame(frame):
   
    for widget in frame.winfo_children():
        widget.destroy()

def realone():
    clean_frame(mainFrame) 
    customtkinter.CTkLabel(mainFrame,text="Welcome",font=("Arial",20,"bold")).pack(padx=10,pady=10) 
    instruction = customtkinter.CTkLabel(mainFrame,text="For those interested in checking their band scores, there are four main components available in this app.",font=("Georgia",15)).place(relx=0.01,rely=0.1)
    instruction = customtkinter.CTkLabel(mainFrame,text="1. Overall Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.2)
    instruction = customtkinter.CTkLabel(mainFrame,text="2. Reading Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.3)
    instruction = customtkinter.CTkLabel(mainFrame,text="3. Listening Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.4)
    instruction = customtkinter.CTkLabel(mainFrame,text="4. General Reading Band Score",font=("Georgia",15)).place(relx=0.01,rely=0.5)
    instruction = customtkinter.CTkLabel(mainFrame,text="These scores are based on the number of correct answers out of 40 questions in each section. Each score range corresponds to a different band score.",font=("Georgia",15)).place(relx=0.01,rely=0.6)


def Listening():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame, text="Listening Band Score Calculation",font=("Arial",18,"bold")).place(relx=0.41,rely=0.02)
    customtkinter.CTkButton(mainFrame,text="Back to main section",hover_color="blue",command=realone).place(relx=0.65,rely=0.25)

    
    Lresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold")) 
    Lresult_label.place(relx=0.43,rely=0.3) 


    def Listening_submit():
        answerL = listening_entry.get() 
     
        
        band_scores = {
            "9": ["40", "39"],
            "8.5": ["38", "37"],
            "8": ["36", "35"],
            "7.5": ["34", "33", "32"],
            "7": ["31", "30"],
            "6.5": ["29", "28", "27", "26"],
            "6": ["25", "24", "23"],
            "5.5": ["22", "21", "20", "19", "18"],
            "5": ["17", "16"],
            "4.5": ["15", "14", "13"],
            "4": ["12", "11", "10"],
            "3.5": ["9", "8"],
            "3": ["7", "6"],
            "2.5": ["5", "4"],
            "2": ["3", "2"],
            "1.5": ["1"],
            "0": ["0"]
        }

        for band, score in band_scores.items():
            if answerL in score:
                Lresult_label.configure(text=f"Your band score is {band}")
            else:
               Lresult_label.configure("Please enter a valid input.")

    def reset():
       listening_entry.delete(0,"end")
      
       Lresult_label.configure(text="")

    
    listening_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Enter number of correct answers!",width=200,height=30)
    listening_entry.place(relx=0.422,rely=0.15)

  
    listening_submit_button = customtkinter.CTkButton(mainFrame,text="Submit",hover_color="blue",command=Listening_submit)
    listening_submit_button.place(relx=0.45,rely=0.25)

    reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
    reset_button.place(relx=0.25,rely=0.25)

def reading():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame, text="Reading Band Score Calculation",font=("Arial",18,"bold")).place(relx=0.4,rely=0.02)
    customtkinter.CTkButton(mainFrame,text="Back to main section",hover_color="blue",command=realone).place(relx=0.65,rely=0.25)
    
    Rresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
    Rresult_label.place(relx=0.43,rely=0.3)

    def reading_submit():
        answerR = reading_entry.get()

        
        band_scores = {
            "9": ["40", "39"],
            "8.5": ["38", "37"],
            "8": ["36", "35"],
            "7.5": ["34", "33"],
            "7": ["32","31", "30"],
            "6.5": ["29", "28", "27"],
            "6": ["26","25", "24", "23"],
            "5.5": ["22", "21", "20", "19"],
            "5": ["18","17", "16","15"],
            "4.5": [ "14", "13"],
            "4": ["12", "11", "10"],
            "3.5": ["9", "8"],
            "3": ["7", "6"],
            "2.5": ["5", "4"],
            "2": ["3", "2"],
            "1.5": ["1"],
            "0": ["0"]
        }

        for band, score in band_scores.items():
            if answerR in score:
                Rresult_label.configure(text=f"Your band score is {band}")
            else:
               Rresult_label.configure("Please enter a valid input.")
        

    def reset():
       reading_entry.delete(0,"end")
      
       Rresult_label.configure(text="")


    reading_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Enter number of correct answers!",width=200,height=30)
    reading_entry.place(relx=0.422,rely=0.15)

    reading_submit_button = customtkinter.CTkButton(mainFrame,text="Submit",hover_color="blue",command=reading_submit)
    reading_submit_button.place(relx=0.45,rely=0.25)

    reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
    reset_button.place(relx=0.25,rely=0.25)

def general_reading():
    clean_frame(mainFrame)
    customtkinter.CTkLabel(mainFrame, text="General Reading Band Score Calculation",font=("Arial",18,"bold")).place(relx=0.39,rely=0.02)
    customtkinter.CTkButton(mainFrame,text="Back to main section",hover_color="blue",command=realone).place(relx=0.65,rely=0.25)
    
    Rresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
    Rresult_label.place(relx=0.43,rely=0.3)

    def general_reading_submit():
     answerR = general_reading_entry.get()
     

     band_scores = {
            "9": ["40"],
            "8.5": ["39"],
            "8": ["38", "37"],
            "7.5": ["36"],
            "7": ["35", "34"],
            "6.5": ["33","32"],
            "6": ["31","30"],
            "5.5": ["27", "28", "29"],
            "5": ["23", "24","25","26"],
            "4.5": ["19", "20", "21","22"],
            "4": ["15", "16", "17","18"],
            "3.5": ["12", "13","14"],
            "3": ["9", "10","11"],
            "2.5": ["6", "7","8"],
            "0": ["0", "1","2","3","4","5"]
            
        }

     for band, score in band_scores.items():
         if answerR in score:
                Rresult_label.configure(text=f"Your band score is {band}")
         else:
               Rresult_label.configure("Please enter a valid input.")
        

    def reset():
       general_reading_entry.delete(0,"end")
      
       Rresult_label.configure(text="")


    general_reading_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Enter number of correct answers!",width=200,height=30)
    general_reading_entry.place(relx=0.422,rely=0.15)

    general_reading_submit_button = customtkinter.CTkButton(mainFrame,text="Submit",hover_color="blue",command=general_reading_submit)
    general_reading_submit_button.place(relx=0.45,rely=0.25)

    reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
    reset_button.place(relx=0.25,rely=0.25)


  
def OBS():
   clean_frame(mainFrame)
   customtkinter.CTkLabel(mainFrame, text="Hello! This is for your Overall Band Score calculation",font=("Arial",18,"bold")).place(relx=0.32,rely=0.02)
   customtkinter.CTkButton(mainFrame,text="Back to main section",hover_color="blue",command=realone).place(relx=0.65,rely=0.55)
   customtkinter.CTkLabel(mainFrame, text="Listening band score ",fg_color="cyan2",corner_radius=10).place(relx=0.29,rely=0.15)
   customtkinter.CTkLabel(mainFrame, text="Reading band score",fg_color="cyan2",corner_radius=10).place(relx=0.29,rely=0.25)
   customtkinter.CTkLabel(mainFrame, text="Writing band score",fg_color="cyan2",corner_radius=10).place(relx=0.29,rely=0.35)
   customtkinter.CTkLabel(mainFrame, text="Speaking band score",fg_color="cyan2",corner_radius=10).place(relx=0.29,rely=0.45)

   
  
   Oresult_label = customtkinter.CTkLabel(mainFrame,text="",font=("Arial",18,"bold"))
   Oresult_label.place(relx=0.34,rely=0.62)
   
   Orecommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14,"bold"))
   Orecommand_label.place(relx=0.01, rely=0.69)
   O1recommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14))
   O1recommand_label.place(relx=0.01, rely=0.75)
   O2recommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14))
   O2recommand_label.place(relx=0.01, rely=0.79)
   O3recommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14))
   O3recommand_label.place(relx=0.01, rely=0.83)
   O4recommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14))
   O4recommand_label.place(relx=0.01, rely=0.87)
   O5recommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14))
   O5recommand_label.place(relx=0.01, rely=0.91)
   O6recommand_label = customtkinter.CTkLabel(mainFrame, text="", font=("Arial", 14))
   O6recommand_label.place(relx=0.01, rely=0.95)

   def overall_bandscore():

      def calculate(a, b, c, d):

         add = a+b+c+d
         average = add/4

         if average % 1 >= 0.75:
            result = int(average) + 1
            Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
            return result
         elif average % 1 >= 0.5:
            result = int(average)+0.5
            Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
            return result
         elif average % 1 >= 0.25:
            result = int(average)+0.5
            Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
            return result
         elif average > 9:
            result = int(average)
            Oresult_label.configure(text="Score must be between 0 and 9.")
            return result
         else:
            result = int(average)
            Oresult_label.configure(text=f"Congratulation! Your overall band score is {result}!")
            return result

      try:
         L = float(listening_entry.get().strip())
         R = float(reading_entry.get().strip())
         W = float(writing_entry.get().strip())
         S = float(speaking_entry.get().strip())

      except ValueError:
         Oresult_label.configure(text="Please enter valid score!")
      
      result = calculate(L, R, W, S)

      if result >= 0 and result <= 4:
         Orecommand_label.configure(text="Congratulation! You are at an A1 to A2 level.")
         O1recommand_label.configure(text="1. Can understand and use familiar everyday expressions and very basic phrases aimed at the satisfaction of needs of a concrete type.")
         O2recommand_label.configure(text="2. Can introduce herself and others and can ask and answer questions about personal details such as where she lives, people she knows, and things she has")
         O3recommand_label.configure(text="3. Can interact with other people in a simple way provided the other person talks slowly and clearly and is prepared to help.")
         O4recommand_label.configure(text="4. Can understand sentences and frequently used expressions related to areas of most immediate relevance (e.g. very basic personal and family information, shopping, local geography, employment).")
         O5recommand_label.configure(text="5. Can communicate in simple and routine tasks requiring a simple and direct exchange of information on familiar and routine matters.")
         O6recommand_label.configure(text="6. Can describe in simple terms aspects of his/her background, immediate environment and matters in areas of immediate need.")
      elif result >= 4 and result <= 5:
         Orecommand_label.configure(text="Congratulation! You are at B1 level.")
         O1recommand_label.configure(text="1. Can understand the main points of clear standard input on familiar matters regularly encountered in work, school, leisure, etc.")
         O2recommand_label.configure(text="2. Can deal with most situations likely to arise whilst travelling")
         O3recommand_label.configure(text="3. Can produce simple connected text on topics which are familiar or of personal interest.")
         O4recommand_label.configure(text="4. Can describe experiences and events, dreams, hopes and ambitions and briefly give reasons and explanations for opinions and plans.")
      elif result >= 5.5 and result <= 6.5:
         Orecommand_label.configure(text="Congratulation! You are at B2 level.")
         O1recommand_label.configure(text="1. Can understand the main ideas of complex text on both concrete and abstract topics, including technical discussions in his/her field of specialization.")
         O2recommand_label.configure(text="2. Can interact with a degree of fluency and spontaneity that makes regular interaction with native speakers quite possible without strain for either party.")
         O3recommand_label.configure(text="3. Can produce clear, detailed text on a wide range of subjects and explain a viewpoint on a topical issue giving the advantages and disadvantages of various options.")
      elif result >= 7 and result <= 8:
         Orecommand_label.configure(text="Congratulation! You are at C1 level.")
         O1recommand_label.configure(text="1. Can understand a wide range of demanding, longer texts, and recognize implicit meaning.")
         O2recommand_label.configure(text="2. Can express ideas fluently and spontaneously without much obvious searching for expressions.")
         O3recommand_label.configure(text="3. Can use language flexibly and effectively for social, academic and professional purposes.")
         O4recommand_label.configure(text="4. Can produce clear, well-structured, detailed text on complex subjects, showing controlled use of organizational patterns, connectors and cohesive devices.")
      elif result >= 8.5 and result <= 9:
         Orecommand_label.configure(text="Congratulation! You are at C2 level.")
         O1recommand_label.configure(text="1. Can understand with ease virtually everything heard or read.")
         O2recommand_label.configure(text="2. Can summarize information from different spoken and written sources, reconstructing arguments and accounts in a coherent presentation.")
         O3recommand_label.configure(text="3. Can express him/herself spontaneously, very fluently and precisely, differentiating finer shades of meaning even in the most complex situations.")
        
      else:
         Orecommand_label.configure(text="")
         
   def reset():
      listening_entry.delete(0,"end")
      reading_entry.delete(0,"end")
      writing_entry.delete(0,"end")
      speaking_entry.delete(0,"end")
      Oresult_label.configure(text="")
      Orecommand_label.configure(text="")
      O1recommand_label.configure(text="")
      O2recommand_label.configure(text="")
      O3recommand_label.configure(text="")
      O4recommand_label.configure(text="")
      O5recommand_label.configure(text="")
      O6recommand_label.configure(text="")


   listening_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   listening_entry.place(relx=0.422,rely=0.15)

   reading_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   reading_entry.place(relx=0.422,rely=0.25)
  
   writing_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   writing_entry.place(relx=0.422,rely=0.35)
  
   speaking_entry = customtkinter.CTkEntry(mainFrame,placeholder_text="Please enter valid band score!",width=200,height=30)
   speaking_entry.place(relx=0.422,rely=0.45)
   
   overall_band_score_button = customtkinter.CTkButton(mainFrame,text="Calculate",hover_color="blue",command=overall_bandscore)
   overall_band_score_button.place(relx=0.45,rely=0.55)

   reset_button = customtkinter.CTkButton(mainFrame,text="Reset",hover_color="blue",command=reset)
   reset_button.place(relx=0.25,rely=0.55)



customtkinter.set_appearance_mode("deep pink")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("IELTS Calculator")
root.geometry("800x800")


mainFrame = customtkinter.CTkFrame(root,border_color="black",border_width=2)
mainFrame.pack(side="right",fill="both",expand=True)

buttonFrame = customtkinter.CTkFrame(root,border_color="black",border_width=2)
buttonFrame.pack(side="right",fill="y",padx=11)


listeningButton= customtkinter.CTkButton(buttonFrame,text="Listening",border_color="black",border_width=2,command=Listening)
listeningButton.place(relx=0.16,rely=0.5)


readingButton= customtkinter.CTkButton(buttonFrame,text="Reading",border_color="black",border_width=2,command=reading)
readingButton.place(relx=0.16,rely=0.4)

overall_band_score = customtkinter.CTkButton(buttonFrame,text="Overall Band Score",border_color="black",border_width=2,command=OBS)
overall_band_score.place(relx=0.16,rely=0.3)

GeneralreadingButton= customtkinter.CTkButton(buttonFrame,text="General Reading",border_color="black",border_width=2,command=general_reading)
GeneralreadingButton.place(relx=0.16,rely=0.6)


realone()
root.mainloop()