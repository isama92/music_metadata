from pathlib import Path
import mutagen

working_dir = '/mnt/d/Media/fix/queen/output/'
extension = 'flac'

def get_files(dir_path: str) -> list[Path]:
    return list(Path(dir_path).rglob('*.' + extension))

def update_file(file_path: Path):
    file = mutagen.File(file_path)

    tmp = file_path.stem.split('-', 1)
    file['tracknumber'] = tmp[0].strip()
    file['title'] = tmp[1].strip()

    tmp = file_path.parent.name.split('-', 1)
    file['year'] = tmp[0].strip()
    file['album'] = tmp[1].strip()

    file.save()

def main():
    files = get_files(working_dir)
    for file in files:
        update_file(file)

if __name__ == '__main__':
    main()