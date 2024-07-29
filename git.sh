# Add all changes
git add .

# Prompt for a custom commit message
read -p "Enter your commit message: " custom_message

# Commit with the custom message
git commit -m "$custom_message"

# Push to the main branch
git push origin main

# Check status
git status
