from colorama import init, Fore, Back, Style
from typing import Dict, Any, List
import os

init(autoreset=True)

class Interface:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_header(text: str):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{text}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * len(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_success(text: str):
        print(f"{Fore.GREEN}{Style.BRIGHT}✓ {text}{Style.RESET_ALL}")

    @staticmethod
    def print_error(text: str):
        print(f"{Fore.RED}{Style.BRIGHT}✗ {text}{Style.RESET_ALL}")

    @staticmethod
    def print_info(text: str):
        print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")

    @staticmethod
    def print_table(headers: List[str], rows: List[List[Any]]):
        # Calculate column widths
        widths = [len(str(header)) for header in headers]
        for row in rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))

        # Print headers
        header_line = " | ".join(
            f"{Fore.CYAN}{str(header).ljust(width)}{Style.RESET_ALL}"
            for header, width in zip(headers, widths)
        )
        print(header_line)
        print("-" * len(header_line))

        # Print rows
        for row in rows:
            print(" | ".join(
                str(cell).ljust(width)
                for cell, width in zip(row, widths)
            ))

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(f"{Fore.YELLOW}{prompt}: {Style.RESET_ALL}")

    @staticmethod
    def get_menu_choice(options: Dict[str, str]) -> str:
        Interface.print_header("Menu Options")
        for key, value in options.items():
            print(f"{Fore.CYAN}{key}{Style.RESET_ALL}: {value}")
        return Interface.get_input("\nEnter your choice")