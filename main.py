from forYouRequest import *
# main menu for tiktok bot

print(" _____ _ _  _____     _   ______       _                        \n" +
"|_   _(_) ||_   _|   | |  | ___ \     | |                       \n" +
"  | |  _| | _| | ___ | | _| |_/ / ___ | |_ _ __ ___   ___ _ __  \n" +
"  | | | | |/ / |/ _ \| |/ / ___ \/ _ \| __| '_ ` _ \ / _ \ '_ \ \n" +
"  | | | |   <| | (_) |   <| |_/ / (_) | |_| | | | | |  __/ | | |\n" +
"  \_/ |_|_|\_\_/\___/|_|\_\____/ \___/ \__|_| |_| |_|\___|_| |_|\n")
opt = int(input("\nSelect your option: \n  1)Scrape main page\n  2)Login\n  3)FIXME...\n\n>"))
if opt == 1:
    runMe()
elif opt == 2:
    print("IN WORK")
elif opt == 3:
	print("you selected three")
else:
	print(opt)
	print(type(opt))
