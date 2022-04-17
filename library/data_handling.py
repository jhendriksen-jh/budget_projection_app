"""
Functions for accessing the created and used by the app
"""
import os
import pathlib 


def process_username(user: str):
    """
    Determines if data exists for current user and creates file if not
    Args:
        user: name of user/username
    Returns:
        data_location: absolute path determined location of user data file
    """
    headers = ["Date","Type","Category","Account","Amount","Balance"]

    abs_parent_path = pathlib.Path(__file__).parent.parent.resolve()
    user_file = f"{user}.csv"
    data_file_path = f"{abs_parent_path}\\user_data\\"
    user_file_path = f"{data_file_path}\\{user_file}"

    if os.path.exists(user_file_path):
        return user_file_path
    else:
        os.mkdir(data_file_path)
        with open(user_file_path, "w") as empty_user_csv:
            empty_user_csv.write(",".join(headers))

    print(user_file_path)

process_username("dkjfsl")