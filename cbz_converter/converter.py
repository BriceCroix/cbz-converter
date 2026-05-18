import os
import tempfile
import zipfile

import img2pdf
import PIL


def cbz2pdf(input: str, output: str, quality: int | None = None) -> bool:
    """Converts a cbz file into a pdf.

    Parameters
    ----------
    input : str
        Path to a cbz file.
    output : str
        Path to pdf file to be created.
    quality : int | None (optional)
        If provided, allows to lower the quality of the images (0 is worst, 100 is best)

    Returns
    -------
    bool
        True for success.
    """
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with (
        zipfile.ZipFile(input, "r") as zf,
        tempfile.TemporaryDirectory() as tempdir,
        open(output, "wb") as pdf,
    ):
        try:
            zf.extractall(path=tempdir)
            files = [
                os.path.join(tempdir, filename)
                for filename in sorted(os.listdir(tempdir))
            ]
            if quality is not None:
                for file in files:
                    PIL.Image.open(file).save(file, quality=quality, optimize=True)
            pdf.write(img2pdf.convert(files))
            return True
        except Exception as e:
            print(f"Error converting pdf : {e}")
            return False
