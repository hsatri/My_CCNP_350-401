import re
import os

file_path = os.path.join(os.getcwd(), 'study-progress.md')

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
