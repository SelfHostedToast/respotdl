# RESPOTDL

A Python script to download Music to a remote server using the spotdl libraries.

## Dependencies:
SSHPass - used to provide access to local credential file in script execution.
## Environment Variables
- Specify your remote server SSH password in the included 'creds' file.
- Specify your remote environment details in the Environment Variables named "rem_server", "rem_path", and "rem_user". *** (You edit these by editing respotdl.py) ***

- rem_server -> Server IP Address
- rem_user -> Remote Server Username for SSH Authentication
- rem_path -> The path on the remote server where the Music will be stored, e.g. your NAS.
## Usage
- RUN -> 'python respotdl.py'
- Enter your desired URL(s) and type 'done' to execute.
- Answering 'Y' to the remote copy prompt will transfer the downloaded music to your specified location
## TODO:

- [x] Add SCP functionality 
- [x] Delete Files from local after script termination
