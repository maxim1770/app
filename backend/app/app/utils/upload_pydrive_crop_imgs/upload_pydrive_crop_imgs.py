from pathlib import Path

import pydrive
from PIL import Image
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import GoogleDriveFile


def get_drive() -> GoogleDrive:
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        try:
            gauth.Refresh()
        except pydrive.auth.RefreshError:
            gauth.LocalWebserverAuth()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    return GoogleDrive(gauth)


def get_folder_id(drive: GoogleDrive, folder_title: str):
    # Auto-iterate through all files in the root folder.
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file_ in file_list:
        if file_['title'] == folder_title:
            return file_['id']


def set_content_file(drive: GoogleDrive, file_path: Path, file_title: str, file_description: str, *,
                     folder_id: str) -> GoogleDriveFile | None:
    try:

        file_: GoogleDriveFile = drive.CreateFile({'title': file_title,
                                                   'description': file_description,
                                                   'parents': [
                                                       {
                                                           "kind": "drive#fileLink",
                                                           "id": folder_id
                                                       }
                                                   ]})
        file_.SetContentFile(file_path)

        file_.Upload()

        file_.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})

        return file_

    except Exception as _ex:
        return None


def main(drive: GoogleDrive, path: Path, box: tuple, file_title: str, file_description: str, folder_title: str) -> str:
    path_img_part: Path = Path(fr'C:\Users\MaxDroN\Desktop\{path.stem + "_part"}.jpg')

    im = Image.open(path)
    # im.crop((3271, 2129, 5069, 2492)).save(r"C:\Users\MaxDroN\Desktop\image_296_part.jpg", quality=95)

    print(path_img_part)

    im.crop(box).save(path_img_part, quality=95)

    folder_id: str = get_folder_id(drive, folder_title)
    file_: GoogleDriveFile = set_content_file(drive, path_img_part, file_title, file_description, folder_id=folder_id)

    # path_img_part.unlink()

    file_id: str = file_['id']

    return f'[![](https://drive.google.com/uc?export=view&id={file_id})](https://drive.google.com/file/d/{file_id}/view?usp=share_link)'


if __name__ == '__main__':
    drive: GoogleDrive = get_drive()

    path = Path(r"C:\Users\MaxDroN\python_projects\parsing_manuscript_image\data\image_309.jpg")
    box: tuple = (877, 241, 2921, 2825)
    file_title: str = 'Дело же любви есть, часть 2'
    file_description: str = "Источник: evangelie_uchitelnoe_licevoe л. 301"
    folder_title: str = 'Любовь'

    print(main(drive,
               path=path,
               box=box,
               file_title=file_title,
               file_description=file_description,
               folder_title=folder_title,
               ))
