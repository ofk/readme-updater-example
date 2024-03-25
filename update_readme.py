import re
import glob

list_content = ''

readme_paths = glob.glob('root/**/README.md', recursive=True)
if readme_paths:
    items = []
    for readme_path in readme_paths:
        label = readme_path.replace('root/', '').replace('/README.md', '').replace('README.md', '').replace('/', ' / ')
        items.append(f'- [{label}]({readme_path})')
    list_content = '\n'.join(items)

with open('README.md', 'r+') as fp:
    content = fp.read()
    content = re.sub(r'(<!-- BEGIN LIST -->)[\s\S]*?(<!-- END LIST -->)', r'\1\n' + list_content + r'\n\2', content)
    fp.seek(0)
    fp.truncate()
    fp.write(content)
