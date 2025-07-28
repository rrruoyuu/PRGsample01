def calculate_cookie_score(ingredients):
    score = 0
    for item in ingredients:
        item = item.strip().lower()
        if item == "sugar":
            score += 5
        elif item == "butter":
            score += 4
        elif item == "chocolate chips":
            score += 3
        elif item == "flour":
            score -= 2
        else:
            score += 1
    return score


def process_cookie_file(filename):
    with open(filename , 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            cookie_name = parts[0]
            ingredients = parts[1:]
            score = calculate_cookie_score(ingredients)
            print(f'Cookie: {cookie_name}')
            if score > 15:
                print('This cookie deserves a gold medal.')
            elif score > 5:
                print("This cookie is mediocre, but we’re not judging")
            else:
                print('This cookie is a disaster!')
            print('score: ',score)

#main code
while True:
    start = input("Would you like to score some cookies? (Type 'Stop' to quit, 'Yes' to start) ").capitalize()
    process_cookie_file('ingredients.txt')
    repeat = input("Would you like to score more cookies? (Type 'Stop' to quit, 'Yes' to start) ").capitalize()
    if start or repeat == "Stop":
        break