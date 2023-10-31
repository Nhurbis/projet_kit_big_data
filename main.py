""" Purpose: Main entry point for the application."""
from view.task_view import create_gradio_interface
from utils.loggers import debug_logger, errors_logger


if __name__ == "__main__":
    iface = create_gradio_interface()
    try:
        iface.launch(
            server_name="0.0.0.0", inbrowser=True, prevent_thread_lock=True)
        print("Access the application at http://localhost:7860/")
        input("Press Enter to exit...")
        print("The application was closed by the user.")
    except OSError:
        print("The application is already running.")
        print("Please close the other instance and try again.")
        exit(1)
    except Exception as e:
        print(e)
        debug_logger.error(e)
        errors_logger.error(e)
        exit(1)
    except KeyboardInterrupt:
        print("The application was closed by the user.")
        exit(0)
