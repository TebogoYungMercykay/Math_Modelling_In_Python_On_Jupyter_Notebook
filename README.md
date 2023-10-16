#              Mathematical Modelling In Python
---
- Welcome to the `Python Mathematics` repository! This repository contains a collection of Python `scripts`, `examples`, and `resources` to aid in `mathematical computations` and `analysis` using the Python programming language.
- The Python Mathematics repo is designed to help individuals `interested` in mathematics to `leverage` the `power` of Python for `solving mathematical` problems, conducting numerical computations, and `exploring` mathematical concepts.

  <img src="./Images/Math.png" alt="Mathematical Modelling" width="100%" height="400">

- ## `Features`:
  - Basic mathematical operations and functions.
  - Numerical computations and simulations.
  - Symbolic mathematics and equation solving.
  - Data visualization for mathematical analysis.
  - Integration with popular mathematical libraries, such as NumPy, SciPy, and SymPy.
  - Examples and templates for common mathematical tasks.
---
---
- ### Requirements before running codes:
  - ### `Installation`:
    - To use Python for Mathematics, you need to have Python installed on your system. You can download Python from the official website: python.org.
        - Installing it on Ubuntu WSL run these commands:
            - ```sql
                sudo apt update
            - ```sql
                sudo apt install python3-dev python3-pip
            - ```sql
                pip3 install numpy
                # This is to install numpy so you might need more.
        - You can `verify` the `installation` by running a `Python script` that imports `NumPy`:
            - ```sql
                python3 -c "import numpy; print(numpy.__version__)"
  - ### `Recommendation`:
    - Install an IDE that compiles and runs Python codes. Recommendation `VS Code`.
    - How to Set Up Python in `Visual Studio Code`:
        - On `Windows 10`: https://www.youtube.com/watch?v=dNFgRUD2w68
        - On `Windows 11`: https://youtu.be/kCMJxOSiWrg
    - Or alternatively, install `Anaconda` or `Jupyter` Notebook:
        - `Download Anaconda`: Visit the Anaconda website (https://www.anaconda.com/products/individual) and download the appropriate Anaconda distribution for your operating system (Windows, macOS, or Linux).
        - `Run the Installer`: Once the download is complete, run the Anaconda installer executable file.
        - `Follow the Installation Wizard`: The installation wizard will guide you through the installation process. Follow the instructions provided, including accepting the license agreement, selecting the installation location, and choosing whether to add Anaconda to your system's PATH variable.
        - `Complete the Installation`: After the installation is complete, you will have Anaconda installed on your system. It includes the Anaconda Navigator, which provides a graphical user interface for managing environments and launching Jupyter Notebook.
        - `Launch Jupyter Notebook`: Open the Anaconda Navigator and launch Jupyter Notebook from the menu. Alternatively, you can open a terminal or command prompt and run the following command:
            - ```bash
                jupiter notebook
            This will start the Jupyter Notebook server and open a web browser with the Jupyter Notebook interface.
  - ### `Usage`:
    - This provides a set of Python scripts and modules that you can import and utilize in your own projects. To get started, import the necessary modules into your Python scripts or interactive sessions. For example:
    - ```python
        import os, sys
        class HiddenPrints:
            def __enter__(self):
                self._original_stdout = sys.stdout
                sys.stdout = open(os.devnull, 'w')
        
            def __exit__(self, exc_type, exc_val, exc_tb):
                sys.stdout.close()
                sys.stdout = self._original_stdout
        with HiddenPrints():
            print("This Implementation is Just for Python 3 Programming Language Practices")
      ```
---
---
### For Introduction To Python:
- Visit FreeCodeCamp.org on Youtube: [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=rfscVS0vtbw)
- Visit FreeCodeCamp.org on Youtube: [Learn Python - Full Course for Beginners [Tutorial]](https://www.youtube.com/watch?v=8ext9G7xspg)
---
---
<p align="center">The End, Thank You</p>

---
