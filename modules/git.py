import subprocess
def get_user_name():
    user_name = subprocess.run(
        ["git", "config" , "--get" , "user.name"],
        stdout=subprocess.PIPE,
        text=True,
    )
    user_name = user_name.stdout.strip()
    return user_name
def get_user_email():
    user_email = subprocess.run(
        ["git", "config" , "--get" , "user.email"],
        stdout=subprocess.PIPE,
        text=True,
    )
    user_email = user_email.stdout.strip()
    return user_email