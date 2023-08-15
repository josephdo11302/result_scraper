from Controller.controller import Controller
from View.userview import View
from Model.resultlibrary import ResultsLibrary

def main():
    # Create instances of the library, controller, and view
    library = ResultsLibrary()
    controller = Controller(library)
    view = View(controller)

    # Run the main loop of the view
    view.run()

if __name__ == "__main__":
    main()
