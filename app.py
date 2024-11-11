import typer
from pathlib import Path
from PIL import Image
import magic

app = typer.Typer()

# Initialize the magic object for checking file types
mime = magic.Magic(mime=True)


def is_valid_image(file_path: Path) -> bool:
    mime_type = mime.from_file(str(file_path))
    return mime_type.startswith("image/")


def convert_image(image_path: Path, output_format: str):
    try:
        if not is_valid_image(image_path):
            typer.echo(f"{image_path} is not a valid image file.", err=True)
            return
        with Image.open(image_path) as img:
            output_path = image_path.with_suffix(f".{output_format.lower()}")
            img.save(output_path)
            typer.echo(f"Image converted and saved to {output_path}")
    except Exception as e:
        typer.echo(f"Error converting image: {e}", err=True)


@app.command()
def convert(
    path: Path = typer.Argument(
        ..., help="Path to the image file or directory containing images"
    ),
    format: str = typer.Option(..., help="Output format (e.g., jpg, png)"),
):
    if not path.exists():
        typer.echo(f"The path {path} does not exist.", err=True)
        raise typer.Exit(code=1)

    if path.is_file():
        convert_image(path, format)
    elif path.is_dir():
        image_files = [p for p in path.glob("*.*") if is_valid_image(p)]
        if not image_files:
            typer.echo("No valid image files found in the directory.", err=True)
            raise typer.Exit(code=1)

        typer.echo(
            f"The specified path is a directory containing the following image files:"
        )
        for image_path in image_files:
            typer.echo(image_path.name)

        confirm = typer.confirm("Do you want to convert all these image files?")
        if confirm:
            for image_path in image_files:
                convert_image(image_path, format)
        else:
            typer.echo("Operation cancelled.")
            raise typer.Exit()
    else:
        typer.echo("The specified path is neither a file nor a directory.", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
