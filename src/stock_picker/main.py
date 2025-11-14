import sys
import warnings
from datetime import datetime
from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """ Run the StockPicker crew """
    continueChat = True
    while continueChat:
        sector = input("Which sector would you like to search next? (e.g., 'Automobiles'): \n")
        inputs = {
            'sector': sector
        }

        result = StockPicker().crew().kickoff(inputs=inputs)

        print("\n\n === Final Result === \n\n")
        print(result.raw)

        continueChat = input("Would you like to search another sector? (yes/no): \n").strip().lower() == "yes"

if __name__ == "__main__":
    run()