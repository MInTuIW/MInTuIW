import json, random, os

jokes_file = os.path.join(os.path.dirname(__file__), '..', 'jokes.json')
with open(jokes_file, 'r') as f:
    jokes = json.load(f)

joke = random.choice(jokes)

sr, sg, sb = 93, 173, 226   # deep glacier blue (left)
er, eg, eb = 232, 248, 255  # near-white ice blue (right)

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="780" height="28" font-family="monospace" font-size="14">']
parts.append('<style>.c{opacity:0;animation:t 0.03s forwards;animation-delay:var(--d)}@keyframes t{to{opacity:1}}</style>')
parts.append('<rect width="780" height="28" fill="transparent"/><text y="20">')

for i, ch in enumerate(joke):
    t = i / max(len(joke) - 1, 1)
    r = int(sr + (er - sr) * t)
    g = int(sg + (eg - sg) * t)
    b = int(sb + (eb - sb) * t)
    esc = ch
    if ch == '&': esc = '&amp;'
    elif ch == '<': esc = '&lt;'
    elif ch == '>': esc = '&gt;'
    elif ch == '"': esc = '&quot;'
    elif ch == "'": esc = '&apos;'
    parts.append(f'<tspan class="c" style="--d:{i * 0.06:.2f}s" fill="#{r:02x}{g:02x}{b:02x}">{esc}</tspan>')

parts.append('</text></svg>')

svg_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'joke.svg')
with open(svg_path, 'w') as f:
    f.write(''.join(parts))

print(f'Done: {joke}')
