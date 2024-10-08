from pathlib import Path
import json

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

path = Path('numbers.json')
# contnets = json.dumps(numbers)
# path.write_text(contnets)


contnets = path.read_text()
numbers = json.loads(contnets)
print(numbers)