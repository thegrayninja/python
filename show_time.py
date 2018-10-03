from datetime import datetime
import time
import curses

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    while True:
        #print(datetime.now().strftime("%H:%M:%S"))
        stdscr.addstr(0, 0, datetime.now().strftime("%H:%M:%S"))
        stdscr.refresh()
        time.sleep(1)


if __name__ == "__main__":
    main()
    print("bye")
