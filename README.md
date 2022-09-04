_This bot is deprecated and will not receive updates._  
Our new welcome-dialogue using `didscord.py V2` and buttons can be found: [here](https://github.com/Info-Bonn/welcome-dialogue).

# A simple verification bot for discord
Single-guild discord-bot to give roles to a member accepting your servers rules.  
Also sending a neat little welcome message to the user.  

The bot also runs a task all five minutes to ensure that no member is missed due to potential downtime or other errors.   
It's possible to ignore members that joined before a specific date if the system shall not apply to older members.  

## setup
`pip install -r requirements.txt`  
`export TOKEN="your-key"`  
`python3 main.py`

## env variables
| parameter |  description |
| ------ |  ------ |
| `export ROLES="760434164146634752 880220270210740235"`  | Roles to give after verification, separated by a space |
| `export GUILD="760421261649248296"`  | Guild the bot shall be set up for |
| `export START_CHANNEL="877208002762002465"`  | Channel the bot mentions in welcome message |
| `export PREFIX="b!"`  | Command prefix |
| `export CHECK_PERIOD="5"` | Time between two checks for missed members |
| `export NOT_BEFORE="25.08.2021"`  | Members joined before that date won't be captured by verification check task |
| `export VERSION="unknown"` | Version the bot is running |
| `export OWNER_NAME="unknwon"` | Name of the bot owner |
| `export OWNER_ID="100000000000000000"` | ID of the bot owner |

Values `GUILD`, `START_CHANNEL` and `ROLES` need to be changed in order to make the bot run on your server! Those default is only usable for our own discord.  
The shown values are the default values that will be loaded if nothing else is specified.  
Please note that the welcome message is in german, you can update it in `src/verification_listsner.py`/ `get_welcome_text()`.  
