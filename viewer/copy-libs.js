// Copy bpmn-js assets from the Shopee viewer's public/lib into Lazada viewer's
// public/lib so the Lazada BPMN viewer is offline-capable.
// Source: /home/kronosss2002/doanba/shopee-ba-project/viewer/public/lib
// Target: /home/kronosss2002/doanba/lazada-ba-project/viewer/public/lib
const fs = require('fs');
const path = require('path');

const SOURCE = path.resolve(__dirname, '..', '..', 'shopee-ba-project', 'viewer', 'public', 'lib');
const TARGET = path.join(__dirname, 'public', 'lib');

if (!fs.existsSync(SOURCE)) {
  console.error('SOURCE missing: ' + SOURCE);
  process.exit(1);
}

// Recursively copy every file under SOURCE (mirrors its directory structure).
function copyTree(srcDir, dstDir) {
  let count = 0;
  for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
    const src = path.join(srcDir, entry.name);
    const dst = path.join(dstDir, entry.name);
    if (entry.isDirectory()) {
      count += copyTree(src, dst);
    } else if (entry.isFile()) {
      fs.mkdirSync(path.dirname(dst), { recursive: true });
      fs.copyFileSync(src, dst);
      console.log('OK: ' + path.relative(SOURCE, src));
      count++;
    }
  }
  return count;
}

fs.mkdirSync(TARGET, { recursive: true });
const total = copyTree(SOURCE, TARGET);
console.log('DONE - copied ' + total + ' files to ' + TARGET);
