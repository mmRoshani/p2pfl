from p2pfl.management.logger import logger


class NetworkHelper:

    @staticmethod
    def warning_logger(address: str, text: str) -> None:
        logger.warning(
            address, ">>>>>>>>>Network_Helper>>>>>>>>>>" + "\n\n***\t" + text
        )
