import logging

logger = logging.getLogger("WebAuditCLI")

logging.basicConfig(
    filename="scan.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)