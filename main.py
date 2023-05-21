from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()
    print('-' * 50)

def open_articles():
    for scientist in SCIENTISTS:
        formatted_scientist = scientist.replace(" ", "_")
        robot.print_first_paragraph(f"https://en.wikipedia.org/wiki/{formatted_scientist}")
        robot.print_bday_dday(f"https://en.wikipedia.org/wiki/{formatted_scientist}")
        print('-' * 50)


def main():
    introduce_yourself()
    open_articles()

if __name__ == "__main__":
    main()
