
FROM node:18

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build -- --mode production
RUN npm install -g serve

EXPOSE 4173
CMD ["npx", "vite", "preview", "--host"]
