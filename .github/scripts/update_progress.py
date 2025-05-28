import re
import os

# Get the absolute path of this script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Move up two levels to reach project root
project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))

# Build full path to study-progress.md in project root
file_path = os.path.join(project_root, 'study-progress.md')


with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

total = len(re.findall(r'- \[[ xX]\]', content))
done = len(re.findall(r'- \[[xX]\]', content))

percent = int((done / total) * 100) if total else 0
bar_length = 30
filled = int((percent / 100) * bar_length)
bar = '#' * filled + '-' * (bar_length - filled)

progress_text = f'```text\nProgress: [{bar}] {percent}%\n```'

new_content = re.sub(
    r'```text\nProgress: \[.*?\] \d+%\n```',
    progress_text,
    content,
    count=1,
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
