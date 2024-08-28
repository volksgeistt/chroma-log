import sys

class ChromaLog:
    COLORS = {
        'BLACK': '\033[30m',
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
        'RESET': '\033[0m'
    }

    @staticmethod
    def colorize(text, color):
        return f"{ChromaLog.COLORS[color.upper()]}{text}{ChromaLog.COLORS['RESET']}"

    @staticmethod
    def print_colored(text, color, file=sys.stdout):
        print(ChromaLog.colorize(text, color), file=file)

    @staticmethod
    def log(level, message, color):
        ChromaLog.print_colored(f"[{level.upper()}] {message}", color)

    @staticmethod
    def debug(message):
        ChromaLog.log("DEBUG", message, "BLUE")

    @staticmethod
    def info(message):
        ChromaLog.log("INFO", message, "GREEN")

    @staticmethod
    def warning(message):
        ChromaLog.log("WARNING", message, "YELLOW")

    @staticmethod
    def error(message):
        ChromaLog.log("ERROR", message, "RED")

    @staticmethod
    def critical(message):
        ChromaLog.log("CRITICAL", message, "MAGENTA")

def debug(message):
    ChromaLog.debug(message)

def info(message):
    ChromaLog.info(message)

def warning(message):
    ChromaLog.warning(message)

def error(message):
    ChromaLog.error(message)

def critical(message):
    ChromaLog.critical(message)

def colorize(text, color):
    return ChromaLog.colorize(text, color)


if __name__ == "__main__":
    debug("This is a debug message")
    info("This is an info message")
    warning("This is a warning message")
    error("This is an error message")
    critical("This is a critical message")
    print(colorize("This is cyan text", "RED"))
