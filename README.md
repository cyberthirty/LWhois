# LWhois (WHOIS Lookup)

A LWhois is a tool or script developed in Python that queries WHOIS databases to retrieve information about a domain name. WHOIS databases contain registration details for domain names, including the registrant's contact information, registration and expiration dates, and other related data.

## Installation

1. **Clone the Repository**:
  ```bash
  git clone https://github.com/cyberthirty/LWhois.git
  cd LWhois
  ```

2. **Make the Script Executable**:
  ```bash
  chmod +x LWhois.py
  ```

3. **Install Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

To perform a WHOIS lookup for a domain, use the following command:

```bash
./whois_lookup.py -d example.com
```

### Options

- `-d`, `--domain`: Specify the domain name to look up.
- `-h`, `--help`: Show this help message and exit

## Example

```bash
./whois_lookup.py -d example.com
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

