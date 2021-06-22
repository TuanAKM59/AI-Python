import speech_recognition
from datetime import datetime, date
from gtts import gTTS
import playsound
import os
import random
import webbrowser
from pyowm import OWM
from googletrans import Translator
from youtube_search import YoutubeSearch
import wikipedia

os.system("cls")
ear = speech_recognition.Recognizer()
brain = ""
now = datetime.now()
today = date.today()
music_dir = 'D:\\Down nhạc'
songs = random.choices(os.listdir(music_dir))
translator = Translator()
wikipedia.set_lang("vi")

owm = OWM('f267d4a634cbd7287a4cbd02b6a12397')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('hanoi,VN')
weather = observation.weather
temper = weather.temperature('celsius')['temp']
humidity = weather.humidity
cloud = weather.detailed_status
t2 = int(temper)
t3 = str(t2)
t4 = str(humidity)
translation = (translator.translate(cloud, src='en', dest='vi')).text
t5 = str(translation)

x = datetime.now()
time = int(x.strftime("%H"))
if 3 < time < 10:
    loichao = "Chào buổi sáng!"
elif 10 <= time < 15:
    loichao = "Chào buổi trưa!"
elif 15 <= time <= 17:
    loichao = "Chào buổi chiều!"
elif 17 < time <= 22:
    loichao = "Chào buổi tối!"
else:
    loichao = "Khuya rồi đó đi ngủ thôi!"
print(loichao)
output = gTTS(loichao, lang="vi", slow=False)
output.save("output.mp3")
playsound.playsound('output.mp3')
os.remove('output.mp3')

while True:
    with speech_recognition.Microphone() as mic:
        ear.adjust_for_ambient_noise(mic) 
        print("AI: Tôi đang nghe nè...")
        audio = ear.listen(mic,timeout=4, phrase_time_limit=4)
    try:
        you = ear.recognize_google(audio,language="vi-VI")
    except:
        you = ""
    print("You: " + you)
    if you == "":
        brain = "Xin lỗi bạn nói lại được không?"
    elif "xin chào" in you.lower():
        brain = "Xin chào bạn!"
    elif "giờ" in you.lower():
        time = now.strftime("%H:%M:%S") 
        brain = "Bây giờ đang là: " + time
    elif "ngày" in you.lower():
        date = today.strftime("%d/%m/%Y")
        brain = "Hôm nay là ngày: " + date
    elif "thời tiết" in you.lower():
        brain = "Nhiệt độ hiện tại đang là: " + t3 + "°C, " + t5 + ", Độ ẩm: " + t4 + "%"
    elif "nhạc offline" in you.lower():
        os.startfile(os.path.join(music_dir,songs[0]))
        break
    elif "nhạc online" in you.lower():
        with speech_recognition.Microphone() as mic:
            ear.adjust_for_ambient_noise(mic) 
            print("AI: Bạn muốn nghe bài nào nhỉ?...")
            audio = ear.listen(mic,timeout=4, phrase_time_limit=4)
        try:
            you = ear.recognize_google(audio,language="vi-VI")
            print("You: " + you)
            result = YoutubeSearch(you, max_results=3).to_dict()
            url = 'https://www.youtube.com' + result[0]['url_suffix']
            webbrowser.open(url)
            output = gTTS("ok bài hát đang được mở", lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            break
        except:
            you = ""
        if you == "":
            brain = "Xin lỗi tôi không tìm thấy bài hát!"
    elif "google" in you.lower():
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        output = gTTS("Google đang được mở", lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        break
    elif "wikipedia" in you.lower():
        with speech_recognition.Microphone() as mic:
            ear.adjust_for_ambient_noise(mic) 
            print("AI: Bạn muốn nghe tôi nói về ai nào!...")
            audio = ear.listen(mic,timeout=4, phrase_time_limit=4)
        try:
            wiki = ear.recognize_google(audio,language="vi-VI")
            print("You: ", wiki)
            wiki=wikipedia.summary(wiki)
        except:
            wiki = "Xin lỗi tôi không tìm thấy"
        print(wiki)
        break
    elif "youtube" in you.lower():
        webbrowser.open('https://www.youtube.com', new=1)
        output = gTTS("Youtube đang được mở", lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        break
    elif "facebook" in you.lower():
        webbrowser.open('https://www.facebook.com', new=1)
        output = gTTS("Facebook đang được mở", lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        break
    elif "tắt máy" in you.lower():
        os.system('shutdown -s')
        break
    elif "khởi động lại" in you.lower():
        os.system('shutdowwn -r')
        break
    elif "tạm biệt" in you.lower():
        brain = "Chào tạm biệt và hẹn gặp lại!"
        print("AI:", brain)
        output = gTTS(brain, lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        break
    else:
        brain = "Xin lỗi chủ tôi chưa dạy tôi câu này!"
        
    print("AI:", brain)
    output = gTTS(brain, lang="vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3')
    os.remove('output.mp3')