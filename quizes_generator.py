"""
This is a script to generate random quizes (practical for classroom scenario) where each quiz have questions in random orders and the options also
are in random order (meaning the same question across different quizes will have different options ) , the script generate text file quizes ready to be printed 
i go this idea from Automoate the Boring Stuff with Python book 
"""



import random 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

countries = list(capitals.keys())
keyAnswers = list(capitals.values())

random.shuffle(countries)  

for quizNum in range(10):
    with open('.\\quizes\\quiz%s.txt'%(quizNum),'w') as quiz :
        content = ''
        #header
        content += 'Name:\n\nDate:\n\nScore:\n\n'
        content += 'Geography Pop Quiz'.center(40)+'\n\n'
        for country in countries : 

            random.shuffle(countries) 
            random.shuffle(keyAnswers)
            options = [capitals[country]] + keyAnswers[:3]
            random.shuffle(options) # so the answer is not always first choice , of course
            question = ''
            question += f'\nWhat is the capital of {country}?\n'
            for letter ,option in zip(['A','B','C','D'],options):
                question += f'    {letter}. {option}\n'
            content += question


        quiz.write(content)
