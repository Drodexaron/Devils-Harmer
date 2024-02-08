![Devils-Harmer Logo](etc/logo.jpg)

```markdown
# Devils-Harmer

Devils-Harmer is a powerful DDoS (Distributed Denial of Service) attack tool written in Python. It allows users to flood target websites or servers with a high volume of HTTP POST requests, effectively overwhelming them and causing denial of service to legitimate users.

## Features

- **Customizable Attack Parameters**: Users can specify the target URL, number of threads, and provide a list of user agents and IP addresses to use for request spoofing.
  
- **Threading**: Utilizes threading to execute multiple requests concurrently, maximizing the efficiency of the attack.

- **Randomization**: Randomly selects user agents and IP addresses from provided lists for each request, making it difficult to trace the source of the attack.

- **Ctrl+C Signal Handling**: Provides an option to stop the attack using the Ctrl+C keyboard shortcut, ensuring user control and safety.
```
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/devils-harmer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd devils-harmer
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python devils-harmer.py
   ```

2. Follow the on-screen prompts to input the target URL, number of threads, and any additional options.

**Disclaimer:** This tool is intended for educational and testing purposes only. Misuse of this tool for malicious activities is strictly prohibited. The author takes no responsibility for any damages caused by the misuse of this tool.

## License

This project is licensed under the [MIT License](LICENSE).
```
