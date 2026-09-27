from config import get_app_name, get_environment, get_api_key, get_model_name

def main():
    app_name = get_app_name()
    environment = get_environment()
    model_name = get_model_name()
    
    try:
        api_key = get_api_key()
        api_key_configured = bool(api_key)
    except ValueError:
        api_key_configured = False

    print(f"Application: {app_name}")
    print(f"Environment: {environment}")
    print(f"Model: {model_name}")
    print(f"API Key configured: {api_key_configured}")

if __name__ == "__main__":
    main()