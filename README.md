# Command Runner

A Python script to automate the opening of multiple terminal tabs, navigating to a project directory, activating a virtual environment, and running development commands in `zsh` or `bash`.

## Features

- Automatically opens terminal tabs and navigates to your project directory.
- Activates the Python virtual environment for running Django.
- Sets up Node.js environment and runs `npm` commands with `nvm`.
- Opens VS Code for the project directory.

## Prerequisites

Ensure that you have the following installed:

- **Python 3.10+**
- **Poetry lts**
- **Zsh** or **Bash** shell
- **NVM (Node Version Manager)**
- **GNOME Terminal** (If you use other than **GNOME** terminal, let me know so that I can modify for you)
- **Django** and necessary dependencies for the project in your virtual environment
- **npm** and **Node.js** configured with `nvm`

## Installation

1. **Clone the repository**:
   ```bash
   git@github.com:Shakhlyn/o3-running-script.git
   cd o3-running-script
   ```

2. **Set up Python virtual environment**:
   ```bash
   poetry shell
   poetry install
   ```


### N.B.: If you have run the o3 project before, skip the step 3
3. (Skip this step if you have already run the o3 project) **Install project dependencies**:
   Ensure that any Node.js dependencies are installed by running:
   ```bash
   nvm install 14.21.3
   nvm use 14.21.3
   npm install
   ```

## Configuration

- Ensure your `.zshrc` or `.bashrc` file includes NVM initialization:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

- To inspect whether it is in your `.zshrc` or `.bashrc`:
```bash 
vim ~/.zshre 

or,

nano ~/.zshrc
```
- Add an alias:
Add an alias manually in your `.zshrc` or `.bashrc` file.

OR,
After cloning this script project, from the root directory:
In the termial, type
```bash
echo "alias runyaana=\"python3 $(pwd)/o3/o3/main.py\"" >> ~/.zshrc 
```

## Usage

1. **Go to the yaana project**
2. **In the root directory, Run the command**

```bash
runyaana
```


[//]: # (## License)

[//]: # ()
[//]: # (This project is licensed under the MIT License. See [LICENSE]&#40;LICENSE&#41; for more details.)
