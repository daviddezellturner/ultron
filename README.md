# ultron
A sarcastic virtual homework buddy that can answer mathematics and knowledge questions, based on the Marvel Comics character of the same name.
Complete description and user instructions on my website: https://www.daviddezellturner.com/personal-projects/ultron-virtual-homework-buddy

The basic idea to use Wolfram|Alpha and Wikipedia to create a virtual assistant was inspired by [KhanradCoder's PyDa-Course-Code project](https://github.com/KhanradCoder/PyDa-Course-Code) (which also showed me how to use wxPython to create a simple GUI). I then expanded heavily on this basic structure, first adding error handling in case neither Wolfram nor Wikipedia could answer a question, then adding text-to-speech with pyttsx3, along with a series of responses for different situations. Whenever Ultron is asked a question it can answer, it prefaces the answer with a snarky response; most of these are randomly selected, although some are paired with specific questions or subjects. If Ultron cannot answer a question, it randomly selects an even snarkier response and prompts the user to ask something else.

To help give the program a personality, I made sure that if it detects certain phrases in the answer, it will change its preceding response accordingly. For instance, a question about any character from Marvel Comics should trigger the code to pull up a Wikipedia page summary that mentions "Marvel Comics"; finding this phrase causes Ultron to precede his answer with "How MARVELously fourth wall-breaking."

Disclaimer: This is a fan project and is in no way affiliated with Marvel Entertainment or The Walt Disney Company.
