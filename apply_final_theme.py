from pathlib import Path

files = ["home.qmd", "about.qmd", "reflection.qmd", "certificate.qmd", "projects.qmd", "cv.qmd"]

override = r'''
```{=html}
<style>
/* ===== FINAL NAVY + LIGHT BLUE OVERRIDE ===== */

/* navbar */
#quarto-header,
#quarto-header .navbar,
.navbar,
.navbar-expand-lg,
.navbar.navbar-expand-lg,
.headroom,
.headroom--pinned,
.headroom--unpinned {
  background: #163458 !important;
  background-color: #163458 !important;
  background-image: none !important;
  box-shadow: 0 10px 24px rgba(17,39,67,0.18) !important;
  border: none !important;
}

#quarto-header *,
.navbar *,
.navbar-brand,
.navbar-brand .menu-text,
.navbar-nav .nav-link,
.navbar-nav .nav-link .menu-text,
.navbar .nav-link,
.navbar .nav-link .menu-text,
.navbar .navbar-title,
.navbar .title,
.menu-text {
  color: #ffffff !important;
}

/* page background */
html, body, main.content, .page-columns, .page-full, .column-page, #quarto-content {
  background: linear-gradient(180deg, #eef3f8, #e7eef6) !important;
  color: #5c6b7a !important;
}

/* major cards */
.preview-entry-card,
.home-feature-card,
.home-contact-card,
.connect-form,
.guestbook-shell,
.reflection-hero,
.reflection-card,
.certificate-hero,
.certificate-card,
#home-about .home-about-panel,
#home-about .home-about-text,
#home-about .home-about-image,
.panel,
.card,
.card-body,
.callout,
.callout-note,
.callout-tip,
.callout-important,
div[style*="background:rgba(255,255,255"],
div[style*="background: rgba(255,255,255"],
div[style*="rgba(243,236,255"],
div[style*="rgba(241,236,255"] {
  background: rgba(236,243,250,0.95) !important;
  background-color: rgba(236,243,250,0.95) !important;
  background-image: none !important;
  border-color: rgba(176,191,210,0.38) !important;
  color: #5c6b7a !important;
}

/* headings */
h1, h2, h3, h4, h5, h6,
.title,
.quarto-title,
strong, b {
  color: #24364a !important;
}

/* text */
p, li, span, label, small {
  color: #5c6b7a !important;
}

/* buttons */
button,
.btn,
.btn-primary,
.certificate-btn,
.preview-entry-link,
#home-about .home-pill,
#home-connect .connect-btn,
.enter-home-btn,
a.btn,
a[role="button"] {
  background: linear-gradient(135deg, #163458, #234b78) !important;
  background-color: #163458 !important;
  color: #ffffff !important;
  border: 1px solid rgba(255,255,255,0.16) !important;
  box-shadow: 0 12px 24px rgba(24,52,88,0.16) !important;
}

/* inputs */
input, textarea, select {
  background: rgba(255,255,255,0.96) !important;
  border: 1px solid rgba(176,191,210,0.42) !important;
  color: #24364a !important;
}

input::placeholder,
textarea::placeholder {
  color: #7b8794 !important;
}

/* side nav */
.home-side-nav a {
  background: rgba(236,243,250,0.96) !important;
  border: 1px solid rgba(176,191,210,0.34) !important;
  color: #163458 !important;
}

.home-side-nav a.is-active {
  background: linear-gradient(135deg, #163458, #234b78) !important;
  color: #ffffff !important;
}

/* guestbook inner cards */
.guestbook-shell .message-card,
.guestbook-shell .guestbook-bubble,
.guestbook-shell .guestbook-message,
.guestbook-shell .chat-bubble,
.guestbook-shell .guest-entry,
.guestbook-shell .message,
.guestbook-shell .note-card {
  background: rgba(245,249,253,0.97) !important;
  border: 1px solid rgba(185,198,214,0.34) !important;
  box-shadow: 0 10px 22px rgba(31,58,91,0.08) !important;
}

/* remove purple leftovers */
[style*="243,236,255"],
[style*="241,236,255"],
[style*="#7d74d9"],
[style*="#9a92eb"],
[style*="rgba(243,236,255"],
[style*="rgba(241,236,255"] {
  background: rgba(236,243,250,0.95) !important;
  color: #24364a !important;
}
</style>
‘’’

for fn in files:
p = Path(fn)
if not p.exists():
continue
t = p.read_text(encoding=“utf-8”)
if “FINAL NAVY + LIGHT BLUE OVERRIDE” not in t:
p.write_text(t.rstrip() + “\n\n” + override + “\n”, encoding=“utf-8”)

print(“final override added”)