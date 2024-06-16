# Music Metadata

I'm keeping this repository this mainly to remember how to do it and to have a boilerplate the next time I need it.

It updates the track number, title, year and album of all audio files in the subfolders.

All the subfolders's names have to be in the format `1986 - A Kind of Magic`, where the number before the slash is the year where the album is released and the string after is the name of the album.

The audio files have to be in the format `01 - One Vision.flac`, where the number before the dash is the track number and the string after is the name of the track.

## Configuration
There are 2 parameters that need to be set in the `main.py` file:
- `working_dir`: working folder, it will get all the files in all subfolders
- `extension`: it gets only files having this extension

## Requirements
Python 3.9