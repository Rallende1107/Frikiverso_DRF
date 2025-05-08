import os

def user_img_upload_path(instance, filename):
    path = os.path.join('users', 'img', 'avatars')
    return os.path.join(path, filename)