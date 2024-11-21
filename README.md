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

0. **Prerequisite(s)**  
    N.B.: If you have poetry installed in your system, ignore this `step 0`.
   1. **poetry**:
      - #### Step 1: Update Your System
          - Open a terminal 
          `Ctrl + Alt + T`
        
          - Update the package list and Upgrade installed packages:
          ```bash
          sudo apt update && sudo apt upgrade -y
          ```
      - #### Step 2: Use the following command to download and execute the Poetry installer system-wide for all the users
          ```bash
          curl -sSL https://install.python-poetry.org | sudo python3 -
          ```

          ##### If you'd like to install Poetry system-wide for all users, drop `sudo`.  
          😜 However, if you accidentally installed the poetry for all the users, doesn't matter.  
          It is recommended that `You read the damn documentation`. 

      - #### Step 3: Once installed, configure the system to use Poetry by adding it to your PATH. Add this line to your shell configuration file (~/.bashrc, ~/.zshrc, etc.), depending on your shell:
          ```bash
          vim ~/.zshrc
          ```        
         🤔 `vim` is not installed! How will you use nano? 😏Install `vim` or `emac`.  
      Just kidding!!! Use nano. 😃
          ```bash
          nano ~/.zshrc
          ```
         Now `paste` it in your shell config file  
          ```bash
          export PATH="$HOME/.local/bin:$PATH"
          ```
      
       - #### Step 4: Apply the changes to your shell:
          ```bash
          source ~/.bashrc  
          # or 
          source ~/.zshrc
          ```
       - #### Step 5: Verify Installation
          ```bash
          poetry --version
          ```

   2. Just kidding!!! I don't think you need any other prerequisite to install


1. ### **Clone the repository**:
   ```bash
   git@github.com:Shakhlyn/o3-running-script.git
   ```
   Navigate to the project directory using the following command:
   ```bash
   cd o3-running-script
   ```

2. ### **Set up Python virtual environment**:
   ```bash
   poetry shell
   ```
   ```bash
   poetry install
   ```


   **N.B.: If you have run the o3 project before, skip the step 3**
3. ### (Skip this step if you have already run the o3 project) **Install project dependencies**:
   Ensure that any Node.js dependencies are installed by running:
   ```bash
   nvm install 14.21.3
   nvm use 14.21.3
   npm install
   ```

## Configuration

- ### Ensure your `.zshrc` or `.bashrc` file includes NVM initialization:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

- ### To inspect whether it is in your `.zshrc` or `.bashrc`:
```bash 
vim ~/.zshre 
# or
nano ~/.zshrc
```
Now look for `NVM_DIR= ...`
If it is not initialized, paste it.  

Or, you can try to find with `grep`.

- ### Add an alias:
Add an alias manually in your `.zshrc` or `.bashrc` file.

OR,
After cloning this, from the root directory of this script-running project:
In the terminal, type
```bash
echo "alias runyaana=\"python3 $(pwd)/o3/o3/main.py\"" >> ~/.zshrc 
```

Now you need to apply the changes to your shell:
```bash
source ~/.bashrc  
# or 
source ~/.zshrc
```

# Attention:
### If you think this script helps you and want to buy me a Dinner or Lunch, or as many as you wish, I won't embarrass you by refusing the offer.

Just kidding!!!   
or not.
## Usage

- **Navigate to the yaana project's root directory**
- **In the root directory, Run the command**

```bash
runyaana
```


[//]: # (## License)

[//]: # ()
[//]: # (This project is licensed under the MIT License. See [LICENSE]&#40;LICENSE&#41; for more details.)
