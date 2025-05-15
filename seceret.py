import streamlit as st
from PIL import Image

# -- Configuration --
st.set_page_config(
    page_title="Happy Birthday!", 
    page_icon="🎉",
    layout="centered",
)

# -- Session State --
if 'step' not in st.session_state:
    st.session_state.step = 0

# -- Asset Paths (customize!) --
WIFE_IMAGE = 'assets/photo.jpg'
GIFT1_IMAGE = 'assets/Screenshot (7).png'
GIFT2_VIDEO = 'assets/video.mp4'
GIFT3_IMAGE = 'assets/Screenshot (303).png'
GIFT3_AUDIO = 'assets/audio.mp3'
YEAR_MEET = '2023'  # Year you first met

# -- Helpers --
def next_step():
    st.session_state.step += 1

# -- App Flow --
st.title("")

if st.session_state.step == 0:
    st.button('Click here', on_click=next_step)

elif st.session_state.step == 1:
    st.write('Oh, you are here...')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 2:
    st.write('I am still preparing for your birthday baka ')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 3:
    st.write('But since you are here, it must be time hmm')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 4:
    st.write('I see, so it’s time...')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 5:
    st.write('Let’s see what I got...')
    st.button('Reveal', on_click=next_step)

elif st.session_state.step == 6:
    st.balloons()
    st.header('Happy Birthday!')
    st.write('Happy Birthday shweeeeeeeeeeee shimt its your bithday huh shimmmmmt it like i just celebrated your birthday and its now here again shimt its like bro time flew like insane fast speed but shimt , if i now look back to the days shimt yes its been a year and one of the best years with you ofc the hill and hell we gone through is somthing that only we will know  but even after everything we still here and we still stand strong and proud and its not like its because of me its because of you baka , yes you i cant explain in words that how lucky i am to have you like bro you might underestimate yourself but i dont really , for me you are the most adorable , most beautiful person i have. You may not realise but you do things that no one can and because of this i cant contain myself to say that how awesome you are for me and because of you being you i just cant help myself to say I love you as you are and i love everything about you and i love everything you do for me and if i am saying it , i mean it. okok now lets proceed baka i have things for you  I know you will love it but i want you to know that this is not a gift but a promise that i will always be there for you.(See below your photo)')
    try:
        img = Image.open(WIFE_IMAGE)
        st.image(img, use_container_width=True)
    except FileNotFoundError:
        st.warning(f'Please add your wife\'s photo named "{WIFE_IMAGE}"')
    st.button('Oh, wanna more?', on_click=next_step)

elif st.session_state.step == 7:
    st.write('Bro, I don\'t have anything...')
    st.button('Please?', on_click=next_step)

elif st.session_state.step == 8:
    st.subheader('Puzzle 1')
    st.write('I have keys but no locks. I have space but no room. You can enter but can\'t go outside. What am I?(Hint: You pressing it)')
    ans1 = st.text_input('Your answer:', key='p1')
    if ans1.strip().lower() == 'keyboard':
        st.success('Correct! 🎉')
        st.button('Reveal Gift 1', on_click=next_step)

elif st.session_state.step == 9:
    st.header('"How much ever old I get,I will still have a heart of 8yrs"')
    st.write('Do you remember who said that? , yes it was you on your last birthday you said that and ofc i will remember it haha last year on your birthday you was talking about things like that and you was sleepy lol and i was listining your sleepy voice and be like shimt how cute someone can be and bro tbh i now think you are more adorable than before haha.Again its that night and only us here , us our peace and me watching you reading this also you remember that last time you didnt knew my birthday so you said to me that i am 19 and my birthday is today, shimt soory i am just remembring things , thanks for all these memories , thanks really , i am so greatfull to have you here with me . As always I assure you , you have me ok NO MATTER WHAT THE SITUATION IS, so dw about anything , we are doing great just have to keep it up and i belive i will be able to keepup hand in hand with you(See below photo)')
    try:
        img = Image.open(GIFT1_IMAGE)
        st.image(img, caption='Your Gift', use_container_width=True)
    except FileNotFoundError:
        st.warning(f'Please add Gift 1 image named "{GIFT1_IMAGE}"')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 10:
    st.subheader('Puzzle 2')
    st.write(f'What year did we first meet? (YYYY)')
    ans2 = st.text_input('Your answer:', key='p2')
    if ans2.strip() == YEAR_MEET:
        st.success('You got it! ❤️')
        st.button('Reveal Gift 2', on_click=next_step)

elif st.session_state.step == 11:
    st.header('Every year ritual')
    st.write('Like every year you have 3 questions to ask from me , take your time and ask the questions any questions you want and Here’s a video below , i hope you like it ')
    try:
        video_bytes = open(GIFT2_VIDEO, 'rb').read()
        st.video(video_bytes)
    except FileNotFoundError:
        st.warning(f'Please add Gift 2 video named "{GIFT2_VIDEO}"')
    st.button('Next gift huh?', on_click=next_step)

elif st.session_state.step == 12:
    st.write('Well, I hope you like it...')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 13:
    st.write('As I said to you, I will do it...')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 14:
    st.write('I did it...')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 15:
    st.write('As I said, I will bring you back...')
    st.button('Next', on_click=next_step)

elif st.session_state.step == 16:
    st.write('I did it...')
    st.button('So no further ado, here it is...', on_click=next_step)

elif st.session_state.step == 17:
    st.header('Welcome back Esheneeeeeee!')
    st.write('Shimt ok i know you must be insane by now and so listen now , yes i got it back , i got your id back . It did took me wear and tear this and that like i will tell you a overview of it so it all started in march when i told you that i will bring you back no matter what it taks after that i got into work , work of nights grinding for you , searching your id then being friends with the person who took your id so for almost month the person didnt loggined but then one day he did login , i gave him friend request he did accepted it and i ofc cursed him in start because i thought he was the hacker or the one who took your id but after talking i realised that he is not the person wo took your id he just buyed from someone and ok i said that what happend like this id got hacked and all and he said i see and then he said he gave money for this id and will not give it back which was the valid point so i asked how much he paid, he said 249$ , and i be like oh i see . I didnt have that much money to pay at that time to him so i made a trade. I said i will give you my id in exchange for Eshene and when i will get the money i will pay him more then he did and get my id back, after he realised that this id was worth it he accepted the offer.I exchanged the id and it was mixed feeling for me that i got your id back but then again i will not be able to play with you if i didnt got my id back but ok that happend , i got your id in my hand and i was so happy . Now the hard part starts for me , he litrally said i have one month to get my ID back so yeah , had to get somthing and some money , along side with my job i picked up a freelance project of company so dw about it i did it got money and paid him 30% more as i promised but yeah now at this point of time i have our ids with us and now you know why i said i cant play genshin but dw now everything is good , i am happy that i am able get it for you and please dw its ok. I did it because i love you and thats it , Please take it as a gift(Hugs) ')
    try:
        img = Image.open(GIFT3_IMAGE)
        st.image(img, caption='Memorable moment', use_container_width=True)
    except FileNotFoundError:
        st.warning(f'Please add Gift 3 image named "{GIFT3_IMAGE}"')
    try:
        audio_bytes = open(GIFT3_AUDIO, 'rb').read()
        st.audio(audio_bytes, format='audio/mp3')
    except FileNotFoundError:
        st.warning(f'Please add Gift 3 audio named "{GIFT3_AUDIO}"')
    st.snow()
    st.write('Hope you loved it! ❤️')

else:
    st.write('Thank you for celebrating with me! 🎂')
