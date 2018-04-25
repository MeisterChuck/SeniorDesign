from GetData import GetData


def main():
    mental_state = ["Emotion", "Gambling", "Rest", "Structural", "WM"]
    data = GetData(mental_state)
    data.run()
    #classify = ImageClassifier


if __name__ == '__main__':
    main()
