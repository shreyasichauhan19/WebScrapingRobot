from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("The Science Bot")


def introduce_yourself():
    print('-' * 50)
    robot.say_hello()
    print('-' * 50)

def open_articles():
    for scientist in SCIENTISTS:
        formatted_scientist = scientist.replace(" ", "_")
        print(f"~~~~~~~~~~~~~ {scientist} ~~~~~~~~~~~~~~~ "\n)
        robot.data_scraping(f"https://en.wikipedia.org/wiki/{formatted_scientist}")
        print('-' * 50)

def popping_off():
    robot.say_goodbye()
    print('-' * 50)


def main():
    introduce_yourself()
    open_articles()
    popping_off()

if __name__ == "__main__":
    main()
