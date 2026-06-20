# Dense Page

Long headings and dense code are the point of this page.

## A Very Long Heading That Should Still Behave In The Right-Side Navigation

```ts title="src/very-long-example-name.ts" linenums="1"
export function renderDocumentationSurface(kind: "code" | "table" | "callout") {
  return {
    kind,
    stable: true,
    message: "Compact layouts should not clip code actions or line numbers.",
  }
}
```

!!! tip "Small surfaces still need room"

    Compact does not mean cramped. It means fewer wasted pixels.
