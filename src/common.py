FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Figtree:wght@400;500;600&family=Azeret+Mono:wght@400;500&display=swap">'
GH='https://github.com/tuhlee15'
LINKEDIN='https://www.linkedin.com/in/tully-njoroge'
def head(title,desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="helix-console.jpg">
<script>document.documentElement.classList.add('js')</script>
{FONTS}
<link rel="stylesheet" href="site.css">
</head>
<body>'''
def nav(cur=''):
    AC=' aria-current="page"'
    a=lambda h,t,k:f'<a href="{h}"{AC if k==cur else ""}>{t}</a>'
    li=f'<a class="gh" href="{LINKEDIN}" rel="noopener">LinkedIn ↗</a>' if LINKEDIN else ''
    return f'''<header class="nav"><div class="wrap">
  <a class="brand" href="index.html"><span class="mark">TN</span>Tully Njoroge</a>
  <nav aria-label="Main">{a("index.html#work","Work","work")}{a("helix-logistics.html","Helix","helix")}{a("global-portfolios.html","Finance","fin")}{a("extracurriculars.html","Extracurriculars","extra")}{a("index.html#about","About","about")}{li}<a class="gh" href="{GH}" rel="noopener">GitHub ↗</a></nav>
</div></header>'''
def contact():
    li=f'<a class="btn" href="{LINKEDIN}" rel="noopener">LinkedIn <span class="arr">→</span></a>' if LINKEDIN else ''
    return f'''<footer class="contact"><div class="wrap">
  <div class="eyebrow rv">Contact</div>
  <h2 class="display split" style="margin-top:14px">Let's talk.</h2>
  <div class="row rv"><p style="color:var(--muted);max-width:46ch;font-size:18px">Open to roles in management consulting, data analytics and venture capital, and happy to talk about any of the work here.</p>
  <div class="btns">{li}<a class="btn solid" href="{GH}" rel="noopener">GitHub <span class="arr">→</span></a></div></div>
  <div class="foot"><span>© 2026 Tully Njoroge</span><span>Florida, USA</span><span>Built by hand · hosted on GitHub Pages</span></div>
</div></footer>
<script src="site.js"></script>
</body>
</html>
'''
