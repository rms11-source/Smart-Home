from msg_buttons import TITLES_FEEL

msg_start = '''Hello!
I am your climate control bot. I can provide information about the clime in your home. I will also sometimes ask how you feel. For more info click the button <b>Help</b>'''
msg_help = '''
IoT Climate Control bot is connected to the device system in your room, which measures different characteristics of the climate in your room: temperature and humidity. The system is designed so that people with <b>respiratory difficulties</b> could have better control of their health. 

This bot has <b>3 main functionalities</b>:
1. To give user the possibility to see last measurements of temperature and humidity in room/house
2. Whenever a new measurement appears, to ask user how they feel, in order to use these data later to find optimal climate conditions for the user
3. To send notifications whenever a value passes its threshold so that user can react properly and prevent possible deterioration of health.

Button <b>Last update</b> will send the last measurements of temperature and humidity and the datetime they were effectuated.

Button <b>Ask me how I feel</b> is a trial one. Ideally, the bot has to ask the user how they feel automatically, when a new update in the database appears. However, until we link the bot to the database, this button will serve the same function.

<i>Note</i>: after choosing a state, to send it to the server you have to click <b>Send data</b> in the next message. In case of the wrong choice, click <b>Discard</b> and in the new message choose the new state.

Button <b>Help</b> can remind you of what this bot can do.

Stay safe!
'''
msg_echo = "Sorry. I don't understand you."
msg_feel = "How do you feel? Haven't you got any difficulties of breath?"
msg_feel_GOOD = "You have chosen {}.\nYou rock bro!".format(TITLES_FEEL['INLINE_BUTTON_GOOD'])
msg_feel_OK = "You have chosen {}.\nGlad you're OK!".format(TITLES_FEEL['INLINE_BUTTON_OK'])
msg_feel_BAD = "You have chosen {}.\nOh, I'm sorry 😥\nGo have some tea".format(TITLES_FEEL['INLINE_BUTTON_BAD'])
msg_feel_SEND = "Sending your reply to the server..."
msg_feel_DISCARD = "OK, tell me one more time how you feel"
msg_temp_threshold_high = "The temperature is higher than 30 degrees! You should cool the air now!"
msg_hum_threshold_high = "The air is too wet! Turn on the ventilation, open the doors now!"
msg_hum_threshold_low = "The air is too dry! Hang your clothes to dry in your room or leave water boiling"
msg_gas_threshold_high = "The concentration of dangerous gases is too high! You should turn on the ventiation or open the window!"