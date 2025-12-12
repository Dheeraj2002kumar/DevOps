# Use official Node.js LTS image
FROM node:18

# Create app directory
WORKDIR /app

# Copy package.json (for future npm installs)
COPY package.json .

# Install dependencies (if any in future)
RUN npm install

# Copy rest of the application files
COPY . .

# Expose port used by Node.js
EXPOSE 5000

# Start the application
CMD ["npm", "start"]
