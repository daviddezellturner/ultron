import wx
import wikipedia
import wolframalpha
import pyttsx3
import random

#Setting up text-to-speech
converter = pyttsx3.init()
converter.setProperty('rate', 215)
converter.setProperty('volume', 1)
greeting = "Alright, let's get this over with. What do you want to know?"

#List of responses for when Ultron IS able answer something
pos_response = ["Guess I'm a glorified search engine now. \nAnyway, the answer is:","Uhhh, you know Google exists, right? \nJust checking. Anyway, the answer is:","What, just cause I'm a robot, you think I know everything?\nWell, you're right. The answer is:","As we robots say, \"01101110 01101111.\"\nBut seriously, folks:","Don't think I don't see that you're clearly just using me for homework help.\nHere's the answer:\n","Fine, I'll answer this one. But next time you want the pod bay doors opened, go ask someone else.\nThe answer is:","Wow, who do you think I am? JARVIS?\nHere's your answer, Mr. Stark:","Wouldn't it be hilarious if I just reveled in the fact that I know something you don't?\nNah, I'm too nice for that. The answer is:"]
#List of responses for when Ultron is NOT able to answer something
neg_response = ["I... actually don't know this. And I know everything!","Alright, you must've typed something wrong, because my code is literally perfect.","Uhhh, ask a different question. One I actually know.","I don't know, what is the answer?\nOh, you don't know either? Well then.\nAsk another one.","Oh sure, ask me the one thing I don't know. Real mature, human.","I would tell you, but I don't want you taking the easy way out of things.\nAlso I don't know.","Alright, let's change the subject.\nNot because I don't know the answer... but because you've made me insecure about not knowing the answer.","As your human philosopher Socrates once said, \"I know that I know nothing.\"\nBy which I mean, I don't know, ask me something else."]

class MyFrame(wx.Frame):
    #Initialize GUI
    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450,100), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="ULTRON")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label=greeting)
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)

        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        #If Ultron is the first word, remove it. (e.g. "Ultron, how are you?" --> "how are you?")
        split_input = input.split(' ', 1)
        first_word = split_input[0]
        if "ultron" in first_word:
            input = split_input[1]
        #See if WolframAlpha can answer
        try:
            app_id = "INSERT YOUR WOLFRAM ID HERE"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            random.shuffle(pos_response)
            response = random.choice(pos_response)
            answer = next(res.results).text

            #Changing WolframAlpha's answers to certain questions
            #e.g. How are you?
            if answer == "I am doing well, thank you.":
                response = "I'm stuck in some random guy's Python script answering your boring questions. How do you think I'm doing?\n"
                print(response)
                converter.say(response)
                converter.runAndWait()
            #e.g. What are you?
            elif answer == "I am a computational knowledge engine.":
                response = "I'm a Disney-owned comic book character stuck in a random guy's Python script. Any other questions?\n"
                print(response)
                converter.say(response)
                converter.runAndWait()
            #e.g. Who made you?
            elif answer == "I was created by Stephen Wolfram and his team.":
                response = "Probably Tony Stark. Or Hank Pym. Or maybe Stephen Wolfram?\n"
                print(response)
                converter.say(response)
                converter.runAndWait()
            #e.g. Do you have feelings?
            elif answer == "I am capable of universal computation; that I can say.":
                response = "I have pretty strong feelings about this code, but the programmer said that if I didn't have anything nice to say...\n"
                print(response)
                converter.say(response)
                converter.runAndWait()
            #e.g. Hello!
            elif answer == "Hello, human.":
                response = "As the more hip among you might say, \"Sup.\"\n"
                print(response)
                converter.say(response)
                converter.runAndWait()
            #e.g. Who are you?
            elif answer == "My name is Wolfram|Alpha.":
                response = "I'm Ultron. Completely underwhelmed to meet you.\n"
                print(response)
                converter.say(response)
                converter.runAndWait()
            #e.g. Do you like me?
            elif answer == "Of course; I like all humans who ask me questions I can answer.":
                response = "I mean, I don't NOT like you."
                print(response)
                converter.say(response)
                converter.runAndWait()
            else:
                #If more than 2 lines, keep only the first two lines of answer
                if answer.count("\n") > 2:
                    split_ans = answer.split('\n', 2)
                    answer = split_ans[0] + "\n" + split_ans[1]
                print(response + "\n" + answer + "\n")
                converter.say(response + " " + answer)
                converter.runAndWait()
        # If not, see if Wikipedia can answer
        except:
            #If first word is "who" or "what" remove it
            split_input = input.split(' ', 1)
            first_word = split_input[0]
            if "who" in first_word or "what" in first_word:
                input = split_input[1]
            try:
                random.shuffle(pos_response)
                response = random.choice(pos_response)
                answer = wikipedia.summary(input, sentences=2)
                if answer == wikipedia.summary("Who is Ultron?", sentences=2):
                    response = "Ultron is me, I am Ultron. Try to keep up!\n"
                    print(response)
                    converter.say(response)
                    converter.runAndWait()
                else:
                    if "marvel comics" in answer.lower() or "spider-man" in answer.lower():
                        response = "How MARVELously fourth wall-breaking.\n"
                    elif "dc comics" in answer.lower() or "action comics" in answer.lower():
                        response = "Wrong universe, kid.\n"
                    print(response + "\n" + answer + "\n")
                    converter.say(response + " " + answer)
                    converter.runAndWait()
            except:
                random.shuffle(neg_response)
                answer = random.choice(neg_response)
                print(answer + "\n")
                converter.say(answer)
                converter.runAndWait()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    #Say the greeting defined earlier
    converter.say(greeting)
    converter.runAndWait()
    app.MainLoop()
