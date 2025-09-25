while True:
    user=input("you:")
    if user.lower() in ["bye","Exit"]:
        print("bot:Good byee!")
        break
    elif user.lower() in["hello"]:
        print("Hi..... good moring")
    elif user=="how are u":
        print("Im fine...how about u")
    elif user=="fine":
        print("what do you want")
    else:
        print("bot: sorry I can not understand:",user)
