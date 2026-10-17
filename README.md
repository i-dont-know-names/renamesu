# rename! - osu! replay username changer, but awfully simplified

Ever wanted to change the username saved in an osu! replay? Maybe for privacy, or maybe you accidentally saved it as `Guest` while playing offline?

Well, this is the tool for you! ^_^

## Usage

**Requirements:** Python 3.10 or later. That's literally it lmao.

### Getting started

1. Download or clone this repository.
2. Open Command Prompt, Terminal, Konsole, or whatever command line you prefer.
3. Navigate to the folder containing `main.py`.
4. Run the command below:

```bash
python main.py replay.osr username [output_name.osr]
```

- `replay.osr` — the path to the replay you want to edit.
- `username` — the new username you want saved in the replay.
- `output_name.osr` — optional; the name or path for the new replay file.

### Example

```bash
python main.py "C:\Users\idktestnames\AppData\Roaming\osu!\exports\idknames-score.osr" idontknownames "plswork.osr"
```

This saves the edited replay as `plswork.osr` in the specified output location. If you use just a filename for the output, it will be saved in the current working directory.

If you don't specify an output name, it will add "_new" to the end of the file name to refrain from overwriting the original file  

## Issues or suggestions?

Found a bug, something isn't working, or have an idea to improve the tool? Feel free to [open an issue](../../issues)!

I'll get back to you ASAP!! I'm just a 16-year-old making this because she's bored, after all. :p
