# ransomware
 Project developed with the goal to expose how simple lines of code can cause muach damage to a common user or an entire company by using what is called **Ransomware**, a way to encrypt files with a certain algorithm and require for money to the recovery of those data.

 ## How it Works

 1. First, the attacker creates a private key, which only he knows and use it to encrypt the data.

 2. After that, all data is encrypted using this key and the owner of that data is not able to read even restore the original state of it.

 3. The attacker requires for money to use the key he created to reverse the process, that is, decrypt the files.

 ## Running the ransomware example

 Create the python virtual env:
 ```bash
 python -m venv venv
 ```
Activate it:

**windows**
```bash
.\venv\Scripts\Activate.ps1
```

**linux**
```bash
source venv/bin/activate
```

 Install the dependencies:
 ```bash
 pip install -r requirements.txt
 ```

There is the folder `test_files` where it's possible to see 2 example files. The code directly affect them. When encrypted are unreadable.

Execute it:

```bash
python main.py
```

if you wanna to decrypt the files, run:
```bash 
python decrypt.py
```