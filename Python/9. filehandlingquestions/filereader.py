from pathlib import Path

path = Path('./filedigit.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)