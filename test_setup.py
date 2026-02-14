#!/usr/bin/env python3
"""
Quick test script to verify the setup is correct
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8+"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version {version.major}.{version.minor} is too old. Need 3.8+")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    packages = ['streamlit', 'groq']
    all_installed = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            all_installed = False
    
    return all_installed

def check_env_file():
    """Check if .env file exists"""
    if os.path.exists('.env'):
        print("✅ .env file exists")
        
        # Check if API key is set
        with open('.env', 'r') as f:
            content = f.read()
            if 'GROQ_API_KEY' in content and 'your_groq_api_key_here' not in content:
                print("✅ GROQ_API_KEY appears to be set")
                return True
            else:
                print("⚠️  GROQ_API_KEY not configured in .env")
                return False
    else:
        print("⚠️  .env file not found (you can set API key in the app)")
        return False

def check_files():
    """Check if all required files exist"""
    required_files = ['app.py', 'requirements.txt', 'README.md', '.gitignore']
    all_exist = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
            all_exist = False
    
    return all_exist

def main():
    print("🔍 Checking AI Chatbot Setup...\n")
    
    print("1. Python Version")
    python_ok = check_python_version()
    print()
    
    print("2. Required Files")
    files_ok = check_files()
    print()
    
    print("3. Dependencies")
    deps_ok = check_dependencies()
    print()
    
    print("4. Environment Variables")
    env_ok = check_env_file()
    print()
    
    print("="*50)
    if python_ok and files_ok and deps_ok:
        print("✅ Setup looks good! Run: streamlit run app.py")
        if not env_ok:
            print("⚠️  Remember to set your API key in the app sidebar")
    else:
        print("❌ Some issues found. Please fix them before running.")
        print("\nTo install dependencies: pip install -r requirements.txt")
    print("="*50)

if __name__ == "__main__":
    main()
