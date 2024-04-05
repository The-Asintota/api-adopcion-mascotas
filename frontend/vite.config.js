import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api/v1/shelter/": {
        target: "https://api-adopcion-mascotas-dev-qprf.2.us-1.fl0.io",
        changeOrigin: true,
      },
    }
  }
})
