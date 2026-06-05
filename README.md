# Greentext Generator

This project started when I wanted to help a friend start a YT Shorts channel about greentext stories and I made this to fasten up the process of getting the greentext images, and now it's become open source.

---

Generates a 4chan greentext image from a story you write.

## Process

1. Paste your story into `story.txt`
2. Run `python greentext_generator.py`
3. Type your output filename (ex: `output.png`)
4. A random image from `assets/` gets picked and placed onto the resulting greentext image
5. Done

## Requirements

- Pillow library
- arial.ttf and arialbd.ttf in the same folder as the script (often not needed because the fonts are probably already in your system)
- An `assets/` folder with images

## Example Output

<img width="594" height="676" alt="greentext" src="https://github.com/user-attachments/assets/064ec09e-248f-4531-b16b-13e6a63fa42b" />

## Notes

story.txt and the assets/ folder are not included, so make one before running.

You may modify `assets/` to add or remove images.

---

Authored 100% by quandelaa
