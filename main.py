import asyncio
import argparse
import logging
from aiopath import AsyncPath
from aioshutil import copyfile

# Configure error logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def copy_file(file_path: AsyncPath, dest_folder: AsyncPath) -> None:
    """
    Asynchronously copies a file to a subfolder based on its extension.
    """
    try:
        # Extract extension
        ext = file_path.suffix.lstrip(".") or "unknown"

        # Target directory
        target_dir = dest_folder / ext
        # Create directory if it doesn't exist
        await target_dir.mkdir(parents=True, exist_ok=True)

        # Destination path
        target_path = target_dir / file_path.name

        await copyfile(file_path, target_path)

    except Exception as e:
        logging.error(f"Failed to copy {file_path}: {e}")


async def read_folder(src_folder: AsyncPath, dest_folder: AsyncPath) -> None:
    """
    Recursively iterates through the source and copy tasks.
    """
    try:
        tasks = []

        async for item in src_folder.rglob("*"):
            if await item.is_file():
                tasks.append(copy_file(item, dest_folder))

        if tasks:
            await asyncio.gather(*tasks)

    except Exception as e:
        logging.error(f"Failed to read folder {src_folder}: {e}")


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", "-s", required=True, help="Source directory path")
    parser.add_argument("--output", "-o", required=True, help="Output directory path")

    args = parser.parse_args()

    # Initialize AsyncPath objects
    source_path = AsyncPath(args.source)
    output_path = AsyncPath(args.output)

    # Validate source path
    if not await source_path.exists() or not await source_path.is_dir():
        logging.error("Source folder does not exist or is not a directory.")
        return

    await read_folder(source_path, output_path)


if __name__ == "__main__":
    asyncio.run(main())
