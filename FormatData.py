from Functions import *

mental_state = []

mental_state.append("Emotion")
mental_state.append("Gambling")
mental_state.append("Rest")
mental_state.append("Structural")
mental_state.append("WM")

for state in range (0, len(mental_state)):
    # Gets averaged data
    #getfilepath(mental_state[state])

    # Gets averaged images from averaged data
    getaveragedfilepath(mental_state[state])
