---
title: Accent validation
hide:
  - navigation
  - toc
---

# Accent validation

This page is a build fixture for Alloy accent coverage. The smoke check verifies
that every named Material accent and curated Alloy preset has a light and dark
case in the generated HTML.

<style>
.alloy-accent-validation {
  display: grid;
  gap: 1rem;
}

.alloy-accent-validation__grid {
  display: grid;
  gap: 0.5rem;
  grid-template-columns: repeat(auto-fit, minmax(10rem, 1fr));
}

.alloy-accent-validation__case {
  align-items: center;
  background: var(--background);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  color: var(--foreground);
  display: grid;
  gap: 0.5rem;
  grid-template-columns: auto 1fr;
  min-height: 3.5rem;
  padding: 0.625rem;
}

.alloy-accent-validation__swatch {
  background: var(--brand-accent);
  border-radius: 999px;
  box-shadow: inset 0 0 0 1px color-mix(in oklch, var(--foreground) 16%, transparent);
  height: 1.75rem;
  width: 1.75rem;
}

.alloy-accent-validation__label {
  display: grid;
  gap: 0.1rem;
}

.alloy-accent-validation__label small {
  color: var(--muted-foreground);
  font-size: 0.7rem;
}
</style>

<div class="alloy-accent-validation" data-accent-fixture="material-named">
  <h2>Named Material accents</h2>
  <div class="alloy-accent-validation__grid">
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="red" data-md-color-scheme="default" data-md-color-accent="red"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>red</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="red" data-md-color-scheme="slate" data-md-color-accent="red"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>red</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="pink" data-md-color-scheme="default" data-md-color-accent="pink"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>pink</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="pink" data-md-color-scheme="slate" data-md-color-accent="pink"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>pink</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="purple" data-md-color-scheme="default" data-md-color-accent="purple"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>purple</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="purple" data-md-color-scheme="slate" data-md-color-accent="purple"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>purple</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="deep-purple" data-md-color-scheme="default" data-md-color-accent="deep-purple"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>deep-purple</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="deep-purple" data-md-color-scheme="slate" data-md-color-accent="deep-purple"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>deep-purple</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="indigo" data-md-color-scheme="default" data-md-color-accent="indigo"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>indigo</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="indigo" data-md-color-scheme="slate" data-md-color-accent="indigo"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>indigo</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="blue" data-md-color-scheme="default" data-md-color-accent="blue"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>blue</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="blue" data-md-color-scheme="slate" data-md-color-accent="blue"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>blue</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="light-blue" data-md-color-scheme="default" data-md-color-accent="light-blue"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>light-blue</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="light-blue" data-md-color-scheme="slate" data-md-color-accent="light-blue"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>light-blue</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="cyan" data-md-color-scheme="default" data-md-color-accent="cyan"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>cyan</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="cyan" data-md-color-scheme="slate" data-md-color-accent="cyan"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>cyan</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="teal" data-md-color-scheme="default" data-md-color-accent="teal"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>teal</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="teal" data-md-color-scheme="slate" data-md-color-accent="teal"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>teal</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="green" data-md-color-scheme="default" data-md-color-accent="green"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>green</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="green" data-md-color-scheme="slate" data-md-color-accent="green"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>green</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="light-green" data-md-color-scheme="default" data-md-color-accent="light-green"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>light-green</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="light-green" data-md-color-scheme="slate" data-md-color-accent="light-green"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>light-green</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="lime" data-md-color-scheme="default" data-md-color-accent="lime"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>lime</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="lime" data-md-color-scheme="slate" data-md-color-accent="lime"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>lime</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="yellow" data-md-color-scheme="default" data-md-color-accent="yellow"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>yellow</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="yellow" data-md-color-scheme="slate" data-md-color-accent="yellow"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>yellow</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="amber" data-md-color-scheme="default" data-md-color-accent="amber"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>amber</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="amber" data-md-color-scheme="slate" data-md-color-accent="amber"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>amber</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="orange" data-md-color-scheme="default" data-md-color-accent="orange"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>orange</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="orange" data-md-color-scheme="slate" data-md-color-accent="orange"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>orange</code><small>dark</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="deep-orange" data-md-color-scheme="default" data-md-color-accent="deep-orange"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>deep-orange</code><small>light</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="named" data-accent-name="deep-orange" data-md-color-scheme="slate" data-md-color-accent="deep-orange"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>deep-orange</code><small>dark</small></span></div>
  </div>
</div>

<div class="alloy-accent-validation" data-accent-fixture="alloy-presets">
  <h2>Curated Alloy presets</h2>
  <div class="alloy-accent-validation__grid">
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="orange" data-md-color-scheme="default" style="--brand-accent: oklch(0.62 0.18 46);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>orange</code><small>light preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="orange" data-md-color-scheme="slate" style="--brand-accent: oklch(0.74 0.16 56);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>orange</code><small>dark preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="slate" data-md-color-scheme="default" style="--brand-accent: oklch(0.55 0.04 240);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>slate</code><small>light preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="slate" data-md-color-scheme="slate" style="--brand-accent: oklch(0.74 0.03 240);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>slate</code><small>dark preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="cyan" data-md-color-scheme="default" style="--brand-accent: oklch(0.6 0.13 200);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>cyan</code><small>light preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="cyan" data-md-color-scheme="slate" style="--brand-accent: oklch(0.78 0.11 200);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>cyan</code><small>dark preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="violet" data-md-color-scheme="default" style="--brand-accent: oklch(0.55 0.2 290);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>violet</code><small>light preset</small></span></div>
    <div class="alloy-accent-validation__case" data-accent-kind="preset" data-accent-preset="violet" data-md-color-scheme="slate" style="--brand-accent: oklch(0.74 0.15 295);"><span class="alloy-accent-validation__swatch"></span><span class="alloy-accent-validation__label"><code>violet</code><small>dark preset</small></span></div>
  </div>
</div>
