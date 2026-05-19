# CBZ converter

Simple module to convert cbz files to pdf.

## How to use

```bash
uv run python -m cbz_converter <CBZ> [--output <PDF>]
```

- `<CBZ>` can either be a `.cbz` file or a directory containing `.cbz` files.
- `<PDF>` (optional) the file to create, or a file pattern to use when parsing a directory.

Use the following to learn about all options :

```bash
uv run python -m cbz_converter --help
```
