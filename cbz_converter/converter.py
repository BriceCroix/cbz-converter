import os
import tempfile
import zipfile

import img2pdf
import PIL


def cbz2pdf(
    input: str,
    output: str,
    quality: int | None = None,
    width: int | None = None,
    height: int | None = None,
) -> bool:
    """Converts a cbz file into a pdf.

    Parameters
    ----------
    input : str
        Path to a cbz file.
    output : str
        Path to pdf file to be created.
    quality : int | None (optional)
        If provided, allows to lower the quality of the images (0 is worst, 100 is best)
    width : int | None (optional)
        If provided, images will be resized to this maximum width.
    height : int | None (optional)
        If provided, images will be resized to this maximum height.

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
            if quality is not None or width is not None or height is not None:
                for file in files:
                    image = PIL.Image.open(file)

                    if width is not None or height is not None:
                        # Some images are rotated, work with that
                        image_width = min(image.size)
                        image_heigth = max(image.size)
                        ratio = min(
                            (width or image_width) / image_width,
                            (height or image_heigth) / image_heigth,
                        )
                        image = image.resize(
                            size=(int(image.width * ratio), int(image.height * ratio)),
                            resample=PIL.Image.Resampling.LANCZOS,
                        )
                    # quality=75 is the default for jpeg images
                    image.save(file, quality=(quality or 75), optimize=True)
            pdf.write(img2pdf.convert(files))
            return True
        except Exception as e:
            print(f"Error converting pdf : {e}")
            return False
