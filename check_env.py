import sys
import site

print("🐍 Python executable:", sys.executable)
print("📦 Site-packages folder:")
for path in site.getsitepackages():
    print("   ", path)

try:
    import gensim
    print("✅ gensim is installed. Version:", gensim.__version__)
except ImportError:
    print("❌ gensim not found in this environment.")
