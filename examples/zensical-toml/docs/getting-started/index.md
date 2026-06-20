# Getting Started

This section covers the smallest useful Alloy setup.

## Requirements

- Python 3.10 or newer.
- A Zensical project, or a compatible MkDocs project that Zensical can read.

## Minimal Config

=== "zensical.toml"

    ```toml
    [project]
    site_name = "My docs"

    [project.theme]
    name = "alloy"
    ```

=== "mkdocs.yml"

    ```yaml
    site_name: My docs
    theme:
      name: alloy
    ```

## Next

- [Installation](installation.md) shows the package install and local build.
- [Configuration](configuration.md) covers palette, fonts, layout, and feature
  flags.
