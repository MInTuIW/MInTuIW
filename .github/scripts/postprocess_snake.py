import re, os, sys

assets_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')
for fname in os.listdir(assets_dir):
    if not fname.startswith('snake-') or not fname.endswith('.svg'):
        continue
    path = os.path.join(assets_dir, fname)
    with open(path, 'r') as f:
        svg = f.read()

    # Ensure --cs has # prefix
    svg = re.sub(r'--cs:([0-9A-Fa-f]{6})', r'--cs:#\1', svg)

    # Replace snake fill with gradient reference
    svg = svg.replace(
        '.s{shape-rendering:geometricPrecision;fill:var(--cs)',
        '.s{shape-rendering:geometricPrecision;fill:url(#snakeGrad)'
    )

    # Add mint gradient defs (after </style>)
    mint_grad = '''<defs>
<linearGradient id="snakeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#B8DFD8"/>
  <stop offset="100%" stop-color="#2A8F86"/>
</linearGradient>
</defs>'''
    svg = svg.replace('</style>', '</style>' + mint_grad)

    # Remove progress bar
    svg = re.sub(r'<rect class="u[^"]*"[^>]*/>', '', svg)

    with open(path, 'w') as f:
        f.write(svg)
    print(f'Processed: {fname}')
