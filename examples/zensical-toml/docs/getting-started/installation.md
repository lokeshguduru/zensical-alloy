# Installation

Install Zensical and Alloy from PyPI:

```bash
pip install zensical zensical-alloy
```

Then set the theme name.

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

## Serve Locally

```bash
zensical serve
```

Open <http://localhost:8000>.

## Build

```bash
zensical build
```

The generated site lands in `site/` unless your project config sets another
output directory.

## Existing MkDocs Projects

Keep `mkdocs.yml` if you already have one. Zensical can read compatible MkDocs
configuration, so you can test Alloy without renaming the config file.
