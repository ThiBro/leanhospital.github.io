// Generates favicon PNGs and ICO from the LeanHospital header logo icon
// (blue rounded square + white pulse line). Run: node scripts/gen-favicon.js
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const pngToIco = require('png-to-ico').default || require('png-to-ico');

const outDir = path.join(__dirname, '..', 'assets', 'img');

const svg = (rx) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <rect x="0" y="0" width="24" height="24" rx="${rx}" fill="#0E6BA8"/>
  <path d="M3 12h4l2 5 4-10 2 5h6" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`;

const rounded = Buffer.from(svg(5));   // browser tab favicons
const square = Buffer.from(svg(0));    // apple/android home-screen (full bleed)

async function png(src, size, name) {
  await sharp(src, { density: 384 }).resize(size, size).png().toFile(path.join(outDir, name));
  console.log('wrote', name);
}

(async () => {
  await png(rounded, 16, 'favicon-16x16.png');
  await png(rounded, 32, 'favicon-32x32.png');
  await png(square, 180, 'apple-touch-icon.png');
  await png(square, 192, 'android-chrome-192x192.png');
  await png(square, 512, 'android-chrome-512x512.png');

  // favicon.ico bundling 16/32/48
  const sizes = [16, 32, 48];
  const buffers = await Promise.all(
    sizes.map((s) => sharp(rounded, { density: 384 }).resize(s, s).png().toBuffer())
  );
  const ico = await pngToIco(buffers);
  fs.writeFileSync(path.join(outDir, 'favicon.ico'), ico);
  console.log('wrote favicon.ico');
})().catch((e) => { console.error(e); process.exit(1); });
