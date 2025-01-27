learn_alphabet = {
    "a": ["Apple", "Orange", "Mango"],
    "b": ["Banana", "Bat", "Boat"],
    "c": ["Cat", "Car", "Cup"],
    "d": ["Dog", "Duck", "Dove"], # type: ignore
    "e": ["Elephant", "Egg", "Eggplant"],
    "f": ["Fish", "Fruit", "Frog"], # type: ignore
    "g": ["Goat", "Grape", "Giraffe"],
    "h": ["Horse", "Honey", "Hut"],
    "i": ["Icecream", "Igloo", "Iguana"],
    "j": ["Jelly", "Jellyfish", "Joker"],
    "k": ["Kite", "Kite", "Kite"],
    "l": ["Lion", "Lion", "Lion"],
    "m": ["Mango", "Mango", "Mango"],   
    "n": ["Nose", "Nose", "Nose"],
    "o": ["Orange", "Orange", "Orange"],
    "p": ["Pineapple", "Pineapple", "Pineapple"],
    "q": ["Queen", "Queen", "Queen"],
    "r": ["Rabbit", "Rabbit", "Rabbit"],                        
    "s": ["Snake", "Snake", "Snake"],                       
    "t": ["Tiger", "Tiger", "Tiger"],                       
    "u": ["Umbrella", "Umbrella", "Umbrella"],                               
    "v": ["Valentine", "Vacancy", "Vulture"],                                   
    "w": ["Watermelon", "Whale", "Watch"],                                    
    "x": ["X-ray", "X-ray", "X-ray"],                                                                                               
    "y": ["Yogurt", "Yocht", "Yak"],
    "z": ["Zebra", "Zoo", "Zap"]
}

user_input = input("Enter a character : ").lower()

if user_input in learn_alphabet:
    print(f"words start with {user_input} are :")
    for word in learn_alphabet[user_input]:
        print(f"{user_input.upper()} for {word}")
else :
    print("Enter a valid character")