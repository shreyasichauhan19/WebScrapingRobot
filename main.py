from robotics import Robot
import time

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()

def open_articles():
    for scientist in SCIENTISTS:
        formatted_scientist = scientist.replace(" ", "_")
        robot.open_webpage(f"https://en.wikipedia.org/wiki/{formatted_scientist}")
        time.sleep(2)  # pause for 5 seconds to let the page load


def main():
    introduce_yourself()
    open_articles()



if __name__ == "__main__":
    main()