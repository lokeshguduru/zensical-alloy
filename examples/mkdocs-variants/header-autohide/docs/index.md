# Header autohide

This fixture enables Material's `header.autohide` feature so the header
should slide out of view when the user scrolls down and slide back in when
the user scrolls up.

Scroll past the fold to see the behavior. The
[long page](guide/long-page.md) is the most reliable place to test because
it provides enough vertical space for a real scroll gesture.

## What to look for

- Scrolling down past roughly two viewport heights hides the header.
- Scrolling up brings the header back, with a short transition.
- Toggling palette while the header is hidden does not break the slide
  animation.
