# Long page

A long page used to exercise the `header.autohide` feature. Scroll down to
hide the header, scroll up to reveal it again.

## Overview

The autohide feature is a Material engine behavior. Alloy used to suppress
it accidentally by resetting the header transform unconditionally. The
current implementation scopes the reset to `:not([hidden])`, so Material's
`[hidden]` rule (`transform: translateY(-100%)`) can apply when the user
opts into the feature.

## What to verify

- Scrolling several lines down hides the header smoothly.
- Scrolling up at any point brings the header back without flicker.
- The sticky tabs row (rendered inside the header when sticky tabs is
  enabled) rides along with the slide. This fixture does not enable
  `navigation.tabs.sticky`, so tabs sit below the header and scroll away
  with content here.

## Filler section one

Padding the page so a typical viewport leaves room for a real scroll
gesture. Documentation users do not have a single canonical length, so this
fixture errs on the side of obviously-long-enough.

The autohide animation timing is owned by Material:

```text
transform: translateY(-100%);
transition: transform .25s cubic-bezier(.8, 0, .6, 1);
```

Alloy does not override these.

## Filler section two

More padding. Replace this content with anything if a more realistic shape
is useful for future verification.

- The header should never freeze mid-slide.
- Quick scroll reversals (down then up within the same gesture) should also
  reveal the header.
- The header background should remain blurred/translucent through the
  animation.

## Filler section three

Final padding block. If you can see this without scrolling, the page is
not long enough on your viewport - add another `## Filler` block or a
couple of paragraphs and rebuild.

The site reads `header.autohide` from the `features` list in
`mkdocs.yml`. To turn the behavior off temporarily, remove that entry and
rebuild.

## Filler section four

Stretching the page a little further so smaller laptop viewports
(roughly 13" at 1.5x scale) still see meaningful scroll travel.

The fixture intentionally has no rich components on it. The autohide test
should be readable without code blocks, callouts, charts, or tables
competing for attention.

## Filler section five

One more block to make sure the header has room to disappear well before
the user reaches the bottom of the page.

When the header is hidden, the right-side TOC should still be reachable
because it lives inside the content column rather than under the header
chrome.

## Filler section six

Last block. After this paragraph the page ends and the footer takes over.
