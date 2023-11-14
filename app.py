########################################################################
################# S T A R T E R   C O D E ##############################
########################################################################

# Import libraries
from flask import Flask, jsonify, request, send_file, render_template, make_response, send_from_directory
from flask_restful import Resource, Api
import requests
import json # pip install not needed
import os # pip install not needed
import tempfile # pip install not needed
import random #add this bitch again mofos!

# Create the Flask app
app = Flask(__name__)

# Create an API object
api = Api(app)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Create Hello resource
class Hello(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
		response = make_response(render_template('home.html'))
		response.headers['Content-Type'] = 'text/html'
		return response

########################################################################

# Find your resource below to modify your code!
# IMPORTANT: Only create new classes directly below your existing class!


# Create Person 1 resource
class Motivation(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
		response = make_response(render_template('motivation.html'))
		response.headers['Content-Type'] = 'text/html'
		return response

class MotivationAPI(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):

		# Holds a list of motivation quotes to show the user
		motvationQuotes = [
							"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
							"Your life does not get better by chance; it gets better by change. - Jim Rohn",
							"The only person you should try to be better than is the person you were yesterday. - Anonymous",
							"Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
							"Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
							"Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
							"Take care of your body; it's the only place you have to live. - Jim Rohn",
							"The greatest wealth is health. - Virgil",
							"The only bad workout is the one that didn't happen. - Anonymous",
							"Creativity is intelligence having fun. - Albert Einstein",
							"Innovation distinguishes between a leader and a follower. - Steve Jobs",
							"The more I practice, the luckier I get. - Gary Player",
							"Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
							"Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi",
							"The beautiful thing about learning is that no one can take it away from you. - B.B. King",
							"The best way to predict the future is to create it. - Peter Drucker",
							"No act of kindness, no matter how small, is ever wasted. - Aesop",
							"Alone, we can do so little; together, we can do so much. - Helen Keller",
							"The Earth does not belong to us: we belong to the Earth. - Marlee Matlin",
							"We won't have a society if we destroy the environment. - Margaret Mead",
							"The future will either be green or not at all. - Bob Brown",
							"You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
							"The only way to do great work is to love what you do. - Steve Jobs",
							"The biggest risk is not taking any risk. In a world that's changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
							"Your time is limited, don't waste it living someone else's life. - Steve Jobs",
							"Success is not in what you have, but who you are. - Bo Bennett",
							"Every strike brings me closer to the next home run. - Babe Ruth",
							"Your life only gets better when you get better. - Brian Tracy",
							"The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
							"It does not matter how slowly you go as long as you do not stop. - Confucius",
							"The only way to do great work is to love what you do. - Steve Jobs",
							"Believe you can and you're halfway there. - Theodore Roosevelt",
							"In the middle of every difficulty lies opportunity. - Albert Einstein",
							"The future depends on what you do today. - Mahatma Gandhi",
							"The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
							"The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
							"Don't watch the clock; do what it does. Keep going. - Sam Levenson",
							"The harder you work for something, the greater you'll feel when you achieve it. - Anonymous",
							"The only place where success comes before work is in the dictionary. - Vidal Sassoon",
							"Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
							"Someday is not a day of the week. - Denise Brennan-Nelson"
]

		# Returns the question for this resource and a random answer
		return jsonify({'Question': "Need help finding motivation", 
						"Answer": random.choice(motvationQuotes)})

# Create Person 2 resource
class Resource2(Resource):

	def get(self):
			# Ask the user a question
			question = "Would you like to know a way to maximize your study time today?"

			study_suggestions = [
				"You should hand stand against the wall for 5 minutes while singing your favorite song backwards, then hit the books!",
				"Take your TV, turn the volume all the way up, then throw it out the window. Shut the window and ignore the phone calls and knocks on your door. Now you can study like a PRO!",
				"Take a 15 second break, every five minutes, to recharge your chi flow, which you will need, to make it to the Omega level.",
				"Retreat to an underground bunker, miles below the sea, to study with the mole people, they will help you.",
				"Every time you stop studying, jab yourself with a knife. This is a guaranteed way to become very sharp!",
				"If you are having trouble focusing, try to imagine that everybody in the world is naked, except you... isn't that weird? NOW STUDY!",
				"Attempt something much harder than what you are currently working on, realize that it's just not worth it, give up, cry, rebrand yourself as adaptive, and come back to your studies relieved that this is SO much easier than what you were trying to do, and that it will feel so much better just finishing your studying than internalizing a constant sense of blame and dread and identifying as a mistake and a failure.",
				"Take a break from studying, and go on a walk. While on your walk, think about how you are going to study when you get back. Really feel that studying. Each step is a step towards the all too quickly arriving future where you don't have to think about anything at all, just float, in oblivion.",
				"Summon a demon that gradually eats your soul evertime you do not study.",
				"Take a shower and bring your laptop!"
				"Just keep putting off studying, fail all your classes, drop out without getting any refund, go to a mountain, yell \"WHYYYYYY!?\" and then realize that you can avoid all that by just studying here and now, in your cozy little study nook with your mountain of squishmallows.",
				"Take a chance on me where me = studying."
				"Journey deep into your soul and realize that this is all meaningless, that the only meaning is what you bring to the table in the world of forms. Now, either make studying meaningful and get it done.. or.. completely dissolve your ego effectively ending your life as a student and beginning life as a nothing. THEN study.",
				"Take study-enhancing drugs, stay up all night, realize you don't need food and sleep. What could go wrong?",
				"Just do it. (not a brand embassador)",
				"Go to the gym, get a pump, then study.",
				"Take a deep inhalation, completely filling your body with study-clorians... hold it... keep holding till you feel like you are in the computer world.. everything is just 1's and 0's... okay, release! Now you don't need to study.",
				"Fall into a deep sleep and use a pre-recorded suggestion tape to guide your dreams into a study session. Then master all subjects and even summon the great geniuses of yore to assist you. Wake up and realize that now you have to study for real.",
				"Spend less time on apps about studying and study.",
				"Add a comment for every single line of code you write. In this comment, you type without thinking or even looking at the screen.. freetype. When you hit a block, look at all the cryptic weird comments and have an insight. Then use this insight to mitigate any barriers to maximum study power!",
				"Join a study group, become study overlord, make THEM study for YOU.",
				"Quickly contort your hands into many magical ninja jutsus and form a seal. Now you can study.",
				"Use the forbidden shadow clone jutsu to form a clone army to study for you.",
				"Go and make yourself a PERFECT sandwhich, now look at that sandwhich and know that you can't have it until you study."
				
			]

			# Select a random study suggestion
			random_suggestion = random.choice(study_suggestions)

			return jsonify({'question': question, 'suggestion': random_suggestion})

# Create Person 3 resource
class Resource3(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	# asdasdas
	
	def get(self):
		response = make_response(render_template('r3.html'))
		response.headers['Content-Type'] = 'text/html'
		return response
	

	


	

# Create Person 4 resource
class Resource4(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):
		response = make_response(render_template('r4.html'))
		response.headers['Content-Type'] = 'text/html'
		return response
# Add the defined resources along with their corresponding urls
api.add_resource(Hello, '/')

api.add_resource(Motivation, '/Motivation')
api.add_resource(MotivationAPI, '/MotivationAPI')
######################################
# Person 1 additional resources here #

######################################

api.add_resource(Resource2, '/Resource2')
######################################
# Person 2 additional resources here #

######################################

api.add_resource(Resource3, '/Resource3')
######################################
# Person 3 additional resources here #

######################################

api.add_resource(Resource4, '/Resource4')
######################################
# Person 4 additional resources here #

######################################

# Driver function
if __name__ == '__main__':

	app.run(debug = True)