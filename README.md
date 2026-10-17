# osu!replay username changes but awfully simplified

Want to change your username on any osu replay for privacy, or because you accidentally saved it as "guest"? 

this is the tool for you! ^_^

# Usage:

Requirements: 
literally just python 3.10 and later lmao

```python main.py replay.osr <username you want> [output_name.osr]```

Replay will save to where the replay is, so I really recommend putting the replay where you can easily access it.

Example:

```python main.py "C:\Users\idktestnames\AppData\Roaming\osu!\exports\idknames playing a certain map - by a certain artist (01/01/2026).osr" idontknownames "plswork.osr"```

Replay will save to C:\Users\idktestnames\AppData\Roaming\osu!\exports\ as plswork.osr

If you don’t specify a replay name, it will save with an "_new" at the end of the filename so it doesn't overwrite the original replay.

Any issues? open an issue! I will take some time getting back to you, as I'm just a 16 year old doing this because she's bored.
