import logging
from typing import Dict, Any
from datetime import datetime

# =============================
# 1️⃣ Setup Python Logger
# =============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("agentic-ai")


# =============================
# 2️⃣ Log to Console + State
# =============================

def log_step(state: Dict[str, Any], message: str, level: str = "info"):
    """
    Logs message to console and also stores it in state['processing_log']
    """

    timestamp = datetime.utcnow().isoformat()

    log_entry = f"{timestamp} - {message}"

    # Log to console
    if level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)

    # Store in state
    logs = state.get("processing_log", [])
    logs.append(log_entry)

    return logs
