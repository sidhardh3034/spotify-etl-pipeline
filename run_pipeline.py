import subprocess
import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

current_stage = "Starting"

try:
    logger.info("ETL pipeline started.")

    current_stage = "Extraction"
    logger.info("Starting extraction...")
    subprocess.run(
        [sys.executable, "src/extract.py"],
        check=True
    )
    logger.info("Extraction completed successfully.")

    current_stage = "Transformation"
    logger.info("Starting transformation...")
    subprocess.run(
        [sys.executable, "src/transform.py"],
        check=True
    )
    logger.info("Transformation completed successfully.")

    current_stage = "Loading"
    logger.info("Starting loading...")
    subprocess.run(
        [sys.executable, "src/load.py"],
        check=True
    )
    logger.info("Loading completed successfully.")

    logger.info("ETL pipeline completed successfully.")

except Exception as error:
    logger.error(
        "%s stage failed: %s",
        current_stage,
        error
    )

    