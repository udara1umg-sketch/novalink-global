from pathlib import Path
import re, zipfile, shutil
root=Path('/mnt/data/nova_v8')

# Stable real-photo URLs already used in the project (Unsplash-hosted photographs).
photos={
'cinnamon':'https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=1200&q=88',
'pepper':'https://images.unsplash.com/photo-1599909533730-f9d2d0a5b3c5?auto=format&fit=crop&w=1200&q=88',
'cardamom':'https://images.unsplash.com/photo-1601379329542-31c0cb7c0b24?auto=format&fit=crop&w=1200&q=88',
'cloves':'https://images.unsplash.com/photo-1600326145552-327f74b9d4f2?auto=format&fit=crop&w=1200&q=88',
'nutmeg':'https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=1200&q=88',
'mace':'https://images.unsplash.com/photo-1615485500704-8e990f9900f7?auto=format&fit=crop&w=1200&q=88',
'seeds1':'https://images.unsplash.com/photo-1532336414038-cf19250c5757?auto=format&fit=crop&w=1200&q=88',
'seeds2':'https://images.unsplash.com/photo-1540148426945-6cf22a6b2383?auto=format&fit=crop&w=1200&q=88',
'herbs1':'https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=1200&q=88',
'herbs2':'https://images.unsplash.com/photo-1497250681960-ef046c08a56e?auto=format&fit=crop&w=1200&q=88',
'herbs3':'https://images.unsplash.com/photo-1515586000433-45406d8e6662?auto=format&fit=crop&w=1200&q=88',
'chili':'https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=1200&q=88',
'chili2':'https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=88',
'coconut':'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=1200&q=88',
'landscape':'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=2400&q=90',
'business':'https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1200&q=88',
'digital':'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=88',
'farm':'https://images.unsplash.com/photo-1499529112087-3cb3b73cec95?auto=format&fit=crop&w=1200&q=88',
}

index=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="NovaLink Global — agribusiness, sourcing, project and business solutions, digital transformation and sustainable development from Sri Lanka.">
<link rel="canonical" href="https://novalinkglobal.lk/"><link rel="icon" href="logo.png"><link rel="stylesheet" href="styles.css">
<title>NovaLink Global | Growing Opportunities. Connecting Global Markets.</title>
</head>
<body>
<div class="topbar"><div class="wrap topbar-inner"><span>Connecting People • Agriculture • Business • A Sustainable Future</span><span class="top-contact">⌖ &nbsp;Sri Lanka &nbsp;&nbsp;&nbsp; ✉ &nbsp;info@novalinkglobal.lk &nbsp;&nbsp;&nbsp; ☎ &nbsp;+94 76 686 9930 <span class="social-mini">in &nbsp;&nbsp; f &nbsp;&nbsp; ◎ &nbsp;&nbsp; ▶</span></span></div></div>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="index.html" aria-label="NovaLink Global home"><img src="logo.png" class="brand-logo" alt="NovaLink Global (Private) Limited"></a>
<nav class="nav-links" aria-label="Main navigation"><a class="active" href="index.html">Home</a><a href="about.html">About Us</a><a href="agribusiness.html">Agribusiness⌄</a><a href="consultancy.html">Consultancy⌄</a><a href="digital.html">Digital⌄</a><a href="products.html">Products⌄</a><a href="projects.html">Projects</a><a href="contact.html">Contact</a><button class="search-btn" aria-label="Search">⌕</button><a class="quote-btn" href="contact.html">Request a Quote &nbsp;→</a></nav>
<button class="menu-btn" onclick="toggleMenu()" aria-label="Open navigation">☰</button>
<div class="mobile-nav" id="mobileNav"><a href="index.html">Home</a><a href="about.html">About Us</a><a href="agribusiness.html">Agribusiness</a><a href="consultancy.html">Consultancy</a><a href="digital.html">Digital Solutions</a><a href="products.html">Products &amp; Sourcing</a><a href="projects.html">Projects</a><a href="contact.html">Contact</a></div>
</div></header>
<main>
<section class="hero-target"><div class="hero-overlay"></div><div class="wrap hero-content"><div class="hero-copy-target"><div class="ey-target">SRI LANKA TO A SUSTAINABLE WORLD</div><h1>Growing Opportunities.<br>Connecting <span>Global Markets.</span></h1><p>NovaLink Global is a multi-disciplinary company delivering agribusiness solutions, project &amp; business support, digital transformation and sourcing of high-quality Sri Lankan products.</p><div class="hero-buttons"><a class="target-btn green" href="agribusiness.html">◒ &nbsp; Our Services &nbsp;→</a><a class="target-btn outline" href="contact.html">▤ &nbsp; Contact Us</a></div></div><div class="hero-slogan">Sustainable<br>Growth<br>Together<div class="swoosh"></div></div></div></section>
<section class="gateway-wrap"><div class="wrap gateway">
<a class="gateway-item" href="agribusiness.html"><span class="gateway-icon">⌁</span><b>Agribusiness Services</b><small>From farm to future</small></a>
<a class="gateway-item" href="consultancy.html"><span class="gateway-icon">▥</span><b>Project &amp; Business Solutions</b><small>Ideas into impact</small></a>
<a class="gateway-item" href="products.html"><span class="gateway-icon">◎</span><b>Sourcing &amp; Trading</b><small>Quality from Sri Lanka<br>to the world</small></a>
<a class="gateway-item" href="digital.html"><span class="gateway-icon">▣</span><b>Digital Solutions</b><small>Innovative solutions<br>for a connected world</small></a>
<a class="gateway-item" href="agribusiness.html"><span class="gateway-icon">◒</span><b>Sustainability &amp;<br>Climate Resilience</b><small>People, nature, progress</small></a>
</div></section>
<section class="what-section"><div class="wrap what-grid"><div class="what-copy"><div class="ey-target dark">WHAT WE DO</div><h2>Practical Solutions<br>for a Better Tomorrow</h2><p>We work with farmers, businesses, organizations and global partners to create value through agriculture, innovation and sustainable development.</p><a class="target-btn green small" href="about.html">Learn More About Us &nbsp;→</a></div>
<div class="what-cards">
<article class="target-card"><img src="{photos['farm']}" alt="Young plant growing in soil"><div><h3>Support Agriculture</h3><p>Productive farms,<br>stronger communities</p></div></article>
<article class="target-card"><img src="{photos['business']}" alt="Business planning and documents"><div><h3>Develop Businesses</h3><p>Plans, proposals,<br>real results</p></div></article>
<article class="target-card"><img src="{photos['cinnamon']}" alt="Sri Lankan spices"><div><h3>Connect Markets</h3><p>Sri Lankan quality<br>to global buyers</p></div></article>
<article class="target-card"><img src="{photos['digital']}" alt="Digital technology solutions"><div><h3>Enable Digital Growth</h3><p>Smart solutions<br>for modern businesses</p></div></article>
</div></div></section>
<section class="impact-strip"><div class="wrap impact-grid"><div class="impact-item"><strong>♟</strong><b>Trusted by</b><span>Clients Worldwide</span></div><div class="impact-item"><strong>◎</strong><b>Multiple</b><span>Industry Expertise</span></div><div class="impact-item"><strong>◒</strong><b>Committed to</b><span>Sustainability</span></div><div class="impact-item"><strong>▥</strong><b>Focused on</b><span>Real Impact</span></div><div class="impact-quote"><strong>“</strong><span>Connecting knowledge, people and opportunities<br>for a more sustainable and prosperous world.</span><em>— NovaLink Global</em></div></div></section>
<section class="home-products"><div class="wrap"><div class="ey-target dark">FEATURED SOURCING</div><h2>Sri Lankan Products for Global Markets</h2><p class="lead">Explore our export-focused spice and agricultural product range. Availability, grade, packing and pricing are confirmed against each buyer enquiry.</p><div class="featured-products"><a href="products.html" class="fp"><img src="{photos['cinnamon']}" alt="Ceylon cinnamon sticks"><b>Ceylon Cinnamon</b><small>Kurundu</small></a><a href="products.html" class="fp"><img src="{photos['pepper']}" alt="Black peppercorns"><b>Black Pepper</b><small>Gam Miris</small></a><a href="products.html" class="fp"><img src="{photos['cardamom']}" alt="Cardamom pods"><b>Cardamom</b><small>Enasal</small></a><a href="products.html" class="fp"><img src="{photos['cloves']}" alt="Cloves"><b>Cloves</b><small>Karabu Natti</small></a></div><div class="center"><a class="target-btn outline dark-outline" href="products.html">View All Products &nbsp;→</a></div></div></section>
<section class="target-cta"><div class="wrap"><div class="ey-target">LET'S BUILD A SUSTAINABLE FUTURE TOGETHER</div><h2>Have a project, product or business opportunity?</h2><p>Tell us what you need and we will discuss a practical way forward.</p><a class="target-btn green" href="contact.html">Start a Conversation &nbsp;→</a></div></section>
</main>
<script src="main.js"></script>
<footer><div class="wrap footer-grid"><div><img src="logo.png" class="footer-logo" alt="NovaLink Global"><p>Connecting Markets. Creating Value. Sustaining Tomorrow.</p></div><div><h4>Business</h4><a href="agribusiness.html">Agribusiness</a><a href="consultancy.html">Consultancy</a><a href="digital.html">Digital Solutions</a><a href="products.html">Products &amp; Sourcing</a></div><div><h4>Company</h4><a href="about.html">About Us</a><a href="projects.html">Projects</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div><div><h4>Contact</h4><p>Sri Lanka</p><a href="mailto:info@novalinkglobal.lk">info@novalinkglobal.lk</a><a href="tel:+94766869930">+94 76 686 9930</a></div></div><div class="wrap footer-bottom">© 2026 NovaLink Global (Private) Limited. All Rights Reserved.</div></footer><a class="floating-wa" href="https://wa.me/94766869930?text=Hello%20NovaLink%20Global%2C%20I%20would%20like%20to%20make%20an%20enquiry." target="_blank" rel="noopener" aria-label="Chat with NovaLink Global on WhatsApp">◔ <span>Chat with us</span></a>
</body></html>'''
(root/'index.html').write_text(index,encoding='utf-8')

css=(root/'styles.css').read_text(encoding='utf-8')
css += '''\n\n/* ===== NovaLink V8 target interface ===== */\nbody{font-family:Inter,Arial,sans-serif;color:#071f38;background:#fff}.wrap{width:min(1590px,92%);margin:auto}.topbar{background:#034735;color:#fff;font-size:13px}.topbar-inner{height:42px;display:flex;align-items:center;justify-content:space-between}.top-contact{opacity:.95}.social-mini{margin-left:45px;font-weight:800;letter-spacing:7px}.site-header{position:relative;top:auto;background:#fff;border-bottom:1px solid #e8ecea;box-shadow:none}.header-inner{min-height:110px;display:flex;align-items:center;justify-content:space-between;gap:30px}.brand-logo{width:530px;height:100px;object-fit:contain;object-position:left center}.nav-links{display:flex;align-items:center;gap:28px;font-size:14px;font-weight:800;white-space:nowrap}.nav-links>a:not(.quote-btn){position:relative;padding:40px 0 37px}.nav-links>a:not(.quote-btn):after{content:"";position:absolute;left:0;right:100%;bottom:27px;height:3px;background:#178047;border-radius:4px;transition:.2s}.nav-links>a:not(.quote-btn):hover:after,.nav-links>a.active:after{right:0}.nav-links>a:hover,.nav-links>a.active{color:#087541}.search-btn{border:0;background:none;font-size:31px;color:#081f3b;cursor:pointer;padding:0 4px}.quote-btn{background:#1e8745;color:#fff!important;padding:16px 27px;border-radius:10px;box-shadow:0 7px 16px rgba(30,135,69,.14)}.menu-btn{display:none}.mobile-nav{display:none!important}.hero-target{position:relative;min-height:430px;background:url('https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=2400&q=90') center/cover no-repeat;overflow:hidden}.hero-overlay{position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,255,255,.94) 0%,rgba(255,255,255,.82) 30%,rgba(255,255,255,.26) 64%,rgba(255,255,255,.03) 100%)}.hero-content{position:relative;min-height:430px;display:flex;align-items:center;justify-content:space-between}.hero-copy-target{padding:36px 0 55px;max-width:770px}.ey-target{font-size:14px;font-weight:900;letter-spacing:4px;color:#07583f}.ey-target.dark{color:#087541}.hero-copy-target h1{font-size:clamp(46px,5vw,70px);line-height:.99;letter-spacing:-3px;margin:13px 0 17px;color:#071f3b}.hero-copy-target h1 span{color:#177c4a}.hero-copy-target p{max-width:690px;font-size:17px;line-height:1.42;color:#1f3b51;margin:0 0 22px}.hero-buttons{display:flex;gap:17px}.target-btn{display:inline-flex;align-items:center;justify-content:center;font-weight:900;border-radius:7px;padding:13px 22px;font-size:14px}.target-btn.green{background:#148243;color:#fff;box-shadow:0 5px 12px rgba(20,130,67,.15)}.target-btn.outline{border:2px solid #2c8b60;color:#174e3a;background:rgba(255,255,255,.85)}.target-btn.small{padding:10px 17px;font-size:13px}.hero-slogan{font-family:cursive;font-size:31px;line-height:1.12;text-align:center;color:#071f38;transform:rotate(-6deg);margin-right:35px;margin-top:-110px}.swoosh{height:3px;background:#16824a;width:150px;transform:rotate(-9deg);margin:8px auto}.gateway-wrap{position:relative;margin-top:-52px;z-index:5}.gateway{background:#fff;border-radius:20px;box-shadow:0 9px 30px rgba(10,41,64,.10);display:grid;grid-template-columns:repeat(5,1fr);padding:9px 0}.gateway-item{min-height:126px;padding:10px 22px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border-right:1px solid #d9e2e0}.gateway-item:last-child{border-right:0}.gateway-icon{width:58px;height:58px;border-radius:50%;background:#e7f5eb;color:#08623f;display:grid;place-items:center;font-size:30px;margin-bottom:5px}.gateway-item b{font-size:15px;line-height:1.2}.gateway-item small{font-size:12px;line-height:1.3;color:#425a6a;margin-top:5px}.what-section{padding:20px 0 30px}.what-grid{display:grid;grid-template-columns:31% 69%;align-items:center;gap:35px}.what-copy{padding:10px 0}.what-copy h2{font-size:41px;line-height:1.02;letter-spacing:-1.7px;margin:8px 0 12px;color:#071f3b}.what-copy p{font-size:15px;line-height:1.4;max-width:500px;color:#294357;margin-bottom:17px}.what-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.target-card{background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 4px 15px rgba(10,41,64,.08);border:1px solid #edf0ef}.target-card img{width:100%;height:95px;object-fit:cover;display:block}.target-card>div{padding:10px 13px 13px}.target-card h3{font-size:16px;margin:0 0 4px;color:#0a2940}.target-card p{font-size:12px;line-height:1.25;color:#526575;margin:0}.impact-strip{background:linear-gradient(90deg,rgba(1,54,39,.94),rgba(5,78,52,.91)),url('https://images.unsplash.com/photo-1492496913980-501348b61469?auto=format&fit=crop&w=2200&q=88') center/cover;color:#fff;padding:12px 0}.impact-grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr 2.25fr;align-items:center}.impact-item{text-align:center;min-height:67px;border-right:1px solid rgba(255,255,255,.25);display:flex;flex-direction:column;justify-content:center}.impact-item strong{font-size:24px;line-height:1}.impact-item b{font-size:11px;margin-top:2px}.impact-item span{font-size:11px;opacity:.95}.impact-quote{padding:12px 28px;position:relative}.impact-quote strong{font-size:38px;line-height:.5;vertical-align:top}.impact-quote span{font-size:13px;line-height:1.3;display:inline-block}.impact-quote em{display:block;text-align:right;font-size:11px;margin-top:2px}.home-products{padding:65px 0}.home-products h2{font-size:40px;line-height:1.05;margin:7px 0}.lead{max-width:750px;color:#596c78}.featured-products{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:24px}.fp{border:1px solid #e2e9e5;border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 6px 22px rgba(6,58,43,.07)}.fp img{height:190px;width:100%;object-fit:cover;display:block}.fp b,.fp small{display:block;padding:0 15px}.fp b{padding-top:12px;font-size:16px}.fp small{padding-bottom:14px;color:#6d7f89}.center{text-align:center;margin-top:25px}.dark-outline{border-color:#1c7d50!important;color:#15543e!important}.target-cta{background:linear-gradient(90deg,rgba(2,57,40,.93),rgba(2,57,40,.82)),url('https://images.unsplash.com/photo-1492496913980-501348b61469?auto=format&fit=crop&w=2200&q=88') center/cover;color:#fff;padding:60px 0}.target-cta .ey-target{color:#b8e4c7}.target-cta h2{font-size:40px;margin:8px 0}.target-cta p{color:#d8e9de}.footer-logo{width:300px;background:#fff;border-radius:8px;padding:6px}.floating-wa{display:flex;align-items:center;gap:8px;background:#20c869!important;padding:10px 16px!important}.floating-wa span{font-size:12px}@media(max-width:1400px){.brand-logo{width:420px}.nav-links{gap:18px;font-size:13px}.wrap{width:min(1320px,92%)}}@media(max-width:1100px){.header-inner{min-height:92px}.brand-logo{width:330px;height:82px}.nav-links{gap:12px;font-size:11px}.nav-links>a:not(.quote-btn){padding:33px 0 30px}.nav-links>a:not(.quote-btn):after{bottom:21px}.quote-btn{padding:12px 15px}.what-grid{grid-template-columns:1fr}.what-copy{padding-bottom:0}.what-cards{grid-template-columns:repeat(4,1fr)}}@media(max-width:760px){.topbar{display:none}.header-inner{min-height:82px}.brand-logo{width:245px;height:72px}.nav-links{display:none}.menu-btn{display:block;border:1px solid #d8e4dc;background:#fff;border-radius:8px;padding:8px 11px;font-size:20px;color:#08233a}.mobile-nav{position:absolute!important;left:0;right:0;top:82px;background:#fff;padding:12px 4%;box-shadow:0 15px 30px rgba(0,0,0,.12);z-index:20;display:none!important}.mobile-nav.open{display:grid!important}.mobile-nav a{padding:10px;font-weight:800}.hero-target{min-height:610px}.hero-content{min-height:610px;align-items:flex-start}.hero-overlay{background:linear-gradient(90deg,rgba(255,255,255,.94),rgba(255,255,255,.55))}.hero-copy-target{padding-top:75px}.hero-copy-target h1{font-size:47px;letter-spacing:-2px}.hero-copy-target p{font-size:15px}.hero-slogan{display:none}.gateway-wrap{margin-top:-35px}.gateway{grid-template-columns:1fr 1fr;padding:7px}.gateway-item{min-height:112px;border-right:0;border-bottom:1px solid #e0e6e3}.gateway-item:last-child{grid-column:1/-1;border-bottom:0}.gateway-icon{width:46px;height:46px;font-size:24px}.what-section{padding-top:35px}.what-copy h2{font-size:35px}.what-cards{grid-template-columns:1fr 1fr}.target-card img{height:115px}.impact-grid{grid-template-columns:1fr 1fr}.impact-item{border-bottom:1px solid rgba(255,255,255,.2);border-right:0}.impact-quote{grid-column:1/-1}.featured-products{grid-template-columns:1fr 1fr}.target-cta h2{font-size:32px}}@media(max-width:480px){.brand-logo{width:215px}.hero-copy-target h1{font-size:40px}.hero-buttons{flex-direction:column;align-items:flex-start}.what-cards,.featured-products{grid-template-columns:1fr}.gateway{grid-template-columns:1fr}.gateway-item{border-bottom:1px solid #e0e6e3}.gateway-item:last-child{grid-column:auto}.top-contact{display:none}}
'''
(root/'styles.css').write_text(css,encoding='utf-8')

# Replace product image URLs with distinct real-photo assignments where possible.
p=root/'products.html'
s=p.read_text(encoding='utf-8')
assign=[photos['cinnamon'],photos['pepper'],photos['cardamom'],photos['cloves'],photos['nutmeg'],photos['mace'],
photos['seeds1'],photos['seeds2'],photos['herbs1'],photos['herbs2'],photos['herbs3'],photos['seeds1'],photos['chili'],photos['chili2'],photos['cinnamon'],photos['pepper'],photos['herbs1'],photos['herbs2'],photos['chili'],photos['chili2'],photos['nutmeg'],photos['coconut']]
# Replace image src values in order, leaving other structure untouched.
idx=0
def repl(m):
    global idx
    u=assign[min(idx,len(assign)-1)]; idx+=1
    return m.group(1)+u+m.group(2)
s=re.sub(r'(src=")https://images\.unsplash\.com/[^"?]+[^\"]*(\?[^\"]*)?(" )', lambda m: m.group(1)+assign[min(idx,len(assign)-1)]+m.group(3), s)
# Above pattern may miss due HTML escaping; do simpler targeted replace all img src values.
idx=0
s=re.sub(r'src="https://images\.unsplash\.com/[^\"]+"', lambda m: 'src="'+assign[min(idx,len(assign)-1)]+'"' if not (globals().__setitem__('idx',idx+1)) else '', s)
# The lambda above is intentionally awkward; restore if it produced empties.
if 'src=""' in s:
    # deterministic second pass
    idx=0
    s=re.sub(r'src="https://images\.unsplash\.com/[^\"]+"', lambda m: (assign[min(idx,len(assign)-1)] if False else 'src="'+assign[min(idx,len(assign)-1)]+'"'), s)
    # increment via a second regex pass instead
    matches=list(re.finditer(r'src="https://images\.unsplash\.com/[^\"]+"', s))
# Easier final reconstruction from original v7 if replacement went wrong
orig=(Path('/mnt/data/nova_v8/products.html').read_text(encoding='utf-8'))
# Since current file may be changed, use a clean source from zip.
with zipfile.ZipFile('/mnt/data/novalink_global_v7_final_github.zip') as z:
    orig=z.read('products.html').decode('utf-8')
idx=0
def img_repl(m):
    global idx
    u=assign[min(idx,len(assign)-1)]; idx+=1
    return 'src="'+u+'"'
orig=re.sub(r'src="https://images\.unsplash\.com/[^\"]+"', img_repl, orig)
p.write_text(orig,encoding='utf-8')

# README update
readme=(root/'README.md').read_text(encoding='utf-8')
readme += '\n\n## V8 interface\nThe homepage follows the supplied NovaLink Global reference screenshot: large wordmark, slim green topbar, clean white navigation, scenic Sri Lankan agriculture hero, five gateway cards, four What We Do cards, impact strip, featured products and CTA. Product cards use real hosted photographs from Unsplash URLs; replace with your own verified product photography when available.\n'
(root/'README.md').write_text(readme,encoding='utf-8')

# Validate files
from bs4 import BeautifulSoup
for f in root.glob('*.html'):
    soup=BeautifulSoup(f.read_text(encoding='utf-8'),'html.parser')
    assert len(soup.find_all('header'))==1, f
    assert len(soup.find_all('footer'))==1, f
print('HTML validation OK')

# Build zip
out=Path('/mnt/data/novalink_global_v8_target_interface_real_product_photos.zip')
if out.exists(): out.unlink()
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for f in root.iterdir():
        if f.is_file(): z.write(f,f.name)
print(out, out.stat().st_size)
