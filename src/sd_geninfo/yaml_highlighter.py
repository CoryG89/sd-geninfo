from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class YamlHighlighter(RegexHighlighter):
    base_style = "yaml."
    highlights = [
        r'(^|[\n])(?P<key>.*:)',
        r':\s*(?P<value>\w+)',
        r'(?P<boolean>true|false)',
        r'[:\s](?P<number>\d+(\.\d+)?)[\s]',
        r'(?P<string>[\'"][^\'"]*[\'"])\n',
        r'(?P<comment>#.*)'
    ]

yaml_theme = Theme({
    'yaml.key': 'bold magenta',
    'yaml.value': 'bright_white',
    'yaml.boolean': 'bold blue',
    'yaml.number': 'bold green',
    'yaml.string': 'yellow',
    'yaml.comment': 'italic white'
})
