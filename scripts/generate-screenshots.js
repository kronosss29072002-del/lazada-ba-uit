// Generate PNG screenshots of all BPMN diagrams using bpmn-js + embedded HTTP server.
const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const http = require('http');

const PROJECT = path.resolve(__dirname, '..');
const OUT = path.join(PROJECT, 'docs', 'screenshots');

const FILES = [
  { bpmn: 'processes/01-seller-management.bpmn', out: '01-seller-management-asis.png', isAsIs: true },
  { bpmn: 'processes/02-dispute-management.bpmn', out: '02-dispute-management-asis.png', isAsIs: true },
  { bpmn: 'processes/03-order-processing.bpmn', out: '03-order-processing-asis.png', isAsIs: true },
  { bpmn: 'processes/04-return-refund.bpmn', out: '04-return-refund-asis.png', isAsIs: true },
  { bpmn: 'processes/05-customer-service.bpmn', out: '05-customer-service-asis.png', isAsIs: true },
  { bpmn: 'processes/06-marketing.bpmn', out: '06-marketing-asis.png', isAsIs: true },
  { bpmn: 'processes-to-be/01-seller-management.bpmn', out: '01-seller-management-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/02-dispute-management.bpmn', out: '02-dispute-management-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/03-order-processing.bpmn', out: '03-order-processing-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/04-return-refund.bpmn', out: '04-return-refund-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/05-customer-service.bpmn', out: '05-customer-service-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/06-marketing.bpmn', out: '06-marketing-tobe.png', isAsIs: false },
  { bpmn: 'processes/07-hr-training.bpmn', out: '07-hr-training-asis.png', isAsIs: true },
  { bpmn: 'processes/08-payment-settlement.bpmn', out: '08-payment-settlement-asis.png', isAsIs: true },
  { bpmn: 'processes/09-logistics-delivery.bpmn', out: '09-logistics-delivery-asis.png', isAsIs: true },
  { bpmn: 'processes/10-it-platform.bpmn', out: '10-it-platform-asis.png', isAsIs: true },
  { bpmn: 'processes-to-be/07-hr-training.bpmn', out: '07-hr-training-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/08-payment-settlement.bpmn', out: '08-payment-settlement-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/09-logistics-delivery.bpmn', out: '09-logistics-delivery-tobe.png', isAsIs: false },
  { bpmn: 'processes-to-be/10-it-platform.bpmn', out: '10-it-platform-tobe.png', isAsIs: false },
];

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.ttf': 'font/ttf',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.bpmn': 'application/xml',
  '.json': 'application/json; charset=utf-8',
};

function createServer() {
  return http.createServer((req, res) => {
    let urlPath = decodeURIComponent(req.url.split('?')[0]);
    if (urlPath.endsWith('/')) urlPath += 'index.html';
    let filePath = path.normalize(path.join(PROJECT, urlPath));
    if (!fs.existsSync(filePath)) {
      const publicPath = path.normalize(path.join(PROJECT, 'viewer/public', urlPath));
      if (fs.existsSync(publicPath)) {
        filePath = publicPath;
      }
    }
    if (!fs.existsSync(filePath) || !filePath.startsWith(PROJECT)) {
      res.writeHead(404); res.end('Not found'); return;
    }
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Cache-Control': 'no-store'
    });
    fs.createReadStream(filePath).pipe(res);
  });
}

async function main() {
  if (!fs.existsSync(OUT)) fs.mkdirSync(OUT, { recursive: true });

  const server = createServer();
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  const baseUrl = `http://127.0.0.1:${port}`;
  console.log(`HTTP server running on ${baseUrl}`);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const tmpHtmlAbs = path.join(PROJECT, 'viewer/public/_render_tmp.html');

  for (const f of FILES) {
    const xmlPath = path.join(PROJECT, f.bpmn);
    if (!fs.existsSync(xmlPath)) {
      console.log(`SKIP (not found): ${f.bpmn}`);
      continue;
    }
    const xml = fs.readFileSync(xmlPath, 'utf-8');

    const html = `<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<style>
  * { margin:0; padding:0; box-sizing: border-box; }
  html, body { background: #ffffff; font-family: 'Segoe UI', Arial, Helvetica, sans-serif; }
  #diagram-wrapper { display: inline-block; background: #ffffff; padding: 20px; border: 1px solid #e1e4e8; border-radius: 6px; }
  #canvas { width: 1000px; height: 500px; }

  .diagram-legend {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 24px;
    padding: 12px 20px 4px 20px;
    background: #ffffff;
    border-top: 1px solid #eaecef;
    margin-top: 12px;
    font-size: 13px;
    font-weight: 600;
  }
  .legend-item { display: flex; align-items: center; gap: 8px; color: #24292e; }
  .dot-va { width: 16px; height: 16px; background: #E6F4EA; border: 2px solid #137333; border-radius: 4px; }
  .dot-bva { width: 16px; height: 16px; background: #FEF7E0; border: 2px solid #B06000; border-radius: 4px; }
  .dot-nva { width: 16px; height: 16px; background: #FCE8E6; border: 2px solid #C5221F; border-radius: 4px; }
  .djs-label { font-family: 'Segoe UI', Arial, sans-serif !important; font-size: 12px !important; font-weight: 500 !important; }
</style>
<link rel="stylesheet" href="/lib/dist/assets/diagram-js.css">
<link rel="stylesheet" href="/lib/dist/assets/bpmn-js.css">
<link rel="stylesheet" href="/lib/dist/assets/bpmn-font/css/bpmn-embedded.css">
</head><body>
<div id="diagram-wrapper">
  <div id="canvas"></div>
  <div class="diagram-legend">
    <div class="legend-item"><div class="dot-va"></div> 🟢 VA (Value-Added)</div>
    <div class="legend-item"><div class="dot-bva"></div> 🟡 BVA (Business VA)</div>
    <div class="legend-item"><div class="dot-nva"></div> 🔴 NVA (Non-Value / Waste)</div>
  </div>
</div>
<script type="text/plain" id="bpmn-xml">${xml.replace(/<\/script>/g, '<\\/script>')}</script>
<script src="/lib/dist/bpmn-navigated-viewer.production.min.js"><\/script>
<script>
(async () => {
  try {
    const xml = document.getElementById('bpmn-xml').textContent;
    const viewer = new BpmnJS({ container: '#canvas' });
    await viewer.importXML(xml);
    const canvas = viewer.get('canvas');
    // Canvas sizing and fit
    const vb = canvas.viewbox();
    const w = Math.ceil(vb.inner.width + 80);
    const h = Math.ceil(vb.inner.height + 40);

    document.getElementById('canvas').style.width = w + 'px';
    document.getElementById('canvas').style.height = h + 'px';
    document.getElementById('diagram-wrapper').style.width = (w + 40) + 'px';

    canvas.resized();
    canvas.zoom('fit-viewport');
    window.__RENDER_DONE__ = true;
  } catch(e) {
    window.__RENDER_ERROR__ = e.message;
  }
})();
<\/script>
</body></html>`;

    fs.writeFileSync(tmpHtmlAbs, html);

    const page = await browser.newPage();
    page.on('console', msg => {
      if (msg.type() === 'error') console.log(`  [console.error] ${msg.text()}`);
    });
    page.on('pageerror', err => console.log(`  [pageerror] ${err.message}`));

    await page.setViewport({ width: 6500, height: 3500, deviceScaleFactor: 2 });
    await page.goto(`${baseUrl}/_render_tmp.html`, { waitUntil: 'networkidle0', timeout: 30000 });
    await page.waitForFunction(() => window.__RENDER_DONE__ || window.__RENDER_ERROR__, { timeout: 15000 }).catch(() => {});
    await new Promise(r => setTimeout(r, 600));

    const st = await page.evaluate(() => ({done: window.__RENDER_DONE__||false, err: window.__RENDER_ERROR__||null, hasBpmn: typeof window.BpmnJS, canv: document.querySelector('#canvas')?document.querySelector('#canvas').children.length:0}));
    console.log(`  STATE ${f.out}: ` + JSON.stringify(st));
    const err = st.err;
    if (err) {
      console.log(`ERROR ${f.out}: ${err}`);
    } else {
      const outPath = path.join(OUT, f.out);
      const wrapperEl = await page.$('#diagram-wrapper');
      if (wrapperEl) {
        await wrapperEl.screenshot({ path: outPath });
      } else {
        await page.screenshot({ path: outPath });
      }
      const sz = fs.statSync(outPath).size;
      console.log(`OK (wrapper): ${f.out} (${(sz/1024).toFixed(1)} KB)`);
    }
    await page.close();
  }

  try { fs.unlinkSync(tmpHtmlAbs); } catch (e) {}

  await browser.close();
  server.close();
  const count = fs.readdirSync(OUT).filter(f => f.endsWith('.png')).length;
  console.log(`\nDone. ${count} screenshots updated in ${OUT}`);
}

main().catch(e => { console.error(e); process.exit(1); });
