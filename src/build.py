import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from common import head,nav,contact
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')

index=head('Tully Njoroge','Tully Njoroge: MBA in Finance and Entrepreneurship, focused on management consulting, data analytics and venture capital.')+nav()+'''
<main>
<section class="hero" aria-label="Introduction">
  <canvas data-field aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="eyebrow rv">Consulting · Data analytics · Venture capital</div>
    <h1 class="display split"><span>Tully</span> <span>Njoroge</span></h1>
    <p class="lede rv d1">MBA in Finance and Entrepreneurship. I like hard problems, the people behind them, and turning both into something that works.</p>
    <div class="btns rv d2"><a class="btn solid" href="#work">See the work <span class="arr">→</span></a><a class="btn" href="https://www.linkedin.com/in/tully-njoroge" rel="noopener">LinkedIn <span class="arr">→</span></a></div>
    <div class="hero-foot rv d3"><span class="eyebrow">Based in Florida · From Johannesburg</span><div class="scrollcue"><i></i>Scroll</div></div>
  </div>
</section>

<section class="section" id="work"><div class="wrap">
  <div class="sec-head"><h2 class="display split">The work</h2><p class="rv">Three areas, one project each so far. Pick a window.</p></div>
  <div class="windows">
    <a class="win rv" href="helix-logistics.html">
      <div class="win-media"><img src="helix-console.jpg" alt="Helix Ops flight operations console over a map of western Kentucky" loading="lazy"></div>
      <div class="win-body"><span class="code aero">Ventures · Strategy</span><h3 class="display">Helix Logistics</h3><p>A drone-delivery startup built from NASA technology, with a flight simulator you can fly and try to break.</p><span class="more">Explore <span class="arr">→</span></span></div>
    </a>
    <a class="win rv d1" href="global-portfolios.html">
      <div class="win-media fin-art" aria-hidden="true">
        <svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice">
          <g stroke="rgba(238,241,246,.08)"><line x1="0" x2="400" y1="60" y2="60"/><line x1="0" x2="400" y1="120" y2="120"/><line x1="0" x2="400" y1="180" y2="180"/><line x1="0" x2="400" y1="240" y2="240"/></g>
          <polyline class="draw" points="20,230 70,214 110,222 150,188 190,196 230,160 270,150 310,118 350,96 384,70" fill="none" stroke="#e0a24e" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
          <g class="bars"><rect x="40" y="200" width="18" height="40" rx="3" fill="#5b8cff"/><rect x="100" y="186" width="18" height="54" rx="3" fill="#5b8cff"/><rect x="160" y="160" width="18" height="80" rx="3" fill="#5b8cff"/><rect x="220" y="150" width="18" height="90" rx="3" fill="#5b8cff"/><rect x="280" y="120" width="18" height="120" rx="3" fill="#5b8cff"/><rect x="340" y="92" width="18" height="148" rx="3" fill="#5b8cff"/></g>
          <circle cx="384" cy="70" r="6" fill="#eef1f6" stroke="#0b0e14" stroke-width="2"/>
          <text x="20" y="40" font-family="IBM Plex Mono, ui-monospace, monospace" font-size="13" fill="#8d95a6">AEP · BUY · $159.42</text>
        </svg>
      </div>
      <div class="win-body"><span class="code fin">Finance · Equity research</span><h3 class="display">Crummer Truist Portfolio</h3><p>The utilities call and two BUY cases I made for a student fund that invests real money.</p><span class="more">Explore <span class="arr">→</span></span></div>
    </a>
    <a class="win rv d2" href="h1b-employer-research.html">
      <div class="win-media data-art" aria-hidden="true"><canvas data-dots></canvas></div>
      <div class="win-body"><span class="code data">Data analytics · In progress</span><h3 class="display">H-1B Employer Research</h3><p>Mapping employers and job markets so a search starts with evidence, not guesswork.</p><span class="more">Explore <span class="arr">→</span></span></div>
    </a>
  </div>
</div></section>

<section class="section" id="about" style="border-top:1px solid var(--line)"><div class="wrap about">
  <figure class="portrait rv" style="margin:0"><img src="headshot.jpg" alt="Tully Njoroge in a grey suit and light blue tie on the Rollins College campus" width="800" height="1000"><figcaption>Rollins College · Winter Park, FL</figcaption></figure>
  <div>
    <div class="eyebrow rv">About</div>
    <h2 class="display split" style="margin-top:14px">Hi, I'm Tully.</h2>
    <div class="bio rv">
      <p>I like solving problems, including the ones where I'm not the expert in the room yet. I studied psychology and sociology, so I tend to start with the people: how they make decisions, what they actually need, and why the obvious fix sometimes doesn't stick.</p>
      <p>From there I work toward a solution that holds up for the business and for the person on the other side of it. Learning a new field along the way is part of the fun. That's how an MBA student ended up planning drone logistics with NASA.</p>
    </div>
    <dl class="facts rv">
      <div><dt>From</dt><dd>Johannesburg, South Africa</dd></div>
      <div><dt>Currently</dt><dd>Management Program Trainee, General Parts &amp; Machinery</dd></div>
      <div><dt>MBA · 2026</dt><dd>Finance &amp; Entrepreneurship, Crummer Graduate School of Business, Rollins College · GPA 3.8</dd></div>
      <div><dt>BA · 2024</dt><dd>Psychology &amp; Sociology, Rollins College · GPA 3.6</dd></div>
      <div><dt>Certification</dt><dd>CFA Level I candidate</dd></div>
      <div><dt>Looking at</dt><dd>Management consulting · Data analytics · Venture capital</dd></div>
    </dl>
    <div class="btns rv" style="margin-top:22px"><a class="btn" href="extracurriculars.html">Extracurriculars <span class="arr">→</span></a></div>
  </div>
</div></section>
</main>
'''+contact()
open(os.path.join(OUT,'index.html'),'w').write(index)

# ---------------- Helix case study ----------------
helix=head('Helix Logistics','Helix Logistics: autonomous middle-mile delivery of orthopedic implants. MBA capstone with NASA Kennedy Space Center technology transfer.')+nav('helix')+'''
<main>
<section class="cs-hero"><canvas data-field aria-hidden="true"></canvas><div class="wrap">
  <a class="crumb" href="index.html#work">← All work</a>
  <div style="margin-top:28px;display:flex;align-items:center;gap:16px"><img src="helix-logo.png" alt="Helix Logistics logo" width="64" style="width:64px"><span class="code aero">Aerospace · MBA capstone</span></div>
  <h1 class="display split">Helix Logistics</h1>
  <p class="lede rv">Safe skies. Critical deliveries. Autonomous infrastructure for when failure isn't an option.</p>
  <div class="factbar rv d1" data-count-wrap>
    <div><b data-count="7" data-suf=" months">7 months</b><span>Capstone with NASA Kennedy Space Center technology transfer, concluded March 2026</span></div>
    <div><b data-count="1000" data-suf="+">1,000+</b><span>NASA patents screened for commercial fit</span></div>
    <div><b data-count="12">12</b><span>Autonomous-flight technologies shortlisted</span></div>
    <div><b>85 min</b><span>Louisville to Paducah by air, vs 3 h 25 m by ground courier</span></div>
  </div>
  <a class="demo-frame rv" href="simulator.html"><img src="helix-console.jpg" alt="Helix Ops flight operations console" loading="lazy"><span class="btn solid play">Launch simulator <span class="arr">→</span></span></a>
</div></section>

<div class="wrap">
<section class="block" id="problem"><header><span class="code aero">01 · Problem</span><h2 class="display">The problem</h2></header><div class="prose rv">
  <p>Orthopedic surgery runs on implant sets shipped to the hospital for each case: the right sizes, the right instruments, on the morning of surgery. Outside major metros those sets travel long distances by ground courier from regional distribution centers.</p>
  <p>In customer discovery, orthopedic surgeons told us they had cancelled surgeries because a set did not arrive on time. The cause was logistics, not the patient's condition. Device distributors confirmed the other side of it: every missed delivery cascades into rescheduled operating rooms, expedited shipping and strained hospital relationships.</p>
  <p class="muted">Rural and semi-rural hospitals feel this most. They sit far from distribution centers, keep thin backup inventory, and depend on a single road route that weather and traffic can close.</p>
</div></section>

<section class="block" id="solution"><header><span class="code aero">02 · Solution</span><h2 class="display">The solution</h2></header><div class="prose">
  <p class="rv">Helix is an autonomous middle-mile network: hybrid-electric VTOL cargo aircraft that fly implant sets from a distribution hub straight to a hospital pad, around the clock and in most weather. What makes it viable is the software layer. Flying safely beyond line of sight, over people, in shared airspace needs the kind of safety-critical autonomy NASA has spent decades developing.</p>
  <p class="rv">We screened NASA's technology-transfer catalog and built the concept around seven capability areas:</p>
  <div class="grid-cards rv">
    <div><i>AIRSPACE</i><b>UAS traffic management</b><span>Share flight intent, predict conflicts minutes ahead and resolve them automatically.</span></div>
    <div><i>HEALTH</i><b>Fault detection &amp; isolation</b><span>Catch failing motors and power systems early by comparing them to a model, then isolate the faulty unit.</span></div>
    <div><i>ASSURANCE</i><b>Near-real-time V&amp;V</b><span>Runtime monitors that confirm the autonomy is still inside its verified envelope.</span></div>
    <div><i>DATA</i><b>Universal data compiler</b><span>Fuse aircraft, sensor and network data into one stream with failover.</span></div>
    <div><i>WEATHER</i><b>Wind estimation</b><span>Infer wind from the aircraft's own motion and re-plan speed, altitude and ETA.</span></div>
    <div><i>CONTINGENCY</i><b>Emergency landing</b><span>Rank reachable landing sites by population exposure and terrain.</span></div>
    <div><i>LANDING</i><b>Vision-based landing</b><span>Land precisely on a pad when GPS is degraded or visibility is poor.</span></div>
  </div>
  <p class="note rv">These technologies were evaluated from NASA's public technology-transfer catalog as part of the capstone. No licenses were obtained.</p>
</div></section>

<section class="block" id="market"><header><span class="code aero">03 · Market</span><h2 class="display">Market &amp; model</h2></header><div class="prose">
  <p class="rv"><strong>Beachhead: Paducah, Kentucky.</strong> A regional medical hub roughly 200 road miles from the nearest major distribution center in Louisville, with active orthopedic practices and a single highway corridor. Its profile of long distance, real surgical volume and thin backup inventory repeats across the rural Southeast.</p>
  <p class="rv"><strong>Market sizing.</strong> Counting only hospitals and ambulatory surgery centers in our six focus states gives about 3,660 procedural sites. A 300-mile radius around six to eight micro-fulfillment hubs reaches most of them. Our 24-month target was 10–30 anchor accounts (health systems and surgery-center chains), which translates into 100–400 facilities.</p>
  <div class="two rv">
    <div><div class="eyebrow">Phase 1</div><h3 class="display" style="font-size:26px;margin:8px 0">Software licensing</h3><p class="muted">License the autonomy and airspace stack to drone operators, utilities and defense contractors. Early revenue that proves the technology without the capital cost of a fleet.</p></div>
    <div><div class="eyebrow">Phase 2</div><h3 class="display" style="font-size:26px;margin:8px 0">Turnkey delivery</h3><p class="muted">Operate delivery for orthopedic distributors and hospitals on a monthly subscription, starting in Paducah and scaling to a hub network across the Southeast and Texas.</p></div>
  </div>
  <div class="tablewrap rv"><table class="tbl"><tr><th>Delivery plan</th><th>Monthly price</th><th>Deliveries included</th></tr><tr><td>Core</td><td>$69,999</td><td>up to 450</td></tr><tr><td>Growth</td><td>$89,999</td><td>up to 600</td></tr><tr><td>Network</td><td>$109,999</td><td>up to 750</td></tr></table></div>
  <p class="muted rv">Funding path: SBIR/STTR grants for the licensing and engineering work, then a seed round. The pitch closed on an ask of $150K for 20% plus technical hires.</p>
</div></section>

<section class="block" id="prototype"><header><span class="code aero">04 · Prototype</span><h2 class="display">The prototype</h2></header><div class="prose">
  <p class="rv">The original capstone demo was a Python dashboard with four live panels (powertrain health, UAS traffic, validation deviation and unified telemetry) and a basic drone control panel, simulating small drones over Orlando.</p>
  <p class="rv">This rebuild is the console that dashboard was pointing toward, set in the beachhead market:</p>
  <ul class="clean rv">
    <li>A fleet of Chaparral-class hybrid VTOL aircraft (8 lift and 4 cruise propellers, 300–500 lb payload, about 300 miles of range) flying Louisville → Paducah and to five other western Kentucky hospitals.</li>
    <li>Two consoles in one: a <strong>dispatcher</strong> view for orders, fleet and mission status, and a <strong>flight ops</strong> view for one aircraft's health, navigation, telemetry, wind and traffic.</li>
    <li>Nine injectable events (intruder aircraft, pop-up flight restriction, gust front, motor wear, lift-motor failure, generator failure, GPS drift, link loss, fog). Some ask the operator for a decision.</li>
    <li>A four-minute guided demo that walks through a full delivery with every system tested along the way.</li>
  </ul>
  <p class="note rv">Aircraft performance beyond the manufacturer's published payload and range is a modeling assumption. Geography is simplified; facilities, registrations and traffic are fictional. Not affiliated with or endorsed by NASA or Elroy Air.</p>
  <div class="btns rv"><a class="btn solid" href="simulator.html">Launch simulator <span class="arr">→</span></a></div>
</div></section>

<section class="block" id="team" style="border-bottom:0"><header><span class="code aero">05 · Team</span><h2 class="display">Team</h2></header><div class="prose rv">
  <div class="team"><span>Tully Njoroge · Co-founder &amp; project lead, business development</span><span>Quinn Mäensivu · Sales</span><span>Abby DeGroat</span><span>Tim Cook</span><span>Max Farrell</span><span>Jack Johnstone</span><span>Amelia Kondal</span></div>
  <p class="muted">Faculty mentor: Peter McAlindon. Crummer Graduate School of Business, Rollins College, in partnership with NASA Kennedy Space Center technology transfer.</p>
</div></section>
</div>
</main>
'''+contact()
open(os.path.join(OUT,'helix-logistics.html'),'w').write(helix)
print('ok')

# ---------------- Finance ----------------
import json
SECT=[('Communication Services',10.60,10.61),('Consumer Discretionary',9.10,9.96),('Consumer Staples',6.40,5.26),('Energy',4.10,3.50),('Financials',11.40,12.33),('Health Care',9.50,9.54),('Industrials',8.90,8.98),('Information Technology',33.00,33.37),('Materials',2.02,2.02),('Real Estate',1.98,1.97),('Utilities',3.00,2.46)]
TILT={'Communication Services':0,'Consumer Discretionary':-9,'Consumer Staples':22,'Energy':17,'Financials':-8,'Health Care':0,'Industrials':-1,'Information Technology':-1,'Materials':0,'Real Estate':1,'Utilities':22}
sect_rows=[{'k':k,'v':TILT[k],'tip':f'Portfolio {p:.2f}% · S&amp;P 500 {s:.2f}%<br>Tilt {TILT[k]:+d}% (proportional)'} for k,p,s in SECT]
ESG=[('Communication Services',38.47,36.38,-5),('Consumer Discretionary',20.04,25.41,27),('Consumer Staples',25.48,24.34,-4),('Energy',29.85,36.13,21),('Financials',35.16,41.52,18),('Health Care',43.68,46.12,6),('Industrials',30.14,25.59,-15),('Information Technology',19.64,19.47,-1),('Materials',27.57,26.87,-3),('Real Estate',39.66,67.94,71),('Utilities',13.58,21.61,59),('Overall equity portfolio',27.90,29.56,6)]
esg_rows=[{'k':k,'v':t,'tip':f'Fund {c:.2f} · S&amp;P 500 {s:.2f}<br>Relative tilt {t:+d}%'} for k,s,c,t in ESG]
FF=[{'k':'AEP','name':'American Electric Power','base':159.42,'lo':138,'hi':166,'price':131.92,'up':'≈21%'},{'k':'NFG','name':'National Fuel Gas','base':104.83,'lo':95,'hi':115,'price':92.92,'up':'≈13%'}]
j=lambda o:json.dumps(o).replace('"','&quot;')
sect_tbl=''.join(f'<tr><td>{k}</td><td>{p:.2f}%</td><td>{s:.2f}%</td><td>{TILT[k]:+d}%</td></tr>' for k,p,s in SECT)
esg_tbl=''.join(f'<tr><td>{k}</td><td>{s:.2f}</td><td>{c:.2f}</td><td>{t:+d}%</td></tr>' for k,s,c,t in ESG)

fin=head('Crummer Truist Portfolio','Utilities sector research for the 2026 Crummer Truist Portfolio: an overweight call and BUY cases for AEP and NFG.')+nav('fin')+f'''
<main>
<section class="cs-hero"><div class="wrap">
  <a class="crumb" href="index.html#work">← All work</a>
  <div style="margin-top:28px"><span class="code fin">Finance · Equity research · 2026</span></div>
  <h1 class="display split">Crummer Truist Portfolio</h1>
  <p class="lede rv">I was the Utilities sector analyst for the 2026 Crummer Truist Portfolio, a student-managed fund endowed by SunTrust (now Truist) that invests real money to pay for scholarships. I set the fund's utilities weight and built the BUY cases for American Electric Power and National Fuel Gas.</p>
  <div class="factbar rv d1" data-count-wrap>
    <div><b data-count="3" data-dec="2" data-suf="%">3.00%</b><span>Utilities weight, vs 2.46% in the S&amp;P 500</span></div>
    <div><b data-count="21" data-pre="+" data-suf="%">+21%</b><span>AEP upside to $159.42 base-case value</span></div>
    <div><b data-count="13" data-pre="+" data-suf="%">+13%</b><span>NFG upside to $104.83 base-case value</span></div>
    <div><b data-count="54000" data-pre="$">$54,000</b><span>Scholarships the portfolio funded this year</span></div>
  </div>
</div></section>

<div class="wrap">
<section class="block"><header><span class="code fin">01 · The fund</span><h2 class="display">How the fund works</h2></header><div class="prose">
  <p class="rv">An 11-person MBA team runs the portfolio under an Investment Policy Statement. It trades once a year, in early April, so every position has to hold up for twelve months without adjustment. This year's team set a late-cycle economic outlook, held 20% in bonds (the top of the allowed range) and tilted equities toward defensive sectors.</p>
  <p class="rv">Each of the eleven S&amp;P sectors gets a sector ETF for passive exposure plus two individual stocks chosen to beat it. Every pick had to be undervalued on rigorous analysis, with AI and ESG as tie-breaking themes rather than goals.</p>
  <div class="chart rv"><h4>Sector tilts vs the S&amp;P 500</h4><p class="sub">Proportional tilt, (portfolio − index) ÷ index. Within ±1% counts as neutral. Hover a sector for the weights.</p>
    <div class="legend"><span><i style="background:#5b8cff"></i>Overweight</span><span><i style="background:#c47a22"></i>Underweight</span><span><i style="background:#4a5160"></i>Neutral</span></div>
    <div data-chart="diverging" data-highlight="Utilities" data-label="Sector tilts versus the S&amp;P 500" data-rows="{j(sect_rows)}"></div>
    <details class="table-view"><summary>Show as table</summary><div class="tablewrap"><table class="tbl"><tr><th>Sector</th><th>Portfolio</th><th>S&amp;P 500</th><th>Tilt</th></tr>{sect_tbl}</table></div></details>
  </div>
</div></section>

<section class="block"><header><span class="code fin">02 · Sector call</span><h2 class="display">Overweight utilities</h2></header><div class="prose">
  <p class="rv"><strong>Demand is reaccelerating.</strong> After two decades of flat electricity demand, the EIA projects consumption growth of 1% in 2026 and 3% in 2027, the strongest four-year stretch since 2000. U.S. data-center consumption is expected to triple by 2032. Utility capital investment rose 12% in 2025 with another 6% projected for 2026 (Edison Electric Institute).</p>
  <p class="rv"><strong>Regulated utilities turn that capex into earnings.</strong> New generation and transmission go into the rate base, which earns an allowed return. Power, not chips, may be the binding constraint on AI growth, which puts regulated utilities at the center of the buildout.</p>
  <p class="rv"><strong>It also fits a late cycle.</strong> Earnings tied to allowed returns rather than economic activity make the sector a natural defensive hedge, and valuations still sat below historical medians despite above-trend growth.</p>
  <p class="rv"><strong>Why only 3%.</strong> With the 10-year Treasury projected at 4.20%, yield-sensitive investors face a real alternative, and some of the AI thesis is already priced in. The recommendation was a measured overweight: 3.00% against a 2.46% benchmark weight, a 22% proportional tilt.</p>
</div></section>

<section class="block"><header><span class="code fin">03 · Stock picks</span><h2 class="display">Two BUYs</h2></header><div class="prose" style="max-width:none">
  <div class="chart rv"><h4>Dividend-discount value vs market price</h4><p class="sub">Three-stage DDM. Hover a row for details.</p>
    <div class="legend"><span><i style="background:#5b8cff"></i>Sensitivity range</span><span><i style="background:#eef1f6;border-radius:50%"></i>Base-case value</span><span><i style="background:#c47a22;width:3px"></i>Price, 3 Mar 2026</span></div>
    <div data-chart="football" data-label="Valuation ranges for AEP and NFG versus market price" data-rows="{j(FF)}"></div>
  </div>

  <article class="stock rv">
    <div class="stock-head"><div><h3 class="display">American Electric Power</h3><div class="tick">NASDAQ: AEP · Electric utilities · Columbus, OH</div></div><span class="rating">BUY</span></div>
    <div class="keyrow"><div><b>$159.42</b><span>Base-case value</span></div><div><b>$131.92</b><span>Price, 3 Mar 2026</span></div><div><b>2.9%</b><span>Dividend yield</span></div><div><b>BBB+</b><span>Credit rating</span></div></div>
    <div class="stock-body">
      <div><h4>Thesis</h4><ul class="clean">
        <li><strong>56 GW</strong> of contracted data-center load with Google, Meta and AWS by 2030, double the 28 GW pipeline.</li>
        <li>A <strong>$72B</strong> five-year capex plan, with $5–8B more identified, flowing straight into rate base.</li>
        <li>The nation's largest transmission system, about <strong>40,000 miles</strong>, gives faster speed-to-power than peers.</li>
        <li>Capex-to-depreciation rose from <strong>1.9× to 2.50×</strong> (2021–2025); earned ROE 9.1%, targeting about 9.5% by 2030.</li>
      </ul></div>
      <div><h4>Valuation &amp; risks</h4><p>Three-stage DDM with a 7.5–9.0% cost of equity, 6.75% near-term growth and 3.5% terminal growth: base case $159.42, sensitivity range $138–$166. Dividends have grown at a 5.66% CAGR over five years, to $3.80 a share.</p><p style="margin-top:10px;color:var(--muted)">Risks: the capex program is funding-intensive, so a higher-for-longer rate path squeezes the spread between allowed returns and funding costs; hyperscaler projects face permitting and supply-chain delays.</p></div>
    </div>
    <div class="exhibits"><figure><img src="aep-ratebase.png" alt="AEP total rate base versus EPS, 2023 to 2028 estimates" loading="lazy"><figcaption>Rate base vs EPS · 2023–25 actual, 2026–28 estimates</figcaption></figure><figure><img src="aep-margin.png" alt="AEP operating margin versus electric utilities industry, 2021 to 2025" loading="lazy"><figcaption>Operating margin vs industry · 2021–25</figcaption></figure></div>
  </article>

  <article class="stock rv">
    <div class="stock-head"><div><h3 class="display">National Fuel Gas</h3><div class="tick">NYSE: NFG · Integrated natural gas · Williamsville, NY</div></div><span class="rating">BUY</span></div>
    <div class="keyrow"><div><b>$104.83</b><span>Base-case value</span></div><div><b>$92.92</b><span>Price, 3 Mar 2026</span></div><div><b>2.3%</b><span>Dividend yield</span></div><div><b>BBB-</b><span>Credit rating</span></div></div>
    <div class="stock-body">
      <div><h4>Thesis</h4><ul class="clean">
        <li>The <strong>$2.62B</strong> CenterPoint Ohio acquisition doubles the utility rate base to about $3.2B and adds 335,000 customers, shifting earnings toward regulated cash flow.</li>
        <li>Pipeline expansions to a Pennsylvania data-center and power site (Shippingport Lateral, 205,000 Dth/day) and Tioga Pathway add <strong>$30M+</strong> a year of contracted revenue.</li>
        <li>Record <strong>426 Bcf</strong> production in FY2025 with 15+ years of drilling inventory.</li>
        <li>FY2025 revenue up 17.1% to $2.28B, adjusted EPS up 38% to $6.91; 55th consecutive dividend increase.</li>
      </ul></div>
      <div><h4>Valuation &amp; risks</h4><p>Three-stage DDM with an 8.0–10.0% cost of equity, 13% near-term growth and 3.5% terminal growth: base case $104.83, sensitivity range $95–$115. Net debt to EBITDA is targeted at about 1.75× by FY2026, and upstream cash flow funds regulated growth.</p><p style="margin-top:10px;color:var(--muted)">Risks: natural gas price exposure in the upstream segment, integration and approval risk on the CenterPoint deal, and affordability pushback from a pending Pennsylvania rate case.</p></div>
    </div>
    <div class="exhibits"><figure><img src="nfg-revenue-mix.png" alt="NFG 2025 revenue by business segment" loading="lazy"><figcaption>FY2025 revenue by segment</figcaption></figure><figure><img src="nfg-leverage.png" alt="NFG net debt to EBITDA versus the utilities sector ETF, 2021 to 2025" loading="lazy"><figcaption>Net debt / EBITDA vs utilities ETF · 2021–25</figcaption></figure></div>
  </article>
</div></section>

<section class="block"><header><span class="code fin">04 · ESG</span><h2 class="display">ESG as an investment input</h2></header><div class="prose">
  <p class="rv">ESG has shifted from headline pledges to financially material metrics, and the fund treats it as a risk input rather than a scoring exercise. Holdings are screened with FactSet's Truvalue Labs, an event-based score built from news, regulatory filings and NGO reports instead of company self-reporting, and aligned with SASB, GRI, TCFD and the EU Taxonomy.</p>
  <p class="rv">The portfolio scored 29.56 against 27.90 for the S&amp;P 500, a 6% positive tilt. Utilities carried one of the largest tilts at +59%.</p>
  <div class="chart rv"><h4>ESG tilt by sector vs the S&amp;P 500</h4><p class="sub">Truvalue industry-percentile score, relative to the index average. Hover for scores.</p>
    <div class="legend"><span><i style="background:#5b8cff"></i>Above index</span><span><i style="background:#c47a22"></i>Below index</span><span><i style="background:#4a5160"></i>Within ±1%</span></div>
    <div data-chart="diverging" data-highlight="Utilities" data-label="ESG tilt by sector" data-rows="{j(esg_rows)}"></div>
    <details class="table-view"><summary>Show as table</summary><div class="tablewrap"><table class="tbl"><tr><th>Sector</th><th>S&amp;P avg</th><th>Fund avg</th><th>Tilt</th></tr>{esg_tbl}</table></div></details>
  </div>
</div></section>

<section class="block" style="border-bottom:0"><header><span class="code fin">05 · Report</span><h2 class="display">Full report</h2></header><div class="prose rv">
  <p>The complete 2026 Crummer Truist Portfolio, including every sector, the fixed-income book and the performance attribution, is published by Rollins College.</p>
  <div class="btns"><a class="btn solid" href="https://scholarship.rollins.edu/suntrust/40" rel="noopener">Read the full report <span class="arr">→</span></a></div>
  <p class="muted">Crummer Investment Management, 2026: Alexis Matton, Carlos Meyer, Amelia Kondal, Numair Aziz, Madison Kalhor, Taylor Payne, Hannah Gilbert, Chris Brennan, Ian Dean, Tully Njoroge and Dylan Reilly. Student research for educational purposes; not investment advice.</p>
</div></section>
</div>
</main>
'''+contact()
open(os.path.join(OUT,'global-portfolios.html'),'w').write(fin)

# ---------------- H-1B ----------------
h1b=head('H-1B Employer Research','Employer and labor-market analysis for an experienced-hire consulting search.')+nav()+'''
<main>
<section class="cs-hero"><div class="wrap">
  <a class="crumb" href="index.html#work">← All work</a>
  <div style="margin-top:28px"><span class="code data">Data · In progress</span></div>
  <h1 class="display split">H-1B Employer Research</h1>
  <p class="lede rv">Which employers and which cities give an experienced hire the best odds? This project combines employer filings, firm directories and market research into a target list, then makes it explorable.</p>
  <div class="factbar rv d1" data-count-wrap>
    <div><b data-count="170" data-pre="~">~170</b><span>Boutique and mid-market consulting firms mapped across four metros</span></div>
    <div><b data-count="59">59</b><span>Employers in the target workbook</span></div>
    <div><b data-count="2">2</b><span>Strongest metros for the experienced-hire pool</span></div>
    <div><b>Power BI</b><span>Interactive report in progress</span></div>
  </div>
</div></section>
<div class="wrap">
<section class="block"><header><span class="code data">Scope</span><h2 class="display">What it covers</h2></header><div class="prose rv">
  <p>A metro-level comparison of consulting markets, a firm map covering Boston, New York, Austin and Los Angeles, and an employer workbook spanning university tech-transfer offices, academic medical centers, research nonprofits and multilateral organizations.</p>
  <p class="muted">Key findings: Dallas–Fort Worth and Atlanta came out strongest for the experienced-hire pool. Among the four mapped cities, Boston was the strongest market and Austin the weakest.</p>
</div></section>
<section class="block" style="border-bottom:0"><header><span class="code data">Next</span><h2 class="display">Coming next</h2></header><div class="prose rv">
  <p>The full interactive Power BI report, with the data model built in SQL and the cleaning scripts in Python, will be published here.</p>
</div></section>
</div>
</main>
'''+contact()
open(os.path.join(OUT,'h1b-employer-research.html'),'w').write(h1b)
print('all pages ok')

# ---------------- Extracurriculars ----------------
extra=head('Extracurriculars','Tully Njoroge outside the classroom: NCAA Division II varsity swimming and team captain at Rollins College, Crummer Finance Organization and the MBA Association.')+nav('extra')+"""
<main>
<section class="cs-hero"><div class="wrap">
  <a class="crumb" href="index.html#about">← Home</a>
  <div style="margin-top:28px"><span class="code data">Leadership · Athletics</span></div>
  <h1 class="display split" style="font-size:clamp(22px,6vw,104px)">Extracurriculars</h1>
  <p class="lede rv">Most of what I know about leading people I learned in a pool at six in the morning. The rest came from running student organizations, where nobody is required to show up and you have to give them a reason to.</p>
</div></section>

<div class="wrap">
<section class="block"><header><span class="code aero">Athletics</span><h2 class="display">Varsity swimming</h2><p class="eyebrow">Rollins College · NCAA Division II · 2020–2025</p></header><div class="prose" style="max-width:none">
  <div class="pool rv"><canvas data-pool aria-hidden="true"></canvas><span class="pool-label">Lane 4 · TN</span></div>
  <div class="factbar rv" data-count-wrap style="margin-top:0">
    <div><b data-count="5">5</b><span>Seasons on the Rollins varsity team, 2020–2025</span></div>
    <div><b data-count="2">2</b><span>Seasons as team captain, 2022–23 and 2023–24</span></div>
    <div><b data-count="40" data-suf="+">40+</b><span>Teammates led as captain</span></div>
    <div><b data-count="24" data-pre="~" data-suf=" hrs">~24 hrs</b><span>Of training a week, alongside a full course load</span></div>
  </div>
  <div class="prose" style="margin-top:8px">
    <p class="rv">I swam five seasons for Rollins in NCAA Division II while finishing a psychology and sociology degree and starting the MBA. Balancing roughly 24 hours a week of training with a full academic load taught me more about time management than any planner ever has.</p>
    <p class="rv"><strong>Team captain, 2022–23 and 2023–24.</strong> As captain I was the link between more than 40 teammates and the coaching staff: setting the tone at practice, keeping morale up through a long season, and making sure quieter teammates were heard. It is where I learned that leading is mostly listening, then doing the unglamorous work first.</p>
    <p class="rv"><strong>Most Improved Athlete.</strong> Recognized by the team for progress over a season, which I'll take as proof that showing up consistently beats natural talent, at least eventually.</p>
  </div>
</div></section>

<section class="block" style="border-bottom:0"><header><span class="code fin">Leadership</span><h2 class="display">Crummer leadership</h2><p class="eyebrow">Crummer Graduate School of Business</p></header><div class="prose" style="max-width:none">
  <div class="roles">
    <article class="role rv">
      <div class="role-top"><span class="eyebrow">Aug 2025 – May 2026</span><span class="code fin">Finance</span></div>
      <h3 class="display">Vice President</h3>
      <div class="org">Crummer Finance Organization</div>
      <ul class="clean">
        <li>Partnered with the President on annual strategic planning, setting the organization's priorities and its calendar of events.</li>
        <li>Served as the link between student services, the faculty advisor and members, so initiatives lined up with what students actually needed.</li>
        <li>Coordinated professional-development events and industry networking opportunities for members.</li>
      </ul>
    </article>
    <article class="role rv d1">
      <div class="role-top"><span class="eyebrow">MBA Association</span><span class="code aero">Community</span></div>
      <h3 class="display">International Student Representative</h3>
      <div class="org">MBA Association, Crummer Graduate School of Business</div>
      <ul class="clean">
        <li>Represented the international students in my MBA class within the MBA Association.</li>
        <li>Served as their point of contact, taking questions and concerns to the association and the school.</li>
        <li>Having moved from Johannesburg myself, I knew the experience from both sides.</li>
      </ul>
    </article>
  </div>
</div></section>
</div>
</main>
"""+contact()
open(os.path.join(OUT,'extracurriculars.html'),'w').write(extra)
print('extracurriculars ok')
