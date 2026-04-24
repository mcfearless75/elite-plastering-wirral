"""Generate area landing pages for Elite Plastering Wirral."""

import os

AREAS = [
    {
        "slug": "birkenhead",
        "name": "Birkenhead",
        "county": "Merseyside",
        "title": "Plasterer Birkenhead | Elite Plastering Wirral",
        "desc": "Expert plastering, joinery and damp course specialists in Birkenhead. 15+ years experience, fully insured. Free no-obligation quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in Birkenhead",
        "intro": "Birkenhead's mix of Victorian terraces, Edwardian semis and modern new-builds keeps our team busy year-round. Whether you need a full re-plaster on a period property, bespoke joinery for a town-centre flat, or damp course treatment on an older terrace — we know these properties inside out and deliver the finish they deserve.",
        "local": "We work across all of Birkenhead, from Oxton and Prenton to Rock Ferry and Tranmere. If you're renovating or just need a patch repair, give us a call.",
        "nearby": ["Wallasey", "Wirral", "Heswall"],
        "nearby_slugs": ["wallasey", "wirral", "heswall"],
        "lat": 53.3928, "lng": -3.0142,
    },
    {
        "slug": "wallasey",
        "name": "Wallasey",
        "county": "Merseyside",
        "title": "Plasterer Wallasey | Elite Plastering Wirral",
        "desc": "Professional plastering, joinery and damp proofing in Wallasey. Trusted local tradesmen with 15+ years experience. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in Wallasey",
        "intro": "Wallasey's coastal position means older properties here can suffer from penetrating damp and salt-laden air eroding external renders. Our team has extensive experience treating damp in Wallasey homes — diagnosing the cause properly rather than just masking it — and finishing with a plaster or render that actually lasts.",
        "local": "We cover New Brighton, Seacombe, Liscard, Poulton and all surrounding areas. Period properties are our speciality — we understand the quirks of older builds.",
        "nearby": ["Birkenhead", "Hoylake", "Meols"],
        "nearby_slugs": ["birkenhead", "hoylake", "meols"],
        "lat": 53.4161, "lng": -3.0564,
    },
    {
        "slug": "heswall",
        "name": "Heswall",
        "county": "Merseyside",
        "title": "Plasterer Heswall | Elite Plastering Wirral",
        "desc": "High-quality plastering, joinery and damp course in Heswall and the Dee Estuary villages. 15+ years experience. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in Heswall",
        "intro": "Heswall is home to some of Wirral's finest properties — detached homes, extensions and high-spec renovations where the quality of finish really matters. Our team takes pride in delivering work that's built to last and looks the part. From smooth skim finishes to bespoke fitted joinery, we match the standard the area demands.",
        "local": "We work throughout Heswall, Thurstaston, Gayton and Barnston. Whether it's a full renovation or a single room re-plaster, we'll give you an honest quote and a quality result.",
        "nearby": ["West Kirby", "Wirral", "Chester"],
        "nearby_slugs": ["west-kirby", "wirral", "chester"],
        "lat": 53.3278, "lng": -3.1017,
    },
    {
        "slug": "west-kirby",
        "name": "West Kirby",
        "county": "Merseyside",
        "title": "Plasterer West Kirby | Elite Plastering Wirral",
        "desc": "Trusted plastering, joinery and damp proofing in West Kirby. Serving the Dee Estuary coast for 15+ years. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in West Kirby",
        "intro": "West Kirby's blend of seafront properties, family homes and recent new-builds means we're regularly called out for everything from extension plastering and damp course treatment on older houses, to media walls and bespoke joinery in contemporary interiors. Whatever the job, we treat every property with care and deliver a finish that stands up to scrutiny.",
        "local": "We cover West Kirby, Caldy, Grange and Frankby. As a local Wirral company, we're never far away and always contactable.",
        "nearby": ["Hoylake", "Heswall", "Meols"],
        "nearby_slugs": ["hoylake", "heswall", "meols"],
        "lat": 53.3703, "lng": -3.1853,
    },
    {
        "slug": "hoylake",
        "name": "Hoylake",
        "county": "Merseyside",
        "title": "Plasterer Hoylake | Elite Plastering Wirral",
        "desc": "Plastering, joinery and damp course specialists in Hoylake. 15+ years experience on the Wirral coast. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in Hoylake",
        "intro": "Hoylake's position on the North Wirral coast makes damp a recurring issue for many homeowners here — particularly in older Victorian and Edwardian properties. We've been treating damp in Hoylake homes for years and know exactly what's needed. We also carry out full re-plasters, extensions, bespoke joinery and media wall builds throughout the town.",
        "local": "We work across Hoylake, Meols and the surrounding coast. Fast response, free survey, honest quote.",
        "nearby": ["West Kirby", "Wallasey", "Meols"],
        "nearby_slugs": ["west-kirby", "wallasey", "meols"],
        "lat": 53.3931, "lng": -3.1775,
    },
    {
        "slug": "meols",
        "name": "Meols",
        "county": "Merseyside",
        "title": "Plasterer Meols | Elite Plastering Wirral",
        "desc": "Local plastering, joinery and damp proofing in Meols. Wirral-based tradesmen with 15+ years experience. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in Meols",
        "intro": "Meols is a quiet coastal village but its older housing stock regularly needs the kind of careful, considered trades work that only experience can deliver. We work on everything from patch plastering after damp treatment to full room re-plasters and fitted joinery projects — always leaving the property clean and tidy.",
        "local": "Meols sits between Hoylake and West Kirby — two areas we cover constantly. We're always local, always reachable.",
        "nearby": ["Hoylake", "West Kirby", "Wallasey"],
        "nearby_slugs": ["hoylake", "west-kirby", "wallasey"],
        "lat": 53.3999, "lng": -3.1567,
    },
    {
        "slug": "chester",
        "name": "Chester",
        "county": "Cheshire",
        "title": "Plasterer Chester | Elite Plastering Wirral",
        "desc": "Professional plastering, joinery and damp course in Chester. 15+ years experience on heritage and modern properties. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery in Chester",
        "intro": "Chester's rich architectural heritage — from Georgian townhouses to Victorian villas and modern city-centre apartments — demands tradesmen who understand different construction methods and materials. Our team works across Chester regularly, delivering plaster finishes, damp course treatments and bespoke joinery on properties of all ages and types.",
        "local": "We cover Chester city and surrounding villages. Heritage plasterwork, lime render, modern skim — we handle it all with the same high standard.",
        "nearby": ["Wirral", "Heswall", "Birkenhead"],
        "nearby_slugs": ["wirral", "heswall", "birkenhead"],
        "lat": 53.1905, "lng": -2.8927,
    },
    {
        "slug": "wirral",
        "name": "Wirral",
        "county": "Merseyside",
        "title": "Plasterer Wirral | Elite Plastering Wirral — Local Specialists",
        "desc": "Wirral's trusted plastering, joinery and damp course specialists. 15+ years covering the whole Peninsula. Free quotes — call 07508 474298.",
        "h1": "Plastering & Joinery Across the Wirral Peninsula",
        "intro": "We're a Wirral-based trades team covering the entire peninsula and beyond. From Birkenhead and Wallasey in the north to Heswall and the Dee Estuary coast in the south — wherever you are on Wirral, we're not far away. Our team of experienced plasterers, joiners and damp course specialists bring the same high standard to every job, every time.",
        "local": "Wirral is our home patch. We've worked in hundreds of homes across the peninsula over the past 15+ years, from quick patch repairs to full-scale renovations.",
        "nearby": ["Birkenhead", "Heswall", "Chester"],
        "nearby_slugs": ["birkenhead", "heswall", "chester"],
        "lat": 53.3686, "lng": -3.0834,
    },
]

STAR_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
CHECK_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
PIN_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'


def page(area):
    nearby_links = " &bull; ".join(
        f'<a href="{s}.html">{n}</a>'
        for n, s in zip(area["nearby"], area["nearby_slugs"])
    )

    schema = {
        "context": "https://schema.org",
        "type": "HomeAndConstructionBusiness",
        "name": "Elite Plastering Wirral",
        "description": area["desc"],
        "url": f"https://www.eliteplasteringwirral.com/areas/{area['slug']}.html",
        "telephone": "+447508474298",
        "email": "info@hillplasteringandjoinery.co.uk",
        "areaServed": area["name"],
        "address": {
            "type": "PostalAddress",
            "addressLocality": area["name"],
            "addressRegion": area["county"],
            "addressCountry": "GB"
        },
        "geo": {"type": "GeoCoordinates", "latitude": area["lat"], "longitude": area["lng"]},
    }

    import json
    schema_str = json.dumps(schema, indent=4).replace('"type"', '"@type"').replace('"context"', '"@context"')

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{area["title"]}</title>
  <meta name="description" content="{area["desc"]}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.eliteplasteringwirral.com/areas/{area["slug"]}.html" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{area["title"]}" />
  <meta property="og:description" content="{area["desc"]}" />
  <meta property="og:url" content="https://www.eliteplasteringwirral.com/areas/{area["slug"]}.html" />
  <meta property="og:site_name" content="Elite Plastering Wirral" />

  <script type="application/ld+json">
  {schema_str}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="../css/style.css" />
  <link rel="stylesheet" href="../css/area.css" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%230F172A'/><text x='16' y='22' text-anchor='middle' font-size='18' font-weight='900' fill='%23F59E0B' font-family='sans-serif'>E</text></svg>" />
</head>

<body>

  <!-- Navigation -->
  <header>
    <nav class="nav" role="navigation" aria-label="Main navigation">
      <div class="nav-inner">
        <a href="../index.html" class="nav-logo" aria-label="Elite Plastering Wirral — home">
          <img src="https://static.wixstatic.com/media/83a797_c8249e8d40c14e8da410e8919b6bafe1~mv2.png" alt="Elite Plastering Wirral logo" class="nav-logo-img" width="40" height="36" loading="eager" />
          <div>
            <span class="nav-logo-name">Elite Plastering Wirral</span>
            <span class="nav-logo-sub">Joinery &amp; Damp Course</span>
          </div>
        </a>
        <ul class="nav-links" id="nav-links">
          <li><a href="../index.html#services">Services</a></li>
          <li><a href="../index.html#portfolio">Work</a></li>
          <li><a href="../index.html#testimonials">Reviews</a></li>
          <li><a href="../index.html#areas">Areas</a></li>
          <li><a href="../index.html#contact" class="nav-cta">Free Quote</a></li>
        </ul>
        <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
  </header>

  <main>

    <!-- Breadcrumb -->
    <div class="breadcrumb-bar">
      <div class="container">
        <nav aria-label="Breadcrumb">
          <ol class="breadcrumb">
            <li><a href="../index.html">Home</a></li>
            <li aria-current="page">{area["name"]}</li>
          </ol>
        </nav>
      </div>
    </div>

    <!-- Area Hero -->
    <section class="area-hero">
      <div class="area-hero-bg"></div>
      <div class="container">
        <div class="area-hero-content">
          <div class="hero-tag">
            <span class="dot"></span>
            Serving {area["name"]}, {area["county"]}
          </div>
          <h1>{area["h1"]}</h1>
          <p class="hero-sub">{area["intro"]}</p>
          <div class="hero-actions">
            <a href="../index.html#contact" class="btn-primary">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.42 2 2 0 0 1 3.6 1.28h3a2 2 0 0 1 2 1.72c.13 1 .36 1.98.7 2.91a2 2 0 0 1-.45 2.11L7.91 9c1.04 1.82 2.48 3.41 4.18 4.61l.97-.97a2 2 0 0 1 2.11-.45c.93.34 1.91.57 2.91.7a2 2 0 0 1 1.72 2.03z"/></svg>
              Get a Free Quote
            </a>
            <a href="tel:07508474298" class="btn-outline">07508 474298</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Services in area -->
    <section class="section services" aria-labelledby="services-h">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Services in {area["name"]}</span>
          <h2 id="services-h">What We Do in {area["name"]}</h2>
          <p>{area["local"]}</p>
        </div>

        <div class="area-services-grid">

          <div class="area-service reveal d1">
            <div class="area-service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            </div>
            <h3>Plastering in {area["name"]}</h3>
            <p>Full re-plasters, skimming, rendering, patch repairs and Artex removal. Any size job — same high standard every time.</p>
            <ul class="service-features">
              <li class="service-feature">{CHECK_SVG} Skimming &amp; full re-plaster</li>
              <li class="service-feature">{CHECK_SVG} Exterior rendering</li>
              <li class="service-feature">{CHECK_SVG} Patch repairs &amp; crack filling</li>
              <li class="service-feature">{CHECK_SVG} Artex removal &amp; boarding</li>
            </ul>
          </div>

          <div class="area-service reveal d2">
            <div class="area-service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <h3>Joinery in {area["name"]}</h3>
            <p>Bespoke cabinets, fitted wardrobes, media walls and custom furniture — all designed and built to your exact specification.</p>
            <ul class="service-features">
              <li class="service-feature">{CHECK_SVG} Custom cabinets &amp; wardrobes</li>
              <li class="service-feature">{CHECK_SVG} Media walls</li>
              <li class="service-feature">{CHECK_SVG} Bookshelves &amp; shelving</li>
              <li class="service-feature">{CHECK_SVG} Door frames &amp; skirting</li>
            </ul>
          </div>

          <div class="area-service reveal d3">
            <div class="area-service-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
            </div>
            <h3>Damp Course in {area["name"]}</h3>
            <p>15+ years treating damp in {area["county"]} properties. We find the root cause — not just mask it — and apply a lasting fix.</p>
            <ul class="service-features">
              <li class="service-feature">{CHECK_SVG} Rising damp treatment</li>
              <li class="service-feature">{CHECK_SVG} Penetrating damp surveys</li>
              <li class="service-feature">{CHECK_SVG} Waterproofing &amp; tanking</li>
              <li class="service-feature">{CHECK_SVG} Condensation control</li>
            </ul>
          </div>

        </div>
      </div>
    </section>

    <!-- Trust signals -->
    <section class="section why-us" aria-label="Why choose us">
      <div class="container">
        <div class="section-header centered reveal">
          <span class="section-tag">Why Choose Us</span>
          <h2>Why {area["name"]} Homeowners Choose Elite</h2>
        </div>
        <div class="area-trust-grid">
          <div class="area-trust reveal d1">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <h4>Fully Insured</h4>
            <p>Full public liability on every job.</p>
          </div>
          <div class="area-trust reveal d2">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <h4>15+ Years Experience</h4>
            <p>Hundreds of {area["name"]} jobs completed.</p>
          </div>
          <div class="area-trust reveal d3">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>
            <h4>Free Quotes</h4>
            <p>No-obligation quote for every job.</p>
          </div>
          <div class="area-trust reveal d4">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            <h4>24/7 Available</h4>
            <p>Always contactable — day or night.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="section testimonials" aria-labelledby="reviews-h">
      <div class="container">
        <div class="section-header centered reveal">
          <span class="section-tag">Reviews</span>
          <h2 id="reviews-h">What Customers Say</h2>
        </div>
        <div class="area-reviews-grid">
          <article class="testimonial-card reveal d1">
            <div class="testimonial-quote">"</div>
            <div class="testimonial-stars" aria-label="5 stars">{STAR_SVG * 5}</div>
            <blockquote class="testimonial-text">Kev and Dave did a joinery job for us and they exceeded my expectations. Friendly, knowledgeable, and delivered exactly what I wanted. Clean, professional — highly recommend.</blockquote>
            <footer class="testimonial-author">
              <div class="testimonial-avatar">ST</div>
              <div><p class="testimonial-name">Sarah T.</p><p class="testimonial-location">Wirral</p></div>
            </footer>
          </article>
          <article class="testimonial-card reveal d2">
            <div class="testimonial-quote">"</div>
            <div class="testimonial-stars" aria-label="5 stars">{STAR_SVG * 5}</div>
            <blockquote class="testimonial-text">We used Kev, Lee and the team for a plastering job and I couldn't be happier. Professional, efficient, and an excellent finish. Would highly recommend to anyone.</blockquote>
            <footer class="testimonial-author">
              <div class="testimonial-avatar">JD</div>
              <div><p class="testimonial-name">John D.</p><p class="testimonial-location">Wirral</p></div>
            </footer>
          </article>
        </div>
      </div>
    </section>

    <!-- Nearby areas -->
    <section class="section areas" aria-labelledby="nearby-h">
      <div class="container">
        <div class="section-header centered reveal">
          <span class="section-tag">Also Covering</span>
          <h2 id="nearby-h">Nearby Areas We Serve</h2>
          <p>We cover {area["name"]} and all surrounding areas. Click to see our service pages for nearby locations.</p>
        </div>
        <div class="areas-chips reveal">
          {chr(10).join(f'<a href="{s}.html" class="area-chip">{PIN_SVG} {n}</a>' for n, s in zip(area["nearby"], area["nearby_slugs"]))}
          <a href="../index.html#areas" class="area-chip">{PIN_SVG} All Areas</a>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="area-cta-section">
      <div class="container">
        <div class="area-cta-box reveal">
          <h2>Need a Plasterer in {area["name"]}?</h2>
          <p>Call us now for a free, no-obligation quote. We'll come out, assess the job, and give you a straight answer.</p>
          <div class="hero-actions" style="justify-content:center;">
            <a href="../index.html#contact" class="btn-primary">Get a Free Quote</a>
            <a href="tel:07508474298" class="btn-outline">Call 07508 474298</a>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-logo-name" style="font-size:1.1rem;">Elite Plastering Wirral</div>
          <span class="nav-logo-sub">Joinery &amp; Damp Course</span>
          <p>Wirral's trusted plastering, joinery and damp course specialists. Quality workmanship on every job.</p>
        </div>
        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="../index.html#services">Plastering</a></li>
            <li><a href="../index.html#services">Joinery</a></li>
            <li><a href="../index.html#services">Damp Course</a></li>
            <li><a href="../index.html#services">Media Walls</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Areas</h5>
          <ul>
            {chr(10).join(f'            <li><a href="{s}.html">{n}</a></li>' for n, s in zip(area["nearby"], area["nearby_slugs"]))}
            <li><a href="../index.html#areas">All Areas</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; <span class="year"></span> Elite Plastering Wirral. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="../index.html">Home</a>
          <a href="../index.html#contact">Contact</a>
        </div>
      </div>
    </div>
  </footer>

  <button class="back-to-top" id="back-to-top" aria-label="Back to top">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"/></svg>
  </button>

  <script src="../js/main.js"></script>
  <script>document.querySelectorAll('.year').forEach(e => e.textContent = new Date().getFullYear());</script>
</body>
</html>"""


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "..", "areas")
    os.makedirs(out_dir, exist_ok=True)
    for area in AREAS:
        path = os.path.join(out_dir, f"{area['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(area))
        print(f"  OK {area['slug']}.html")
    print(f"\nGenerated {len(AREAS)} area pages in /areas/")


if __name__ == "__main__":
    main()
