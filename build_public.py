"""Build the public GitHub Pages site from the local editable sources.

Only explicit HTML pages and approved Homemade storefront assets are copied.
Original uploads and private recipes are never part of this build.
"""
from pathlib import Path
import re, shutil, json

root=Path(__file__).resolve().parent
sources=['index.html','404.html','pages/kruiden-abc.html','pages/contact.html','pages/our-garden-journal.html','pages/privacy-policy.html','pages/thank-you.html']
for relative in sources:
    html=(root/'_src'/relative).read_text(encoding='utf-8')
    assert 'password-gate.' not in html, f'Remove legacy gate from {relative}'
    assert not re.search(r'gh[pousr]_[A-Za-z0-9_]{20,}',html), 'Unexpected credential in HTML'
    (root/relative).write_text(html,encoding='utf-8')

source=root/'HomeMade By Jess'/'public'
destination=root/'homemade'
public_origin='https://gardenbyjess.store/homemade'
old_origin='https://homemade-by-jess.forest67.chatgpt.site'
slugs=['privacy','cookies','voorwaarden','annuleren-klachten','contact']
files=['index.html','style.css','shop.js','privacy-controls.js','privacy.html','cookies.html','voorwaarden.html','annuleren-klachten.html','contact.html','404.html','robots.txt','sitemap.xml','llms.txt','assets/mark.svg','assets/brownietaart-detail.webp','assets/chocoladetaarten-hero.webp','assets/social-share.jpg']
for relative in files:
    target=destination/relative
    target.parent.mkdir(parents=True,exist_ok=True)
    if Path(relative).suffix in ['.html','.xml','.txt','.css','.js']:
        text=(source/relative).read_text(encoding='utf-8').replace(old_origin,public_origin)
        if relative.endswith('.html'):
            for slug in slugs:
                text=text.replace(f'href="{slug}"',f'href="/homemade/{slug}.html"')
                text=text.replace(f'href="{public_origin}/{slug}"',f'href="{public_origin}/{slug}.html"')
                text=text.replace(f'content="{public_origin}/{slug}"',f'content="{public_origin}/{slug}.html"')
            text=text.replace('href="/"','href="/homemade/"').replace('href="/#','href="/homemade/#')
            text=text.replace('href="/assets/','href="/homemade/assets/').replace('href="/style.css"','href="/homemade/style.css"')
            text=text.replace('</header>','<a class="garden-return" href="/">← Garden by Jess · Kruidenthee</a></header>',1)
        if relative in ['sitemap.xml','llms.txt']:
            for slug in slugs:
                text=re.sub(re.escape(public_origin+'/'+slug)+r'(?=[<)#\s]|$)',public_origin+'/'+slug+'.html',text)
        if relative=='style.css':
            text+='\n.garden-return{font-size:11px;color:var(--muted);text-decoration:underline}.header{flex-wrap:wrap}.header .garden-return{flex-basis:100%;text-align:right;margin-top:-25px}@media(max-width:700px){.header{height:125px}.header .garden-return{margin-top:-18px;font-size:10px}}\n'
        (target).write_text(text,encoding='utf-8')
    else: shutil.copy2(source/relative,target)

urls=['https://gardenbyjess.store/']+['https://gardenbyjess.store/'+x for x in sources if x not in ['index.html','404.html','pages/thank-you.html']]+[public_origin+'/']+[public_origin+'/'+slug+'.html' for slug in slugs]
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+url+'</loc></url>' for url in urls)+'</urlset>',encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://gardenbyjess.store/sitemap.xml\n',encoding='utf-8')
print(f'Built {len(sources)} unlocked Garden pages and {len(files)} safe Homemade files.')
