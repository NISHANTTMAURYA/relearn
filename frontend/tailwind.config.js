/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        canvas: {
          DEFAULT: '#FBFBFA',
          subtle: '#F8FAFC',
          card: '#FFFFFF'
        },
        charcoal: {
          DEFAULT: '#0F172A',
          muted: '#475569',
          subtle: '#94A3B8',
          faint: '#CBD5E1'
        },
        border: {
          DEFAULT: '#E2E8F0',
          dark: '#CBD5E1'
        },
        brand: {
          DEFAULT: '#4F46E5', // deep indigo
          hover: '#4338CA',
          light: '#EEF2FF',
          border: '#C7D2FE'
        },
        mastery: {
          DEFAULT: '#059669', // soft emerald
          hover: '#047857',
          light: '#ECFDF5',
          border: '#A7F3D0'
        },
        slip: {
          DEFAULT: '#D97706', // soft amber
          hover: '#B45309',
          light: '#FFFBEB',
          border: '#FDE68A'
        },
        unsure: {
          DEFAULT: '#64748B',
          light: '#F1F5F9',
          border: '#CBD5E1'
        },
        misconception: {
          DEFAULT: '#E11D48', // rose/crimson
          light: '#FFF1F2',
          border: '#FECDD3'
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Consolas', 'monospace'],
        serif: ['Newsreader', 'Georgia', 'serif']
      }
    },
  },
  plugins: [],
}
