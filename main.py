from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()

def open_articles():
    for scientist in SCIENTISTS:
        formatted_scientist = scientist.replace(" ", "_")
        robot.print_first_paragraph(f"https://en.wikipedia.org/wiki/{formatted_scientist}")
        print('-' * 50)

def main():
    introduce_yourself()
    open_articles()

if __name__ == "__main__":
    main()