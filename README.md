# 🧰 extra

`EXTRA-64` is a lightweight command-line utility for encoding and decoding files using Base64. It supports automatic deletion of the input file after conversion and provides a clean, colored output for better user experience.

---

## ✨ Features

- 🔐 **Base64 Encoding** – Convert raw text files to base64-encoded format.
- 🔓 **Base64 Decoding** – Revert encoded files back to their original content.
- 🧼 **Auto-cleanup** – Deletes the input file after a successful operation.
- 🌿 **Colored CLI Output** – Stylish green terminal messages.
- 🖥️ **Simple Syntax** – Use with just a few flags.

---

## 🧪 Installation

Make the script executable:

```bash

chmod +x extra.py

```

---

## 🚀 Usage

#### 🔐 Encode raw text to Base64

```bash
python3 extra.py -i raw.txt -o encoded.txt

```

- -i raw.txt: Input file to encode

- -o encoded.txt: Output file to write Base64

This will delete the original raw.txt after encoding.

---

#### 🔓 Decode Base64 back to raw text

```bash

python3 extra.py -i encoded.txt -o raw.txt --reverse

```

- --reverse: Tells the tool to decode instead of encode

This will delete the encoded.txt after decoding.

---

### 🆘 Help Menu


```bash

python3 extra.py --help


```
