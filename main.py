from Final.Profile import Profile
from Final.User import *
from colorama import Fore, Back, Style


def main():
    print(Fore.BLUE + "============ creating users =============")
    # Save instantiate new users
    admin = User(None, "admin@email.com", "password", "Admin")
    subscriber = User(None, "newGuy@email.com", "password", "Subscriber")
    writer = User(None, "thisguy@email.com", "password", "Writer")
    editor = User(None, "thatguy@email.com", "password", "Editor")
    print("=========================================")

    # add users to array
    users = [admin, subscriber, writer, editor]
    print(Fore.GREEN + "============ saving users ===============")
    # save each user
    for user in users:
        User.save(user)
    print("=========================================")

    # check that all users are created
    print(Fore.MAGENTA + "============ retrieving users ============")
    print(User.get_all())
    print("=========================================")

    User.get_by_pk(3)

    # create user profiles
    all_users = User.get_all()
    for u in all_users:
        if u.role == "Writer":
            print(u.user_id)
            profile = Profile(None, u.user_id, "first_name", None, "last_name", "writer_profile")
            profile.save(profile)

    print(Profile.get_all())


if __name__ == "__main__":
    main()
