ALLOWED_TAGS = [
    'a', 'div', 'p', 'span', 'img', 'em', 'i', 'li', 'ol', 'ul', 'strong', 'br', 'hr',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'table', 'tbody', 'thead', 'tr', 'td', 'th',
    'abbr', 'acronym', 'b', 'blockquote', 'code', 'strike', 'u', 'sup', 'sub', 'pre', 'iframe',
]

STYLES = [
    'background-color', 'font-size', 'line-height', 'color', 'font-family'
]

ATTRIBUTES = {
    '*': ['style', 'align', 'title', 'alt', 'width', 'height', 'src'],
    'a': ['href', ],
}