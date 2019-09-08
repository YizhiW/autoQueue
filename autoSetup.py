import autoQueue

if __name__ == '__main__':

    obj = autoQueue.AutoQueue()

    print("##################################")
    print("First step: Get the icon location")
    print("##################################")

    input("Please move your mouse to the location of your WOW icon and stop there, press enter to continue")
    pos = obj.get_mouse_pos()
    print(f"The location of your icon is x:{pos.x}, y:{pos.y}, "
          f"please put it into .env WOW_ICON_X and WOW_ICON_Y"
          f"\n")

    print("##################################")
    print("Second step: Get the button location")
    print("##################################")

    input("Please move your mouse to the location of your '进入游戏' button and stop there, press enter to continue")
    pos = obj.get_mouse_pos()
    print(f"The location of your button is x:{pos.x}, y:{pos.y}, "
          f"please put it into .env RUNGAME_X and RUNGAME_Y"
          f"\n")

    print("##################################")
    print("Third step: Get the server location")
    print("##################################")

    input("Please move your mouse to your server and stop there, press enter to continue")
    pos = obj.get_mouse_pos()
    print(f"The location of your server is x:{pos.x}, y:{pos.y}, "
          f"please put it into .env SERVER_X and SERVER_Y"
          f"\n")
    input("press enter to exit")