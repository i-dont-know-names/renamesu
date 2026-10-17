import sys
from pathlib import Path


def change_username(replay_file, username, output_file=None):
    replay_file = Path(replay_file)

    if not replay_file.is_file():
        raise ValueError("Can't find that replay file")

    if not username.strip():
        raise ValueError("Username can't be empty")

    new_name = username.encode("utf-8")
    data = replay_file.read_bytes()
    pos = 5

    def read_string():
        nonlocal pos

        if pos >= len(data):
            raise ValueError("Replay file looks broken")

        if data[pos] == 0:
            pos += 1
            return

        if data[pos] != 11:
            raise ValueError("Replay file looks broken")

        pos += 1
        length = 0
        shift = 0

        while True:
            if pos >= len(data):
                raise ValueError("Replay file looks broken")

            b = data[pos]
            pos += 1
            length |= (b & 127) << shift

            if b < 128:
                break

            shift += 7
            if shift > 28:
                raise ValueError("Replay file looks broken")

        pos += length
        if pos > len(data):
            raise ValueError("Replay file looks broken")

    read_string()
    name_start = pos
    read_string()
    name_end = pos

    length = len(new_name)
    length_bytes = bytearray()

    while length >= 128:
        length_bytes.append((length & 127) | 128)
        length >>= 7

    length_bytes.append(length)

    replacement = b"\x0b" + bytes(length_bytes) + new_name
    changed_data = data[:name_start] + replacement + data[name_end:]

    if output_file is None:
        output_file = replay_file.with_name(replay_file.stem + "_new.osr")
    else:
        output_file = Path(output_file)

    if output_file.resolve() == replay_file.resolve():
        raise ValueError("Use a different output filename so the original stays safe")

    output_file.write_bytes(changed_data)
    return output_file


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python epic_name_changer.py <replay.osr> <username> [output.osr]")
        sys.exit(1)

    try:
        output = change_username(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3] if len(sys.argv) == 4 else None
        )
        print(f"Done, saved to {output}")

    except (ValueError, OSError, UnicodeEncodeError) as e:
        print(f"Couldn't change username: {e}")
        sys.exit(1)