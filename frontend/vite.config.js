import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: './',
  build: { outDir: 'dist' },
  plugins: [vue()],
  server: {
    proxy: {
      '/detect': {
        target: 'http://backend:5000',
        changeOrigin: true
      }
    }
  }
})
