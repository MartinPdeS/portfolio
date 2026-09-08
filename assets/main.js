'use strict';

const filters = document.querySelector('.filter-bar');
const projects = [...document.querySelectorAll('.project')];
filters.hidden = false;
filters.addEventListener('click', (event) => {
  const button = event.target.closest('button[data-filter]');
  if (!button) return;
  filters.querySelectorAll('button').forEach((item) => {
    item.setAttribute('aria-pressed', String(item === button));
  });
  let count = 0;
  projects.forEach((project) => {
    project.hidden = button.dataset.filter !== 'all' && project.dataset.category !== button.dataset.filter;
    if (!project.hidden) count += 1;
  });
  document.querySelector('#filter-status').textContent = `${count} ${count === 1 ? 'project' : 'projects'} shown.`;
});

// A static, illustrative interference field, not a numerical scattering solver.
// Redraw only on input/resize; no animation loop or continuous background work.
const canvas = document.querySelector('#wave-field');
const context = canvas.getContext('2d');
const wavelength = document.querySelector('#wavelength');
function drawField() {
  if (!context) return;
  const bounds = canvas.getBoundingClientRect();
  const scale = Math.min(window.devicePixelRatio || 1, 2);
  const width = bounds.width;
  const height = bounds.height;
  if (!width || !height) return;
  canvas.width = Math.round(width * scale);
  canvas.height = Math.round(height * scale);
  context.setTransform(scale, 0, 0, scale, 0, 0);
  const cx = width * 0.51;
  const cy = height * 0.5;
  const radius = width * 0.085;
  const period = Number(wavelength.value) * width / 530;
  for (let x = 9; x < width; x += 5) {
    for (let y = 9; y < height; y += 5) {
      const dx = x - cx;
      const dy = y - cy;
      const distance = Math.hypot(dx, dy);
      if (distance < radius + 4) continue;
      const incident = Math.cos(x * Math.PI * 2 / period);
      const scattered = Math.cos((distance + cx) * Math.PI * 2 / period) * Math.min(1.8, Math.sqrt(radius / distance) * 2);
      const amplitude = incident + scattered;
      const fade = Math.min(1, x / 45, (width - x) / 45, y / 45, (height - y) / 45);
      context.fillStyle = amplitude > 0 ? `rgba(168,71,40,${Math.min(.8, Math.abs(amplitude) * .36) * fade})` : `rgba(76,102,84,${Math.min(.65, Math.abs(amplitude) * .29) * fade})`;
      context.beginPath();
      context.arc(x, y, .6 + Math.abs(amplitude) * .63, 0, Math.PI * 2);
      context.fill();
    }
  }
  context.strokeStyle = 'rgba(168,71,40,.4)';
  context.lineWidth = .7;
  [radius + 7, radius + 15].forEach((r) => {
    context.beginPath();context.arc(cx, cy, r, 0, Math.PI * 2);context.stroke();
  });
  const gradient = context.createRadialGradient(cx-radius*.3, cy-radius*.3, 0, cx, cy, radius);
  gradient.addColorStop(0, '#d48c66');gradient.addColorStop(.7, '#b55c37');gradient.addColorStop(1, '#8d3d24');
  context.fillStyle = gradient;
  context.beginPath();context.arc(cx, cy, radius, 0, Math.PI * 2);context.fill();
  context.fillStyle = '#60665e';
  context.font = '8px Arial';
  context.fillText('INCIDENT WAVE →', 15, height - 18);
  context.fillText('SCATTERED FIELD', width - 100, height - 18);
}
if (context) {
  document.querySelector('.wave-controls').hidden = false;
  wavelength.addEventListener('input', () => {
    document.querySelector('#wavelength-value').value = `${wavelength.value} a.u.`;
    drawField();
  });
  new ResizeObserver(drawField).observe(canvas);
  drawField();
}
