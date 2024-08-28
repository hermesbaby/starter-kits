import argparse
from pyad import aduser, adgroup

def get_user_groups(username):
    try:
        user = aduser.ADUser.from_cn(username)
        groups = user.get_attribute("memberOf")
        return [adgroup.ADGroup.from_dn(group).cn for group in groups]
    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
        return []

def main(usernames):
    all_user_groups = {}

    for username in usernames:
        groups = get_user_groups(username)
        all_user_groups[username] = groups
        print(f"Groups for user {username}:")
        for group in groups:
            print(f"  {group}")
        print()

    if len(usernames) > 1:
        shared_groups = set(all_user_groups[usernames[0]])
        for groups in all_user_groups.values():
            shared_groups &= set(groups)

        print("Shared groups between all users:")
        for group in shared_groups:
            print(f"  {group}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get group memberships for specified Active Directory users.")
    parser.add_argument('usernames', metavar='U', type=str, nargs='+', help='List of usernames to check')
    args = parser.parse_args()

    main(args.usernames)
