import subprocess  # Import subprocess for shell commands
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace this with your bot's token
BOT_TOKEN = "7678398628:AAGsmPlqC3HjcV9qHiZZQfm3i9v6xif2W6w"

async def track_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Execute the SSH command to generate the temporary link
        command = "ssh -R maxsoft:80:localhost:8080 serveo.net"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Extract the generated link from the output
        output = result.stdout
        link = ""
        for line in output.splitlines():
            if "http://" in line or "https://" in line:  # Look for the link
                link = line.strip()
                break
        
        # Send the link back to the user
        if link:
            await update.message.reply_text(f"Here is your generated link:\n{link}")
        else:
            await update.message.reply_text("Failed to generate the link. Please try again.")
    
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

def main():
    # Create an Application instance with your bot token
    application = Application.builder().token(BOT_TOKEN).build()

    # Add a command handler for /track
    application.add_handler(CommandHandler("track", track_command))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
