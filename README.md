# CBZ converter

Simple module to convert cbz files to pdf.

## How to use

```bash
uv run python -m cbz_converter <CBZ> [--output <PDF>]
```

- `<CBZ>` can either be a `.cbz` file or a directory containing `.cbz` files.
- `<PDF>` (optional) the file to create, or the folder to create when `<CBZ>` is itself a folder.
